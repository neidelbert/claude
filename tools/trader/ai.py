#!/usr/bin/env python3
"""KI-Zweitmeinung (ab Monat 2): Claude liest die Schlagzeilen zu den Kandidaten des Morgen-Scans und bewertet sie.

Läuft einmal am Tag zum Börsenstart, wenn
  - das Datum in trader/system.json („ai.start“) erreicht ist und
  - das GitHub-Secret ANTHROPIC_API_KEY angelegt ist.
Ergebnis: trader/lab/ai/<Tag>.json. Abends vergleicht der Rückblick, wie die bewerteten Aktien gelaufen sind,
damit messbar wird, ob die KI-Meinung hilft. Nur Spielgeld, keine Kaufempfehlung.
"""

import json
import os

MODEL = "claude-opus-5-5"
MAX_TOKENS = 4000

SCHEMA = {
    "type": "object",
    "properties": {
        "ratings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string"},
                    "news": {"type": "string", "enum": ["positiv", "neutral", "negativ", "keine"]},
                    "risk": {"type": "string", "enum": ["niedrig", "mittel", "hoch"]},
                    "why": {"type": "string"},
                },
                "required": ["symbol", "news", "risk", "why"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["ratings"],
    "additionalProperties": False,
}

PROMPT = """Du hilfst bei einem Daytrading-Experiment mit Spielgeld (US-Aktien, nur Kauf, Haltedauer höchstens ein Tag).
Bewerte für jede Aktie unten die Nachrichtenlage der letzten 24 Stunden für einen Kauf heute:
- news: positiv / neutral / negativ / keine (wenn keine Meldung vorliegt)
- risk: Risiko für einen Tages-Trade (z. B. Zahlen heute, Übernahme-Gerücht, Klage = hoch)
- why: ein kurzer deutscher Satz (höchstens 20 Wörter), warum.
Bewerte nur, was in den Meldungen steht. Erfinde nichts. Jede Aktie genau einmal.

Aktien: {symbols}

Meldungen:
{items}
"""


def enabled(cfg, day):
    a = cfg.get("ai") or {}
    return bool(a.get("start")) and day >= a["start"] and bool(os.environ.get("ANTHROPIC_API_KEY"))


def due_without_key(cfg, day):
    """Startdatum erreicht, aber noch kein Schlüssel: dann erinnert der Push zum Börsenstart."""
    a = cfg.get("ai") or {}
    return bool(a.get("start")) and day >= a["start"] and not os.environ.get("ANTHROPIC_API_KEY")


def review(symbols, items):
    """-> Liste {symbol, news, risk, why}. Fehler werden als Ausnahme gemeldet."""
    import anthropic
    lines = []
    for it in items[:60]:
        lines.append("- [%s] %s%s" % (it.get("ticker") or ",".join(it.get("touches") or []), it.get("title", ""),
                                      (" – " + it["summary"][:300]) if it.get("summary") else ""))
    client = anthropic.Anthropic()
    resp = client.beta.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": PROMPT.format(symbols=", ".join(symbols),
                                                            items="\n".join(lines) or "(keine)")}],
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError("KI hat abgelehnt")
    text = next(b.text for b in resp.content if b.type == "text")
    rows = json.loads(text)["ratings"]
    want = set(symbols)
    return [r for r in rows if r["symbol"] in want]
