#!/usr/bin/env python3
"""Steuerung des Trader-Systems auf GitHub Actions. Nur Standardbibliothek.

Die Cloud-Sitzung von Claude erreicht Yahoo, Nasdaq Trader, SEC und das
House Clerk nicht. GitHub Actions schon. Dieses Skript ruft dort die Skripte
der trader-* Skills auf, schreibt trader/UEBERSICHT.md und schickt eine
Push-Nachricht über ntfy (App „ntfy“ auf dem iPhone).

    python3 tools/trader/system.py auto                 # was gerade fällig ist (Zeitplan)
    python3 tools/trader/system.py morning [--force]    # Morgen-Scan, News, Pelosi
    python3 tools/trader/system.py orb [--force]        # Opening-Range-Ausbruch
    python3 tools/trader/system.py alerts               # Preisalarme prüfen
    python3 tools/trader/system.py ticker TSLA [--alerts]   # News, Einstieg, Ausstiegsplan
    python3 tools/trader/system.py test                 # Test-Push
    python3 tools/trader/system.py render               # nur UEBERSICHT.md neu bauen

--no-publish: nichts committen (lokal). NTFY_DRY=1: Push nur ausgeben.
Einstellungen: trader/system.json. Der Push-Kanal kann über das Secret
NTFY_TOPIC überschrieben werden.

Eine Liste von Charts, die zu einer Regel passen, ist keine Kaufliste.
Das System platziert nie eine Order.
"""

import argparse
import datetime
import importlib.util
import json
import os
import subprocess
import sys
import time
import traceback
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
T = "trader"                         # Datenordner, relativ zu ROOT

_spec = importlib.util.spec_from_file_location("trader_scan", os.path.join(HERE, "scan.py"))
scan = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(scan)

DEFAULT_CONFIG = {
    "ntfy_server": "https://ntfy.sh",
    "ntfy_topic": "",
    "news_top": 10,                  # News für die ersten N Treffer des Morgen-Scans
    "pelosi_members": ["pelosi"],
    "orb_source": "watchlist",       # "watchlist" = Treffer des Morgen-Scans, "universe" = alle Aktien
    "universe_max_age_days": 6,
    "push_morning": True,
    "push_orb": True,
    "push_alerts": True,
    "push_errors": True,
}

# Zeitfenster in New Yorker Zeit, in denen „auto“ einen Teil startet.
# GitHub startet Zeitpläne oft 5 bis 30 Minuten zu spät, daher großzügig.
MORNING_WINDOW = (datetime.time(7, 30), datetime.time(9, 25))
ORB_WINDOW = (datetime.time(10, 10), datetime.time(12, 0))
LAB_WINDOW = (datetime.time(16, 20), datetime.time(19, 30))   # nach Börsenschluss

SETUP_DE = {
    "breakout_20d": "Schlusskurs über jedem Schlusskurs der 20 Tage davor",
    "bull_flag": "über 10 % gestiegen, dann 5 Tage in einer 5-%-Spanne",
    "reclaim_ma20": "gestern unter, heute über dem 20-Tage-Schnitt",
    "oversold": "RSI 14 unter 30",
    "oversold_bounce": "RSI gestern unter 30, heute im Plus geschlossen",
    "orb": "5-Minuten-Kerze schließt über dem Hoch der ersten 15 Minuten",
}
SETUP_ORDER = ["breakout_20d", "bull_flag", "reclaim_ma20", "oversold", "oversold_bounce"]
PART_DE = {"morning": "Morgen-Scan", "orb": "ORB-Scan", "live": "Labor live", "lab": "Labor", "alerts": "Preisalarme",
           "ticker": "Ticker-Analyse", "test": "Test-Push"}
WEEKDAY_DE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
NOTE_DE = "Eine Liste von Charts, die zu einer Regel passen, ist keine Kaufliste."

LOG = []


# ---------------------------------------------------------------- Hilfen

def p(*parts):
    return os.path.join(ROOT, *parts)


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)


def berlin(utc):
    """UTC -> deutsche Zeit (MEZ/MESZ), EU-Regel: letzter Sonntag im März / Oktober, 1:00 UTC."""
    def last_sunday(y, m):
        d = datetime.date(y, m, 31)
        return d - datetime.timedelta(days=(d.weekday() + 1) % 7)
    y = utc.year
    start = datetime.datetime.combine(last_sunday(y, 3), datetime.time(1))
    end = datetime.datetime.combine(last_sunday(y, 10), datetime.time(1))
    summer = start <= utc < end
    return utc + datetime.timedelta(hours=2 if summer else 1), ("MESZ" if summer else "MEZ")


def de_num(x, nd=2):
    s = "{:,.{nd}f}".format(float(x), nd=nd)
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def de_int(x):
    return "{:,}".format(int(x)).replace(",", ".")


def usd(x):
    return "%s $" % de_num(x) if x is not None else "–"


def pct(x):
    return ("%+.2f" % float(x)).replace(".", ",") + " %"


def stamp(utc):
    """'Do 22.10. 08:15 Uhr ET (14:15 Uhr MESZ)'"""
    et = scan.to_eastern(utc)
    de, zone = berlin(utc)
    return "%s %s %s Uhr ET (%s Uhr %s)" % (WEEKDAY_DE[et.weekday()], et.strftime("%d.%m."),
                                            et.strftime("%H:%M"), de.strftime("%H:%M"), zone)


def date_de(iso):
    try:
        d = datetime.date.fromisoformat(iso[:10])
        return "%s %s" % (WEEKDAY_DE[d.weekday()], d.strftime("%d.%m.%Y"))
    except (TypeError, ValueError):
        return iso or "–"


def read_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def write_json(path, doc):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def config():
    cfg = dict(DEFAULT_CONFIG)
    cfg.update({k: v for k, v in (read_json(p(T, "system.json"), {}) or {}).items() if not k.startswith("_")})
    return cfg


def run(name, args, timeout=1500):
    """Ein Skript aus tools/trader starten. -> (Exit-Code, stdout, stderr)."""
    cmd = [sys.executable, os.path.join(HERE, args[0])] + list(args[1:])
    t0 = time.time()
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        rc, out, err = r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        rc, out, err = 124, "", "Zeitlimit von %d Sekunden überschritten" % timeout
    LOG.append("$ %s  (Exit %d, %.0f s)\n%s%s" % (" ".join(args), rc, time.time() - t0,
                                                   out if len(out) < 20000 else out[:20000] + "\n…gekürzt\n",
                                                   ("[stderr]\n" + err) if err.strip() else ""))
    print(LOG[-1], flush=True)
    return rc, out, err


def run_json(name, args, timeout=1500):
    """Wie run, aber stdout als JSON. -> (Exit-Code, doc oder None, Fehlertext)."""
    rc, out, err = run(name, args, timeout)
    try:
        return rc, json.loads(out), ""
    except ValueError:
        reason = (err.strip().splitlines() or out.strip().splitlines() or ["keine Ausgabe"])[-1]
        return rc, None, reason


def run_url():
    server, repo, rid = (os.environ.get(k) for k in ("GITHUB_SERVER_URL", "GITHUB_REPOSITORY", "GITHUB_RUN_ID"))
    return "%s/%s/actions/runs/%s" % (server, repo, rid) if server and repo and rid else None


def overview_url():
    repo = os.environ.get("GITHUB_REPOSITORY", "neidelbert/claude")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    return "https://github.com/%s/blob/%s/trader/UEBERSICHT.md" % (repo, branch)


# ---------------------------------------------------------------- Push (ntfy)

def reply_topic(cfg):
    return os.environ.get("NTFY_REPLY_TOPIC") or cfg.get("ntfy_reply_topic")


def yes_no_actions(cfg, pid):
    """Buttons Ja / Nein / Übersicht. Ja und Nein schicken „ja <id>“ an den privaten Antwortkanal."""
    url = cfg["ntfy_server"].rstrip("/") + "/" + reply_topic(cfg)
    return [{"action": "http", "label": "Ja", "url": url, "method": "POST", "body": "ja " + pid, "clear": True},
            {"action": "http", "label": "Nein", "url": url, "method": "POST", "body": "nein " + pid, "clear": True},
            {"action": "view", "label": "Übersicht", "url": overview_url()}]


def read_answers(cfg):
    """Antworten der letzten 24 Stunden aus dem Antwortkanal -> {id: {"answer", "ts"}} (letzte zählt)."""
    topic = reply_topic(cfg)
    if not topic:
        return {}
    url = "%s/%s/json?poll=1&since=24h" % (cfg["ntfy_server"].rstrip("/"), topic)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "trader-system"}), timeout=20) as r:
        lines = r.read().decode("utf-8", "replace").splitlines()
    out = {}
    for line in lines:
        try:
            m = json.loads(line)
        except ValueError:
            continue
        words = (m.get("message") or "").strip().lower().split()
        if m.get("event") == "message" and len(words) == 2 and words[0] in ("ja", "nein"):
            out[words[1]] = {"answer": words[0], "ts": int(m.get("time") or 0)}
    return out


def push(cfg, title, message, priority=3, tags=None, actions=None):
    topic = os.environ.get("NTFY_TOPIC") or cfg.get("ntfy_topic")
    if actions is None:
        actions = [{"action": "view", "label": "Übersicht", "url": overview_url()}]
        if run_url():
            actions.append({"action": "view", "label": "Lauf ansehen", "url": run_url()})
    body = {"topic": topic, "title": title, "message": message, "priority": priority,
            "tags": tags or [], "click": overview_url(), "actions": actions}
    if os.environ.get("NTFY_DRY") or not topic:
        print("PUSH (nicht gesendet%s): %s\n%s" % ("" if topic else ", kein Kanal", title, message))
        return False
    req = urllib.request.Request(cfg["ntfy_server"].rstrip("/") + "/", method="POST",
                                 data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                r.read()
            print("Push gesendet: %s" % title)
            return True
        except Exception as e:  # Netz kurz weg: zweimal neu versuchen
            print("Push fehlgeschlagen (%s), Versuch %d" % (e, attempt + 1))
            time.sleep(3)
    return False


# ---------------------------------------------------------------- Status

def status_path(part):
    return p(T, "status", part + ".json")


def save_status(part, ok, summary, steps, data=None, when=None):
    when = when or utcnow()
    et = scan.to_eastern(when)
    write_json(status_path(part), {"part": part, "ok": ok, "summary": summary, "ran_at": when.isoformat() + "Z",
                                   "date_et": et.date().isoformat(), "steps": steps, "data": data or {},
                                   "run_url": run_url()})


def done_today(part, today):
    st = read_json(status_path(part), {}) or {}
    return st.get("date_et") == today.isoformat() and st.get("ok")


def step(steps, name, ok, detail):
    steps.append({"name": name, "ok": ok, "detail": detail})
    return ok


# ---------------------------------------------------------------- Morgen-Scan

def do_morning(cfg, now, force):
    owned = ["universe.txt", "watchlist.json", "state/news.json", "state/pelosi.json", "status/morning.json"]
    steps, data = [], {}
    et = scan.to_eastern(now)
    trading, why = scan.trading_day(et.date())

    # 1. Aktienliste: wöchentlich oder wenn sie fehlt
    old = read_json(status_path("morning"), {}) or {}
    uni_date = (old.get("data") or {}).get("universe_date")
    stale = (not os.path.exists(p(T, "universe.txt")) or not uni_date or
             (et.date() - datetime.date.fromisoformat(uni_date)).days > cfg["universe_max_age_days"])
    data["universe_date"] = uni_date
    if stale:
        rc, out, err = run("universe", ["scan.py", "universe"])
        if rc == 0:
            data["universe_date"] = et.date().isoformat()
            kept = [l for l in out.splitlines() if l.startswith("Kept ")]
            n = kept[0].split(" US-")[0].replace("Kept ", "").replace(",", ".") if kept else ""
            step(steps, "Aktienliste", True, "neu geladen: %s Aktien" % n if n else "neu geladen")
        elif os.path.exists(p(T, "universe.txt")):
            step(steps, "Aktienliste", False, "Neu laden fehlgeschlagen, alte Liste genutzt: " + (err or out).strip()[-200:])
        else:
            step(steps, "Aktienliste", False, (err or out).strip()[-200:])
            return False, "Aktienliste fehlt", steps, data, owned
    else:
        step(steps, "Aktienliste", True, "vom %s" % date_de(uni_date))

    # 2. Daily-Scan
    # erst in eine Zwischendatei: ein Lauf ohne Daten darf die letzte gute Watchlist nicht überschreiben
    tmp = "%s/watchlist.new.json" % T
    rc, doc, reason = run_json("daily", ["scan.py", "daily", "--json", "--out", tmp])
    c = (doc or {}).get("counts", {})
    if not doc or not c.get("fetched"):
        if os.path.exists(p(tmp)):
            os.remove(p(tmp))
        reason = reason or "Yahoo hat keine Daten geliefert (0 von %s Charts)" % de_int((doc or {}).get("universe") or 0)
        step(steps, "Daily-Scan", False, reason)
        return False, "Daily-Scan fehlgeschlagen: " + reason, steps, data, owned
    os.replace(p(tmp), p(T, "watchlist.json"))
    hits = doc.get("hits", [])
    per = {k: sum(1 for h in hits if k in h.get("setups", [])) for k in SETUP_ORDER}
    data["daily"] = {"as_of": doc.get("as_of"), "universe": doc.get("universe"), "fetched": c.get("fetched"),
                     "liquid": (c.get("fetched") or 0) - (c.get("illiquid") or 0), "scanned": doc.get("scanned"),
                     "failed": doc.get("failed"), "hits": len(hits), "per_setup": per}
    step(steps, "Daily-Scan", True, "%s von %s Charts geladen, %s gescannt, %s Treffer" % (
        de_int(c.get("fetched") or 0), de_int(doc.get("universe") or 0), de_int(doc.get("scanned") or 0),
        de_int(len(hits))))

    # 3. News zu den ersten Treffern
    top = [h["symbol"] for h in hits[:cfg["news_top"]]]
    if top:
        args = ["news.py", "--tickers"] + top + ["--json", "--hours", "24"]
        if not os.environ.get("SEC_USER_AGENT"):
            args.append("--no-sec")
        rc, nd, reason = run_json("news", args, timeout=600)
        if nd is None:
            step(steps, "News", False, reason)
        else:
            items = nd.get("items", [])
            data["news"] = {"tickers": top, "items": items[:40], "moves": nd.get("moves", []),
                            "notes": nd.get("notes", [])}
            dead = not items and not nd.get("moves") and nd.get("notes")
            step(steps, "News", not dead, "; ".join(nd["notes"])[:200] if dead else
                 "%d neue Meldungen zu %d Tickern" % (len(items), len(top)))

    # 4. Pelosi-Tracker (Meldungen an das House Clerk)
    members = cfg.get("pelosi_members") or []
    if members:
        args = ["ptr.py", "new", "--json", "--state", "%s/state/pelosi.json" % T]
        for m in members:
            args += ["--member", m]
        rc, pd, reason = run_json("pelosi", args, timeout=300)
        if pd is None:
            step(steps, "Pelosi-Tracker", False, reason)
        else:
            fresh = pd.get("new", [])
            data["pelosi"] = {"members": members, "new": fresh[:20]}
            step(steps, "Pelosi-Tracker", True, "%d neue Meldung%s" % (len(fresh), "" if len(fresh) == 1 else "en"))

    ok = all(s["ok"] for s in steps)
    summary = "%s Treffer" % de_int(len(hits))
    if cfg["push_morning"]:
        lines = ["Schlusskurse vom %s · %s Charts gescannt" % (date_de(doc.get("as_of", "")),
                                                             de_int(doc.get("scanned") or 0))]
        lines.append(" · ".join("%s %s" % (k, de_int(v)) for k, v in per.items() if v))
        if hits:
            lines.append("Meistgehandelt: " + ", ".join(h["symbol"] for h in hits[:6]))
        n = data.get("news")
        if n is not None:
            moving = [m for m in n["moves"] if m.get("moving")]
            lines.append("News: %d neue Meldungen zu den ersten %d" % (len(n["items"]), len(n["tickers"])) +
                         ("; starke Bewegung: " + ", ".join("%s %s" % (m["ticker"], pct(m["pct"])) for m in moving[:4])
                          if moving else ""))
        pl = data.get("pelosi")
        if pl is not None:
            lines.append("Pelosi: " + ("%d neue Meldung(en)" % len(pl["new"]) if pl["new"] else "nichts Neues"))
        if not trading:
            lines.append("Heute kein Handelstag (%s)." % ("Wochenende" if why == "weekend" else why))
        bad = [s for s in steps if not s["ok"]]
        if bad:
            lines.append("Probleme: " + "; ".join("%s: %s" % (s["name"], s["detail"]) for s in bad))
        lines.append(NOTE_DE)
        push(cfg, "Morgen-Scan: %s Charts passen zu einer Regel" % de_int(len(hits)), "\n".join(lines),
             priority=3 if ok else 4, tags=["chart_with_upwards_trend"] if ok else ["warning"])
    return ok, summary, steps, data, owned


# ---------------------------------------------------------------- ORB-Scan

def do_orb(cfg, now, force):
    owned = ["orb.json", "status/orb.json"]
    steps, data = [], {}
    args = ["scan.py", "orb", "--json", "--out", "%s/orb.new.json" % T]
    src = cfg.get("orb_source", "watchlist")
    if src == "watchlist" and os.path.exists(p(T, "watchlist.json")):
        args += ["--watchlist", "%s/watchlist.json" % T, "--max-confirm", "0"]
        src_de = "Treffer des Morgen-Scans"
    else:
        src_de = "alle Aktien der Liste (die 200 meistgehandelten Kandidaten geprüft)"
    rc, doc, reason = run_json("orb", args)
    if doc and not (doc.get("counts") or {}).get("fetched"):
        doc, reason = None, "Yahoo hat keine 5-Minuten-Daten geliefert"
    if not doc:
        if os.path.exists(p(T, "orb.new.json")):
            os.remove(p(T, "orb.new.json"))
        step(steps, "ORB-Scan", False, reason)
        if force and cfg["push_orb"]:
            push(cfg, "ORB-Scan: nichts gelaufen", "Grund: %s" % reason, priority=2, tags=["hourglass"])
        # manuell zu früh / am Wochenende gestartet: nur Bescheid geben, nichts speichern
        return (None if force else False), reason, steps, data, owned
    if os.path.exists(p(T, "orb.new.json")):
        os.replace(p(T, "orb.new.json"), p(T, "orb.json"))
    c = doc.get("counts", {})
    hits = doc.get("hits", [])
    data["orb"] = {"as_of": doc.get("as_of"), "source": src_de, "universe": doc.get("universe"),
                   "fetched": c.get("fetched"), "scanned": doc.get("scanned"), "candidates": c.get("candidates"),
                   "confirmed": c.get("confirmed"), "unconfirmed": doc.get("unconfirmed"), "hits": len(hits)}
    step(steps, "ORB-Scan", True, "%s von %s nutzbaren Charts über der Eröffnungsspanne" % (
        de_int(len(hits)), de_int(doc.get("scanned") or 0)))
    if cfg["push_orb"]:
        cut = (doc.get("as_of") or "").split(" ")
        lines = ["Quelle: %s · %s nutzbare Charts" % (src_de, de_int(doc.get("scanned") or 0))]
        if doc.get("unconfirmed"):
            lines.append("TEILWEISE: %s Kandidaten nicht geprüft" % de_int(doc["unconfirmed"]))
        for h in sorted(hits, key=lambda h: h.get("_t") or h.get("bar_index") or 0)[-8:][::-1]:
            lines.append("%s Uhr ET  %s  %s  (%s über dem Hoch %s)" % (
                h.get("bar_start", "?"), h["symbol"], usd(h["price"]), pct(h["pct_over"]).lstrip("+"),
                usd(h["or_high"])))
        if hits:
            lines.append("Spätere Treffer liegen näher am aktuellen Kurs.")
        lines.append(NOTE_DE)
        push(cfg, "ORB %s Uhr ET: %s Charts über der Eröffnungsspanne" % (cut[1] if len(cut) > 1 else "",
                                                                          de_int(len(hits))),
             "\n".join(lines), priority=3, tags=["bell"])
    return True, "%s Treffer" % de_int(len(hits)), steps, data, owned


# ---------------------------------------------------------------- Labor (Testphase)

def lab_rank_line(r):
    t = r["test"]
    return "%s: %s Trades, %s %% Treffer, %s € bei 100 € pro Trade" % (
        r["label"], de_int(t.get("n", 0)), de_num(t.get("win_rate", 0), 0), de_num(t.get("eur", 0)))


def do_lab(cfg, now, force):
    owned = ["lab/results.json", "status/lab.json"]
    steps, data = [], {}
    rc, fd, reason = run_json("lab-fetch", ["lab.py", "fetch"], timeout=1200)
    if fd is None or not fd.get("fetched"):
        step(steps, "Kerzen laden", False, reason or "keine Kerzen geladen")
    else:
        step(steps, "Kerzen laden", True, "%s von %s Aktien" % (de_int(fd["fetched"]), de_int(fd["symbols"])))
    rc, rd, reason = run_json("lab-run", ["lab.py", "run"], timeout=1800)
    if rd is None or rd.get("error"):
        step(steps, "Testen", False, (rd or {}).get("error") or reason)
        return False, "Labor fehlgeschlagen", steps, data, owned
    res = read_json(p(T, "lab", "results.json"), {}) or {}
    rows = res.get("variants", [])
    passed = [r for r in rows if r.get("passed")]
    data = {"days": res.get("days"), "symbols": res.get("symbols"), "trades": rd.get("trades"),
            "passed": len(passed), "best": rows[0]["id"] if rows else None}
    step(steps, "Testen", True, "%s Varianten, %s Trades, %d bestanden" % (
        de_int(len(rows)), de_int(rd.get("trades") or 0), len(passed)))
    lines = ["%s Aktien · %s Tage (%s Lerntage, %s Prüftage) · %s Spielgeld-Trades" % (
        de_int(res.get("symbols") or 0), de_int(res.get("days") or 0), de_int(res.get("n_train_days") or 0),
        de_int(res.get("n_test_days") or 0), de_int(rd.get("trades") or 0))]
    lines.append("Bestanden: %d von %d Varianten" % (len(passed), len(rows)))
    for i, r in enumerate(rows[:3], 1):
        lines.append("%d. %s" % (i, lab_rank_line(r)))
    lines.append("Was heißt das? Prüftage sind Tage, die das System beim Lernen nicht gesehen hat. Nur was "
                 "dort im Plus ist, zählt. „Bei 100 € pro Trade“ ist vor Gebühren; mit 1 € je Order "
                 "kosten 100 Trades 200 €.")
    push(cfg, "Labor: %d von %d Varianten bestanden" % (len(passed), len(rows)), "\n".join(lines),
         priority=3, tags=["test_tube"])
    return True, "%d von %d bestanden" % (len(passed), len(rows)), steps, data, owned


STRAT_SHORT = {"orb": "Opening-Range-Ausbruch", "gap": "News-Sprung", "bounce": "Erholung"}
WHY_IN = {
    "orb": "Der Kurs hat über dem Hoch der ersten Minuten geschlossen. Der Stopp liegt dort, wo die Idee falsch wäre.",
    "gap": "Die Aktie ist mit viel Umsatz über dem Vortag gestartet und steigt weiter über ihr erstes Hoch.",
    "bounce": "Die stark gefallene Aktie steigt wieder über ihren Tagesdurchschnittspreis (VWAP).",
}
WHY_OUT = {
    "Stopp": "Der Stopp hat den Verlust begrenzt. Das ist normal: viele Trades enden so, entscheidend ist die Summe.",
    "Ziel": "Das Ziel war ein Vielfaches des Risikos (R). Erreicht heißt: Gewinn größer als ein Stopp-Verlust.",
    "Schluss": "Daytrades werden vor Börsenschluss verkauft, damit nichts über Nacht passiert.",
}
LESSONS = [
    "R ist das Risiko eines Trades: Abstand von Einstieg zu Stopp. Ziel 2R heißt: doppelt so weit nach oben wie zum Stopp.",
    "Trefferquote allein sagt wenig. 40 % Treffer können reichen, wenn die Gewinne größer sind als die Verluste.",
    "Gebühren zählen: Bei 100 € Einsatz kostet 1 € je Order 2 % pro Trade. Ein Broker mit sehr kleinen Gebühren ist Pflicht.",
    "Prüftage sind Tage, die das System beim Lernen nicht gesehen hat. Nur dort zeigt sich, ob eine Regel wirklich funktioniert.",
    "Der Spread ist der Abstand zwischen Kauf- und Verkaufskurs. Bei viel gehandelten Aktien ist er klein.",
    "Volumen ist die Zahl gehandelter Aktien. Viel Volumen beim Ausbruch heißt: viele machen mit, das Signal ist stärker.",
    "Der VWAP ist der Durchschnittspreis des Tages, gewichtet nach Volumen. Viele Händler orientieren sich daran.",
    "Ein Monat beweist wenig. Erst viele Trades über mehrere Monate zeigen, ob eine Regel mehr als Glück ist.",
]


def lesson(day):
    return LESSONS[datetime.date.fromisoformat(day).toordinal() % len(LESSONS)]


def lab_module():
    spec = importlib.util.spec_from_file_location("trader_lab", os.path.join(HERE, "lab.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def do_live(cfg, now, force):
    et = scan.to_eastern(now)
    day = et.date().isoformat()
    owned = ["lab/live/%s.json" % day, "lab/decisions.json", "status/live.json"]
    steps = []
    old = read_json(status_path("live"), {}) or {}
    data = dict(old.get("data") or {}) if old.get("date_et") == day else {}
    # Ja/Nein aus dem Antwortkanal übernehmen (bleiben dauerhaft in decisions.json)
    dec_path = p(T, "lab", "decisions.json")
    decisions = read_json(dec_path, {}) or {}
    new_answers = 0
    try:
        for pid, a in read_answers(cfg).items():
            if decisions.get(pid, {}).get("ts") != a["ts"]:
                decisions[pid] = a
                new_answers += 1
        if new_answers:
            write_json(dec_path, decisions)
    except Exception as e:
        step(steps, "Antworten lesen", False, str(e)[:200])
    rc, ld, reason = run_json("live", ["lab.py", "live"], timeout=900)
    if ld is None or ld.get("error"):
        step(steps, "Labor live", False, (ld or {}).get("error") or reason)
        return False, "Labor live fehlgeschlagen", steps, data, owned
    step(steps, "Labor live", True, "%s Aktien, %s Spielgeld-Trades, %s offen" % (
        de_int(ld["symbols"]), de_int(ld["trades"]), de_int(ld["open"])))
    data.update({"date": day, "as_of": ld["as_of"], "trades": ld["trades"], "open": ld["open"],
                 "symbols": ld["symbols"], "failed": ld["failed"]})
    events = ld.get("events", [])
    if events:
        groups = {}
        for e in events:
            groups.setdefault((e["event"], e["symbol"], e["strategy"], e["why"] if e["event"] == "out" else ""),
                              []).append(e)
        n_in = sum(1 for k in groups if k[0] == "in")
        n_out = len(groups) - n_in
        lines, why = [], []
        for (ev, sym, strat, _), es in sorted(groups.items(), key=lambda kv: (kv[1][0]["in_k"], kv[0][0] != "in")):
            e = es[0]
            many = " (%d Varianten)" % len(es) if len(es) > 1 else ""
            if ev == "in":
                lines.append("Einstieg %s Uhr ET · %s %s · %s%s · Stopp %s · Ziel %s" % (
                    e["in_at"], sym, usd(e["entry"]), STRAT_SHORT[strat], many, usd(e["stop"]), usd(e["target"])))
                why.append(WHY_IN[strat])
            else:
                res = ", ".join("%s €" % de_num(x["eur"]) for x in es)
                lines.append("Ausstieg %s Uhr ET · %s %s · %s · %s bei 100 € pro Trade" % (
                    e["out_at"], sym, usd(e["exit"]), e["why"], res))
                why.append(WHY_OUT[e["why"]])
        seen = []
        for w in why:
            if w not in seen:
                seen.append(w)
        # Vorschläge: ein Push je Einstieg mit Ja/Nein, damit die Buttons eindeutig sind
        for (ev, sym, strat, _), es in groups.items():
            if ev != "in" or not reply_topic(cfg):
                continue
            e = es[0]
            pid = "%s-%s-%s" % (day.replace("-", ""), sym.replace(".", "_"), strat)
            risk_eur = (e["entry"] - e["stop"]) / e["entry"] * 100
            open_now = e["open"]
            msg = ["%s %s · Einstieg %s Uhr ET · %s" % (sym, usd(e["entry"]), e["in_at"], STRAT_SHORT[strat]),
                   "Stopp %s · Ziel %s · Risiko bei 100 €: %s €" % (usd(e["stop"]), usd(e["target"]),
                                                                     de_num(risk_eur)),
                   WHY_IN[strat],
                   "Ja = du hättest mitgemacht (zählt ab dem nächsten Kurs nach deiner Antwort). "
                   "Ohne Antwort zählt nur die Regel. Spielgeld."]
            if not open_now:
                msg.insert(1, "Schon beendet: %s %s Uhr ET" % (e["why"], e["out_at"]))
            push(cfg, "Vorschlag: %s (%s)" % (sym, STRAT_SHORT[strat]), "\n".join(msg), priority=4,
                 tags=["question"], actions=yes_no_actions(cfg, pid) if open_now else None)
        lines.append("Was heißt das? " + " ".join(seen[:2]))
        lines.append("Spielgeld (Testphase), kein echtes Geld.")
        if n_out:
            push(cfg, "Labor live: %d Einstieg%s, %d Ausstieg%s" % (n_in, "" if n_in == 1 else "e", n_out,
                                                                   "" if n_out == 1 else "e"),
                 "\n".join(lines), priority=3, tags=["chart_with_upwards_trend"])
    sess = scan.session(et.date())
    closed = sess and et.time() >= sess[1]
    if closed and data.get("eod") != day:
        lab = lab_module()
        sm = lab.day_summary(day) or {}
        data["eod"] = day
        lines = ["%s Spielgeld-Trades heute (alle %d Varianten zusammen)" % (de_int(sm.get("n_trades", 0)),
                                                                            len(lab.variants()))]
        for k, s in sorted((sm.get("by_strategy") or {}).items()):
            lines.append("%s: %s Trades, %s € bei 100 € pro Trade" % (STRAT_SHORT.get(k, k), de_int(s["n"]),
                                                                     de_num(s["eur"])))
        focus = [r for r in sm.get("variants", []) if r["id"] in sm.get("focus", [])]
        for r in focus[:3]:
            lines.append("Top-Variante %s: %s Trades, %s €" % (r["label"], de_int(r["n"]), de_num(r["eur"])))
        lk = (read_json(p(T, "lab", "live", "%s.json" % day), {}) or {}).get("lukas", [])
        if lk:
            done_lk = [t for t in lk if t.get("status") not in ("verpasst",)]
            lines.append("Deine Ja-Trades: %d, zusammen %s € bei 100 € pro Trade%s" % (
                len(done_lk), de_num(sum(t.get("eur", 0) for t in done_lk)),
                " (%d verpasst)" % (len(lk) - len(done_lk)) if len(lk) > len(done_lk) else ""))
        nein = [k for k, v in decisions.items() if k.startswith(day.replace("-", "")) and v["answer"] == "nein"]
        if nein:
            lines.append("Nein gesagt: %d" % len(nein))
        lines.append("Lektion: " + lesson(day))
        push(cfg, "Tagesbilanz Labor %s" % date_de(day), "\n".join(lines), priority=3, tags=["memo"])
        return True, "Tagesbilanz: %s Trades" % de_int(sm.get("n_trades", 0)), steps, data, owned
    if events or new_answers or force or et.minute % 30 < 10:   # sonst kein Commit, höchstens alle 30 Minuten
        return True, "%s Trades, %s offen" % (de_int(ld["trades"]), de_int(ld["open"])), steps, data, owned
    return None, "keine neuen Ereignisse", steps, data, owned


def render_live(out):
    st = read_json(status_path("live"), None)
    if not st:
        return
    day = (st.get("data") or {}).get("date")
    doc = read_json(p(T, "lab", "live", "%s.json" % day), None) if day else None
    if not doc:
        return
    labels = {v["id"]: v["label"] for v in lab_module().variants()}
    out += ["", "## Labor live – %s, Stand %s" % (date_de(day), doc.get("as_of")), "",
            "%s Aktien beobachtet · %s Spielgeld-Trades aller Varianten · %s offen" % (
                de_int(doc["symbols"]), de_int(doc["n_trades"]), de_int(doc["n_open"])), "",
            "| Top-Variante | Trades | offen | € bei 100 €/Trade |", "|---|---|---|---|"]
    for vid in doc.get("focus", []):
        pv = doc["per_variant"].get(vid, {"n": 0, "open": 0, "eur": 0})
        out.append("| %s | %s | %s | %s € |" % (labels.get(vid, vid), pv["n"], pv["open"], de_num(pv["eur"])))
    lk = doc.get("lukas", [])
    if lk:
        out += ["", "**Deine Ja-Trades heute** (Einstieg zum ersten Kurs nach deiner Antwort):", "",
                "| Aktie | Regel | Antwort | Einstieg | Stand | Ergebnis |", "|---|---|---|---|---|---|"]
        for t in lk:
            state = {"verpasst": "verpasst (Stopp oder Ziel schon erreicht)"}.get(t["status"]) or (
                "offen, Kurs %s" % usd(t.get("last")) if t["status"] == "offen" else "%s %s Uhr" % (t["why"], t["out_at"]))
            out.append("| %s | %s | %s Uhr ET | %s | %s | %s |" % (
                t["symbol"], STRAT_SHORT.get(t["strategy"], t["strategy"]), t["answer_at"],
                usd(t.get("entry")) if t.get("entry") else "–", state,
                "%s €" % de_num(t["eur"]) if t.get("eur") is not None else "–"))
    ft = [t for t in doc["trades"] if t["variant"] in doc.get("focus", [])]
    if ft:
        out += ["", "| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |", "|---|---|---|---|---|---|---|"]
        for t in ft[-20:]:
            state = "offen, Kurs %s" % usd(t["last"]) if t["open"] else "%s %s Uhr" % (t["why"], t["out_at"])
            out.append("| %s | %s | %s %s | %s | %s | %s | %s € |" % (
                t["symbol"], labels.get(t["variant"], t["variant"]).split(" · ")[0], t["in_at"], usd(t["entry"]),
                usd(t["stop"]), usd(t["target"]), state, de_num(t["eur"])))


def render_lab(out):
    res = read_json(p(T, "lab", "results.json"), None)
    if not res:
        return
    rows = res.get("variants", [])
    out += ["", "## Labor (Testphase, Spielgeld ohne Limit)", "",
            "%s Aktien · %s Handelstage · Lerntage %s bis %s · **Prüftage %s bis %s** · %s Varianten" % (
                de_int(res.get("symbols") or 0), de_int(res.get("days") or 0),
                date_de((res.get("train") or ["", ""])[0]), date_de((res.get("train") or ["", ""])[1]),
                date_de(res["test"][0]), date_de(res["test"][1]), de_int(len(rows))), "",
            "| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |",
            "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows[:12], 1):
        t = r["test"]
        if not t.get("n"):
            out.append("| %d | %s | 0 | – | – | – | – | – | nein |" % (i, r["label"]))
            continue
        out.append("| %d | %s | %s | %s %% | %s | %s € | %s € | %s | %s |" % (
            i, r["label"], de_int(t["n"]), de_num(t["win_rate"], 0), pct(t["avg_pct"]), de_num(t["eur"]),
            de_num(t["eur_after_fees"]), "unwahrscheinlich" if abs(t.get("t", 0)) >= 2 else "möglich",
            "**ja**" if r["passed"] else "nein"))
    out += ["", "So liest du das: Ein Trade ist ein Kauf und Verkauf am selben Tag. „Treffer“ ist der Anteil der "
            "Trades mit Plus. „€ bei 100 €/Trade“ ist die Summe, wenn jeder Trade mit 100 € gemacht worden wäre. "
            "„Zufall möglich“ heißt: zu wenige oder zu schwankende Trades, das Ergebnis kann Glück sein.", ""]
    for k, txt in (res.get("strategies") or {}).items():
        out.append("- **%s**" % txt)


# ---------------------------------------------------------------- Preisalarme

def ring_de(r, rules, quotes):
    rule = next((x for x in rules if x.get("id") == r.get("id")), {})
    sym, typ = r.get("symbol") or rule.get("symbol", ""), rule.get("type")
    q = quotes.get(sym)
    if typ == "opening_bell":
        return "Eröffnungsglocke: die NYSE hat geöffnet."
    if typ == "time":
        return "%s Uhr ET: %s" % (rule.get("at", "?"), rule.get("label") or "Zeitalarm")
    if typ in ("stop", "below"):
        return "%s %s: an oder unter %s %s" % (sym, usd(q), "deinem Stopp" if typ == "stop" else "der Marke",
                                               usd(rule.get("price")))
    if typ in ("target", "above"):
        return "%s %s: an oder über %s %s" % (sym, usd(q), "deinem Ziel" if typ == "target" else "der Marke",
                                              usd(rule.get("price")))
    if typ == "pct_move":
        return "%s %s: Bewegung von %s %% oder mehr seit gestern" % (sym, usd(q), de_num(rule.get("pct", 0), 1))
    return r.get("message", "Alarm")


def alert_rules():
    doc = read_json(p(T, "alerts.json"), {}) or {}
    return doc.get("rules") or []


def do_alerts(cfg, now, force):
    owned = ["state/alerts.json", "prices.json", "status/alerts.json"]
    steps, data = [], {}
    rules = alert_rules()
    if not rules:
        return None, "keine Alarme angelegt", steps, data, owned
    rc, doc, reason = run_json("alerts", ["alerts.py", "check", "--json"], timeout=300)
    if not doc:
        step(steps, "Preisalarme", False, reason)
        return False, reason, steps, data, owned
    rings = doc.get("rings", [])
    old = (read_json(status_path("alerts"), {}) or {}).get("data", {})
    texts = [ring_de(r, rules, doc.get("quotes", {})) for r in rings]
    history = ([{"at": now.isoformat() + "Z", "text": t} for t in texts] + old.get("history", []))[:30]
    data = {"history": history, "quotes": doc.get("quotes", {}), "market_open": (doc.get("market") or {}).get("open"),
            "errors": doc.get("errors", [])}
    step(steps, "Preisalarme", True, "%d Regeln geprüft, %d ausgelöst" % (len(rules), len(rings)))
    if rings and cfg["push_alerts"]:
        urgent = any((next((x for x in rules if x.get("id") == r.get("id")), {}).get("type") in ("stop", "time"))
                     for r in rings)
        push(cfg, "Preisalarm: " + ", ".join(sorted({r.get("symbol") or "NYSE" for r in rings})), "\n".join(texts),
             priority=5 if urgent else 4, tags=["rotating_light"])
    if not rings and not force:
        return None, "nichts ausgelöst", steps, data, owned   # kein Commit alle 15 Minuten
    return True, "%d ausgelöst" % len(rings), steps, data, owned


# ---------------------------------------------------------------- Ticker-Analyse

def do_ticker(cfg, now, symbol, add_alerts):
    owned = ["entry.json", "plan.json", "status/ticker.json"] + (["alerts.json", "state/alerts.json"] if add_alerts else [])
    sym = symbol.upper().strip()
    steps, data = [], {"symbol": sym}
    args = ["news.py", "--tickers", sym, "--json", "--all", "--hours", "72", "--dry-run"]
    if not os.environ.get("SEC_USER_AGENT"):
        args.append("--no-sec")
    rc, nd, reason = run_json("news", args, timeout=300)
    if nd is None:
        step(steps, "News", False, reason)
    else:
        data["news"] = {"items": nd.get("items", [])[:15], "moves": nd.get("moves", [])}
        dead = not nd.get("items") and not nd.get("moves") and nd.get("notes")
        step(steps, "News", not dead, "; ".join(nd["notes"])[:200] if dead else
             "%d Meldungen der letzten 72 Stunden" % len(nd.get("items", [])))

    rc, ed, reason = run_json("entry", ["entry.py", "check", sym, "--json", "--write", "%s/entry.json" % T], timeout=300)
    if ed is None:
        step(steps, "Einstieg", False, reason)
    else:
        orr, trig = ed.get("opening_range") or {}, ed.get("trigger") or {}
        data["entry"] = {"status": ed.get("status"), "phase": ed.get("phase"), "reason": ed.get("reason"),
                         "or_high": orr.get("high"), "or_low": orr.get("low"),
                         "time": trig.get("time"), "price": trig.get("price"), "date": ed.get("date")}
        step(steps, "Einstieg", True, ed.get("status", "?"))
        if ed.get("status") == "triggered":
            rc, xd, reason = run_json("exit", ["exit.py", "plan", "--json", "--write", "%s/plan.json" % T], timeout=300)
            if xd is None:
                step(steps, "Ausstiegsplan", False, reason)
            else:
                plan = read_json(p(T, "plan.json"), {}) or {}
                data["plan"] = {k: plan.get(k) for k in ("entry", "stop", "target", "risk_per_share",
                                                         "reward_risk", "flat_by", "stop_label", "target_label")}
                step(steps, "Ausstiegsplan", True, "Stopp %s, Ziel %s" % (usd(plan.get("stop")), usd(plan.get("target"))))
                if add_alerts:
                    rc, out, err = run("alerts-add", ["alerts.py", "add", "--from-plan"], timeout=60)
                    step(steps, "Alarme", rc == 0, "Stopp, Ziel und „flat by close“ angelegt" if rc == 0 else
                         (err or out).strip()[-200:])

    e = data.get("entry") or {}
    status_de = {"triggered": "ausgelöst", "waiting": "wartet", "expired": "abgelaufen",
                 "no-data": "keine Daten"}.get(e.get("status"), e.get("status") or "unbekannt")
    lines = []
    for m in (data.get("news") or {}).get("moves", [])[:1]:
        lines.append("Kurs %s (%s seit gestern)" % (usd(m.get("price")), pct(m.get("pct", 0))))
    if e:
        if e.get("or_high") is not None:
            lines.append("Eröffnungsspanne %s bis %s" % (usd(e["or_low"]), usd(e["or_high"])))
        lines.append("Einstiegsregel: %s" % status_de + (" um %s zu %s" % (e["time"], usd(e["price"]))
                                                        if e.get("status") == "triggered" else ""))
    pl = data.get("plan")
    if pl:
        lines.append("Plan: Stopp %s, Ziel %s, Risiko je Aktie %s, raus bis %s Uhr ET" % (
            usd(pl["stop"]), usd(pl["target"]), usd(pl["risk_per_share"]), pl.get("flat_by") or "15:55"))
    n = (data.get("news") or {}).get("items", [])
    if n:
        lines.append("Neueste Meldung: " + n[0].get("title", "")[:120])
    ok = all(s["ok"] for s in steps)
    if not ok:
        lines.append("Probleme: " + "; ".join("%s: %s" % (s["name"], s["detail"]) for s in steps if not s["ok"]))
    lines.append("Regelprüfung, keine Empfehlung. Order nur über /trader-risk und /trader-broker.")
    push(cfg, "Ticker %s: Einstiegsregel %s" % (sym, status_de), "\n".join(lines), priority=3, tags=["mag"])
    return ok, "%s: %s" % (sym, status_de), steps, data, owned


# ---------------------------------------------------------------- UEBERSICHT.md

def md_escape(s):
    return str(s or "").replace("|", "/").replace("\n", " ").strip()


def news_time(iso):
    try:
        dt = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
        utc = (dt - dt.utcoffset()).replace(tzinfo=None) if dt.tzinfo else dt
        et = scan.to_eastern(utc)
        return "%s %s Uhr ET" % (et.strftime("%d.%m."), et.strftime("%H:%M"))
    except (AttributeError, ValueError, TypeError):
        return "–"


def render():
    now = utcnow()
    et = scan.to_eastern(now)
    st = {k: read_json(status_path(k), None) for k in PART_DE}
    out = ["# Trader-Übersicht", "",
           "Stand: %s · wird bei jedem Lauf neu gebaut." % stamp(now), ""]
    sess = scan.session(et.date())
    if sess:
        o, c = sess
        state = ("offen" if o <= et.time() < c else "vor der Eröffnung" if et.time() < o else "geschlossen")
        out.append("NYSE heute: %s (Handelszeit %s bis %s Uhr ET)." % (state, o.strftime("%H:%M"), c.strftime("%H:%M")))
    else:
        why = scan.trading_day(et.date())[1]
        out.append("NYSE heute: geschlossen (%s)." % ("Wochenende" if why == "weekend" else
                                                      why.replace("NYSE holiday: ", "Feiertag: ")))
    out += ["", "## Systemstatus", "", "| Teil | Letzter Lauf | Ergebnis |", "|---|---|---|"]
    for k, name in PART_DE.items():
        s = st[k]
        if k == "test" and not s:
            continue
        if not s:
            out.append("| %s | noch nie | – |" % name)
            continue
        when = datetime.datetime.fromisoformat(s["ran_at"].rstrip("Z"))
        res = ("OK" if s["ok"] else "**FEHLER**") + " – " + md_escape(s["summary"])
        link = " ([Lauf](%s))" % s["run_url"] if s.get("run_url") else ""
        out.append("| %s | %s | %s%s |" % (name, stamp(when), res, link))
    bad = [(PART_DE[k], x) for k in PART_DE if st[k] for x in st[k]["steps"] if not x["ok"]]
    if bad:
        out += ["", "**Probleme:**"] + ["- %s / %s: %s" % (a, x["name"], md_escape(x["detail"])) for a, x in bad]
    out += ["", "Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, "
            "Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, "
            "Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET)."]

    # Morgen-Scan
    wl = read_json(p(T, "watchlist.json"), None)
    md = ((st["morning"] or {}).get("data") or {})
    if wl and wl.get("mode") == "daily":
        hits = wl.get("hits", [])
        d = md.get("daily") or {}
        out += ["", "## Morgen-Scan – Schlusskurse vom %s" % date_de(wl.get("as_of", "")), ""]
        if d:
            out.append("%s Aktien in der Liste · %s Charts geladen · %s liquide (ab 5 $ und 1.000.000 Aktien) · "
                       "%s gescannt · **%s passen zu einer Regel**" % (
                           de_int(d.get("universe") or 0), de_int(d.get("fetched") or 0), de_int(d.get("liquid") or 0),
                           de_int(d.get("scanned") or 0), de_int(len(hits))))
        out += ["", "| Regel | Anzahl | Meistgehandelt |", "|---|---|---|"]
        for k in SETUP_ORDER:
            sel = [h for h in hits if k in h.get("setups", [])]
            out.append("| `%s` | %s | %s |" % (k, de_int(len(sel)), ", ".join(h["symbol"] for h in sel[:8]) or "–"))
        out += ["", "**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):", "",
                "| Ticker | Kurs | RSI | Regeln |", "|---|---|---|---|"]
        for h in hits[:20]:
            out.append("| %s | %s | %s | %s |" % (h["symbol"], usd(h.get("price")),
                                                  de_num(h["rsi"], 1) if h.get("rsi") is not None else "–",
                                                  ", ".join("`%s`" % s for s in h.get("setups", []))))
        out.append("")
        out.append("Alle %s Treffer: [watchlist.json](watchlist.json)" % de_int(len(hits)))

    # ORB
    orb = read_json(p(T, "orb.json"), None)
    if orb and orb.get("mode") == "orb":
        od = ((st["orb"] or {}).get("data") or {}).get("orb") or {}
        hits = orb.get("hits", [])
        out += ["", "## ORB-Scan – %s" % md_escape(orb.get("as_of")), ""]
        out.append("Quelle: %s · %s nutzbare Charts · **%s über der Eröffnungsspanne**" % (
            od.get("source", "?"), de_int(orb.get("scanned") or 0), de_int(len(hits))))
        if orb.get("unconfirmed"):
            out.append("")
            out.append("TEILWEISE: %s Kandidaten wurden nicht geprüft." % de_int(orb["unconfirmed"]))
        if hits:
            out += ["", "| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |", "|---|---|---|---|---|"]
            for h in hits[:30]:
                out.append("| %s | %s | %s | %s – %s | %s |" % (h.get("at", "?"), h["symbol"], usd(h["price"]),
                                                              usd(h["or_low"]), usd(h["or_high"]), pct(h["pct_over"])))
            if len(hits) > 30:
                out.append("")
                out.append("… und %s weitere in [orb.json](orb.json)." % de_int(len(hits) - 30))
            out += ["", "Ein späterer Treffer liegt näher am aktuellen Kurs."]

    # News
    nd = md.get("news")
    if nd:
        out += ["", "## News zu den ersten %d Treffern (letzte 24 Stunden, nur neue)" % len(nd["tickers"]), ""]
        moving = [m for m in nd.get("moves", []) if m.get("moving")]
        if nd.get("moves"):
            out.append("Bewegung seit gestern: " + " · ".join(
                ("**%s %s**" if m.get("moving") else "%s %s") % (m["ticker"], pct(m["pct"])) for m in nd["moves"]))
            out.append("")
        if not nd["items"]:
            out.append("Keine neuen Meldungen.")
        for it in nd["items"][:25]:
            tags = ", ".join(it.get("tags") or [])
            out.append("- %s · **%s** · [%s](%s)%s" % (news_time(it.get("time")), it.get("ticker"),
                                                      md_escape(it.get("title")), it.get("link"),
                                                      " · " + tags if tags else ""))
        for n in nd.get("notes", []):
            out.append("- Hinweis: %s" % md_escape(n))

    # Pelosi
    pl = md.get("pelosi")
    if pl is not None:
        out += ["", "## Pelosi-Tracker (%s)" % ", ".join(pl["members"]), ""]
        if not pl["new"]:
            out.append("Keine neue Meldung seit dem letzten Lauf.")
        for r in pl["new"]:
            out.append("- %s · %s (%s) · [PDF](%s)" % (date_de(r.get("filed")), md_escape(r.get("name")),
                                                       r.get("district", ""), r.get("url")))
        out.append("")
        out.append("Meldungen kommen Tage bis Wochen nach dem Handel und nennen nur Betragsspannen.")

    # Ticker-Analyse
    td = (st["ticker"] or {}).get("data") or {}
    if td.get("symbol"):
        out += ["", "## Ticker-Analyse: %s" % td["symbol"], ""]
        e = td.get("entry") or {}
        if e:
            out.append("- Einstiegsregel (Opening-Range-Ausbruch): **%s**%s" % (
                {"triggered": "ausgelöst", "waiting": "wartet", "expired": "abgelaufen",
                 "no-data": "keine Daten"}.get(e.get("status"), e.get("status")),
                " um %s zu %s" % (e["time"], usd(e["price"])) if e.get("status") == "triggered" else ""))
            if e.get("or_high") is not None:
                out.append("- Eröffnungsspanne: %s bis %s" % (usd(e["or_low"]), usd(e["or_high"])))
            if e.get("reason"):
                out.append("- Grund (Originaltext): %s" % md_escape(e["reason"]))
        pln = td.get("plan")
        if pln:
            out.append("- Plan: Einstieg %s · Stopp %s · Ziel %s · Risiko je Aktie %s · raus bis %s Uhr ET" % (
                usd(pln["entry"]), usd(pln["stop"]), usd(pln["target"]), usd(pln["risk_per_share"]),
                pln.get("flat_by") or "15:55"))
        for it in (td.get("news") or {}).get("items", [])[:8]:
            out.append("- %s · [%s](%s)" % (news_time(it.get("time")), md_escape(it.get("title")), it.get("link")))

    render_live(out)
    render_lab(out)

    # Alarme
    rules = alert_rules()
    ad = ((st["alerts"] or {}).get("data") or {})
    out += ["", "## Preisalarme", ""]
    if not rules:
        out.append("Keine Alarme angelegt. Eine Ticker-Analyse mit „Alarme setzen“ legt Stopp, Ziel und "
                   "„flat by close“ aus dem Plan an.")
    else:
        out += ["| Alarm | Ticker | Art | Marke | Tag |", "|---|---|---|---|---|"]
        for r in rules:
            mark = usd(r["price"]) if r.get("price") is not None else (
                r.get("at") or ("%s %%" % de_num(r["pct"], 1) if r.get("pct") is not None else "–"))
            out.append("| %s | %s | %s | %s | %s |" % (r.get("id"), r.get("symbol", "–"), r.get("type"), mark,
                                                       date_de(r["date"]) if r.get("date") else "jeden Tag"))
    for h in ad.get("history", [])[:10]:
        when = datetime.datetime.fromisoformat(h["at"].rstrip("Z"))
        out.append("- %s: %s" % (stamp(when), md_escape(h["text"])))

    out += ["", "## Bedienung", "",
            "- **Manuell starten:** GitHub → Actions → „Trader-System“ → „Run workflow“ → Teil wählen "
            "(bei „ticker“ den Ticker eintragen). Oder Claude im Chat bitten.",
            "- **Push aufs iPhone:** App „ntfy“, Kanal aus `trader/system.json` abonnieren.",
            "- **Einstellungen:** `trader/system.json`.",
            "", "## Regeln (Legende)", ""]
    for k, v in SETUP_DE.items():
        out.append("- `%s`: %s" % (k, v))
    out += ["", "---", "", NOTE_DE + " Kostenlose Yahoo-Daten, verzögert und inoffiziell, nicht in Echtzeit. "
            "Ein Treffer ist veraltet, sobald der Kurs weitergelaufen ist. Das System platziert keine Orders "
            "und gibt keine Kaufempfehlung.", ""]
    with open(p(T, "UEBERSICHT.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))


# ---------------------------------------------------------------- Commit & Push

def git(*args, check=True):
    r = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(args), r.stderr.strip()))
    return r


def publish(owned, message):
    """Eigene Dateien auf den neuesten Stand des Branches legen, Übersicht neu bauen, pushen.
    Mehrere Läufe gleichzeitig überschreiben sich so nicht gegenseitig."""
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    keep = {}
    for rel in owned:
        path = p(T, rel)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                keep[rel] = fh.read()
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898283+github-actions[bot]@users.noreply.github.com")
    for attempt in range(5):
        git("fetch", "-q", "origin", branch)
        git("reset", "-q", "--hard", "FETCH_HEAD")
        for rel, blob in keep.items():
            os.makedirs(os.path.dirname(p(T, rel)), exist_ok=True)
            with open(p(T, rel), "wb") as fh:
                fh.write(blob)
        render()
        git("add", "-A", T)
        if not git("diff", "--cached", "--quiet", check=False).returncode:
            print("Nichts zu committen.")
            return
        git("commit", "-q", "-m", message + " [skip ci]")
        if git("push", "-q", "origin", "HEAD:" + branch, check=False).returncode == 0:
            print("Gepusht nach %s." % branch)
            return
        time.sleep(2 * (attempt + 1))
    raise RuntimeError("Push nach %s fünfmal fehlgeschlagen" % branch)


# ---------------------------------------------------------------- Ablauf

def main(argv=None):
    ap = argparse.ArgumentParser(description="Trader-System auf GitHub Actions")
    ap.add_argument("part", choices=["auto", "morning", "orb", "live", "lab", "alerts", "ticker", "test", "render"])
    ap.add_argument("symbol", nargs="?")
    ap.add_argument("--force", action="store_true", help="Zeitfenster und „heute schon gelaufen“ ignorieren")
    ap.add_argument("--alerts", action="store_true", help="bei ticker: Alarme aus dem Plan anlegen")
    ap.add_argument("--no-publish", action="store_true")
    a = ap.parse_args(argv)
    os.chdir(ROOT)
    cfg = config()
    if a.part == "render":
        render()
        return 0

    now = utcnow()
    et = scan.to_eastern(now)
    trading, _ = scan.trading_day(et.date())
    jobs = []
    if a.part == "auto":
        t = et.time()
        if trading and MORNING_WINDOW[0] <= t <= MORNING_WINDOW[1] and not done_today("morning", et.date()):
            jobs.append("morning")
        if trading and ORB_WINDOW[0] <= t <= ORB_WINDOW[1] and not done_today("orb", et.date()):
            jobs.append("orb")
        lab_due = trading and LAB_WINDOW[0] <= t <= LAB_WINDOW[1] and not done_today("lab", et.date())
        sess = scan.session(et.date())
        if sess:
            o_dt = datetime.datetime.combine(et.date(), sess[0]) + datetime.timedelta(minutes=5)
            c_dt = datetime.datetime.combine(et.date(), sess[1]) + datetime.timedelta(minutes=60)
            live_old = read_json(status_path("live"), {}) or {}
            eod_done = (live_old.get("data") or {}).get("eod") == et.date().isoformat()
            if o_dt.time() <= t <= c_dt.time() and not (t >= sess[1] and eod_done):
                jobs.append("live")
        if lab_due:
            jobs.append("lab")
        if sess and sess[0] <= t <= (datetime.datetime.combine(et.date(), sess[1]) +
                                     datetime.timedelta(minutes=15)).time():
            jobs.append("alerts")
        if not jobs:
            print("Nichts fällig (%s)." % stamp(now))
            return 0
    elif a.part == "ticker":
        if not a.symbol:
            ap.error("ticker braucht ein Symbol, z. B. ticker TSLA")
        jobs.append("ticker")
    else:
        jobs.append(a.part)

    owned, done, failed = [], [], []
    force = a.part != "auto"
    for job in jobs:
        LOG.clear()
        try:
            if job == "test":
                try:
                    last = read_answers(cfg).get("test")
                except Exception:
                    last = None
                seen = ("Deine letzte Test-Antwort ist angekommen: „%s“ um %s." % (
                    last["answer"], stamp(datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=last["ts"])))
                    if last else "Tippe auf Ja oder Nein und starte den Test noch einmal: dann steht hier deine Antwort.")
                ok = push(cfg, "Trader-System: Test", "Die Push-Nachrichten kommen an. Stand: %s\n%s" % (stamp(now), seen),
                          priority=3, tags=["white_check_mark"],
                          actions=yes_no_actions(cfg, "test") if reply_topic(cfg) else None)
                res = (ok, "Push gesendet" if ok else "Push nicht gesendet", [], {}, ["status/test.json"])
            elif job == "ticker":
                res = do_ticker(cfg, now, a.symbol, a.alerts)
            else:
                res = {"morning": do_morning, "orb": do_orb, "live": do_live, "lab": do_lab,
                       "alerts": do_alerts}[job](cfg, now, force)
            ok, summary, steps, data, own = res
        except Exception as e:
            traceback.print_exc()
            ok, summary, steps, data, own = False, "Absturz: %s" % e, [{"name": job, "ok": False, "detail": str(e)}], {}, \
                ["status/%s.json" % job]
        before = read_json(status_path(job), {}) or {}
        failed_before = before.get("date_et") == et.date().isoformat() and not before.get("ok")
        if ok is None:                 # nichts zu tun, nichts speichern
            print("%s: %s" % (PART_DE[job], summary))
            continue
        save_status(job, ok, summary, steps, data, now)
        os.makedirs(p(T, "logs"), exist_ok=True)
        with open(p(T, "logs", job + ".txt"), "w", encoding="utf-8") as fh:
            fh.write("%s – %s\n\n%s" % (PART_DE[job], stamp(now), "\n".join(LOG)))
        owned += own + ["logs/%s.txt" % job]
        done.append(job)
        if not ok:
            failed.append((job, summary))
            # derselbe Fehler am selben Tag nur einmal melden
            # der Morgen-Scan meldet Teilprobleme schon in seinem eigenen Push
            pushed = job == "morning" and (data or {}).get("daily")
            if cfg["push_errors"] and job in ("morning", "orb", "live", "lab", "alerts") and not failed_before and not pushed:
                bad = [s for s in steps if not s["ok"]]
                push(cfg, "Trader-System: Problem beim %s" % PART_DE[job],
                     "\n".join("%s: %s" % (s["name"], s["detail"]) for s in bad) or summary,
                     priority=4, tags=["warning"])
    if "lab" in done and os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            fh.write("lab_ran=true\n")
    if not done:
        return 0
    if a.no_publish or not os.environ.get("GITHUB_ACTIONS"):
        render()
        print("Lokal: nicht committet.")
    else:
        publish(sorted(set(owned)), "trader: " + ", ".join(done) + " " + now.strftime("%Y-%m-%dT%H:%MZ"))
    return 0   # Fehler sind schon gemeldet (Push + Übersicht); Exit 1 nur bei Absturz


if __name__ == "__main__":
    sys.exit(main())
