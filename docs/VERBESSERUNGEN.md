# Suche nach Verbesserungen (Nacht zum 23.10.2026, bis 2:30 Uhr)

Geprüft wurden: Recherche (Studien, Profi-Regeln, Aufbau von Trading-Apps), die echten Labor-Ergebnisse,
Lauf-Protokolle der Workflows und Browser-Tests der Oberfläche. Bewertet nach: Bringt es uns dem Ziel näher
(ehrliche Messung → Simulator → echtes Geld)? Aufwand? Risiko?

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

## Geprüft, (noch) nicht umgesetzt
| Idee | Grund |
|---|---|
| Leerverkauf (Short) wie in der Studie | im Plan ausgeschlossen (kein Leerverkauf ohne dein OK) |
| Hebel wie in der Studie (bis 4×) | im Plan ausgeschlossen |
| Alle 7.000 Aktien statt ~230 im Live-Labor | zu viele Anfragen an die kostenlosen Yahoo-Daten alle 10 Minuten |
| Bezahlte Echtzeit-Daten | 0 €-Budget in Monat 1 |
| KI-Zweitmeinung (Claude-API) | im Interview auf Monat 2 verschoben, braucht API-Schlüssel und Budget |
| Markt-Filter (nur handeln, wenn der Gesamtmarkt steigt) | sinnvoll, erst testen, wenn genug Live-Tage da sind → Kandidat für nächste Woche |
| Notizen zu Trades auf der Webseite | braucht einen Speicher; möglich über den ntfy-Antwortkanal → Kandidat |
