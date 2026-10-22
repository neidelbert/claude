# Trader-System – kompletter Plan

Stand 22.10.2026, nach dem Interview mit Lukas (8 Runden). Lukas ist Anfänger, Claude baut alles.

## Ziel
Ein verständliches KI-gestütztes Daytrading-System für US-Aktien, mit dem Lukas 2–3 Stunden am Tag
mitentscheidet. Es lernt aus allen Tests und zeigt ehrlich, ob es Geld verdient. Erst Spielgeld.
Echtes Geld erst nach strenger Prüfung und Lukas' Ja.
Niemand kann Gewinne versprechen, auch keine KI. Die meisten Daytrader verlieren Geld. Das System misst
deshalb ehrlich und schützt vor Glückstreffern.

## Entscheidungen aus dem Interview
| Thema | Entscheidung |
|---|---|
| Markt | US-Aktien. Welche, entscheidet das System nach den Messergebnissen |
| Zeit | Mo–Fr, wechselnde 2–3 Stunden (15:30–22:00 Uhr deutsche Zeit); dazwischen unregelmäßig |
| Rolle Lukas | Mitentscheiden: Push mit Ja/Nein-Buttons. Ohne Antwort handelt das System nach Regel |
| Messung | zwei Spalten: „Regel“ (alle Signale) und „Lukas“ (nur Ja-Trades) |
| Strategien | alle testen, die besten behalten (Opening-Range-Ausbruch, Erholung nach Absturz, News-Sprung) |
| Trades | höchstens 1–3 pro Tag und Strategie im Simulator |
| KI (Claude) | Monat 1 nur feste Regeln. KI-Zweitmeinung (Claude-API) ab Monat 2 als Option |
| Dazulernen | Varianten an alten Tagen testen und auf ungesehenen Tagen bestätigen; nur was dort hält, wird übernommen |
| Backtest | ja, mit den letzten ~60 Tagen 5-Minuten-Daten |
| Phasen | Testphase (Labor) → Simulator → Echt |
| Testphase (Labor) | komplette Testphase: Spielgeld ohne jedes Limit und Verbot, alle Strategien und Varianten, alle Zahlen sichtbar, Lernen |
| Simulator | Vorbereitung auf echtes Geld, 100 € so, als wären sie echt: Grenzen 3 € pro Trade / 8 € pro Tag / 30 € pro Monat, Gebühren, Spread |
| Echt | erst nach 2 Simulator-Monaten am Stück im Plus, ≥ 40 Trades, Grenzen nie gerissen, nach Gebühren positiv, dann Lukas' Ja |
| Broker später | gemeinsam prüfen (Schnittstelle, Gebühren, Bruchstücke, deutsche Steuer). Trade Republic hat keine Schnittstelle |
| Kosten | 0 € im Monat (Yahoo-Daten, GitHub, ntfy) |
| Privat | Repo öffentlich, alles Persönliche mit Passwort verschlüsselt. Push-Kanäle als Secrets |
| Webseite | wie eine iPhone-App: Tab-Leiste, große Zahlen, Ampeln, hell/dunkel automatisch, App-Symbol auf dem Home-Bildschirm |
| Startseite „Heute“ | alle relevanten Infos: Kontostand, Tagesergebnis, Grenzen-Ampel, offene Trades live, nächster Schritt, kleine Charts |
| Pushes | alles (Scans, Vorschläge, Ein- und Ausstiege, News, Tagesbilanz), jeder mit 1–2 Sätzen Erklärung |
| Lernen | Erklärung in jedem Push, Tageslektion, Glossar zum Antippen, Wochen-Rückblick |
| Termine | wöchentlich gemeinsam (Lukas + Claude) den Wochen-Rückblick durchgehen |
| Alter | 18+ |

## Wichtige Fakten für Lukas (kommen auch in die Lern-Seite)
- **Gebühren bei 100 €:** 1 € pro Order (z. B. Trade Republic) heißt 2 € pro Trade für Kauf und Verkauf.
  Das sind 2 % des Kapitals, bevor überhaupt ein Cent verdient ist. Der Simulator rechnet das ein.
  Bei der Broker-Wahl ist das der wichtigste Punkt.
- **Verzögerte Daten:** Die kostenlosen Yahoo-Kurse sind inoffiziell und können verzögert sein. Für
  Spielgeld reicht das, für echtes Geld wird es neu bewertet.
- **Ein Monat beweist wenig.** Deshalb gibt es die strenge Prüfung und das Lernen nur auf ungesehenen Tagen.
- **Steuern (Deutschland):** Gewinne sind kapitalertragsteuerpflichtig, mit Freistellungsauftrag beim
  Broker. Das wird vor der Echt-Phase geklärt.

## Aufbau (Technik)
Alles läuft kostenlos auf GitHub Actions im Repo `neidelbert/claude`, ohne eigenen Server.

```
GitHub Actions (alle 5 Min. im Handel, sonst seltener)
  ├─ Scanner (gibt es schon): Morgen-Scan, ORB-Scan, News, Pelosi
  ├─ Labor:      tools/trader/lab.py      – Strategien × Varianten, Backtest 60 Tage, Live-Spielgeld ohne Limit
  ├─ Lernen:     tools/trader/learn.py    – wöchentlich: Varianten auf alten Tagen testen, auf ungesehenen bestätigen
  ├─ Simulator:  tools/trader/sim.py      – 100 € wie echt, Grenzen, Gebühren, Spread, Ja/Nein von Lukas
  ├─ Antworten:  ntfy-Antwortkanal lesen  – Ja/Nein-Buttons aus dem Push
  ├─ Texte:      tools/trader/texte.py    – Erklärungen, Tageslektion, Wochen-Rückblick (Textbausteine; KI ab Monat 2)
  └─ Webseite:   site/ → verschlüsselte data.enc → GitHub Pages
iPhone: ntfy-Pushes mit Ja/Nein-Buttons + Webseite als Home-Bildschirm-App
```

- **Ja/Nein ohne Server:** Der Push-Button schickt „ja ID“ oder „nein ID“ an einen zweiten, privaten
  ntfy-Kanal. Der nächste Lauf liest diesen Kanal.
- **Verschlüsselung:** AES-GCM mit einem Schlüssel aus dem Passwort (PBKDF2). Das Passwort liegt nur im
  GitHub-Secret `SITE_PASSWORD` und bei Lukas. Die Seite entschlüsselt im Browser; nach dem ersten Mal
  bleibt sie auf dem iPhone entsperrt.
- **Ehrliche Messung:** Jeder Trade wird mit Zeitstempel und Daten-Stand gespeichert und nie nachträglich
  geändert. Kennzahlen: Trefferquote, durchschnittliches R, Ergebnis nach Gebühren, größter Rückgang,
  Anzahl Trades. Beim Spielgeld werden alle Gewinn- und Verlustzahlen gezeigt.
- **Lernen ohne Selbstbetrug:** 60 Tage werden geteilt: rund 40 Tage zum Lernen, 20 ungesehene Tage zum
  Prüfen. Dazu kommen live die neuen Tage. Übernommen wird nur eine Variante, die auf den ungesehenen
  Tagen nach Gebühren positiv ist und genug Trades hat (≥ 30).

## Webseite (Tabs)
1. **Heute:** Phase (Labor/Simulator), Markt offen/zu mit Countdown, Kontostand, Tagesergebnis,
   Grenzen-Ampel, offene Trades live mit Abstand zu Stopp und Ziel, „Nächster Schritt“, offene Vorschläge
   mit Ja/Nein, kleine Charts
2. **Trades:** jeder Trade mit Einstieg, Stopp, Ziel, Ergebnis, Gebühren und 2–3 Sätzen „Warum / was
   ist passiert“. Filter: Regel / Lukas / Strategie
3. **Labor:** Rangliste der Strategien und Varianten, Lern- und Prüftage getrennt, was übernommen wurde und warum
4. **Scanner:** Morgen- und ORB-Treffer, News, Pelosi (wie heute in UEBERSICHT.md, nur schöner)
5. **Lernen:** Tageslektion, Wochen-Rückblick, Glossar (Fachwörter überall antippbar), „So funktioniert das System“
6. **Mehr:** Systemstatus, Einstellungen (nur lesen), Echtgeld-Prüfung als Checkliste mit Ampel

## Pushes (alle mit 1–2 Sätzen „Was heißt das?“)
- Morgen-Scan (ca. 14:00 Uhr deutsche Zeit) · Börsenstart · ORB-Treffer
- **Vorschlag** mit Buttons Ja / Nein / Webseite, Einstieg, Stopp, Ziel und Risiko in €
- Einstieg ausgeführt · Stopp oder Ziel erreicht · Zwangsschluss vor Börsenende
- News zu offenen Trades · Grenze erreicht (Simulator)
- Tagesbilanz (ca. 22:15 Uhr) mit Tageslektion · Wochen-Rückblick (Freitag)
- Fehler im System (einmal pro Tag und Fehler)

## Fahrplan bis „fertig“
| Schritt | Inhalt | fertig, wenn |
|---|---|---|
| 1 | Interview, Plan | ✓ dieser Plan |
| 2 ✓ | **Labor-Kern:** 60-Tage-Daten holen, Strategien ORB / Erholung / News-Sprung mit Varianten, Backtest, Trade-Buch | Rangliste mit Lern- und Prüftagen steht |
| 3 ✓ | **Live-Labor:** alle 5 Min. im Handel Signale prüfen, Spielgeld-Trades öffnen und schließen, Pushes mit Erklärung | ein Handelstag läuft komplett allein |
| 4 ✓ (gebaut, wartet auf deinen ersten Test) | **Ja/Nein:** Vorschlags-Pushes mit Buttons, Antwortkanal, Spalte „Lukas“ | Lukas hat per Push zugestimmt und abgelehnt |
| 5 | **Webseite:** iPhone-App-Design, alle Tabs, Glossar, verschlüsselt, GitHub Pages, Home-Bildschirm-Symbol | Lukas öffnet sie auf dem iPhone mit Passwort |
| 6 | **Texte:** Tageslektion, Tagesbilanz, Wochen-Rückblick | ein Freitag mit Rückblick ist gelaufen |
| 7 | **Lernen:** wöchentliches Nachtraining mit Bestätigung auf ungesehenen Tagen, Änderungsprotokoll | erste übernommene oder abgelehnte Variante mit Begründung |
| 8 | **Simulator:** 100 € wie echt, Grenzen 3/8/30 €, Gebühren, Spread. Startet, sobald eine Labor-Strategie die Prüfung besteht | erster Simulator-Monat läuft |
| 9 | **Echtgeld-Prüfung:** Checkliste mit Ampel auf der Webseite | automatisch grün oder rot |
| 10 | **KI-Zweitmeinung (optional, ab Monat 2):** Claude liest News und bewertet Vorschläge, getrennt gemessen | nur wenn Lukas Kosten bis ca. 10 €/Monat freigibt |
| 11 | **Echt (frühestens nach 2 Simulator-Monaten im Plus):** Broker gemeinsam wählen, Steuern klären, jede Order mit Ja | Lukas entscheidet |

Bauzeit für die Schritte 2–7: etwa 1–2 Wochen. Danach läuft die Messung. Realistisch dauert es 3–6 Monate,
bis feststeht, ob eine Strategie den Simulator zwei Monate am Stück im Plus hält. Es kann auch sein, dass
keine Strategie das schafft. Dann zeigt das System das ehrlich.

## Was Lukas einmalig tun muss (Anleitung kommt beim jeweiligen Schritt)
- Schritt 4: nichts, die Ja/Nein-Buttons funktionieren ohne zweites Abo
- Schritt 5: GitHub → Settings → Secrets → `SITE_PASSWORD` anlegen; Settings → Pages → Source „GitHub Actions“
- Schritt 5: Webseite in Safari öffnen → Teilen → „Zum Home-Bildschirm“

## Regeln, die immer gelten
- Das System platziert keine echte Order. Echtes Geld nur über trader-risk und trader-broker, mit Lukas'
  Ja pro Order.
- Kein Hebel, keine Optionen, kein Leerverkauf.
- Treffer heißen „passt zu einer Regel“, nie „Kauf“.
- Jeder Spielgeld-Trade wird vor Börsenschluss geschlossen (Daytrading, nichts über Nacht).
