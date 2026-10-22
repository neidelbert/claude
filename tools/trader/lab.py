#!/usr/bin/env python3
"""Labor des Trader-Systems: testet Strategien und Varianten an 5-Minuten-Kerzen.
Nur Standardbibliothek. Spielgeld, Testphase: kein Limit, alle Zahlen sichtbar.

    python3 tools/trader/lab.py fetch              # 5-Minuten-Kerzen (ca. 60 Tage) laden und im Cache sammeln
    python3 tools/trader/lab.py run                # alle Varianten testen -> trader/lab/results.json
    python3 tools/trader/lab.py run --offline DIR  # Kerzen aus DIR/<SYM>.json.gz (Tests)
    python3 tools/trader/lab.py live               # heute: Spielgeld-Trades aller Varianten bis jetzt
    python3 tools/trader/lab.py selftest           # Rechenregeln an künstlichen Kerzen prüfen

Ablauf eines Trades (nur Kauf, nur innerhalb eines Tages):
  - Einstieg zum Schlusskurs der Signal-Kerze plus Spread-Aufschlag (SLIP).
  - Danach Kerze für Kerze: Tief am oder unter dem Stopp -> raus zum Stopp (öffnet die Kerze schon darunter:
    raus zum Eröffnungskurs). Hoch am oder über dem Ziel -> raus zum Ziel. Beides in derselben Kerze:
    Stopp zählt (vorsichtig gerechnet).
  - Spätestens zum Schluss der Kerze, die um 15:55 Uhr ET endet (bei frühem Schluss 12:55 Uhr), wird verkauft.
Lerntage und Prüftage: Die ältesten zwei Drittel der Tage sind Lerntage, das jüngste Drittel sind Prüftage.
Eine Variante „besteht“, wenn sie auf den Prüftagen genug Trades hat und dort im Plus ist.
"""

import argparse
import concurrent.futures
import datetime
import gzip
import importlib.util
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
_spec = importlib.util.spec_from_file_location("trader_scan", os.path.join(HERE, "scan.py"))
scan = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(scan)

CACHE = os.path.join(ROOT, ".cache", "lab", "bars")   # nicht im Git, über actions/cache gesammelt
OUT = os.path.join(ROOT, "trader", "lab", "results.json")

BAR = 5                 # Minuten je Kerze
SLIP = 0.0005           # 0,05 % Spread-Aufschlag je Seite (Kauf teurer, Verkauf billiger)
STAKE = 100.0           # Rechengröße: Ergebnis „bei 100 € pro Trade“
FEE = 1.0               # Gebühr je Order in € (Beispiel Trade Republic), nur zur Anzeige „nach Gebühren“
MIN_TEST_TRADES = 30    # so viele Trades braucht eine Variante auf den Prüftagen
TEST_SHARE = 1 / 3      # Anteil der jüngsten Tage, die nur zum Prüfen dienen
MIN_RISK = 0.001        # Stopp mindestens 0,1 % unter dem Einstieg, sonst zu eng
CURVE_TOP = 8           # Tageskurven für die besten N Varianten
TRADES_TOP = 3          # Einzeltrades für die besten N Varianten
WORKERS = 4             # gleichzeitige Downloads
FETCH_PAUSE = 0.2       # Sekunden Pause je Download und Faden

# Viel gehandelte US-Aktien als feste Grundliste; dazu kommen die ersten Treffer des Morgen-Scans.
BASE_SYMBOLS = """
AAPL MSFT NVDA AMZN GOOGL META TSLA AVGO AMD NFLX ORCL CRM ADBE INTC QCOM MU AMAT LRCX KLAC TXN
ARM SMCI MRVL ON ASML TSM PLTR SNOW CRWD PANW ZS NET DDOG SHOP UBER LYFT ABNB DASH COIN HOOD
SOFI PYPL SQ AFRM UPST RBLX U SNAP PINS SPOT ROKU DIS CMCSA T VZ TMUS
JPM BAC WFC C GS MS SCHW BLK AXP V MA COF
XOM CVX OXY COP SLB HAL DVN MPC
LLY UNH JNJ PFE MRK ABBV BMY AMGN GILD MRNA CVS ISRG TMO DHR ABT MDT
WMT COST TGT HD LOW NKE SBUX MCD CMG LULU KO PEP PG PM MO
BA CAT DE GE HON LMT RTX NOC UPS FDX UNP DAL UAL AAL CCL RCL NCLH
F GM RIVN LCID NIO XPEV LI
MARA RIOT MSTR CLSK
GME AMC DKNG PENN CHWY ETSY EBAY BABA JD PDD BIDU
IBM CSCO DELL HPQ ANET VRT CRWV NOW INTU WDAY TEAM MDB OKTA
BRK.B SPY QQQ IWM
""".split()

ORB_STOPS = {"mid": "Stopp Mitte der Spanne", "low": "Stopp Tief der Spanne"}


# ---------------------------------------------------------------- Varianten

def variants():
    out = []
    for orm in (15, 30):
        for stop in ("mid", "low"):
            for tgt in (1.0, 1.5, 2.0):
                for rv in (0.0, 1.5):
                    out.append({"strategy": "orb", "or_min": orm, "stop": stop, "target_r": tgt, "rvol": rv})
    for gap in (2.0, 4.0):
        for rv in (2.0, 3.0):
            for tgt in (1.5, 2.0, 3.0):
                out.append({"strategy": "gap", "gap": gap, "rvol": rv, "target_r": tgt})
    for trig in ("rsi30", "gapdown3"):
        for stop in ("daylow", "pct1.5"):
            for tgt in (1.0, 2.0):
                out.append({"strategy": "bounce", "trigger": trig, "stop": stop, "target_r": tgt})
    for v in out:
        v["id"] = vid(v)
        v["label"] = label(v)
    return out


def vid(v):
    if v["strategy"] == "orb":
        return "orb-%d-%s-%sR-v%s" % (v["or_min"], v["stop"], fmt(v["target_r"]), fmt(v["rvol"]))
    if v["strategy"] == "gap":
        return "gap-%s-v%s-%sR" % (fmt(v["gap"]), fmt(v["rvol"]), fmt(v["target_r"]))
    return "bounce-%s-%s-%sR" % (v["trigger"], v["stop"], fmt(v["target_r"]))


def fmt(x):
    return ("%g" % x)


def de(x):
    return ("%g" % x).replace(".", ",")


def label(v):
    if v["strategy"] == "orb":
        return "Opening-Range-Ausbruch %d Min · %s · Ziel %sR%s" % (
            v["or_min"], ORB_STOPS[v["stop"]], de(v["target_r"]),
            " · Volumen ≥ %s×" % de(v["rvol"]) if v["rvol"] else "")
    if v["strategy"] == "gap":
        return "News-Sprung: Lücke ≥ %s %% · Volumen ≥ %s× · Ziel %sR" % (de(v["gap"]), de(v["rvol"]), de(v["target_r"]))
    trig = "RSI unter 30" if v["trigger"] == "rsi30" else "Lücke nach unten ≥ 3 %"
    stop = "Stopp Tagestief" if v["stop"] == "daylow" else "Stopp 1,5 % darunter"
    return "Erholung: %s · %s · Ziel %sR" % (trig, stop, de(v["target_r"]))


STRATEGY_DE = {
    "orb": "Opening-Range-Ausbruch: Die ersten 15 oder 30 Minuten bilden eine Spanne. Schließt eine "
           "5-Minuten-Kerze über ihrem Hoch, wird gekauft.",
    "gap": "News-Sprung: Die Aktie öffnet deutlich über dem Vortag (meist wegen einer Nachricht) und mit viel "
           "Umsatz. Gekauft wird, wenn sie über das Hoch der ersten 5 Minuten steigt.",
    "bounce": "Erholung: Eine stark gefallene Aktie (RSI unter 30 oder Lücke nach unten) steigt wieder über "
              "ihren Tagesdurchschnittspreis (VWAP).",
}


# ---------------------------------------------------------------- Kerzen

def load_series(path):
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


def save_series(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as fh:
        json.dump(s, fh, separators=(",", ":"))


def merge(old, new):
    """Zwei Reihen {t,o,h,l,c,v} nach Zeitstempel zusammenführen (neue gewinnen)."""
    rows = {}
    for s in (old, new):
        if not s:
            continue
        for i, t in enumerate(s["t"]):
            rows[t] = tuple(s[k][i] for k in ("o", "h", "l", "c", "v"))
    ts = sorted(rows)
    return {"t": ts, **{k: [rows[t][j] for t in ts] for j, k in enumerate(("o", "h", "l", "c", "v"))}}


def fetch_one(sym):
    time.sleep(FETCH_PAUSE)
    s = scan.parse_chart(scan.yahoo_get(scan.chart_path(sym, "60d", "5m")), sym)
    return {k: s[k] for k in ("t", "o", "h", "l", "c", "v")}


def symbols_for_run():
    syms = list(BASE_SYMBOLS)
    wl = os.path.join(ROOT, "trader", "watchlist.json")
    try:
        with open(wl, encoding="utf-8") as fh:
            for h in json.load(fh).get("hits", [])[:50]:
                syms.append(h["symbol"])
    except (OSError, ValueError, KeyError):
        pass
    seen, out = set(), []
    for s in syms:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def cmd_fetch(a):
    syms = symbols_for_run()
    ok, failed = 0, []
    t0 = time.time()
    with concurrent.futures.ThreadPoolExecutor(WORKERS) as ex:
        futs = {ex.submit(fetch_one, s): s for s in syms}
        for f in concurrent.futures.as_completed(futs):
            sym = futs[f]
            try:
                new = f.result()
            except Exception as e:
                failed.append("%s (%s)" % (sym, e))
                continue
            path = os.path.join(CACHE, sym + ".json.gz")
            old = load_series(path) if os.path.exists(path) else None
            save_series(path, merge(old, new))
            ok += 1
    print(json.dumps({"symbols": len(syms), "fetched": ok, "failed": failed[:20], "n_failed": len(failed),
                      "seconds": round(time.time() - t0, 1)}))
    return 0 if ok else 1


def split_days(s, now_ts=None):
    """Reihe -> {datum: [(k, o, h, l, c, v), ...]} nur reguläre Handelszeit, k = Kerze ab 9:30 (0, 1, 2 ...).
    now_ts: Kerzen, die zu diesem Zeitpunkt noch nicht geschlossen sind, fallen weg (live)."""
    days = {}
    for i, ts in enumerate(s["t"]):
        if now_ts is not None and ts + BAR * 60 > now_ts:
            continue
        o, h, l, c, v = (s[k][i] for k in ("o", "h", "l", "c", "v"))
        if None in (o, h, l, c):
            continue
        et = scan.ts_to_eastern(ts)
        if et.second or et.minute % BAR:
            continue                       # Live-Tick außerhalb des Rasters
        sess = scan.session(et.date())
        if not sess:
            continue
        mins = (et.hour * 60 + et.minute) - (9 * 60 + 30)
        close_min = (sess[1].hour * 60 + sess[1].minute) - (9 * 60 + 30)
        if mins < 0 or mins + BAR > close_min:
            continue
        days.setdefault(et.date().isoformat(), []).append((mins // BAR, o, h, l, c, v or 0))
    out = {}
    for d, bars in days.items():
        bars.sort()
        uniq = {}
        for b in bars:
            uniq[b[0]] = b
        out[d] = [uniq[k] for k in sorted(uniq)]
    return out


def last_k(date_iso):
    """Index der letzten Kerze, die bis zum Ausstieg (5 Min. vor Schluss) schließt."""
    d = datetime.date.fromisoformat(date_iso)
    sess = scan.session(d)
    close_min = (sess[1].hour * 60 + sess[1].minute) - (9 * 60 + 30)
    return (close_min - 5) // BAR - 1      # 16:00 -> Kerze 15:50 (k = 76), schließt 15:55


# ---------------------------------------------------------------- Kennzahlen je Tag

def rsi(closes, n=14):
    if len(closes) < n + 1:
        return None
    gains = losses = 0.0
    for i in range(1, n + 1):
        d = closes[i] - closes[i - 1]
        gains += max(d, 0)
        losses += max(-d, 0)
    ag, al = gains / n, losses / n
    for i in range(n + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        ag = (ag * (n - 1) + max(d, 0)) / n
        al = (al * (n - 1) + max(-d, 0)) / n
    if al == 0:
        return 100.0
    return 100 - 100 / (1 + ag / al)


def contexts(days):
    """Je Tag: Vortagesschluss, RSI(14) der Tagesschlüsse bis zum Vortag, Durchschnittsvolumen der
    ersten Kerzen der 10 Tage davor (für 1, 3 und 6 Kerzen)."""
    dates = sorted(days)
    ctx = {}
    closes = []
    first = {1: [], 3: [], 6: []}
    for d in dates:
        bars = days[d]
        c = {"prev_close": closes[-1] if closes else None, "rsi": rsi(closes[-40:]) if len(closes) >= 15 else None}
        for n in first:
            hist = first[n][-10:]
            c["vol%d" % n] = (sum(hist) / len(hist)) if len(hist) >= 5 else None
        ctx[d] = c
        full = len(bars) >= last_k(d) + 1 and bars[0][0] == 0
        if bars:
            closes.append(bars[-1][4])
        if full:
            for n in first:
                first[n].append(sum(b[5] for b in bars[:n]))
    return ctx


# ---------------------------------------------------------------- Signale

def signal_orb(v, bars, c):
    n = v["or_min"] // BAR
    if len(bars) <= n or [b[0] for b in bars[:n]] != list(range(n)):
        return None
    hi = max(b[2] for b in bars[:n])
    lo = min(b[3] for b in bars[:n])
    if v["rvol"]:
        avg = c.get("vol%d" % (3 if n == 3 else 6))
        if not avg or sum(b[5] for b in bars[:n]) < v["rvol"] * avg:
            return None
    latest = (12 * 60 - 9 * 60 - 30) // BAR          # kein Einstieg mehr ab 12:00 Uhr ET
    for i in range(n, len(bars)):
        k = bars[i][0]
        if k >= latest:
            return None
        if bars[i][4] > hi:
            stop = (hi + lo) / 2 if v["stop"] == "mid" else lo
            return i, stop
    return None


def signal_gap(v, bars, c):
    pc = c.get("prev_close")
    if not pc or not bars or bars[0][0] != 0:
        return None
    if bars[0][1] < pc * (1 + v["gap"] / 100):
        return None
    avg = c.get("vol3")
    if not avg or sum(b[5] for b in bars[:3]) < v["rvol"] * avg:
        return None
    hi, lo = bars[0][2], bars[0][3]
    latest = 60 // BAR                                  # bis 10:30 Uhr ET
    for i in range(1, len(bars)):
        if bars[i][0] >= latest:
            return None
        if bars[i][4] > hi:
            return i, lo
    return None


def signal_bounce(v, bars, c):
    pc = c.get("prev_close")
    if not pc or not bars or bars[0][0] != 0:
        return None
    if v["trigger"] == "rsi30":
        if c.get("rsi") is None or c["rsi"] >= 30:
            return None
    elif bars[0][1] > pc * 0.97:
        return None
    pv = vol = 0.0
    low = math.inf
    start, latest = 30 // BAR, (13 * 60 - 9 * 60 - 30) // BAR   # ab 10:00, bis 13:00 Uhr ET
    for i, b in enumerate(bars):
        typ = (b[2] + b[3] + b[4]) / 3
        pv += typ * b[5]
        vol += b[5]
        low = min(low, b[3])
        if b[0] >= latest:
            return None
        if b[0] >= start and vol and b[4] > pv / vol and i and bars[i - 1][4] <= pv / vol:
            stop = low if v["stop"] == "daylow" else b[4] * (1 - 0.015)
            return i, stop
    return None


SIGNALS = {"orb": signal_orb, "gap": signal_gap, "bounce": signal_bounce}


def simulate(bars, i, stop, target_r, end_k):
    """Trade ab Kerze i. -> dict oder None (Risiko zu klein)."""
    entry = bars[i][4] * (1 + SLIP)
    risk = entry - stop
    if risk <= entry * MIN_RISK:
        return None
    target = entry + target_r * risk
    exit_p, why, exit_k, hit = None, "Schluss", bars[i][0], False
    for b in bars[i + 1:]:
        k, o, h, l, c, _ = b
        if k > end_k:
            break
        exit_k = k
        if o <= stop:
            exit_p, why, hit = o, "Stopp", True
            break
        if l <= stop:
            exit_p, why, hit = stop, "Stopp", True
            break
        if o >= target:
            exit_p, why, hit = o, "Ziel", True
            break
        if h >= target:
            exit_p, why, hit = target, "Ziel", True
            break
        exit_p = c
    if exit_p is None:
        exit_p = bars[i][4]
    exit_p *= (1 - SLIP)
    pct = exit_p / entry - 1
    return {"entry": round(entry, 4), "stop": round(stop, 4), "target": round(target, 4), "exit": round(exit_p, 4),
            "why": why, "r": round((exit_p - entry) / risk, 3), "pct": round(pct * 100, 3),
            "in_k": bars[i][0], "out_k": exit_k, "open": not hit and exit_k < end_k}


def clock(k):
    m = 9 * 60 + 30 + (k + 1) * BAR
    return "%d:%02d" % (m // 60, m % 60)


# ---------------------------------------------------------------- Auswertung

def stats(trades):
    n = len(trades)
    if not n:
        return {"n": 0}
    wins = sum(1 for t in trades if t["pct"] > 0)
    gross_win = sum(t["pct"] for t in trades if t["pct"] > 0)
    gross_loss = -sum(t["pct"] for t in trades if t["pct"] < 0)
    eur = [t["pct"] / 100 * STAKE for t in trades]
    peak = run = dd = 0.0
    for e in eur:
        run += e
        peak = max(peak, run)
        dd = min(dd, run - peak)
    fee_total = 2 * FEE * n
    mean = sum(t["pct"] for t in trades) / n
    sd = math.sqrt(sum((t["pct"] - mean) ** 2 for t in trades) / (n - 1)) if n > 1 else 0.0
    tval = mean / (sd / math.sqrt(n)) if sd else 0.0   # ab etwa 2 ist Zufall unwahrscheinlich
    return {"n": n, "t": round(tval, 2), "win_rate": round(wins / n * 100, 1), "avg_r": round(sum(t["r"] for t in trades) / n, 3),
            "avg_pct": round(sum(t["pct"] for t in trades) / n, 3), "eur": round(sum(eur), 2),
            "eur_after_fees": round(sum(eur) - fee_total, 2), "profit_factor": round(gross_win / gross_loss, 2)
            if gross_loss else None, "max_dd_eur": round(dd, 2), "stops": sum(1 for t in trades if t["why"] == "Stopp"),
            "targets": sum(1 for t in trades if t["why"] == "Ziel")}


def cmd_run(a):
    t0 = time.time()
    src = a.offline or CACHE
    files = sorted(f for f in os.listdir(src) if f.endswith(".json.gz")) if os.path.isdir(src) else []
    if not files:
        print(json.dumps({"error": "keine Kerzen im Cache (%s): erst fetch" % src}))
        return 1
    data = {}
    for f in files:
        try:
            d = split_days(load_series(os.path.join(src, f)))
        except Exception:
            continue
        if d:
            data[f[:-8]] = d
    all_days = sorted({d for days in data.values() for d in days})
    n_test = max(1, int(round(len(all_days) * TEST_SHARE)))
    test_days = set(all_days[-n_test:])
    vs = variants()
    trades = {v["id"]: [] for v in vs}
    for sym, days in data.items():
        ctx = contexts(days)
        for d, bars in days.items():
            if len(bars) < 10:
                continue
            end_k = last_k(d)
            for v in vs:
                sig = SIGNALS[v["strategy"]](v, bars, ctx[d])
                if not sig:
                    continue
                t = simulate(bars, sig[0], sig[1], v["target_r"], end_k)
                if t:
                    t.update(symbol=sym, date=d, test=d in test_days)
                    trades[v["id"]].append(t)
    rows = []
    for v in vs:
        tr = trades[v["id"]]
        train = stats([t for t in tr if not t["test"]])
        test = stats([t for t in tr if t["test"]])
        passed = bool(test.get("n", 0) >= MIN_TEST_TRADES and test.get("avg_pct", 0) > 0 and train.get("avg_pct", -1) > 0)
        score = test.get("avg_pct", -99) if test.get("n", 0) >= MIN_TEST_TRADES else -99
        rows.append(dict(v, train=train, test=test, all=stats(tr), passed=passed, score=score))
    rows.sort(key=lambda r: (r["passed"], r["score"], r["all"].get("eur", -1e9)), reverse=True)
    curves, samples = {}, {}
    for r in rows[:CURVE_TOP]:
        per = {}
        for t in trades[r["id"]]:
            per[t["date"]] = per.get(t["date"], 0) + t["pct"] / 100 * STAKE
        run, pts = 0.0, []
        for d in all_days:
            run += per.get(d, 0)
            pts.append([d, round(run, 2)])
        curves[r["id"]] = pts
    for r in rows[:TRADES_TOP]:
        last = sorted(trades[r["id"]], key=lambda t: (t["date"], t["in_k"]))[-40:]
        samples[r["id"]] = [dict(t, in_at=clock(t["in_k"]), out_at=clock(t["out_k"])) for t in last]
    best_per = {}
    for r in rows:
        best_per.setdefault(r["strategy"], r["id"])
    doc = {"created_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "symbols": len(data), "days": len(all_days),
           "train": [all_days[0], all_days[-n_test - 1]] if len(all_days) > n_test else None,
           "test": [all_days[-n_test], all_days[-1]], "n_train_days": len(all_days) - n_test, "n_test_days": n_test,
           "settings": {"slip_pct": SLIP * 100, "stake_eur": STAKE, "fee_eur": FEE,
                        "min_test_trades": MIN_TEST_TRADES},
           "strategies": STRATEGY_DE, "best_per_strategy": best_per,
           "variants": rows, "curves": curves, "samples": samples, "seconds": round(time.time() - t0, 1)}
    out = a.out or OUT
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(json.dumps({"symbols": len(data), "days": len(all_days), "variants": len(rows),
                      "trades": sum(len(t) for t in trades.values()), "passed": sum(1 for r in rows if r["passed"]),
                      "best": rows[0]["id"], "seconds": doc["seconds"]}))
    return 0


# ---------------------------------------------------------------- Live (heute, alle paar Minuten)

LIVE_DIR = os.path.join(ROOT, "trader", "lab", "live")
FOCUS_TOP = 3           # Pushes für die besten N Varianten der Rangliste (+ die beste je Strategie)


def fetch_today(sym):
    time.sleep(FETCH_PAUSE)
    s = scan.parse_chart(scan.yahoo_get(scan.chart_path(sym, "1d", "5m")), sym)
    return {k: s[k] for k in ("t", "o", "h", "l", "c", "v")}


def focus_ids():
    try:
        with open(OUT, encoding="utf-8") as fh:
            res = json.load(fh)
    except (OSError, ValueError):
        return []
    rows = res.get("variants", [])
    ids = [r["id"] for r in rows[:FOCUS_TOP]]
    for sid in (res.get("best_per_strategy") or {}).values():
        if sid not in ids:
            ids.append(sid)
    return ids


def cmd_live(a):
    t0 = time.time()
    now = scan.parse_now(a.now)
    et = scan.to_eastern(now)
    day = et.date().isoformat()
    if not scan.session(et.date()):
        print(json.dumps({"error": "heute kein Handelstag"}))
        return 1
    now_ts = int((now - datetime.datetime(1970, 1, 1)).total_seconds())
    syms = symbols_for_run()
    today, failed = {}, []
    if a.offline:
        for f in sorted(os.listdir(a.offline)):
            if f.endswith(".json.gz"):
                today[f[:-8]] = load_series(os.path.join(a.offline, f))
    else:
        with concurrent.futures.ThreadPoolExecutor(WORKERS) as ex:
            futs = {ex.submit(fetch_today, s): s for s in syms}
            for f in concurrent.futures.as_completed(futs):
                try:
                    today[futs[f]] = f.result()
                except Exception as e:
                    failed.append(futs[f])
    vs = variants()
    end_k = last_k(day)
    trades = []
    today_bars = {}
    for sym, ser in today.items():
        bars = split_days(ser, now_ts).get(day)
        if not bars:
            continue
        today_bars[sym] = bars
        hist_path = os.path.join(CACHE, sym + ".json.gz")
        hist = split_days(load_series(hist_path)) if os.path.exists(hist_path) else {}
        hist = {d: b for d, b in hist.items() if d < day}
        hist[day] = bars
        ctx = contexts(hist)[day]
        for v in vs:
            sig = SIGNALS[v["strategy"]](v, bars, ctx)
            if not sig:
                continue
            t = simulate(bars, sig[0], sig[1], v["target_r"], end_k)
            if not t:
                continue
            t.update(variant=v["id"], strategy=v["strategy"], symbol=sym, in_at=clock(t["in_k"]),
                     out_at=None if t["open"] else clock(t["out_k"]), last=round(bars[-1][4], 4),
                     eur=round(t["pct"] / 100 * STAKE, 2), key="%s|%s" % (v["id"], sym))
            trades.append(t)
    path = os.path.join(LIVE_DIR, day + ".json")
    try:
        with open(path, encoding="utf-8") as fh:
            old = {t["key"]: t for t in json.load(fh).get("trades", [])}
    except (OSError, ValueError):
        old = {}
    focus = focus_ids()
    lukas = lukas_trades(day, trades, today_bars, focus, end_k)
    events = []
    for t in trades:
        o = old.get(t["key"], {})
        t["told_in"], t["told_out"] = o.get("told_in", False), o.get("told_out", False)
        if t["variant"] not in focus:
            continue
        if not t["told_in"]:
            events.append(dict(t, event="in"))
            t["told_in"] = True
        if not t["open"] and not t["told_out"]:
            events.append(dict(t, event="out"))
            t["told_out"] = True
    per = {}
    for t in trades:
        p = per.setdefault(t["variant"], {"n": 0, "open": 0, "eur": 0.0, "wins": 0})
        p["n"] += 1
        p["open"] += t["open"]
        p["eur"] = round(p["eur"] + t["eur"], 2)
        p["wins"] += t["pct"] > 0
    labels = {v["id"]: v["label"] for v in vs}
    doc = {"date": day, "as_of": "%s Uhr ET" % et.strftime("%H:%M"), "symbols": len(today), "failed": len(failed),
           "focus": focus, "labels": {k: labels[k] for k in focus if k in labels}, "per_variant": per,
           "n_trades": len(trades), "n_open": sum(1 for t in trades if t["open"]), "lukas": lukas,
           "trades": sorted(trades, key=lambda t: (t["in_k"], t["symbol"], t["variant"]))}
    os.makedirs(LIVE_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(json.dumps({"date": day, "as_of": doc["as_of"], "symbols": len(today), "failed": len(failed),
                      "trades": len(trades), "open": doc["n_open"], "events": events,
                      "labels": doc["labels"], "seconds": round(time.time() - t0, 1)}, ensure_ascii=False))
    return 0


DECISIONS = os.path.join(ROOT, "trader", "lab", "decisions.json")


def lukas_trades(day, trades, today_bars, focus, end_k):
    """Ja-Antworten von Lukas -> eigene Trades. Je Vorschlag (Aktie + Strategie) zählt die Top-Variante dieser
    Strategie. Einstieg zum Schluss der ersten Kerze, die nach der Antwort schließt; Stopp und Ziel wie die Regel.
    Liegt der Kurs dann schon am Stopp oder Ziel: „verpasst“."""
    try:
        with open(DECISIONS, encoding="utf-8") as fh:
            dec = json.load(fh)
    except (OSError, ValueError):
        return []
    prefix = day.replace("-", "") + "-"
    out = []
    for pid, d in sorted(dec.items()):
        if not pid.startswith(prefix) or d.get("answer") != "ja":
            continue
        _, sym, strat = pid.split("-", 2)
        sym = sym.replace("_", ".")
        cands = [t for t in trades if t["symbol"] == sym and t["strategy"] == strat]
        cands.sort(key=lambda t: focus.index(t["variant"]) if t["variant"] in focus else 99)
        if not cands or sym not in today_bars:
            continue
        rule = cands[0]
        bars = today_bars[sym]
        answer_et = scan.ts_to_eastern(d["ts"])
        ans_min = answer_et.hour * 60 + answer_et.minute - (9 * 60 + 30)
        row = {"pid": pid, "symbol": sym, "strategy": strat, "variant": rule["variant"],
               "answer_at": answer_et.strftime("%H:%M"), "stop": rule["stop"], "target": rule["target"]}
        j = next((i for i, b in enumerate(bars) if (b[0] + 1) * BAR >= ans_min and b[0] >= rule["in_k"]), None)
        if j is None:
            row.update(status="wartet")       # nächste Kerze noch nicht geschlossen
            out.append(row)
            continue
        price = bars[j][4] * (1 + SLIP)
        if price <= rule["stop"] or price >= rule["target"] or bars[j][0] > end_k:
            row.update(status="verpasst", entry=round(price, 4))
            out.append(row)
            continue
        risk = price - rule["stop"]
        t = simulate(bars, j, rule["stop"], (rule["target"] - price) / risk, end_k)
        if not t:
            row.update(status="verpasst", entry=round(price, 4))
        else:
            row.update(status="offen" if t["open"] else "beendet", entry=t["entry"], exit=t["exit"], why=t["why"],
                       pct=t["pct"], eur=round(t["pct"] / 100 * STAKE, 2), in_at=clock(t["in_k"]),
                       out_at=None if t["open"] else clock(t["out_k"]), last=round(bars[-1][4], 4))
        out.append(row)
    return out


def day_summary(day):
    """Tagesbilanz aus trader/lab/live/<tag>.json für Push und Übersicht."""
    try:
        with open(os.path.join(LIVE_DIR, day + ".json"), encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError):
        return None
    labels = {v["id"]: v["label"] for v in variants()}
    rows = sorted(({"id": k, "label": labels.get(k, k), **p} for k, p in doc["per_variant"].items()),
                  key=lambda r: r["eur"], reverse=True)
    by_strat = {}
    for t in doc["trades"]:
        s = by_strat.setdefault(t["strategy"], {"n": 0, "eur": 0.0})
        s["n"] += 1
        s["eur"] = round(s["eur"] + t["eur"], 2)
    return {"date": day, "n_trades": doc["n_trades"], "n_open": doc["n_open"], "variants": rows,
            "focus": doc.get("focus", []), "by_strategy": by_strat}


# ---------------------------------------------------------------- Selbsttest

def _series(day, rows):
    """Künstliche Kerzen für einen Tag: rows = [(o, h, l, c, v), ...] ab 9:30 Uhr ET."""
    open_utc = scan.eastern_to_utc(datetime.datetime.combine(day, datetime.time(9, 30)))
    epoch = datetime.datetime(1970, 1, 1)
    s = {k: [] for k in ("t", "o", "h", "l", "c", "v")}
    for i, r in enumerate(rows):
        s["t"].append(int((open_utc - epoch).total_seconds()) + i * 300)
        for k, x in zip(("o", "h", "l", "c", "v"), r):
            s[k].append(x)
    return s


def cmd_selftest(a):
    day = datetime.date(2026, 10, 20)
    flat = [(100, 100.5, 99.5, 100, 1000)] * 3                       # Spanne 99,5 bis 100,5
    up = [(100, 101, 100, 100.8, 1000), (100.8, 103, 100.7, 102.9, 1000)]
    rest = [(102.9, 103, 102.8, 102.9, 1000)] * 73
    days = split_days(_series(day, flat + up + rest))
    bars = days[day.isoformat()]
    assert len(bars) == 78 and last_k(day.isoformat()) == 76, (len(bars), last_k(day.isoformat()))
    v = {"strategy": "orb", "or_min": 15, "stop": "mid", "target_r": 2.0, "rvol": 0}
    i, stop = signal_orb(v, bars, {})
    assert i == 3 and stop == 100.0, (i, stop)                       # 9:45-Kerze schließt 100,8 > 100,5
    t = simulate(bars, i, stop, 2.0, 76)
    assert t["why"] == "Ziel" and abs(t["exit"] - t["target"] * (1 - SLIP)) < 1e-3, t
    # Stopp und Ziel in derselben Kerze: Stopp zählt
    both = flat + [(100, 101, 100, 100.8, 1000), (100.8, 103, 99, 101, 1000)] + rest
    b2 = split_days(_series(day, both))[day.isoformat()]
    t2 = simulate(b2, 3, 100.0, 2.0, 76)
    assert t2["why"] == "Stopp" and t2["r"] < -0.9, t2
    # ohne Stopp und Ziel: raus zum Schluss der 15:50-Kerze
    calm = flat + [(100, 100.7, 100, 100.6, 1000)] + [(100.6, 100.7, 100.5, 100.6, 1000)] * 74
    b3 = split_days(_series(day, calm))[day.isoformat()]
    t3 = simulate(b3, 3, 100.0, 2.0, 76)
    assert t3["why"] == "Schluss" and t3["out_k"] == 76, t3
    assert clock(76) == "15:55" and clock(3) == "9:50"
    assert t3["open"] is False
    # live: nur die ersten 6 Kerzen geschlossen -> Trade offen
    open_utc = scan.eastern_to_utc(datetime.datetime.combine(day, datetime.time(9, 30)))
    now_ts = int((open_utc - datetime.datetime(1970, 1, 1)).total_seconds()) + 6 * 300
    b4 = split_days(_series(day, calm), now_ts)[day.isoformat()]
    assert len(b4) == 6, len(b4)
    t4 = simulate(b4, 3, 100.0, 2.0, 76)
    assert t4["open"] is True and t4["out_k"] == 5, t4
    assert len(variants()) == 44 and len({v["id"] for v in variants()}) == 44
    print("Selbsttest ok: Einstieg, Ziel, Stopp vor Ziel, Ausstieg zum Schluss, offener Live-Trade, 44 Varianten.")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Labor: Strategien an 5-Minuten-Kerzen testen")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("fetch")
    r = sub.add_parser("run")
    r.add_argument("--offline", metavar="DIR")
    r.add_argument("--out")
    lv = sub.add_parser("live")
    lv.add_argument("--now", help='New Yorker Zeit, z. B. "2026-10-22 10:40"')
    lv.add_argument("--offline", metavar="DIR", help="heutige Kerzen aus DIR/<SYM>.json.gz")
    sub.add_parser("selftest")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 1
    return {"fetch": cmd_fetch, "run": cmd_run, "live": cmd_live, "selftest": cmd_selftest}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
