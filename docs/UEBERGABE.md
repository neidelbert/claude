# Übergabe – Trader-System (für jede neue Claude-Sitzung zuerst lesen)

Stand: 23.10.2026, 05:00 Uhr. Repo: `neidelbert/claude` (öffentlich), Branch `main`.

## Worum es geht
Lukas (Anfänger, programmiert nicht) baut mit Claude ein KI-gestütztes Daytrading-System für US-Aktien.
Phasen: **Testphase** (Spielgeld ohne Limit, alle Strategien) → **Simulator** (100 € wie echt, Grenzen
3/8/30 €, Gebühr 1 € je Order) → **echtes Geld** (erst nach 2 Simulator-Monaten am Stück im Plus und Lukas' Ja).
Den ganzen Plan enthält `docs/TRADER-PLAN.md`, das Interview mit Lukas ist dort eingearbeitet.

## Was läuft
| Teil | Wo | Wann |
|---|---|---|
| Steuerung | `tools/trader/system.py` (Teile: auto, morning, orb, live, lab, alerts, ticker, test, message, render) | – |
| Zeitplan | `.github/workflows/trader-system.yml` | Mo–Fr: 12:00–12:45 UTC alle 15 Min., 13–21 UTC alle 10 Min., 21:20–22:50 UTC |
| Morgen-Scan | `scan.py` (Daily), `news.py`, `ptr.py` (Pelosi) | ab ca. 8:00 Uhr ET |
| ORB-Scan | `scan.py orb` | ab ca. 10:10 Uhr ET |
| Labor live | `lab.py live`: Spielgeld-Trades aller Varianten, Vorschlags-Pushes mit Ja/Nein | alle 10 Min. im Handel |
| Auswertung Börsenstart | `open_summary` in `do_live` (Plan, Weg zum Ziel, offene Fragen) | erster Live-Lauf nach 9:35 Uhr ET |
| Auswertung Börsenschluss | Tagesbilanz in `do_live` (+ Weg zum Ziel, offene Fragen) | ca. 16:00–17:00 Uhr ET |
| Labor-Rangliste | `lab.py fetch/run`: 58 Varianten an 60 Tagen 5-Min.-Kerzen, Lern-/Prüftage | nach Börsenschluss |
| Wochen-Rückblick | `week_review` in `system.py` | letzter Handelstag der Woche |
| Simulator | `sim.py` (Vorschau = Backtest der Top-Variante; live ab `sim.start_date`) | in jeder Webseite |
| Webseite | `site/index.html` + `tools/trader/site.py` → Branch `gh-pages` | nach jedem Commit eines Laufs |
| Prüfungen | `pruefen.yml` (YAML, Python, Selbsttest bei jedem Push), `seite-pruefen.yml` (live, manuell) | – |

## Adressen und Kanäle
- **Webseite:** https://neidelbert.github.io/claude/. Die Daten sind verschlüsselt und lassen sich nur mit Lukas' Passwort öffnen.
  Das Passwort steht **nicht** im Repo, Lukas hat es aus dem Chat. Geht es verloren, muss ein neues
  Schlüsselpaar her: `trader/site_key.json` neu erzeugen (RSA-2048, privater Schlüssel mit PBKDF2-SHA256
  200.000 Runden + AES-GCM und `site_salt` aus `trader/system.json` verschlüsseln).
- **Artifact (Kopie ohne Ja/Nein):** https://claude.ai/artifact/E5sJZ36t6nHv8xSrW5Rsc1. Es wird Mo–Fr um 14:37, 18:37 und 22:37 Uhr
  (Berlin) von einer geplanten Aufgabe neu gebaut (`site.py artifact`).
- **Push (App ntfy, Server ntfy.sh):** Kanal `ntfy_topic` in `trader/system.json`. Ja/Nein und Notizen gehen an
  `ntfy_reply_topic`, den Lukas nicht abonnieren muss. Beide Namen stehen im öffentlichen Repo; die Secrets
  `NTFY_TOPIC`/`NTFY_REPLY_TOPIC` würden sie überschreiben (offene Frage an Lukas).
- **Daten im Repo:** `trader/` (watchlist, orb, status/, logs/, lab/results.json, lab/live/<tag>.json,
  lab/decisions.json, lab/notes.json, lab/changes.json, lab/weekly/). `trader/UEBERSICHT.md` ist die Übersicht
  als Markdown.

## Wichtige Regeln für Claude (aus Erfahrung)
1. **Die Claude-Sitzung hat kein freies Internet** (Yahoo, ntfy und github.io sind gesperrt). Alles, was Netz braucht, läuft auf
   GitHub Actions. Starten mit `mcp__github__actions_run_trigger` (`trader-system.yml`, Eingabe `teil`).
2. **Nachts oder zum Testen immer `leise: true`**, sonst bekommt Lukas einen Push.
3. **Vor jedem Push Workflow-YAML prüfen** (`python3 -c "import yaml; yaml.safe_load(open(...))"`). Ein Doppelpunkt
   in einem Schritt-Namen hat einmal den ganzen Zeitplan gestoppt.
4. **Keine Testdaten committen:** Vor dem Commit `trader/status/live.json`, `trader/lab/live/`, `decisions.json`,
   `notes.json`, `.cache/` und `_site/` prüfen. Offline testen mit `lab.py run --offline` / `live --offline --now`.
5. **Ablauf für Änderungen:** Branch `claude/<thema>` → Commit → PR → Merge (Lukas hat dem zugestimmt).
6. **Selbsttest:** `python3 tools/trader/lab.py selftest`. Browser-Test der Seite: Playwright mit
   `/opt/pw-browsers` (siehe frühere Tests: iPhone-13-Format, hell/dunkel, keine JS-Fehler, kein seitliches Scrollen).
7. **Ehrlich bleiben:** Spielgeld-Zahlen zeigen (erlaubt), aber nie Gewinne versprechen. Echtes Geld nur mit Lukas' Ja.

## Stand der Ergebnisse (23.10.2026 nachts)
- Labor: 58 Varianten, **5 bestanden** (alle Opening-Range-Ausbruch 30 Min. mit Volumen ≥ 1,5×). Die beste bringt
  +18,18 € an den Prüftagen bei 100 € pro Trade, der Zufallswert liegt unter 2.
- „Stocks in Play“ (Studie) ist in unserer Umsetzung im Minus. Der Markt-Filter ist an den Prüftagen besser, an
  den Lerntagen im Minus.
- Simulator-Vorschau: 100 € → **18,88 €** mit 1 € Gebühr je Order, ohne Gebühr ~99 €. Die Gebühren sind das größte Problem.
- Erster Live-Tag: 22.10. (nachträglich gerechnet, 1.534 Spielgeld-Trades aller Varianten).

## Offen
- **Lukas' offene Fragen** stehen in `docs/AUSWERTUNG.md`: Simulator-Start, Broker und Gebühren, Push-Kanal privat,
  Push-Menge, SEC-Agent, KI-Zweitmeinung ab Monat 2, Datenschutz der Antworten.
- **Nächste Ideen** in `docs/VERBESSERUNGEN.md` (Punkte-Tabelle).
- **Auswertungen** kommen auf Lukas' Wunsch nur zum Börsenstart und Börsenschluss als Push, nicht nachts.
- **Geplante Erinnerung dieser Sitzung:** 23.10. 14:50 UTC (Kontrolle des ersten Zeitplan-Tags). Eine neue Sitzung sieht sie mit `list_triggers`.

## Wie eine neue Sitzung weitermacht
1. Repo `neidelbert/claude` klonen bzw. holen, dann diese Datei, `CLAUDE.md`, `docs/TRADER-PLAN.md` und `docs/AUSWERTUNG.md` lesen.
2. Den Zustand prüfen: `trader/status/*.json`, die letzten Actions-Läufe (`mcp__github__actions_list`) und `docs/VERBESSERUNGEN.md`.
3. Lukas kurz auf Deutsch berichten und dann seine nächste Anweisung umsetzen.

## Änderungsprotokoll (jede Änderung hier ergänzen: Datum, PR, was, warum)
| Datum | PR | Änderung |
|---|---|---|
| 22.10. | #1 | CLAUDE.md: Antworten und Skill-Ausgaben auf Deutsch |
| 22.10. | #2 | Trader-System auf GitHub Actions (Netz in der Claude-Sitzung gesperrt), iPhone-Push über ntfy, Übersicht |
| 22.10. | #3 | Plan nach dem Interview, Labor-Kern (44 Varianten, Lern-/Prüftage) |
| 22.10. | #4 | Labor live: Spielgeld-Trades alle 10 Min., Pushes, Tagesbilanz |
| 22.10. | #5 | Ja/Nein-Buttons im Push, Spalte „Lukas“ |
| 22.10. | #6 | Webseite (iPhone-App, verschlüsselt) |
| 23.10. | #7 | Stocks in Play, Simulator (100 €, 3/8/30 €), Lernprotokoll, Wochen-Rückblick, Echtgeld-Prüfung, Tabs Heute/Konto/Trades/Labor/Mehr |
| 23.10. | #8 | Tagebuch über mehrere Tage, Varianten-Details, Ticker-Analyse, Einstellungen, Einführung |
| 23.10. | #9 | Auswertung der Nacht (docs/AUSWERTUNG.md) |
| 23.10. | #10–#12 | Versuche, Pages aus dem Workflow einzuschalten (geht nicht mit dem Workflow-Token) |
| 23.10. | #13 | Oberfläche zusätzlich als privates Artifact (+ geplante Aufgabe 14:37/18:37/22:37 Uhr) |
| 23.10. | #14 | Reparatur: Doppelpunkt im Schritt-Namen machte den Workflow ungültig |
| 23.10. | #15 | Volumen-Rangliste, Gebühren-Grenze je Variante, „Weg zum Ziel“, Prüf-Workflow |
| 23.10. | #16 | Push-Links vorübergehend auf GitHub-Übersicht |
| 23.10. | #17 | Webseite online ohne Secret: öffentlicher Schlüssel + Branch gh-pages |
| 23.10. | #18 | Workflow „Webseite prüfen“ (Live-Test) |
| 23.10. | #19 | Option „leise“, Liste der Verbesserungen |
| 23.10. | #20 | Markt-Filter (58 Varianten), Punkte-Tabelle |
| 23.10. | #21 | Notizen zu Trades; Fehler behoben: Ja/Nein-IDs wurden kleingeschrieben |
| 23.10. | #22, #24 | Protokoll: Unterbrechung durch Neustart, Notiz-Test |
| 23.10. | #23 | Test-Notiz im Prüf-Workflow |
| 23.10. | #25 | Test-Notiz entfernt, Auswertung aktualisiert |
| 23.10. | #26 | SQ durch XYZ ersetzt (keine Daten mehr) |
| 23.10. | #27 | Übergabe-Dokument, CLAUDE.md verweist darauf |
| 23.10. | #28 | Auswertung zum Börsenstart und Börsenschluss statt nachts (5:40-Erinnerung gelöscht); dieses Änderungsprotokoll |
