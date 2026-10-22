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

SETUP_DE = {
    "breakout_20d": "Schlusskurs über jedem Schlusskurs der 20 Tage davor",
    "bull_flag": "über 10 % gestiegen, dann 5 Tage in einer 5-%-Spanne",
    "reclaim_ma20": "gestern unter, heute über dem 20-Tage-Schnitt",
    "oversold": "RSI 14 unter 30",
    "oversold_bounce": "RSI gestern unter 30, heute im Plus geschlossen",
    "orb": "5-Minuten-Kerze schließt über dem Hoch der ersten 15 Minuten",
}
SETUP_ORDER = ["breakout_20d", "bull_flag", "reclaim_ma20", "oversold", "oversold_bounce"]
PART_DE = {"morning": "Morgen-Scan", "orb": "ORB-Scan", "alerts": "Preisalarme",
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

def push(cfg, title, message, priority=3, tags=None):
    topic = os.environ.get("NTFY_TOPIC") or cfg.get("ntfy_topic")
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
            step(steps, "Aktienliste", True, "neu geladen: " + (kept[0].split(" US-")[0].replace("Kept ", "") +
                                                                 " Aktien" if kept else "ok"))
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
            "Preisalarme alle 15 Minuten während der Handelszeit."]

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
    ap.add_argument("part", choices=["auto", "morning", "orb", "alerts", "ticker", "test", "render"])
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
        sess = scan.session(et.date())
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
                ok = push(cfg, "Trader-System: Test", "Die Push-Nachrichten kommen an. Stand: %s" % stamp(now),
                          priority=3, tags=["white_check_mark"])
                res = (ok, "Push gesendet" if ok else "Push nicht gesendet", [], {}, ["status/test.json"])
            elif job == "ticker":
                res = do_ticker(cfg, now, a.symbol, a.alerts)
            else:
                res = {"morning": do_morning, "orb": do_orb, "alerts": do_alerts}[job](cfg, now, force)
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
            if cfg["push_errors"] and job in ("morning", "orb", "alerts") and not failed_before and not pushed:
                bad = [s for s in steps if not s["ok"]]
                push(cfg, "Trader-System: Problem beim %s" % PART_DE[job],
                     "\n".join("%s: %s" % (s["name"], s["detail"]) for s in bad) or summary,
                     priority=4, tags=["warning"])
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
