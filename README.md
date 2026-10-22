# claude

## Trader-System

Läuft auf GitHub Actions (`.github/workflows/trader-system.yml`), weil die Claude-Cloud-Sitzung
Yahoo, Nasdaq Trader, SEC und das House Clerk nicht erreicht.

- **Übersicht:** [trader/UEBERSICHT.md](trader/UEBERSICHT.md), nach jedem Lauf neu gebaut.
- **iPhone-Push:** App „ntfy“ installieren → „+“ → Kanal `lukas-trader-4iy8o6ly2j1x` (Server ntfy.sh).
- **Zeitplan (Mo–Fr, NYSE-Handelstage):** Morgen-Scan ab ca. 8:00 Uhr ET (Daily-Scan, News zu den
  ersten 10 Treffern, Pelosi-Tracker), ORB-Scan ab ca. 10:15 Uhr ET, Preisalarme alle 15 Minuten.
- **Manuell:** Actions → „Trader-System“ → „Run workflow“ → Teil wählen (`morning`, `orb`, `ticker` + Symbol,
  `alerts`, `test`). Claude kann das im Chat ebenfalls starten.
- **Einstellungen:** `trader/system.json`. Steuerung: `tools/trader/system.py`, die übrigen Skripte in
  `tools/trader/` sind Kopien aus den `trader-*` Skills.

Eine Liste von Charts, die zu einer Regel passen, ist keine Kaufliste. Das System platziert keine Orders.
