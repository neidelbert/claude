# Trader-Übersicht

Stand: Fr 27.11. 07:32 Uhr ET (13:32 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: vor der Eröffnung (Handelszeit 09:30 bis 13:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Fr 27.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 374 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45935567529)) |
| ORB-Scan | Mi 25.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 115 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45562375663)) |
| Labor live | Mi 25.11. 16:00 Uhr ET (22:00 Uhr MEZ) | OK – Tagesbilanz: 4.546 Trades ([Lauf](https://github.com/neidelbert/claude/actions/runs/45606660043)) |
| Labor | Mi 25.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 18 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/45606660043)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Mi 25.11.2026

5.922 Aktien in der Liste · 5.922 Charts geladen · 1.467 liquide (ab 5 $ und 1.000.000 Aktien) · 1.465 gescannt · **374 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 158 | INSM, HD, DIS, PG, MCD, TJX, T, VZ |
| `bull_flag` | 12 | BILL, IBN, ATAT, ACHC, MBGL, SGRY, ENR, PGNY |
| `reclaim_ma20` | 118 | V, QCOM, IBM, HPQ, SBUX, LMT, ABT, NEE |
| `oversold` | 45 | SNDK, MSTR, INTU, COIN, DDOG, MPC, NTNX, CRCL |
| `oversold_bounce` | 65 | MSTR, COIN, FCX, BMNR, CRCL, PBR, VALE, SCCO |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| SNDK | 94,39 $ | 29,3 | `oversold` |
| INSM | 170,31 $ | 82,9 | `breakout_20d` |
| V | 424,39 $ | 58,9 | `reclaim_ma20` |
| HD | 361,26 $ | 68,3 | `breakout_20d` |
| MSTR | 79,96 $ | 27,2 | `oversold`, `oversold_bounce` |
| QCOM | 168,66 $ | 49,7 | `reclaim_ma20` |
| DIS | 125,60 $ | 68,7 | `breakout_20d` |
| PG | 173,23 $ | 66,9 | `breakout_20d` |
| MCD | 283,50 $ | 69,5 | `breakout_20d` |
| TJX | 146,09 $ | 61,1 | `breakout_20d` |
| IBM | 243,47 $ | 54,0 | `reclaim_ma20` |
| HPQ | 31,15 $ | 57,5 | `reclaim_ma20` |
| INTU | 271,72 $ | 29,8 | `oversold` |
| COIN | 103,72 $ | 28,6 | `oversold`, `oversold_bounce` |
| SBUX | 107,74 $ | 56,1 | `reclaim_ma20` |
| T | 22,97 $ | 58,5 | `breakout_20d` |
| LMT | 599,24 $ | 55,5 | `reclaim_ma20` |
| VZ | 47,28 $ | 61,1 | `breakout_20d` |
| RKT | 15,30 $ | 67,5 | `breakout_20d` |
| DDOG | 158,25 $ | 30,0 | `oversold` |

Alle 374 Treffer: [watchlist.json](watchlist.json)

## ORB-Scan – 2026-11-25 10:10 ET

Quelle: Treffer des Morgen-Scans · 346 nutzbare Charts · **115 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | ADM | 66,40 $ | 64,78 $ – 66,22 $ | +0,27 % |
| 9:50 AM | AGLT | 5,58 $ | 5,14 $ – 5,42 $ | +2,97 % |
| 9:50 AM | AGMB | 5,72 $ | 5,48 $ – 5,71 $ | +0,22 % |
| 9:50 AM | ALKT | 13,64 $ | 13,34 $ – 13,60 $ | +0,32 % |
| 9:50 AM | BTU | 15,36 $ | 15,14 $ – 15,33 $ | +0,23 % |
| 9:50 AM | CNQ | 45,31 $ | 44,52 $ – 45,14 $ | +0,37 % |
| 9:50 AM | CRK | 12,25 $ | 11,92 $ – 12,13 $ | +0,99 % |
| 9:50 AM | CUE | 7,01 $ | 6,31 $ – 6,89 $ | +1,73 % |
| 9:50 AM | DAR | 48,62 $ | 46,16 $ – 48,32 $ | +0,62 % |
| 9:50 AM | DINO | 85,09 $ | 83,98 $ – 85,06 $ | +0,04 % |
| 9:50 AM | DKNG | 16,11 $ | 15,66 $ – 15,96 $ | +0,94 % |
| 9:50 AM | ENPH | 19,53 $ | 19,08 $ – 19,49 $ | +0,18 % |
| 9:50 AM | ET | 18,60 $ | 18,43 $ – 18,58 $ | +0,13 % |
| 9:50 AM | EXE | 82,79 $ | 81,14 $ – 82,19 $ | +0,72 % |
| 9:50 AM | FLUT | 68,10 $ | 66,19 $ – 67,43 $ | +0,99 % |
| 9:50 AM | GRNT | 5,63 $ | 5,47 $ – 5,57 $ | +1,08 % |
| 9:50 AM | LILAK | 9,47 $ | 9,30 $ – 9,45 $ | +0,21 % |
| 9:50 AM | MUR | 32,94 $ | 32,05 $ – 32,66 $ | +0,86 % |
| 9:50 AM | OLMA | 8,06 $ | 7,27 $ – 8,06 $ | +0,00 % |
| 9:50 AM | OXY | 54,09 $ | 52,96 $ – 53,78 $ | +0,58 % |
| 9:50 AM | SEDG | 18,09 $ | 17,30 $ – 17,83 $ | +1,49 % |
| 9:50 AM | SHEL | 93,53 $ | 92,85 $ – 93,45 $ | +0,09 % |
| 9:50 AM | SSL | 11,54 $ | 11,33 $ – 11,48 $ | +0,48 % |
| 9:50 AM | VIST | 49,25 $ | 48,24 $ – 49,15 $ | +0,20 % |
| 9:55 AM | ALTG | 6,16 $ | 5,81 $ – 6,10 $ | +0,98 % |
| 9:55 AM | BG | 88,25 $ | 83,60 $ – 87,79 $ | +0,52 % |
| 9:55 AM | DEO | 100,67 $ | 100,24 $ – 100,64 $ | +0,03 % |
| 9:55 AM | DOX | 42,19 $ | 41,64 $ – 42,08 $ | +0,26 % |
| 9:55 AM | EMBC | 8,03 $ | 7,14 $ – 7,95 $ | +1,13 % |
| 9:55 AM | EPRT | 29,22 $ | 29,00 $ – 29,18 $ | +0,14 % |

… und 85 weitere in [orb.json](orb.json).

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: DIS +2,52 % · HD +2,14 % · INSM +0,09 % · MCD +1,00 % · **MSTR +3,11 %** · PG +0,44 % · QCOM +2,24 % · **SNDK -5,57 %** · TJX +1,55 % · V +1,83 %

- 27.11. 07:09 Uhr ET · **V** · [What Is Visa (V) Doing With Stablecoin Payments In Europe And Asia?](https://finance.yahoo.com/markets/crypto/articles/visa-v-doing-stablecoin-payments-120939492.html?.tsrc=rss)
- 27.11. 07:03 Uhr ET · **MSTR** · [Crypto Stocks Gain After Bitcoin Tops $61K In Tech Rebound, But Analysts Want A Move Above $62K](https://stocktwits.com/news-articles/markets/cryptocurrency/crypto-stocks-gain-after-bitcoin-tops-61-k-in-tech-rebound-but-analysts-want-a-move-above-62-k/cNbCsYgR9Ns?.tsrc=rss)
- 27.11. 07:03 Uhr ET · **PG** · [The Dates That Matter Most For Procter & Gamble Stock](https://www.trefis.com/stock/pg/articles/629330/the-dates-that-matter-most-for-procter-gamble-stock/2026-11-27?.tsrc=rss)
- 27.11. 07:00 Uhr ET · **SNDK** · [He was right about AI and still lost $35 billion](https://finance.yahoo.com/video/ai-still-lost-35-billion-120000023.html?.tsrc=rss)
- 27.11. 06:50 Uhr ET · **QCOM** · [Why Is Qualcomm Stock Rallying Today?](https://investorshub.advfn.com/market-news/article/40788/why-is-qualcomm-stock-rallying-today?.tsrc=rss)
- 27.11. 06:33 Uhr ET · **INSM** · [Sanofi Stock Surges 26% as $41 Billion Insmed Deal Boosts Confidence](https://finance.yahoo.com/markets/stocks/articles/sanofi-stock-surges-26-41-113324950.html?.tsrc=rss) · deal, people
- 27.11. 06:18 Uhr ET · **SNDK** · [Micron vs. SanDisk: Which Is the Better AI Stock to Buy for 2027?](https://finance.yahoo.com/markets/stocks/articles/micron-vs-sandisk-better-ai-111815853.html?.tsrc=rss)
- 27.11. 06:09 Uhr ET · **MCD** · [Can BROS' 100-Basis-Point SG&A Leverage Support 2026 Earnings Growth?](https://finance.yahoo.com/markets/stocks/articles/bros-100-basis-point-sg-110900892.html?.tsrc=rss) · earnings
- 27.11. 06:01 Uhr ET · **SNDK** · [The Anatomy of an AI Rally: Anthropic Stock Quickly Finds Its Place](https://finance.yahoo.com/m/eac9c281-033c-3c73-8b9a-a27703a8cdc9/the-anatomy-of-an-ai-rally%3A.html?.tsrc=rss)
- 27.11. 05:55 Uhr ET · **SNDK** · [Micron's Higher FY27 CapEx: Can Supply Security Boost Its Growth Further?](https://finance.yahoo.com/markets/stocks/articles/microns-higher-fy27-capex-supply-105500633.html?.tsrc=rss)
- 27.11. 05:22 Uhr ET · **SNDK** · [Sandisk, Bloom, Marvell, AMD, Nvidia, HP, and More Stocks That Explain Today’s Market](https://finance.yahoo.com/m/977de44c-fcf5-3369-bcdd-0c3ddc7cfec9/sandisk%2C-bloom%2C-marvell%2C-amd%2C.html?.tsrc=rss)
- 27.11. 01:45 Uhr ET · **V** · [Visa and NBX plan stablecoin-linked payment card](https://www.electronicpaymentsinternational.com/news/visa-and-nbx-plan-stablecoin-linked-payment-card/?.tsrc=rss)
- 27.11. 01:44 Uhr ET · **INSM** · [The Zacks Analyst Blog Highlights Vera Therapeutics, BridgeBio Pharma, Revolution Medicines, Agios Pharmaceuticals and Stoke Therapeutics](https://finance.yahoo.com/healthcare/articles/zacks-analyst-blog-highlights-vera-064400990.html?.tsrc=rss) · deal
- 26.11. 22:08 Uhr ET · **QCOM** · [SoftBank’s “Worst Sell-Off” Since ’08 Is Bad News for Arm. Here’s the Number That Matters](https://www.tikr.com/blog/softbanks-worst-sell-off-since-08-is-bad-news-for-arm-heres-the-number-that-matters?ref=yahoofinance&tlnk=yf-261127-3ggwv4gr&.tsrc=rss) · risk
- 26.11. 19:00 Uhr ET · **HD** · [Home Depot shoppers can now dodge a classic cart disaster](https://www.thestreet.com/investing/stocks/home-depot-shoppers-can-now-dodge-a-classic-cart-disaster?.tsrc=rss)
- 26.11. 18:45 Uhr ET · **PG** · [2 Dividend Stocks to Buy in November and 1 to Leave on the Shelf](https://www.fool.com/investing/2026/11/26/2-dividend-stocks-to-buy-in-november-and-1-to-leave-on-the-shelf/?.tsrc=rss) · capital
- 26.11. 16:33 Uhr ET · **V** · [The Nasdaq Composite Is in a Correction, but These 3 Dividend Stocks Are Near 52-Week Highs. Here's Why They're Still Worth Buying Right Now.](https://www.fool.com/investing/2026/11/26/the-nasdaq-composite-is-in-a-correction-but-these-3-dividend-stocks-are-near-52-week-highs-here-s-why-they-re-still-worth-buying-right-now/?.tsrc=rss) · capital
- 26.11. 16:33 Uhr ET · **DIS** · [Take-Two’s (TTWO) GTA 6 Could Be a Cash Cow for the Next Decade](https://finance.yahoo.com/markets/stocks/articles/two-ttwo-gta-6-could-213300568.html?.tsrc=rss)
- 26.11. 16:22 Uhr ET · **DIS** · [Disney Stock Just Closed at Its Highest Level Since April 2022](https://247wallst.com/investing/2026/11/26/disney-stock-just-closed-at-its-highest-level-since-april-2022/?.tsrc=rss)
- 26.11. 16:20 Uhr ET · **SNDK** · [Sandisk’s 8-for-1 Split Is Done. Here’s What Investors Should Do Next.](https://www.fool.com/investing/2026/11/26/sandisks-8-for-1-split-is-done-heres-what-investors-should-do-next/?.tsrc=rss) · capital
- 26.11. 16:07 Uhr ET · **TJX** · [3 Dividend Stocks That Could Benefit From the Black Friday Shopping Rush](https://247wallst.com/investing/2026/11/26/3-dividend-stocks-that-could-benefit-from-the-black-friday-shopping-rush/?.tsrc=rss) · capital
- 26.11. 15:46 Uhr ET · **V** · [Billionaire Chris Hohn’s TCI Has 30% of Its $49.6 Billion Stock Portfolio in GE Aerospace](https://247wallst.com/investing/2026/11/26/billionaire-chris-hohns-tci-has-30-of-its-49-6-billion-stock-portfolio-in-ge-aerospace/?.tsrc=rss)
- 26.11. 15:29 Uhr ET · **PG** · [Here’s How Many Shares of Procter & Gamble You’d Need to Own to Collect $1,000 in Annual Dividends](https://www.fool.com/investing/2026/11/26/here-s-how-many-shares-of-procter-and-gamble-you-d-need-to-own-to-collect-usd1-000-in-annual-dividends/?.tsrc=rss) · capital
- 26.11. 15:09 Uhr ET · **DIS** · [Walt Disney (DIS) Lifts Dividend On Strong Earnings, Is The Stock Still Cheap?](https://finance.yahoo.com/markets/stocks/articles/walt-disney-dis-lifts-dividend-200909244.html?.tsrc=rss) · earnings, capital
- 26.11. 14:30 Uhr ET · **SNDK** · [Sandisk Trades at Under 3x Earnings After an 8-for-1 Split and a 70% Crash. Why SNDK Stock Isn’t Doomed Despite NAND Price Warnings.](https://www.barchart.com/story/news/9022920/sandisk-trades-at-under-3x-earnings-after-an-8-for-1-split-and-a-70-crash-why-sndk-stock-isnt-doomed-despite-nand-price-warnings?.tsrc=rss) · earnings

## Pelosi-Tracker (pelosi)

Keine neue Meldung seit dem letzten Lauf.

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

## Labor live – Mi 25.11.2026, Stand 16:00 Uhr ET

431 Aktien beobachtet · 4.546 Spielgeld-Trades aller Varianten · 0 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 0 | 0 | 0,00 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 2 | 0 | 6,11 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 4 | 0 | 7,77 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 4 | 0 | 7,77 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 3 | 0 | 12,01 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 16 | 0 | 33,48 € |
| Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 0 | 1,44 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| DE | Ausbruch 30 Min | 10:05 630,32 $ | 580,51 $ | 729,92 $ | Schluss 15:55 Uhr | 2,01 € |
| DE | Ausbruch 30 Min | 10:05 630,32 $ | 580,51 $ | 729,92 $ | Schluss 15:55 Uhr | 2,01 € |
| EMBJ | Opening-Range-Ausbruch 30 Min | 10:05 17,37 $ | 16,92 $ | 18,28 $ | Schluss 15:55 Uhr | 2,72 € |
| EMBJ | Ausbruch 30 Min | 10:05 17,37 $ | 16,92 $ | 18,28 $ | Schluss 15:55 Uhr | 2,72 € |
| EMBJ | Ausbruch 30 Min | 10:05 17,37 $ | 16,92 $ | 18,28 $ | Schluss 15:55 Uhr | 2,72 € |
| EPRT | Ausbruch 30 Min | 10:05 29,32 $ | 29,00 $ | 29,97 $ | Schluss 15:55 Uhr | 0,97 € |
| PAAS | Ausbruch 30 Min | 10:05 30,29 $ | 29,43 $ | 32,00 $ | Ziel 13:10 Uhr | 5,59 € |
| PBR | Ausbruch 30 Min | 10:05 15,87 $ | 15,52 $ | 16,58 $ | Schluss 15:55 Uhr | 1,10 € |
| SEDG | Ausbruch 30 Min | 10:05 18,89 $ | 17,30 $ | 22,07 $ | Schluss 15:55 Uhr | 4,77 € |
| SHOP | Ausbruch 30 Min | 10:05 127,47 $ | 123,74 $ | 134,94 $ | Schluss 15:55 Uhr | 4,90 € |
| SNEX | Ausbruch 30 Min | 10:05 38,45 $ | 37,08 $ | 41,20 $ | Stopp 10:20 Uhr | -3,62 € |
| SOFI | Ausbruch 30 Min | 10:05 12,42 $ | 11,95 $ | 13,35 $ | Schluss 15:55 Uhr | 5,10 € |
| SPY | Ausbruch 30 Min | 10:05 704,55 $ | 695,47 $ | 722,72 $ | Schluss 15:55 Uhr | 1,69 € |
| VALE | Ausbruch 30 Min | 10:05 9,51 $ | 9,26 $ | 10,02 $ | Schluss 15:55 Uhr | 3,01 € |
| WDAY | Opening-Range-Ausbruch 30 Min | 10:05 181,80 $ | 173,00 $ | 199,39 $ | Schluss 15:55 Uhr | -0,09 € |
| WDAY | Ausbruch 30 Min | 10:05 181,80 $ | 173,00 $ | 199,39 $ | Schluss 15:55 Uhr | -0,09 € |
| WDAY | Ausbruch 30 Min | 10:05 181,80 $ | 173,00 $ | 199,39 $ | Schluss 15:55 Uhr | -0,09 € |
| EMBJ | Erholung: Lücke nach unten ≥ 3 % | 10:30 17,27 $ | 16,92 $ | 17,98 $ | Schluss 15:55 Uhr | 3,31 € |
| TSLA | Erholung: Lücke nach unten ≥ 3 % | 10:35 365,93 $ | 357,64 $ | 382,52 $ | Ziel 14:20 Uhr | 4,48 € |
| AVGO | Erholung: Lücke nach unten ≥ 3 % | 12:10 285,95 $ | 278,00 $ | 301,86 $ | Schluss 15:55 Uhr | 4,22 € |

## Labor (Testphase, Spielgeld ohne Limit)

1.044 Aktien · 84 Handelstage · Lerntage Do 30.07.2026 bis Fr 16.10.2026 · **Prüftage Mo 19.10.2026 bis Mi 25.11.2026** · 80 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 78 | 63 % | +0,90 % | 70,39 € | -85,61 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 78 | 63 % | +0,90 % | 69,80 € | -86,20 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 78 | 63 % | +0,78 % | 60,85 € | -95,15 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 4× normal | 129 | 57 % | +0,52 % | 67,24 € | -190,76 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 2R | 135 | 56 % | +0,46 % | 62,28 € | -207,72 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 129 | 55 % | +0,44 % | 56,53 € | -201,47 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 129 | 55 % | +0,43 % | 55,61 € | -202,39 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 3R | 135 | 56 % | +0,43 % | 57,64 € | -212,36 € | möglich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 1,5R | 135 | 56 % | +0,38 % | 51,73 € | -218,27 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 238 | 53 % | +0,37 % | 88,22 € | -387,78 € | möglich | **ja** |
| 11 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 129 | 55 % | +0,35 % | 45,44 € | -212,56 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 259 | 52 % | +0,34 % | 87,59 € | -430,40 € | möglich | **ja** |

So liest du das: Ein Trade ist ein Kauf und Verkauf am selben Tag. „Treffer“ ist der Anteil der Trades mit Plus. „€ bei 100 €/Trade“ ist die Summe, wenn jeder Trade mit 100 € gemacht worden wäre. „Zufall möglich“ heißt: zu wenige oder zu schwankende Trades, das Ergebnis kann Glück sein.

- **Beste Signale: Aus allen News-Sprüngen des Tages (Lücke ≥ 2 %, viel Startvolumen) zählt nur der erste, der zu den gelernten Mustern passt (sehr viel Volumen, starke Schwankung, Einstieg bis 10:30 Uhr ET). Höchstens 1 Trade am Tag – so bleiben die Gebühren klein.**
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
