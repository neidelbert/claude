# Trader-Übersicht

Stand: Do 22.10. 20:04 Uhr ET (02:04 Uhr MESZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: geschlossen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Do 22.10. 18:31 Uhr ET (00:31 Uhr MESZ) | OK – 823 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865573995)) |
| ORB-Scan | noch nie | – |
| Labor live | noch nie | – |
| Labor | Do 22.10. 20:04 Uhr ET (02:04 Uhr MESZ) | OK – 5 von 58 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/39875812193)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Do 22.10.2026

5.945 Aktien in der Liste · 5.943 Charts geladen · 1.597 liquide (ab 5 $ und 1.000.000 Aktien) · 1.595 gescannt · **823 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 512 | AAPL, PG, LLY, WMT, BRK.B, V, IBM, COST |
| `bull_flag` | 75 | WMT, V, MA, SHOP, MPC, KDP, MDT, NU |
| `reclaim_ma20` | 120 | JNJ, BX, VZ, BKNG, ABT, TGT, RKT, LEN |
| `oversold` | 135 | LRCX, AMAT, CRWV, SKHY, KLAC, COHR, CAT, BAC |
| `oversold_bounce` | 41 | BAC, CMG, INSM, ALK, CZR, AVAV, RCUS, MGM |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| AAPL | 348,22 $ | 64,5 | `breakout_20d` |
| LRCX | 230,15 $ | 24,6 | `oversold` |
| AMAT | 375,58 $ | 25,2 | `oversold` |
| CRWV | 55,60 $ | 26,8 | `oversold` |
| PG | 165,59 $ | 74,5 | `breakout_20d` |
| LLY | 1.306,69 $ | 70,7 | `breakout_20d` |
| WMT | 121,12 $ | 74,7 | `breakout_20d`, `bull_flag` |
| SKHY | 131,69 $ | 29,8 | `oversold` |
| BRK.B | 546,97 $ | 81,8 | `breakout_20d` |
| KLAC | 147,83 $ | 23,8 | `oversold` |
| V | 414,34 $ | 79,3 | `breakout_20d`, `bull_flag` |
| IBM | 252,11 $ | 71,2 | `breakout_20d` |
| COST | 1.018,21 $ | 78,9 | `breakout_20d` |
| SPOT | 583,66 $ | 70,6 | `breakout_20d` |
| NOW | 157,00 $ | 69,0 | `breakout_20d` |
| JNJ | 267,61 $ | 57,2 | `reclaim_ma20` |
| COHR | 207,82 $ | 29,8 | `oversold` |
| MA | 633,21 $ | 79,8 | `breakout_20d`, `bull_flag` |
| CRM | 250,29 $ | 63,1 | `breakout_20d` |
| UNH | 424,98 $ | 72,1 | `breakout_20d` |

Alle 823 Treffer: [watchlist.json](watchlist.json)

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: AAPL +1,23 % · **AMAT -8,16 %** · BRK.B +1,48 % · **CRWV -10,06 %** · **KLAC -9,55 %** · LLY +2,83 % · **LRCX -11,76 %** · **PG +5,58 %** · **SKHY -8,07 %** · WMT +2,82 %

- 22.10. 18:27 Uhr ET · **AAPL** · [Dow Jones Futures: Moderna Crashes, Meta Fuels AI Meltdown, But Warren Buffett Market Thriving](https://finance.yahoo.com/m/47e878bb-824d-3243-a8e9-b86b1c3f85d3/dow-jones-futures%3A-moderna.html?.tsrc=rss) · macro
- 22.10. 18:15 Uhr ET · **LLY** · [Amgen vs. Eli Lilly: Does the GLP-1 Mania Make LLY Stock a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/22/amgen-vs-eli-lilly-does-the-glp-1-mania-make-lly-stock-a-better-buy-in-2026/?.tsrc=rss)
- 22.10. 18:04 Uhr ET · **PG** · [Procter & Gamble Q1 Earnings Call Highlights](https://www.marketbeat.com/instant-alerts/transcript-procter-gamble-q1-earnings-call-highlights-2026-10-22/?utm_source=yahoofinance&utm_medium=yahoofinance&.tsrc=rss) · earnings
- 22.10. 17:56 Uhr ET · **WMT** · [Affirm, Sam's Club Strike Exclusive Buy Now, Pay Later Deal](https://finance.yahoo.com/video/affirm-sams-club-strike-exclusive-215624903.html?.tsrc=rss) · deal, people
- 22.10. 17:51 Uhr ET · **CRWV** · [Stock Market Today, Oct. 22: CoreWeave Slides on Bernstein Downgrade and Financing Worries](https://www.fool.com/coverage/stock-market-today/2026/10/22/stock-market-today-oct-22-coreweave-slides-on-bernstein-downgrade-and-financing-worries/?.tsrc=rss) · analyst
- 22.10. 17:18 Uhr ET · **LLY** · [What Does Eli Lilly (LLY) Mean To Signal With Its $5 Billion Richmond Build?](https://finance.yahoo.com/healthcare/articles/does-eli-lilly-lly-mean-211802614.html?.tsrc=rss)
- 22.10. 17:01 Uhr ET · **LRCX** · [Chip Stocks Tumble Despite Solid Earnings Reports](https://finance.yahoo.com/m/590849aa-2dbe-3494-8c1f-3805dca35f0b/chip-stocks-tumble-despite.html?.tsrc=rss) · earnings
- 22.10. 17:00 Uhr ET · **BRK.B** · [Kinsale Capital Group, Inc. (KNSL) Q3 Earnings Surpass Estimates](https://finance.yahoo.com/markets/stocks/articles/kinsale-capital-group-inc-knsl-210006034.html?.tsrc=rss) · earnings
- 22.10. 16:53 Uhr ET · **CRWV** · [Tesla, SpaceX, Meta, Lockheed Martin, Lam Research, Spotify, and More Stocks That Explain Today’s Market](https://finance.yahoo.com/m/add35572-856e-31cb-981d-91d3cc20d822/tesla%2C-spacex%2C-meta%2C-lockheed.html?.tsrc=rss)
- 22.10. 16:47 Uhr ET · **CRWV** · [CoreWeave and Nebius Stocks Are Crashing. Time to Buy the Dip?](https://www.fool.com/investing/2026/10/22/coreweave-and-nebius-stocks-are-crashing-time-to/?.tsrc=rss)
- 22.10. 16:45 Uhr ET · **WMT** · [Walmart (WMT) Advances While Market Declines: Some Information for Investors](https://finance.yahoo.com/markets/stocks/articles/walmart-wmt-advances-while-market-204504019.html?.tsrc=rss)
- 22.10. 16:45 Uhr ET · **BRK.B** · [Berkshire Hathaway B (BRK.B) Increases Despite Market Slip: Here's What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/berkshire-hathaway-b-brk-b-204502243.html?.tsrc=rss)
- 22.10. 16:44 Uhr ET · **AAPL** · [Meta Eyes an Early Equity Deal for Its AI War Chest—and Berkshire Could Be a Buyer](https://finance.yahoo.com/m/640c88c4-a539-3735-a0ee-746427e88883/meta-eyes-an-early-equity.html?.tsrc=rss) · deal
- 22.10. 16:41 Uhr ET · **PG** · [P&G’s Boosts Q1 Beauty Sales, but Says It Can Do Better](https://wwd.com/business-news/financial/procter-gamble-boosts-q1-2027-beauty-sales-1239381875/?.tsrc=rss)
- 22.10. 16:38 Uhr ET · **LRCX** · [Stock Market Today: Nasdaq Thrashed, Dow Up; Moderna, Meta Lead Sell-Off (Live Coverage)](https://finance.yahoo.com/m/a6067e2b-5ce6-3182-915b-58daa8b6d0f9/stock-market-today%3A-nasdaq.html?.tsrc=rss)
- 22.10. 16:34 Uhr ET · **AAPL** · [Apple’s foldable iPhone has a $2,000 app problem](https://finance.yahoo.com/video/apples-foldable-iphone-has-a-2000-app-problem-203418718.html?.tsrc=rss)
- 22.10. 16:33 Uhr ET · **AAPL** · [Here Are 4 ETFs That Run an Entire Retirement Portfolio for Less Than $50 a Year on $100,000](https://247wallst.com/investing/etf/2026/10/22/here-are-4-etfs-that-run-an-entire-retirement-portfolio-for-less-than-50-a-year-on-100000/?.tsrc=rss)
- 22.10. 16:32 Uhr ET · **AAPL** · [Apple Reportedly Raised Its iPhone Duo Target 44%. Here’s What November 2 Has to Show](https://www.tikr.com/blog/apple-reportedly-raised-its-iphone-duo-target-44-heres-what-november-2-has-to-show?ref=yahoofinance&.tsrc=rss)
- 22.10. 16:28 Uhr ET · **CRWV** · [CoreWeave Sinks 10% as Bernstein Slashes Target to $51: “The Fundamentals Are Probably Stuck”](https://www.tikr.com/blog/coreweave-sinks-10-as-bernstein-slashes-target-to-51-the-fundamentals-are-probably-stuck?ref=yahoofinance&.tsrc=rss) · analyst
- 22.10. 16:20 Uhr ET · **AAPL** · [What Intel, Boeing, Nike Have In Common With Each Other — And Apple](https://finance.yahoo.com/m/901193fa-8922-3df6-9417-b947a80babdc/what-intel%2C-boeing%2C-nike-have.html?.tsrc=rss)
- 22.10. 16:13 Uhr ET · **PG** · [Procter & Gamble Soars 6% on Earnings Beat, Shrugs Off $1.4 Billion Cost Hit: “Strong Start”](https://www.tikr.com/blog/procter-gamble-soars-6-on-earnings-beat-shrugs-off-1-4-billion-cost-hit-strong-start?ref=yahoofinance&.tsrc=rss) · earnings
- 22.10. 16:12 Uhr ET · **LRCX** · [IonQ Sinks 3%, Rigetti Down 5%, D-Wave Down 4% as Quantum Stocks Slide Again in Tech Selloff](https://www.tikr.com/blog/ionq-sinks-3-rigetti-down-5-d-wave-down-4-as-quantum-stocks-slide-again-in-tech-selloff?ref=yahoofinance&.tsrc=rss)
- 22.10. 16:11 Uhr ET · **AAPL** · [Resideo Announces Expected Q1 Software Update to Honeywell Home Smart Thermostats for Compatibility with Apple HomeView](https://finance.yahoo.com/technology/articles/resideo-announces-expected-q1-software-201100727.html?.tsrc=rss) · earnings
- 22.10. 16:04 Uhr ET · **CRWV** · [Companies Are Spending Billions To Build Data Centers. The Timeline For Them To Pay Off is Fuzzy.](https://www.ibtimes.com/companies-are-spending-billions-build-data-centers-timeline-them-pay-off-fuzzy-3808890?.tsrc=rss)
- 22.10. 16:03 Uhr ET · **CRWV** · [AI Selloff Takes These Data Center Stocks With It. How They Can Blunt the Pain.](https://finance.yahoo.com/m/8abcc1d9-6265-3276-947e-5a37db88999e/ai-selloff-takes-these-data.html?.tsrc=rss)

## Pelosi-Tracker (pelosi)

- Fr 02.10.2026 · Hon. Nancy Pelosi (CA11) · [PDF](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035553.pdf)

Meldungen kommen Tage bis Wochen nach dem Handel und nennen nur Betragsspannen.

## Ticker-Analyse: AAPL

- Einstiegsregel (Opening-Range-Ausbruch): **abgelaufen**
- Eröffnungsspanne: 344,60 $ bis 347,28 $
- Grund (Originaltext): no close above the range high $347.28 by 15:30, the last time for a new entry
- 22.10. 18:27 Uhr ET · [Dow Jones Futures: Moderna Crashes, Meta Fuels AI Meltdown, But Warren Buffett Market Thriving](https://finance.yahoo.com/m/47e878bb-824d-3243-a8e9-b86b1c3f85d3/dow-jones-futures%3A-moderna.html?.tsrc=rss)
- 22.10. 16:44 Uhr ET · [Meta Eyes an Early Equity Deal for Its AI War Chest—and Berkshire Could Be a Buyer](https://finance.yahoo.com/m/640c88c4-a539-3735-a0ee-746427e88883/meta-eyes-an-early-equity.html?.tsrc=rss)
- 22.10. 16:34 Uhr ET · [Apple’s foldable iPhone has a $2,000 app problem](https://finance.yahoo.com/video/apples-foldable-iphone-has-a-2000-app-problem-203418718.html?.tsrc=rss)
- 22.10. 16:33 Uhr ET · [Here Are 4 ETFs That Run an Entire Retirement Portfolio for Less Than $50 a Year on $100,000](https://247wallst.com/investing/etf/2026/10/22/here-are-4-etfs-that-run-an-entire-retirement-portfolio-for-less-than-50-a-year-on-100000/?.tsrc=rss)
- 22.10. 16:32 Uhr ET · [Apple Reportedly Raised Its iPhone Duo Target 44%. Here’s What November 2 Has to Show](https://www.tikr.com/blog/apple-reportedly-raised-its-iphone-duo-target-44-heres-what-november-2-has-to-show?ref=yahoofinance&.tsrc=rss)
- 22.10. 16:20 Uhr ET · [What Intel, Boeing, Nike Have In Common With Each Other — And Apple](https://finance.yahoo.com/m/901193fa-8922-3df6-9417-b947a80babdc/what-intel%2C-boeing%2C-nike-have.html?.tsrc=rss)
- 22.10. 16:11 Uhr ET · [Resideo Announces Expected Q1 Software Update to Honeywell Home Smart Thermostats for Compatibility with Apple HomeView](https://finance.yahoo.com/technology/articles/resideo-announces-expected-q1-software-201100727.html?.tsrc=rss)
- 22.10. 15:51 Uhr ET · [How much Apple stock does CEO John Ternus actually own?](https://www.thestreet.com/personalities/how-much-apple-stock-does-john-ternus-own?.tsrc=rss)

## Labor (Testphase, Spielgeld ohne Limit)

178 Aktien · 60 Handelstage · Lerntage Do 30.07.2026 bis Do 24.09.2026 · **Prüftage Fr 25.09.2026 bis Do 22.10.2026** · 58 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · Volumen ≥ 1,5× | 183 | 47 % | +0,10 % | 18,18 € | -347,82 € | möglich | **ja** |
| 2 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 1,5R · Volumen ≥ 1,5× | 183 | 47 % | +0,08 % | 14,80 € | -351,20 € | möglich | **ja** |
| 3 | Opening-Range-Ausbruch 30 Min · Stopp Mitte der Spanne · Ziel 2R · Volumen ≥ 1,5× | 183 | 44 % | +0,05 % | 9,44 € | -356,56 € | möglich | **ja** |
| 4 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 1R · Volumen ≥ 1,5× | 183 | 47 % | +0,04 % | 8,00 € | -358,00 € | möglich | **ja** |
| 5 | Opening-Range-Ausbruch 30 Min · Stopp Mitte der Spanne · Ziel 1,5R · Volumen ≥ 1,5× | 183 | 46 % | +0,03 % | 4,61 € | -361,39 € | möglich | **ja** |
| 6 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R | 94 | 52 % | +0,71 % | 66,42 € | -121,58 € | unwahrscheinlich | nein |
| 7 | Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 2R | 94 | 52 % | +0,47 % | 44,24 € | -143,76 € | unwahrscheinlich | nein |
| 8 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 1R | 94 | 53 % | +0,26 % | 24,68 € | -163,32 € | möglich | nein |
| 9 | Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 106 | 50 % | +0,25 % | 26,79 € | -185,21 € | möglich | nein |
| 10 | Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 1,5R | 106 | 50 % | +0,23 % | 24,66 € | -187,34 € | möglich | nein |
| 11 | Erholung: RSI unter 30 · Stopp 1,5 % darunter · Ziel 2R | 199 | 48 % | +0,14 % | 28,09 € | -369,90 € | möglich | nein |
| 12 | Erholung: RSI unter 30 · Stopp Tagestief · Ziel 2R | 199 | 44 % | +0,14 % | 26,82 € | -371,18 € | möglich | nein |

So liest du das: Ein Trade ist ein Kauf und Verkauf am selben Tag. „Treffer“ ist der Anteil der Trades mit Plus. „€ bei 100 €/Trade“ ist die Summe, wenn jeder Trade mit 100 € gemacht worden wäre. „Zufall möglich“ heißt: zu wenige oder zu schwankende Trades, das Ergebnis kann Glück sein.

- **Opening-Range-Ausbruch: Die ersten 15 oder 30 Minuten bilden eine Spanne. Schließt eine 5-Minuten-Kerze über ihrem Hoch, wird gekauft.**
- **News-Sprung: Die Aktie öffnet deutlich über dem Vortag (meist wegen einer Nachricht) und mit viel Umsatz. Gekauft wird, wenn sie über das Hoch der ersten 5 Minuten steigt.**
- **Stocks in Play (nach der Studie von Zarattini, Barbon und Aziz, 2024): Nur Aktien mit ungewöhnlich viel Umsatz in den ersten 5 Minuten. Ist die erste 5-Minuten-Kerze grün, wird über ihrem Hoch gekauft. Der Stopp liegt eng (10 oder 20 % der durchschnittlichen Tagesschwankung ATR), verkauft wird spätestens zum Schluss. Die Studie handelte auch Leerverkäufe und mit Hebel – hier nur Kauf, ohne Hebel.**
- **Ausbruch mit Markt-Filter: der beste 30-Minuten-Ausbruch, aber nur, wenn der Gesamtmarkt (SPY) zur Signal-Kerze über seinem Eröffnungskurs steht. Profis kaufen ungern gegen einen fallenden Markt.**
- **Ausbruch mit Volumen-Rangliste: wie der 30-Minuten-Ausbruch, aber nur bei den 10 oder 20 Aktien mit dem ungewöhnlichsten Volumen in den ersten 30 Minuten – so wählen Profis ihre „Stocks in Play“.**
- **Erholung: Eine stark gefallene Aktie (RSI unter 30 oder Lücke nach unten) steigt wieder über ihren Tagesdurchschnittspreis (VWAP).**

## Preisalarme

Keine Alarme angelegt. Eine Ticker-Analyse mit „Alarme setzen“ legt Stopp, Ziel und „flat by close“ aus dem Plan an.

## Bedienung

- **Manuell starten:** GitHub → Actions → „Trader-System“ → „Run workflow“ → Teil wählen (bei „ticker“ den Ticker eintragen). Oder Claude im Chat bitten.
- **Push aufs iPhone:** App „ntfy“, Kanal aus `trader/system.json` abonnieren.
- **Einstellungen:** `trader/system.json`.

## Regeln (Legende)

- `breakout_20d`: Schlusskurs über jedem Schlusskurs der 20 Tage davor
- `bull_flag`: über 10 % gestiegen, dann 5 Tage in einer 5-%-Spanne
- `reclaim_ma20`: gestern unter, heute über dem 20-Tage-Schnitt
- `oversold`: RSI 14 unter 30
- `oversold_bounce`: RSI gestern unter 30, heute im Plus geschlossen
- `orb`: 5-Minuten-Kerze schließt über dem Hoch der ersten 15 Minuten

---

Eine Liste von Charts, die zu einer Regel passen, ist keine Kaufliste. Kostenlose Yahoo-Daten, verzögert und inoffiziell, nicht in Echtzeit. Ein Treffer ist veraltet, sobald der Kurs weitergelaufen ist. Das System platziert keine Orders und gibt keine Kaufempfehlung.
