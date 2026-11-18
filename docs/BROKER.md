# Broker-Vergleich (Stand 18.11.2026)

Ziel: später 100 € echtes Geld, US-Aktien, höchstens 1 Trade am Tag („Beste Signale“), Order möglichst per Schnittstelle (API).
Alle Angaben aus Vergleichsseiten und Anbieter-Seiten. **Vor einer Kontoeröffnung die aktuelle Preisliste beim Anbieter prüfen.**

## Was eine Order kosten darf
Das Labor rechnet je Regel aus, bis zu welcher Gebühr je Order sie sich lohnt („be_fee“, bei 100 € je Trade).
Stand 17.11.: Die besten Regeln (News-Sprung ≥ 4 %, Volumen ≥ 3×) liegen bei **0,55–0,75 € je Order**
(über alle Tage), die meisten anderen unter 0,40 €. Mit 1 € je Order ist also keine Regel im Plus.
Eine Gebühr ist bei 100 € Einsatz ein großer Anteil: Hin und zurück kosten 2 × 1 € = 2 % des Einsatzes.

## Anbieter
| Broker | Gebühr US-Aktie je Order | API | Passt? |
|---|---|---|---|
| Trade Republic | 1 € (Bestpreis), 2 € Direktpreis seit 2.7.2026; Währungstausch ca. 1,20 € je 1.000 € | nein | einfach, aber zu teuer für unsere Regeln |
| Scalable Capital | 0,99–1,99 € je Order (je nach Börse), Flatrate ab 4,99 €/Monat | nein | Flatrate wäre interessant, aber keine API |
| DEGIRO | ca. 2 € | nein | zu teuer |
| Interactive Brokers (IBKR Pro, gestaffelt) | 0,0005–0,0035 $ je Aktie, **mindestens 0,35 $ je Order**, dazu Börsen- und Clearing-Gebühren | ja (sehr umfangreich) | **günstigste Option mit API**; bei 100 € und wenigen Aktien greift fast immer das Minimum |
| Alpaca (Alpaca Europe, Spanien) | in den USA ohne Ordergebühr; EU-Gebühren noch nicht klar | ja (für Programme gebaut) | beobachten: seit Juli 2026 in 29 EWR-Ländern, Bedingungen für Deutschland ungeklärt |

## Regeln in den USA
Die „Pattern Day Trader“-Regel (mindestens 25.000 $ für häufiges Daytrading) wurde 2026 abgeschafft und durch eine
Intraday-Margin-Regel ersetzt (SEC-Freigabe April 2026, gültig ab 4.6.2026, Übergangszeit für Broker bis Okt. 2027).
Mit einem **Barkonto ohne Kredit** und 1 Trade am Tag spielt das für uns ohnehin kaum eine Rolle.

## Empfehlung (vorläufig)
1. Bis zum GO weiter Spielgeld. Das Labor zeigt je Regel, bis zu welcher Gebühr je Order sie sich lohnt (`be_fee`); bei IBKR wären es meist rund 0,35–0,50 € statt 1 €.
2. Kommt das GO, ist **Interactive Brokers** der naheliegende Kandidat (niedrigste Mindestgebühr, API für spätere Automatik).
   Alternative: Alpaca, falls es dann für Deutschland offen ist und günstig bleibt.
3. Echte Orders nur mit Lukas' Ja (trader-risk und trader-broker), keine Gewinnversprechen.

## Quellen
- [Handelsblatt: Online-Broker im Vergleich 2026](https://www.handelsblatt.com/finanzen/online-broker/)
- [WiWo: Scalable Capital oder Trade Republic? 2026](https://www.wiwo.de/vergleich/scalable-capital-oder-trade-republic/)
- [neuebanken.de: Trade Republic & Co. ab Juli 2026](https://www.neuebanken.de/pfof-verbot-2026-neobroker/)
- [Geldaura: Online-Broker-Vergleich 2026](https://geldaura.com/vergleiche/beste-online-broker-2026/)
- [Butterfly Market Insider: Interactive Brokers vs Trade Republic](https://butterflymarketinsider.com/de/broker/interactive-brokers-vs-trade-republic/)
- [Interactive Brokers: Provisionen und Gebühren](https://www.interactivebrokers.co.uk/de/pricing/commissions-home.php?region=americas)
- [BrokerChooser: Interactive Brokers Gebühren](https://brokerchooser.com/de/broker-reviews/interactive-brokers-review/interactive-brokers-fees)
- [Alpaca: Expansion nach Europa](https://alpaca.markets/blog/alpaca-expands-into-europe-and-launches-european-equities-trading/)
- [Finance Magnates: Alpaca in 29 EWR-Ländern](https://www.financemagnates.com/forex/alpaca-passports-investment-services-into-29-eea-countries-from-spanish-hub/)
- [Alpaca EU](https://alpaca.markets/eu)
- [King & Spalding: FINRA ändert Margin-Regeln fürs Daytrading](https://www.kslaw.com/insights/articles/finra-adopts-sweeping-changes-to-margin-requirements-for-day-trading)
- [ACA: FINRA beendet die Pattern-Day-Trader-Regel](https://www.acaglobal.com/industry-insights/finra-ends-the-pattern-day-trader-rule/)
