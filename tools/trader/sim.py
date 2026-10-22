#!/usr/bin/env python3
"""Simulator: 100 € Spielgeld, als wären sie echt. Nur Standardbibliothek.

    python3 tools/trader/sim.py            # beide Rechnungen als JSON ausgeben

Regeln (aus dem Plan, Werte in trader/system.json unter „sim“):
  - Start 100 €, kein Hebel, kein Leerverkauf, nur so viel kaufen, wie Geld frei ist.
  - Höchstens 3 € Verlust am Stopp je Trade (daraus folgt die Positionsgröße), Bruchstücke von Aktien erlaubt.
  - Tagesgrenze 8 € Verlust (inkl. Gebühren): danach an diesem Tag kein neuer Trade.
  - Monatsgrenze 30 €: danach bis Monatsende kein neuer Trade.
  - Gebühr je Order (Kauf und Verkauf je 1 €, wie Trade Republic). Zum Vergleich wird auch mit 0 € gerechnet.
  - Unter 20 € Positionsgröße wird nicht gehandelt (die Gebühr wäre zu groß).
Zwei Rechnungen:
  - „vorschau“: die aktuelle Top-Variante des Labors an den letzten ~60 Tagen (Backtest, also Vergangenheit).
  - „live“: ab dem Simulator-Start jeden Handelstag die Top-Variante, die an diesem Morgen vorne lag.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
T = os.path.join(ROOT, "trader")

DEFAULTS = {"start_eur": 100.0, "max_loss_trade": 3.0, "max_loss_day": 8.0, "max_loss_month": 30.0,
            "fee_eur": 1.0, "min_position": 20.0, "start_date": None}


def settings():
    try:
        with open(os.path.join(T, "system.json"), encoding="utf-8") as fh:
            cfg = json.load(fh)
    except (OSError, ValueError):
        cfg = {}
    out = dict(DEFAULTS)
    out.update({k: v for k, v in (cfg.get("sim") or {}).items() if not k.startswith("_")})
    return out


def run(trades, s, fee):
    """trades: [{date, symbol, entry, stop, exit, why, in_k, out_k, ...}] -> Kontoverlauf."""
    cash = s["start_eur"]
    book, days, months = [], {}, {}
    by_day = {}
    for t in trades:
        by_day.setdefault(t["date"], []).append(t)
    for d in sorted(by_day):
        month = d[:7]
        m = months.setdefault(month, {"month": month, "pnl": 0.0, "trades": 0, "stopped": False})
        day = {"date": d, "pnl": 0.0, "trades": 0, "stopped": False, "skipped": 0}
        events = []
        for t in by_day[d]:
            events.append((t["in_k"], 1, t))
            events.append((t["out_k"], 2, t))
        events.sort(key=lambda e: (e[0], e[1]))
        open_pos = {}
        for k, kind, t in events:
            key = id(t)
            if kind == 1:
                if m["stopped"] or day["stopped"]:
                    day["skipped"] += 1
                    continue
                risk = (t["entry"] - t["stop"]) / t["entry"]
                value = min(cash - fee, s["max_loss_trade"] / risk if risk > 0 else 0)
                if value < s["min_position"]:
                    day["skipped"] += 1
                    continue
                cash -= value + fee
                open_pos[key] = value
            elif key in open_pos:
                value = open_pos.pop(key)
                back = value * t["exit"] / t["entry"]
                cash += back - fee
                pnl = back - value - 2 * fee
                day["pnl"] += pnl
                m["pnl"] += pnl
                day["trades"] += 1
                m["trades"] += 1
                book.append({"date": d, "symbol": t["symbol"], "value": round(value, 2), "pnl": round(pnl, 2),
                             "fees": 2 * fee, "why": t["why"], "in_k": t["in_k"], "out_k": t["out_k"],
                             "variant": t.get("variant")})
                if day["pnl"] <= -s["max_loss_day"]:
                    day["stopped"] = True
                if m["pnl"] <= -s["max_loss_month"]:
                    m["stopped"] = True
        day["pnl"] = round(day["pnl"], 2)
        day["equity"] = round(cash, 2)
        days[d] = day
    for m in months.values():
        m["pnl"] = round(m["pnl"], 2)
    eq = [days[d]["equity"] for d in sorted(days)]
    peak, dd = s["start_eur"], 0.0
    for e in eq:
        peak = max(peak, e)
        dd = min(dd, e - peak)
    wins = sum(1 for b in book if b["pnl"] > 0)
    return {"equity": round(cash, 2), "pnl": round(cash - s["start_eur"], 2), "trades": len(book),
            "win_rate": round(wins / len(book) * 100, 1) if book else None, "max_dd": round(dd, 2),
            "days": [days[d] for d in sorted(days)], "months": [months[k] for k in sorted(months)],
            "book": book[-60:], "day_stops": sum(1 for d in days.values() if d["stopped"]),
            "month_stops": sum(1 for m in months.values() if m["stopped"])}


def live_trades(start_date):
    """Trades der jeweiligen Top-Variante des Tages aus trader/lab/live/*.json ab start_date."""
    out = []
    live_dir = os.path.join(T, "lab", "live")
    if not start_date or not os.path.isdir(live_dir):
        return out
    for f in sorted(os.listdir(live_dir)):
        if not f.endswith(".json") or f[:-5] < start_date:
            continue
        try:
            with open(os.path.join(live_dir, f), encoding="utf-8") as fh:
                doc = json.load(fh)
        except (OSError, ValueError):
            continue
        champ = (doc.get("focus") or [None])[0]
        out += [dict(t, date=doc["date"]) for t in doc.get("trades", []) if t["variant"] == champ and not t["open"]]
    return out


def compute():
    s = settings()
    try:
        with open(os.path.join(T, "lab", "results.json"), encoding="utf-8") as fh:
            res = json.load(fh)
    except (OSError, ValueError):
        res = {}
    pre = res.get("champion_trades") or []
    out = {"settings": s, "champion": res.get("champion"),
           "vorschau": {"fee": run(pre, s, s["fee_eur"]), "no_fee": run(pre, s, 0.0)} if pre else None,
           "live": None}
    lt = live_trades(s["start_date"])
    if s["start_date"]:
        out["live"] = {"start": s["start_date"], "fee": run(lt, s, s["fee_eur"]), "no_fee": run(lt, s, 0.0)}
    out["checks"] = checks(out)
    return out


def checks(sim):
    """Echtgeld-Prüfung: alle Punkte müssen grün sein, dann entscheidet Lukas."""
    live = (sim.get("live") or {}).get("fee")
    months = [m for m in (live or {}).get("months", [])]
    full = months[:-1] if months else []          # der laufende Monat zählt erst, wenn er vorbei ist
    last2 = full[-2:]
    return [
        {"name": "Simulator läuft", "ok": bool(sim.get("live")),
         "detail": "seit %s" % sim["live"]["start"] if sim.get("live") else "noch nicht gestartet"},
        {"name": "2 volle Simulator-Monate", "ok": len(full) >= 2, "detail": "%d von 2" % min(len(full), 2)},
        {"name": "Beide Monate im Plus (nach Gebühren)", "ok": len(last2) == 2 and all(m["pnl"] > 0 for m in last2),
         "detail": ", ".join("%s: %+.2f €" % (m["month"], m["pnl"]) for m in last2) or "–"},
        {"name": "Mindestens 40 Trades", "ok": (live or {}).get("trades", 0) >= 40,
         "detail": "%d Trades" % (live or {}).get("trades", 0)},
        {"name": "Monatsgrenze nie gerissen", "ok": bool(live) and live["month_stops"] == 0,
         "detail": "%d Mal" % (live or {}).get("month_stops", 0)},
        {"name": "Broker mit kleinen Gebühren und Schnittstelle gewählt", "ok": False, "detail": "gemeinsam prüfen"},
        {"name": "Steuern geklärt (Freistellungsauftrag)", "ok": False, "detail": "vor dem Start klären"},
        {"name": "Dein Ja", "ok": False, "detail": "erst wenn alles andere grün ist"},
    ]


if __name__ == "__main__":
    json.dump(compute(), sys.stdout, ensure_ascii=False, indent=1)
    print()
