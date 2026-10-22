# Trader-System – Plan (Stand 22.10.2026, nach dem Interview mit Lukas)

## Ziel
Ein KI-gestütztes Daytrading-System für US-Aktien mit einer einfachen, privaten iPhone-Webseite,
die alles in einfacher Sprache erklärt. Start mit 100 € **Spielgeld**; echtes Geld erst, wenn die
ehrliche Messung über 2–3 Monate im Plus war. Niemand kann Gewinne versprechen – auch keine KI.

## Entscheidungen aus dem Interview
| Thema | Entscheidung |
|---|---|
| Start | Spielgeld (Paper-Trading), virtuelle 100 € |
| Automatik | KI sucht, prüft und schlägt vor. Bei echtem Geld braucht jede Order Lukas' Ja |
| Broker | Trade Republic vorhanden (keine Schnittstelle) → spielt erst bei echtem Geld eine Rolle |
| Zeit | Lukas schaut nur unregelmäßig → feste Stopps, jeder Daytrade wird bis Börsenschluss geschlossen |
| Privat | Repo bleibt öffentlich, alles Persönliche wird mit Passwort verschlüsselt (kostenlos) |
| Grenzen (Spielgeld) | max. 3 € Verlust pro Trade, 8 € pro Tag, 30 € (30 %) pro Monat; dann Pause |
| Erklärungen | Kurz: 2–3 Sätze pro Vorschlag + Glossar |
| Pushes | nur die Tagesbilanz am Abend |
| Alter | 18+ |
| Markt | US-Aktien |
| Erfolg Monat 1 | Ehrliche Messung: lief jeden Tag, hielt alle Grenzen, zeigt Plus oder Minus |

## Konflikt und Lösung
„Vorschlag + mein Ja“ und „nur Tagesbilanz-Push / unregelmäßig“ passen nicht zusammen: Ein
Einstieg um 10:15 Uhr ET (16:15 Uhr bei uns) wartet nicht bis zum Abend. Daher:
- **Spielgeld-Phase:** Das System nimmt die Spielgeld-Trades **selbst nach festen Regeln** (es geht kein
  echtes Geld raus). Nur so lässt sich ehrlich messen, ob die Regeln etwas taugen.
- **Echtgeld-Phase (später):** jede Order nur mit Lukas' Ja (trader-risk → trader-broker). Wie genau,
  klären wir, wenn es so weit ist.

## Bausteine
1. **Spielgeld-Konto** (`paper`): 100 € Start, Bruchstücke von Aktien erlaubt, Einstieg per
   Opening-Range-Ausbruch auf den Morgen-Treffern, Stopp = Mitte der Spanne, Ziel = 2R, raus spätestens
   15:55 Uhr ET. Positionsgröße so, dass der Verlust am Stopp ≤ 3 € ist (trader-exit + trader-budget).
   Tages- und Monatsgrenze aus trader-risk. Kosten realistisch (Spread-Aufschlag).
2. **Tagesbilanz** am Abend als Push: Kontostand, Trades des Tages, Grenzen, ein Satz Erklärung.
3. **Webseite** (GitHub Pages, iPhone-Design, verschlüsselt):
   - *Heute*: Was ist los? Markt offen/zu, Kontostand, offene Trades, Ampel für die Grenzen
   - *Trades*: jeder Trade mit Einstieg, Stopp, Ziel, Ergebnis und 2–3 Sätzen Erklärung
   - *Scanner*: Morgen-Treffer und ORB-Treffer, Regeln in einfacher Sprache
   - *News*: Meldungen zu den Treffern
   - *Monat*: Verlauf des Kontos, Gewinn/Verlust-Tage, ehrliche Bewertung
   - *Lernen*: Glossar und kurze Erklärungen
4. **Verschlüsselung:** Daten werden auf GitHub Actions mit dem Passwort (Secret `SITE_PASSWORD`)
   verschlüsselt (AES-GCM), die Seite entschlüsselt im Browser. Ohne Passwort sieht man nichts Persönliches.

## Schritte
- [x] Schritt 1: Interview
- [ ] Schritt 2: Spielgeld-Konto + Tagesbilanz-Push
- [ ] Schritt 3: Webseite (iPhone-Design, verschlüsselt) + Passwort
- [ ] Schritt 4: 4 Wochen Messung, wöchentlich gemeinsam auswerten
- [ ] Schritt 5: Regeln verbessern (Backtest mit trader-timemachine), weiter messen
- [ ] Schritt 6: Entscheidung über echtes Geld (Broker mit Schnittstelle, Steuern, Freistellungsauftrag)

## Was Lukas einmalig tun muss (in Schritt 3)
- In GitHub ein Secret `SITE_PASSWORD` anlegen (Anleitung kommt mit Bildern/Schritten).
- GitHub Pages einschalten: Settings → Pages → Source „GitHub Actions“.
