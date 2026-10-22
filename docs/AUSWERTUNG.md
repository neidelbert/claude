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

## Offene Fragen an dich
1. **Webseite einschalten (dringend):** Hast du schon
   (a) das Secret `SITE_PASSWORD` angelegt und
   (b) unter Settings → Pages bei „Source“ **GitHub Actions** gewählt?
   Das Veröffentlichen ist heute Nacht fehlgeschlagen, wahrscheinlich weil (b) fehlt.
2. **Ja/Nein-Test:** Hast du im Test-Push auf „Ja“ oder „Nein“ getippt? Dann prüfe ich, ob die Antwort angekommen ist.
3. **Simulator-Start:** Ab wann soll der echte Simulator zählen? Mein Vorschlag: sobald eine Variante 4 Wochen live im
   Plus bleibt. Oder soll er sofort parallel starten?
4. **Gebühren und Kapital:** Mit 1 € je Order frisst die Gebühr jeden Gewinn. Was davon soll ich prüfen?
   (a) Broker mit sehr kleinen Gebühren und Schnittstelle suchen
   (b) mit mehr Kapital rechnen (z. B. 500 €)
   (c) seltener handeln (höchstens 1 Trade pro Tag)
5. **Push-Kanal privat machen?** Das Repo ist öffentlich, also kann jeder den Kanalnamen lesen. Ich kann dir zeigen, wie
   du zwei Secrets (`NTFY_TOPIC`, `NTFY_REPLY_TOPIC`) mit neuen Namen anlegst.
6. **Wie viele Pushes?** Ab heute kommen Vorschläge nur für die Top-Varianten, dazu Ausstiege und die Tagesbilanz. Wird es
   zu viel, kann ich auf „nur Vorschläge + Tagesbilanz“ umstellen.
7. **SEC-Meldungen (8-K)?** Dafür braucht die SEC Name und E-Mail. Optional als Secret `SEC_USER_AGENT`.
8. **KI-Zweitmeinung ab Monat 2?** Claude würde die News zu jedem Vorschlag lesen und bewerten. Das braucht einen
   Claude-API-Schlüssel und kostet ca. 5–10 € im Monat. Ja oder nein?
9. **Datenschutz:** Deine Ja/Nein-Antworten liegen im Klartext im öffentlichen Repo, die Webseite ist verschlüsselt.
   Ist das okay, oder soll ich sie auch verschlüsseln?

## Zu deinem Ziel „Geld verdienen, um mehr in Claude zu investieren“
Ehrlich gesagt: Das System kann dir zeigen, **ob** eine Regel funktioniert, aber es kann keinen Gewinn versprechen.
Die meisten Daytrader verlieren Geld. Der sicherste Weg ist der, den wir gehen: erst messen, dann mit Spielgeld beweisen,
dann klein und nur mit deinem Ja.

## Heute (Freitag)
- ca. 14:00 Uhr: Morgen-Scan (Push)
- 15:30–22:00 Uhr: erster echter Live-Tag des Labors, mit Vorschlägen und Ja/Nein
- ca. 22:10 Uhr: Tagesbilanz, danach die neue Rangliste und der erste **Wochen-Rückblick**
- 16:50 Uhr: Ich prüfe, ob der Zeitplan von selbst läuft, und melde mich
