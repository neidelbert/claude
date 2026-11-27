# Trader-Übersicht

Stand: Fr 27.11. 16:22 Uhr ET (22:22 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: geschlossen (Handelszeit 09:30 bis 13:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Fr 27.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 374 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45935567529)) |
| ORB-Scan | Fr 27.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 95 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45967520442)) |
| Labor live | Fr 27.11. 13:00 Uhr ET (19:00 Uhr MEZ) | OK – Tagesbilanz: 3.289 Trades ([Lauf](https://github.com/neidelbert/claude/actions/runs/45967520442)) |
| Labor | Fr 27.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 16 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/46009167121)) |
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

## ORB-Scan – 2026-11-27 10:10 ET

Quelle: Treffer des Morgen-Scans · 351 nutzbare Charts · **95 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | ADIG | 10,65 $ | 10,18 $ – 10,52 $ | +1,21 % |
| 9:50 AM | ADP | 319,16 $ | 315,64 $ – 318,40 $ | +0,24 % |
| 9:50 AM | ANF | 183,94 $ | 173,55 $ – 183,75 $ | +0,10 % |
| 9:50 AM | AON | 348,11 $ | 343,48 $ – 347,59 $ | +0,15 % |
| 9:50 AM | ATAT | 41,01 $ | 39,60 $ – 40,88 $ | +0,32 % |
| 9:50 AM | BOX | 47,42 $ | 46,24 $ – 47,24 $ | +0,38 % |
| 9:50 AM | BRO | 78,56 $ | 77,30 $ – 78,55 $ | +0,01 % |
| 9:50 AM | BTI | 60,31 $ | 59,59 $ – 60,28 $ | +0,04 % |
| 9:50 AM | CDW | 180,43 $ | 175,82 $ – 180,10 $ | +0,18 % |
| 9:50 AM | CHKP | 164,57 $ | 160,76 $ – 164,44 $ | +0,08 % |
| 9:50 AM | CHTR | 152,43 $ | 146,87 $ – 150,22 $ | +1,47 % |
| 9:50 AM | CLX | 111,71 $ | 110,00 $ – 111,36 $ | +0,31 % |
| 9:50 AM | CMCSA | 26,07 $ | 25,73 $ – 26,02 $ | +0,19 % |
| 9:50 AM | CNH | 12,03 $ | 11,82 $ – 11,99 $ | +0,33 % |
| 9:50 AM | CRVS | 11,35 $ | 10,97 $ – 11,33 $ | +0,21 % |
| 9:50 AM | DBX | 37,91 $ | 37,27 $ – 37,83 $ | +0,21 % |
| 9:50 AM | DIS | 126,91 $ | 125,45 $ – 126,89 $ | +0,02 % |
| 9:50 AM | DKS | 160,99 $ | 157,00 $ – 159,63 $ | +0,86 % |
| 9:50 AM | EAT | 207,99 $ | 202,60 $ – 207,30 $ | +0,33 % |
| 9:50 AM | ENR | 28,33 $ | 27,44 $ – 28,26 $ | +0,25 % |
| 9:50 AM | FISV | 60,91 $ | 59,84 $ – 60,87 $ | +0,07 % |
| 9:50 AM | FOUR | 45,04 $ | 43,61 $ – 44,86 $ | +0,40 % |
| 9:50 AM | HDB | 28,57 $ | 28,14 $ – 28,49 $ | +0,26 % |
| 9:50 AM | HSY | 183,20 $ | 181,00 $ – 183,00 $ | +0,11 % |
| 9:50 AM | IBN | 35,98 $ | 35,48 $ – 35,85 $ | +0,38 % |
| 9:50 AM | INFY | 13,09 $ | 12,69 $ – 13,04 $ | +0,38 % |
| 9:50 AM | INSM | 170,68 $ | 170,25 $ – 170,66 $ | +0,01 % |
| 9:50 AM | IRWD | 5,32 $ | 5,13 $ – 5,32 $ | +0,08 % |
| 9:50 AM | LFTO | 25,49 $ | 24,02 $ – 25,33 $ | +0,65 % |
| 9:50 AM | MBGL | 23,53 $ | 23,08 $ – 23,43 $ | +0,43 % |

… und 65 weitere in [orb.json](orb.json).

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

## Labor live – Fr 27.11.2026, Stand 13:00 Uhr ET

435 Aktien beobachtet · 3.289 Spielgeld-Trades aller Varianten · 0 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 1 | 0 | 0,17 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 1 | 0 | 0,17 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 1 | 0 | 0,17 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 2 | 0 | -1,56 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 1 | 0 | 1,42 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 2 | 0 | 1,31 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 2 | 0 | 1,31 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 2 | 0 | -0,93 € |
| Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 0 | -0,95 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| ANF | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 182,56 $ | 181,57 $ | – | Stopp 9:45 Uhr | -0,59 € |
| AON | News-Sprung: Lücke ≥ 4 % | 9:50 348,28 $ | 343,48 $ | 355,49 $ | Schluss 12:55 Uhr | 0,17 € |
| AON | News-Sprung: Lücke ≥ 4 % | 9:50 348,28 $ | 343,48 $ | 357,89 $ | Schluss 12:55 Uhr | 0,17 € |
| AON | News-Sprung: Lücke ≥ 4 % | 9:50 348,28 $ | 343,48 $ | 362,70 $ | Schluss 12:55 Uhr | 0,17 € |
| INGM | Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET | 9:55 28,15 $ | 27,69 $ | 29,55 $ | Schluss 12:55 Uhr | -0,95 € |
| SEDG | Stocks in Play (Studie): Top 20 nach Startvolumen | 10:00 21,11 $ | 20,92 $ | – | Stopp 10:05 Uhr | -0,97 € |
| DV | Opening-Range-Ausbruch 30 Min | 10:20 13,62 $ | 13,60 $ | 13,67 $ | Stopp 10:45 Uhr | -0,21 € |
| DV | Ausbruch 30 Min | 10:20 13,62 $ | 13,60 $ | 13,67 $ | Stopp 10:45 Uhr | -0,21 € |
| VRTX | Opening-Range-Ausbruch 30 Min | 10:20 524,02 $ | 502,90 $ | 566,26 $ | Schluss 12:55 Uhr | 1,52 € |
| VRTX | Ausbruch 30 Min | 10:20 524,02 $ | 502,90 $ | 566,26 $ | Schluss 12:55 Uhr | 1,52 € |
| NTNX | Erholung: Lücke nach unten ≥ 3 % | 10:40 45,50 $ | 44,48 $ | 47,54 $ | Schluss 12:55 Uhr | 1,42 € |
| HR | Ausbruch 30 Min | 11:50 20,54 $ | 20,36 $ | 20,90 $ | Schluss 12:55 Uhr | 0,10 € |
| C | Ausbruch 30 Min | 11:55 116,35 $ | 115,21 $ | 118,62 $ | Stopp 12:50 Uhr | -1,03 € |

## Labor (Testphase, Spielgeld ohne Limit)

1.101 Aktien · 85 Handelstage · Lerntage Do 30.07.2026 bis Mo 19.10.2026 · **Prüftage Di 20.10.2026 bis Fr 27.11.2026** · 80 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 86 | 62 % | +0,67 % | 57,87 € | -114,13 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 86 | 62 % | +0,67 % | 57,27 € | -114,72 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 86 | 62 % | +0,56 % | 48,33 € | -123,67 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 139 | 55 % | +0,37 % | 50,85 € | -227,15 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 139 | 55 % | +0,36 % | 49,86 € | -228,14 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 139 | 55 % | +0,28 % | 39,55 € | -238,45 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 4× normal | 139 | 55 % | +0,28 % | 39,45 € | -238,55 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 261 | 52 % | +0,27 % | 69,35 € | -452,65 € | möglich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 281 | 52 % | +0,24 % | 66,49 € | -495,51 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 281 | 52 % | +0,23 % | 65,33 € | -496,67 € | möglich | **ja** |
| 11 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R | 281 | 52 % | +0,23 % | 65,33 € | -496,67 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 2R | 148 | 53 % | +0,22 % | 32,27 € | -263,73 € | möglich | **ja** |

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
