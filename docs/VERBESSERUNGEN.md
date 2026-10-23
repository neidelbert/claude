# Suche nach Verbesserungen (Nacht zum 23.10.2026, bis 2:30 Uhr)

Geprüft wurden: Recherche (Studien, Profi-Regeln, Aufbau von Trading-Apps), die echten Labor-Ergebnisse,
Lauf-Protokolle der Workflows und Browser-Tests der Oberfläche. Bewertet nach: Bringt es uns dem Ziel näher
(ehrliche Messung → Simulator → echtes Geld)? Aufwand? Risiko?

## Methode
Jede Idee bekommt 1–3 Punkte für **Nutzen fürs Ziel** (doppelt gewichtet), **wenig Aufwand** und **wenig Risiko**
(max. 12 Punkte). Umgesetzt wird von oben nach unten, solange bis 2:30 Uhr Zeit ist. Quellen der Ideen: Recherche
(Zarattini/Barbon/Aziz 2024, Profi-Regeln zu Risiko und Tagebuch, Aufbau von Broker-Apps), echte Labor-Zahlen,
Workflow-Protokolle, Browser-Tests.

| Idee | Nutzen ×2 | Aufwand | Risiko | Punkte | Ergebnis |
|---|---|---|---|---|---|
| Webseite ohne Secret online (öffentl. Schlüssel, gh-pages) | 3 | 2 | 3 | 11 | ✓ #17 |
| Workflow-Prüfung jeder Änderung | 3 | 3 | 3 | 12 | ✓ #15 |
| Gebühren-Grenze je Variante | 3 | 3 | 3 | 12 | ✓ #15 |
| „Weg zum Ziel“ auf der Startseite | 3 | 3 | 3 | 12 | ✓ #15 |
| Markt-Filter (nur kaufen, wenn SPY im Plus) | 3 | 3 | 3 | 12 | ✓ #20 |
| Ausbruch mit Volumen-Rangliste | 3 | 2 | 3 | 11 | ✓ #15 |
| Live-Prüfung der Webseite | 2 | 3 | 3 | 10 | ✓ #18 |
| Option „leise“ für Nacht-Tests | 1 | 3 | 3 | 8 | ✓ #19 |
| Notizen zu Trades (über ntfy-Antwortkanal) | 2 | 1 | 2 | 7 | ✓ #21 |
| KI-Zweitmeinung (Claude-API) | 2 | 1 | 2 | 7 | Monat 2 (Interview) |
| Alle 7.000 Aktien live | 2 | 1 | 1 | 6 | nein: Datenlimit |
| Leerverkauf / Hebel wie die Studie | 2 | 2 | 1 | 7 | nein: im Plan ausgeschlossen |
| Bezahlte Echtzeitdaten | 2 | 2 | 2 | 8 | nein: 0-€-Budget |

## Umgesetzt
| Verbesserung | Warum | Wo |
|---|---|---|
| Strategie „Stocks in Play“ (8 Varianten) | bekannteste Studie zu profitablem Daytrading (Zarattini/Barbon/Aziz 2024) | #7 |
| Ausbruch mit Volumen-Rangliste (4 Varianten) | bester bisheriger Ausbruch + Auswahl wie bei Profis („Stocks in Play“) | #15 |
| Gebühren-Grenze je Variante („lohnt sich bis X € je Order“) | Gebühren entscheiden bei 100 € über Plus/Minus → wichtigste Zahl für die Broker-Wahl | #15 |
| Simulator 100 € mit 3/8/30-€-Grenzen und Gebühr | Vorbereitung auf echtes Geld, wie im Interview beschlossen | #7 |
| Echtgeld-Prüfung (8 Punkte) | verhindert, dass Glück für Können gehalten wird | #7 |
| „Weg zum Ziel“ auf der Startseite | zeigt jeden Tag, wo wir stehen und was jetzt zählt | #15 |
| Änderungsprotokoll + Wochen-Rückblick | Lernen sichtbar machen, ohne sich selbst zu betrügen | #7 |
| Tagebuch über mehrere Tage, Varianten-Details, Einführung | Anfänger-tauglich, wie in Broker-Apps | #8 |
| Workflow „Prüfen“ für jede Änderung | ein ungültiger Workflow hatte nachts den Zeitplan gestoppt (#12) | #15 |
| Webseite ohne Secret (öffentlicher Schlüssel) + gh-pages | Seite ging nicht online, weil Pages/Secret fehlten | #17 |
| Live-Prüfung der Webseite | Beweis, dass die echte Adresse funktioniert | #18 |
| Option „leise“ für manuelle Läufe | Tests in der Nacht ohne Push | #19 |
| Markt-Filter (2 Varianten) | Profis kaufen ungern gegen einen fallenden Markt; testet den besten Ausbruch nur bei steigendem SPY | #20 |

## Geprüft, (noch) nicht umgesetzt
| Idee | Grund |
|---|---|
| Leerverkauf (Short) wie in der Studie | im Plan ausgeschlossen (kein Leerverkauf ohne dein OK) |
| Hebel wie in der Studie (bis 4×) | im Plan ausgeschlossen |
| Alle 7.000 Aktien statt ~230 im Live-Labor | zu viele Anfragen an die kostenlosen Yahoo-Daten alle 10 Minuten |
| Bezahlte Echtzeit-Daten | 0 €-Budget in Monat 1 |
| KI-Zweitmeinung (Claude-API) | im Interview auf Monat 2 verschoben, braucht API-Schlüssel und Budget |
| Notizen zu Trades auf der Webseite | braucht einen Speicher; möglich über den ntfy-Antwortkanal → Kandidat |

## Protokoll (deutsche Zeit, 23.10.2026)
| Uhrzeit | Schritt |
|---|---|
| 01:31 | Recherche: Profi-Regeln (Risiko je Trade, Tagesgrenze, Tagebuch), Studie Zarattini/Barbon/Aziz, Aufbau von Broker-Apps |
| 01:35 | Stocks in Play, Simulator, Lernprotokoll, Wochen-Rückblick, neue Tabs (#7) |
| 01:41 | Tagebuch über mehrere Tage, Varianten-Details, Ticker-Analyse, Einstellungen, Einführung (#8) |
| 01:46 | Fehler gefunden und behoben: ungültiger Workflow (#14); Prüf-Workflow gegen Wiederholung (#15) |
| 01:48 | Volumen-Rangliste, Gebühren-Grenze, „Weg zum Ziel“ (#15) |
| 01:51 | Pages über gh-pages eingeschaltet; Webseite ohne Secret mit öffentlichem Schlüssel (#17) |
| 01:55 | Live-Prüfung der Webseite (#18), bestanden |
| 01:59 | Option „leise“, Liste der Verbesserungen (#19) |
| 02:03 | Markt-Filter (#20), Punkte-Tabelle; Labor-Lauf: 58 Varianten, 5 bestanden |
| 02:07 | Notizen zu Trades (#21); dabei Fehler gefunden: Ja/Nein-IDs wurden kleingeschrieben, Ja-Trades wären nie gezählt worden → behoben und getestet |
| 02:08–04:50 | **Unterbrechung:** Die Claude-Sitzung wurde neu gestartet, in dieser Zeit lief keine Arbeit. Die Suche endete deshalb um 02:08 statt 02:30 |
| 04:50 | Nach dem Neustart: #21 gemergt, Webseite leise neu gebaut, mit Passwort getestet (58 Varianten, Notizen vorhanden), Live-Prüfung bestanden |
| 04:52–04:55 | Nachgeholte Zeit: Notizen auf echter Infrastruktur getestet (#23): Test-Notiz über ntfy → Live-Lauf → `trader/lab/notes.json` ✓. Nebenbei hat der Live-Lauf den 22.10. nachträglich mit allen Varianten durchgerechnet (1.534 Spielgeld-Trades) |
| 04:56 | Test-Notiz aus dem Tagebuch entfernt; Auswertung (5:40-Push) auf den neuesten Stand gebracht |
| 04:58 | Labor-Protokoll gelesen: SQ liefert keine Daten mehr (Block heißt jetzt XYZ) → Aktienliste korrigiert |
