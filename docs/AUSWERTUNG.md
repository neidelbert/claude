# Auswertung – Nacht zum Freitag, 23.10.2026

## Was heute Nacht fertig geworden ist
| Teil | Stand |
|---|---|
| Labor | 52 Varianten von 4 Strategien, getestet an 178 Aktien über 60 Tage (40 Lerntage, 20 Prüftage) |
| Neue Strategie „Stocks in Play“ | nach der Studie von Zarattini, Barbon und Aziz (2024), der bekanntesten Arbeit zu profitablem Daytrading |
| Labor live | ab heute 15:30 Uhr alle 10 Minuten: Spielgeld-Trades, Vorschläge mit Ja/Nein im Push, Tagesbilanz |
| Simulator | 100 € wie echt, mit Grenzen 3/8/30 € und 1 € Gebühr je Order. Läuft vorerst als Vorschau |
| Lernen | jeden Abend neue Rangliste, Änderungsprotokoll, Wochen-Rückblick am Freitag |
| Echtgeld-Prüfung | Checkliste mit 8 Punkten, alle noch offen |
| Webseite | iPhone-App mit Tabs Heute, Konto, Trades, Labor, Mehr sowie Glossar, Profi-Regeln, Einführung und Einstellungen. Verschlüsselt, Daten nur mit Passwort |

**Sofort nutzbar:** Die Oberfläche liegt als privates Artifact in deinem Claude-Konto: https://claude.ai/artifact/E5sJZ36t6nHv8xSrW5Rsc1
(Datenstand 23.10. nachts, Ja/Nein dort bitte im Push antippen). Die Webseite mit täglichem Update kommt, sobald Pages an ist.

## Ehrliche Zahlen (Labor-Lauf von heute Nacht)
- **3 von 52 Varianten bestanden.** Alle drei sind Opening-Range-Ausbrüche (30 Minuten, hohes Volumen).
  Die beste macht im Schnitt **+0,06 % pro Trade**, das sind +10,06 € auf 179 Trades bei je 100 €. Der Zufallswert
  liegt bei 0,4, das Ergebnis kann also gut Glück sein.
- **Stocks in Play (Studie)** ist in unserer Umsetzung **im Minus**: −0,14 bis −0,23 % pro Trade. Mögliche Gründe:
  nur Kauf, kein Leerverkauf, 230 statt 7.000 Aktien, verzögerte Gratisdaten. Das Labor testet die Strategie weiter.
- **Simulator-Vorschau** (Top-Variante, 100 €, alle Grenzen): **20,90 €** mit 1 € Gebühr je Order und **98,84 €** ohne Gebühr.
  → Mit 100 € Kapital und 1 € je Order ist Daytrading praktisch nicht zu gewinnen, denn jede Runde kostet 2 % Gebühr.
- Fazit: Noch hat keine Regel bewiesen, dass sie Geld verdient. Das ist nach einem Tag normal. Die Live-Tage ab heute
  zeigen, ob sich etwas hält.

## In der Nacht noch behoben
- Eine Änderung hatte die Workflow-Datei ungültig gemacht (ein Doppelpunkt im Schritt-Namen), dadurch lief kurz kein
  Zeitplan. Das ist repariert. Neu prüft ein Workflow „Prüfen“ jede Änderung automatisch, damit so etwas sofort auffällt.
- Neue Varianten „Ausbruch mit Volumen-Rangliste“ (jetzt 56), „Lohnt sich bis X € Gebühr“ je Variante,
  Karte „Weg zum Ziel“ auf der Startseite.
- Pushes öffnen vorerst die Übersicht auf GitHub, bis die Webseite online ist.

- Ja/Nein-Fehler behoben: Die Antworten wurden kleingeschrieben, dadurch wären Ja-Trades nie gezählt worden.
- Neu: Notizen zu jedem Trade (Tagebuch), auf echter Infrastruktur getestet. Markt-Filter im Labor (58 Varianten).
- Der 22.10. ist als erster Live-Tag nachträglich durchgerechnet (1.534 Spielgeld-Trades aller Varianten).

## Entscheidungen von Lukas (23.10. nachmittags)
| Frage | Entscheidung | Umsetzung (#32) |
|---|---|---|
| Simulator-Start | nach der Go-Ampel | Push „GO für den Simulator“ mit Ja/Nein; Ja → `trader/lab/sim_start.json`, Simulator zählt ab dem nächsten Tag |
| Gebühren | nur Trades mit gutem Muster | 18 neue Varianten (76 statt 58): 6 Grundregeln × Filter „Volumen über 4×“, „über 2×“, „bis 12 Uhr ET und Stopp ≥ 0,5 %“ |
| Push-Kanal privat | nein, so lassen | – |
| KI-Zweitmeinung | ja, ab Monat 2 | ab 23.11. (`ai.start`), braucht Secret `ANTHROPIC_API_KEY`; bis dahin aus, danach Erinnerung im Börsenstart-Push. Kosten mit Claude Opus 5.5 (Effort niedrig, 1 Aufruf am Tag): unter 1 € im Monat |
| Datenschutz | verschlüsseln | Ja/Nein, Notizen und deine Ja-Trades AES-verschlüsselt, sobald das Secret `DATEN_SCHLUESSEL` angelegt ist |
| SEC-Meldungen | nein | – |

## Noch offen
1. **Secret `DATEN_SCHLUESSEL` anlegen** (sonst bleibt alles im Klartext): GitHub → Repo `claude` → Settings → Secrets and variables → Actions → „New repository secret“, Name `DATEN_SCHLUESSEL`, Wert: ein langes Passwort (nicht das der Webseite). Hinweis: Die alten Antworten bleiben in der Git-Geschichte lesbar, und die Antworten laufen weiter über den öffentlichen Antwortkanal (ntfy hält sie ca. 12–24 Std.).
2. **Am 23.11.: Secret `ANTHROPIC_API_KEY`** (Schlüssel von console.anthropic.com), dann schaltet sich die KI von selbst ein.

## Zu deinem Ziel „Geld verdienen, um mehr in Claude zu investieren“
Ehrlich gesagt: Das System kann dir zeigen, **ob** eine Regel funktioniert, aber es kann keinen Gewinn versprechen.
Die meisten Daytrader verlieren Geld. Der sicherste Weg ist der, den wir gehen: erst messen, dann mit Spielgeld beweisen,
dann klein und nur mit deinem Ja.

## Heute (Freitag)
- ca. 14:00 Uhr: Morgen-Scan (Push)
- 15:30–22:00 Uhr: erster echter Live-Tag des Labors, mit Vorschlägen und Ja/Nein
- ca. 22:10 Uhr: Tagesbilanz, danach die neue Rangliste und der erste **Wochen-Rückblick**
- 16:50 Uhr: Ich prüfe, ob der Zeitplan von selbst läuft, und melde mich
