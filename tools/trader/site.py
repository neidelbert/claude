#!/usr/bin/env python3
"""Baut die private Webseite des Trader-Systems (GitHub Pages).

    python3 tools/trader/site.py build            # -> _site/ (index.html, data.enc, manifest, icon)
    python3 tools/trader/site.py build --plain    # zusätzlich data.json unverschlüsselt (nur lokal testen!)

Alle Daten der Seite stehen in data.enc, verschlüsselt mit dem Passwort aus dem Secret SITE_PASSWORD
(PBKDF2-SHA256 -> AES-256-GCM). Die Seite entschlüsselt im Browser. Ohne Passwort wird keine Datendatei
gebaut, die Seite zeigt dann nur „Einrichtung fehlt“.
Braucht das Paket „cryptography“ (im Workflow per pip).
"""

import argparse
import base64
import datetime
import importlib.util
import json
import os
import shutil
import struct
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
T = os.path.join(ROOT, "trader")
SRC = os.path.join(ROOT, "site")
OUT = os.path.join(ROOT, "_site")
ITERATIONS = 200000       # PBKDF2-Runden; die Seite rechnet mit demselben Wert (steht in data.enc)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


scan = _load("trader_scan", os.path.join(HERE, "scan.py"))
sim = _load("trader_sim", os.path.join(HERE, "sim.py"))
lab = _load("trader_lab", os.path.join(HERE, "lab.py"))
system = _load("trader_system", os.path.join(HERE, "system.py"))


def rj(*parts, default=None):
    try:
        with open(os.path.join(T, *parts), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


GLOSSARY = {
    "Daytrading": "Kaufen und am selben Tag wieder verkaufen. Nichts bleibt über Nacht liegen.",
    "Spielgeld": "Virtuelles Geld. Alles wird so gerechnet, als wäre es echt, aber kein Euro verlässt dein Konto.",
    "Testphase": "Die erste Phase: Spielgeld ohne jedes Limit. Viele Regeln laufen parallel, das System misst und lernt.",
    "Simulator": "Die zweite Phase: 100 € Spielgeld, als wären sie echt, mit Verlustgrenzen und Gebühren.",
    "Variante": "Eine Regel mit festen Einstellungen, z. B. „Ausbruch nach 15 Minuten, Ziel 2R“. Das Labor testet 58 davon.",
    "Opening Range": "Die Spanne aus Hoch und Tief der ersten 15 oder 30 Minuten nach Börsenstart (9:30 Uhr New York).",
    "Ausbruch": "Der Kurs schließt über dem Hoch einer Spanne. Das deutet an, dass Käufer gerade stärker sind.",
    "News-Sprung": "Eine Aktie startet wegen einer Nachricht deutlich höher als am Vortag, mit viel Umsatz.",
    "Erholung": "Eine stark gefallene Aktie steigt wieder. Gegen den Trend: trifft seltener, springt dafür oft stärker.",
    "Stopp": "Der Preis, bei dem verkauft wird, wenn es schiefgeht. Er begrenzt den Verlust.",
    "Ziel": "Der Preis, bei dem mit Gewinn verkauft wird.",
    "R": "Das Risiko eines Trades: Abstand vom Einstieg zum Stopp. Ziel 2R heißt: doppelt so weit nach oben wie zum Stopp.",
    "Trefferquote": "Anteil der Trades, die mit Plus enden. Allein sagt sie wenig: 40 % reichen, wenn Gewinne größer sind als Verluste.",
    "Prüftage": "Tage, die das System beim Lernen nicht gesehen hat. Nur dort zeigt sich, ob eine Regel wirklich funktioniert.",
    "Lerntage": "Die älteren Tage, an denen das System die Varianten ausprobiert.",
    "Zufallswert": "Der t-Wert. Ab etwa 2 ist ein Ergebnis wahrscheinlich kein Glück mehr. Darunter kann es Zufall sein.",
    "Spread": "Abstand zwischen Kauf- und Verkaufskurs. Jeder Trade zahlt ihn. Bei viel gehandelten Aktien ist er klein.",
    "Gebühr": "Was der Broker je Order verlangt. Bei 100 € Einsatz kosten 1 € je Order 2 % pro Trade.",
    "Volumen": "Die Zahl gehandelter Aktien. Viel Volumen heißt: viele machen mit, ein Signal ist stärker.",
    "VWAP": "Der Durchschnittspreis des Tages, gewichtet nach Volumen. Viele Händler orientieren sich daran.",
    "RSI": "Ein Maß von 0 bis 100 für die letzten 14 Tage. Unter 30 gilt eine Aktie als „überverkauft“, also stark gefallen.",
    "Lücke": "Die Aktie öffnet deutlich über oder unter dem Schlusskurs vom Vortag.",
    "ET": "Uhrzeit in New York (Eastern Time). Meist 6 Stunden hinter deutscher Zeit.",
    "Ticker": "Kurzname einer Aktie, z. B. AAPL für Apple.",
    "Broker": "Die Bank oder App, über die du Aktien kaufst, z. B. Trade Republic.",
}

HOW = [
    ["Morgens", "Vor Börsenstart scannt das System rund 6.000 US-Aktien und sucht Charts, die zu einer Regel passen. Dazu holt es News."],
    ["Börsenstart", "Ab 15:30 Uhr deutscher Zeit prüft das Labor alle 10 Minuten 58 Varianten an rund 180 viel gehandelten Aktien."],
    ["Vorschlag", "Löst eine Top-Variante aus, kommt ein Push mit Ja/Nein. Ohne Antwort zählt nur die Regel. Mit Ja zählt der Trade auch für dich."],
    ["Ausstieg", "Jeder Trade endet am Stopp, am Ziel oder spätestens um 15:55 Uhr New York (21:55 Uhr bei uns)."],
    ["Abends", "Tagesbilanz als Push. Danach rechnet das Labor alle Varianten an den letzten 60 Tagen neu und erstellt die Rangliste."],
    ["Lernen", "Eine Variante zählt nur, wenn sie auch an ungesehenen Prüftagen im Plus ist. So fallen Glückstreffer heraus."],
]


PRO_RULES = [
    ["Nur Aktien, die „im Spiel“ sind", "Profis handeln Aktien mit ungewöhnlich viel Umsatz und einem Grund (News, Zahlen). "
     "Das Labor testet das mit „Stocks in Play“."],
    ["Risiko vorher festlegen", "Vor jedem Trade steht fest, wo der Stopp liegt und wie viel höchstens verloren geht. "
     "Üblich sind 0,25 bis 1 % des Kontos je Trade; im Simulator sind es 3 € von 100 €."],
    ["Tagesgrenze", "Ist die Tagesgrenze erreicht, ist Schluss für heute. Verluste nie „zurückholen“ wollen."],
    ["Wenige, gute Trades", "Lieber 1 bis 3 Trades nach Plan als viele aus dem Bauch. Gebühren fressen sonst alles."],
    ["Nichts über Nacht", "Daytrades werden vor Börsenschluss verkauft."],
    ["Tagebuch führen", "Jeder Trade wird aufgeschrieben und ausgewertet. Das macht dieses System automatisch."],
    ["Ehrlich messen", "Eine Regel zählt erst, wenn sie an vielen ungesehenen Tagen nach Kosten im Plus ist."],
]


def latest_weekly():
    d = os.path.join(T, "lab", "weekly")
    if not os.path.isdir(d):
        return None
    files = sorted(f for f in os.listdir(d) if f.endswith(".json"))
    return rj("lab", "weekly", files[-1]) if files else None


def market_info(now):
    et = scan.to_eastern(now)
    d = et.date()
    sess = scan.session(d)
    info = {"date": d.isoformat(), "now_et": et.strftime("%H:%M")}
    if sess:
        o = scan.eastern_to_utc(datetime.datetime.combine(d, sess[0]))
        c = scan.eastern_to_utc(datetime.datetime.combine(d, sess[1]))
        info.update(open_utc=o.isoformat() + "Z", close_utc=c.isoformat() + "Z", open_et=sess[0].strftime("%H:%M"),
                    close_et=sess[1].strftime("%H:%M"))
    else:
        info["closed_reason"] = "Wochenende" if d.weekday() >= 5 else scan.trading_day(d)[1].replace(
            "NYSE holiday: ", "Feiertag: ")
    nd = d + datetime.timedelta(days=1)
    while not scan.session(nd):
        nd += datetime.timedelta(days=1)
    info["next_open_utc"] = scan.eastern_to_utc(datetime.datetime.combine(nd, datetime.time(9, 30))).isoformat() + "Z"
    return info


def history():
    rows = []
    live_dir = os.path.join(T, "lab", "live")
    if not os.path.isdir(live_dir):
        return rows
    for f in sorted(os.listdir(live_dir)):
        if not f.endswith(".json"):
            continue
        doc = rj("lab", "live", f, default=None)
        if not doc:
            continue
        focus = doc.get("focus") or []
        top = doc["per_variant"].get(focus[0], {}) if focus else {}
        lk = [t for t in doc.get("lukas", []) if t.get("eur") is not None]
        rows.append({"date": doc["date"], "n": doc.get("n_trades", 0),
                     "all_eur": round(sum(p["eur"] for p in doc["per_variant"].values()), 2),
                     "top_eur": top.get("eur", 0), "top_n": top.get("n", 0),
                     "lukas_eur": round(sum(t["eur"] for t in lk), 2), "lukas_n": len(lk)})
    return rows


def journal(today, labels):
    """Tagebuch der letzten Live-Tage (ohne heute): Trades der Top-Varianten und deine Ja-Trades."""
    live_dir = os.path.join(T, "lab", "live")
    if not os.path.isdir(live_dir):
        return []
    out = []
    for f in sorted(os.listdir(live_dir))[-15:]:
        doc = rj("lab", "live", f, default=None)
        if not doc or doc["date"] == today:
            continue
        focus = doc.get("focus", [])
        out.append({"date": doc["date"], "focus": focus,
                    "trades": [{k: t.get(k) for k in ("variant", "strategy", "symbol", "in_at", "out_at", "entry", "stop",
                                                      "target", "exit", "why", "eur", "open", "in_k", "out_k")}
                               for t in doc.get("trades", []) if t["variant"] in focus[:3]],
                    "lukas": doc.get("lukas", [])})
    return out[::-1]


def build_data(cfg):
    now = system.utcnow()
    st = {k: rj("status", k + ".json") for k in system.PART_DE}
    status = []
    for k, name in system.PART_DE.items():
        s = st.get(k)
        if k == "test" and not s:
            continue
        status.append({"part": k, "name": name, "ok": (s or {}).get("ok"), "summary": (s or {}).get("summary"),
                       "ran_at": (s or {}).get("ran_at"), "steps": [x for x in (s or {}).get("steps", []) if not x["ok"]]})
    labels = {v["id"]: v["label"] for v in lab.variants()}
    decisions = rj("lab", "decisions.json", default={}) or {}
    live_day = ((st.get("live") or {}).get("data") or {}).get("date")
    live = rj("lab", "live", "%s.json" % live_day) if live_day else None
    proposals = []
    if live:
        focus = live.get("focus", [])
        live["trades"] = [t for t in live["trades"] if t["variant"] in focus]
        live["per_variant"] = {k: v for k, v in live["per_variant"].items() if k in focus}
        seen = set()
        for t in live["trades"]:
            pid = "%s-%s-%s" % (live["date"].replace("-", ""), t["symbol"].replace(".", "_"), t["strategy"])
            t["pid"] = pid
            if t["open"] and pid not in decisions and pid not in seen:
                seen.add(pid)
                proposals.append(t)
    res = rj("lab", "results.json") or {}
    keep = ("id", "strategy", "label", "train", "test", "passed")
    labd = {k: res.get(k) for k in ("created_at", "symbols", "days", "train", "test", "n_train_days", "n_test_days",
                                    "settings", "strategies")}
    labd["variants"] = [{k: r[k] for k in keep} for r in res.get("variants", [])]
    labd["curves"] = res.get("curves", {})
    wl = rj("watchlist.json") or {}
    md = (st.get("morning") or {}).get("data") or {}
    orb = rj("orb.json") or {}
    td = (st.get("ticker") or {}).get("data") or {}
    hits = wl.get("hits", []) if wl.get("mode") == "daily" else []
    return {
        "generated_at": now.isoformat() + "Z", "phase": "Testphase", "market": market_info(now), "status": status,
        "labels": labels, "live": live, "proposals": proposals, "history": history(), "lab": labd,
        "decisions": {k: v for k, v in decisions.items() if k != "test"},
        "notes": rj("lab", "notes.json", default={}) or {},
        "morning": {"as_of": wl.get("as_of"), "daily": md.get("daily"), "hits": hits[:30],
                    "per_setup": {k: [h["symbol"] for h in hits if k in h.get("setups", [])][:12]
                                  for k in system.SETUP_ORDER},
                    "counts": {k: sum(1 for h in hits if k in h.get("setups", [])) for k in system.SETUP_ORDER},
                    "news": (md.get("news") or {}).get("items", [])[:30], "moves": (md.get("news") or {}).get("moves", []),
                    "pelosi": md.get("pelosi")},
        "orb": {"as_of": orb.get("as_of"), "scanned": orb.get("scanned"), "hits": orb.get("hits", [])[:40]}
        if orb.get("mode") == "orb" else None,
        "ticker": td or None,
        "learn": {"lesson": system.lesson(scan.to_eastern(now).date().isoformat()), "lessons": system.LESSONS,
                  "glossary": GLOSSARY, "how": HOW, "setups": system.SETUP_DE,
                  "strategies": res.get("strategies") or lab.STRATEGY_DE},
        "experiment": dict(zip(("day", "days"), system.experiment_day(cfg, scan.to_eastern(now).date().isoformat())),
                           start=(cfg.get("experiment") or {}).get("start")),
        "go": system.go_checks(cfg),
        "live_days": [{k: v for k, v in d.items() if k != "champ_pcts"} | {"n_champ": len(d["champ_pcts"]),
                      "wins": sum(1 for x in d["champ_pcts"] if x > 0)} for d in system.live_days(cfg)],
        "patterns": res.get("patterns", []),
        "accounts": {k: v for k, v in (res.get("accounts") or {}).items() if k == res.get("champion")},
        "champion": res.get("champion"),
        "sim": sim.compute(),
        "journal": journal(live_day if live else "", labels),
        "settings": {"sim": sim.settings(), "news_top": cfg.get("news_top"), "pelosi": cfg.get("pelosi_members"),
                     "orb_source": cfg.get("orb_source"), "push_topic": os.environ.get("NTFY_TOPIC") or cfg.get("ntfy_topic"),
                     "schedule": [["ca. 14:00 Uhr", "Morgen-Scan, News, Pelosi"], ["15:30 bis 22:00 Uhr", "Labor live alle 10 Minuten, Vorschläge, Alarme"],
                                  ["ca. 22:10 Uhr", "Tagesbilanz"], ["ab ca. 22:20 Uhr", "Labor rechnet die Rangliste neu"],
                                  ["Freitagabend", "Wochen-Rückblick"]]},
        "changes": (rj("lab", "changes.json", default=[]) or [])[-30:][::-1],
        "weekly": latest_weekly(),
        "rules": PRO_RULES,
        "reply": {"server": cfg["ntfy_server"], "topic": system.reply_topic(cfg)},
        "push_topic": os.environ.get("NTFY_TOPIC") or cfg.get("ntfy_topic"),
    }


def encrypt(doc, password, salt_hex):
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    salt = bytes.fromhex(salt_hex)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS).derive(password.encode())
    iv = os.urandom(12)
    ct = AESGCM(key).encrypt(iv, json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), None)
    b = lambda x: base64.b64encode(x).decode()
    return {"v": 1, "kdf": "PBKDF2-SHA256", "iter": ITERATIONS, "salt": b(salt), "iv": b(iv), "ct": b(ct)}


def encrypt_pub(doc, keyfile):
    """Ohne Secret: Daten mit zufälligem AES-Schlüssel verschlüsseln, diesen mit dem öffentlichen RSA-Schlüssel.
    Den privaten Schlüssel (mit Lukas' Passwort verschlüsselt) legt die Datei bei; nur das Passwort öffnet alles."""
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    with open(keyfile, encoding="utf-8") as fh:
        kf = json.load(fh)
    pub = serialization.load_der_public_key(base64.b64decode(kf["pub"]))
    dk = AESGCM.generate_key(bit_length=256)
    iv = os.urandom(12)
    ct = AESGCM(dk).encrypt(iv, json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), None)
    ek = pub.encrypt(dk, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    b = lambda x: base64.b64encode(x).decode()
    p = kf["priv"]
    return {"v": 2, "kdf": "PBKDF2-SHA256", "iter": p["iter"], "salt": p["salt"], "kiv": p["iv"], "kct": p["ct"],
            "ek": b(ek), "iv": b(iv), "ct": b(ct)}


def png(size, path):
    """App-Symbol: dunkelblaues Quadrat mit steigender grüner Linie (ohne Bildbibliothek)."""
    pts = [(0.18, 0.70), (0.38, 0.52), (0.52, 0.60), (0.80, 0.30)]
    pts = [(x * size, y * size) for x, y in pts]
    w = size * 0.055

    def dist(px, py, a, b):
        (x1, y1), (x2, y2) = a, b
        dx, dy = x2 - x1, y2 - y1
        t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)))
        return ((px - x1 - t * dx) ** 2 + (py - y1 - t * dy) ** 2) ** 0.5
    rows = []
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            g = y / size
            r, gg, bb = int(14 + 10 * g), int(30 + 20 * g), int(64 + 40 * g)
            d = min(dist(x + .5, y + .5, pts[i], pts[i + 1]) for i in range(len(pts) - 1))
            if d < w:
                a = min(1, (w - d) * 1.5)
                r, gg, bb = (int(r * (1 - a) + 52 * a), int(gg * (1 - a) + 211 * a), int(bb * (1 - a) + 153 * a))
            row += bytes((r, gg, bb))
        rows.append(bytes(row))
    raw = zlib.compress(b"".join(rows), 9)

    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    data = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)) + \
        chunk(b"IDAT", raw) + chunk(b"IEND", b"")
    with open(path, "wb") as fh:
        fh.write(data)


def cmd_build(a):
    cfg = system.config()
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for f in os.listdir(SRC):
        shutil.copy(os.path.join(SRC, f), os.path.join(OUT, f))
    png(180, os.path.join(OUT, "icon-180.png"))
    png(512, os.path.join(OUT, "icon-512.png"))
    doc = build_data(cfg)
    pw = os.environ.get("SITE_PASSWORD", "")
    keyfile = os.path.join(T, "site_key.json")
    enc = None
    if pw:
        enc = encrypt(doc, pw, cfg.get("site_salt") or "00" * 16)
    elif os.path.exists(keyfile):
        enc = encrypt_pub(doc, keyfile)
    if enc:
        with open(os.path.join(OUT, "data.enc"), "w", encoding="utf-8") as fh:
            json.dump(enc, fh)
        print("data.enc gebaut (Version %d, %d Bytes Klartext)." % (enc["v"], len(json.dumps(doc))))
    else:
        print("Kein Passwort und kein Schlüssel: keine Daten auf der Seite.")
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    if a.plain:
        with open(os.path.join(OUT, "data.json"), "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False)
        print("data.json (unverschlüsselt) gebaut: nur lokal verwenden.")
    return 0


def cmd_artifact(a):
    """Eine Datei mit eingebetteten Daten für ein privates Claude-Artifact (ohne Passwort, Ja/Nein nur im Push)."""
    html = open(os.path.join(SRC, "index.html"), encoding="utf-8").read()
    head_end = html.index("</head>")
    style = html[html.index("<style>"):html.index("</style>") + 8]
    body = html[html.index("<body>") + 6:html.index("</body>")]
    doc = build_data(system.config())
    data = json.dumps(doc, ensure_ascii=False).replace("</", "<\\/")
    out = ("<title>Trader-Labor</title>\n" + style + "\n<script>window.__DATA__ = " + data + ";</script>\n" + body)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(out)
    print("%s gebaut (%d Bytes)." % (a.out, len(out)))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Webseite bauen")
    sub = ap.add_subparsers(dest="cmd")
    b = sub.add_parser("build")
    b.add_argument("--plain", action="store_true")
    ar = sub.add_parser("artifact")
    ar.add_argument("--out", default=os.path.join(ROOT, "_site", "trader-artifact.html"))
    a = ap.parse_args(argv)
    if a.cmd == "artifact":
        return cmd_artifact(a)
    if a.cmd != "build":
        ap.print_help()
        return 1
    return cmd_build(a)


if __name__ == "__main__":
    sys.exit(main())
