# Trader-Übersicht

Stand: Fr 30.10. 13:48 Uhr ET (18:48 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Mi 28.10. 08:39 Uhr ET (13:39 Uhr MEZ) | OK – 501 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40689559352)) |
| ORB-Scan | Mi 28.10. 10:10 Uhr ET (15:10 Uhr MEZ) | OK – 163 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40689559352)) |
| Labor live | Fr 30.10. 13:47 Uhr ET (18:47 Uhr MEZ) | OK – Börsenstart gemeldet ([Lauf](https://github.com/neidelbert/claude/actions/runs/41101519065)) |
| Labor | Do 29.10. 16:20 Uhr ET (21:20 Uhr MEZ) | OK – 6 von 76 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/40927932269)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Di 27.10.2026

5.945 Aktien in der Liste · 5.943 Charts geladen · 1.493 liquide (ab 5 $ und 1.000.000 Aktien) · 1.491 gescannt · **501 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 197 | TSLA, SOFI, TXN, ADI, JNJ, RCL, NXPI, UPS |
| `bull_flag` | 86 | LLY, UNH, SPGI, COP, WM, ABNB, AJG, VEEV |
| `reclaim_ma20` | 120 | SOFI, CDNS, CSCO, MS, PYPL, GM, SNPS, MCHP |
| `oversold` | 56 | BA, BAC, XYL, PCAR, VALE, HWM, XP, CRS |
| `oversold_bounce` | 90 | GOOGL, GOOG, NBIS, CRWV, LRCX, CLS, GE, CAT |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| TSLA | 407,46 $ | 65,9 | `breakout_20d` |
| GOOGL | 320,58 $ | 34,4 | `oversold_bounce` |
| BA | 168,18 $ | 25,5 | `oversold` |
| GOOG | 316,83 $ | 32,9 | `oversold_bounce` |
| NBIS | 170,47 $ | 39,4 | `oversold_bounce` |
| CRWV | 59,57 $ | 35,3 | `oversold_bounce` |
| SOFI | 16,40 $ | 57,6 | `breakout_20d`, `reclaim_ma20` |
| TXN | 308,91 $ | 70,1 | `breakout_20d` |
| LRCX | 240,85 $ | 31,6 | `oversold_bounce` |
| LLY | 1.281,91 $ | 63,2 | `bull_flag` |
| CLS | 276,54 $ | 37,9 | `oversold_bounce` |
| GE | 297,66 $ | 40,7 | `oversold_bounce` |
| CAT | 713,31 $ | 36,5 | `oversold_bounce` |
| ADI | 425,35 $ | 63,6 | `breakout_20d` |
| CBRS | 119,31 $ | 32,6 | `oversold_bounce` |
| CDNS | 343,08 $ | 58,0 | `reclaim_ma20` |
| KLAC | 153,66 $ | 32,9 | `oversold_bounce` |
| CSCO | 111,38 $ | 52,7 | `reclaim_ma20` |
| JNJ | 268,73 $ | 57,3 | `breakout_20d` |
| UNH | 410,39 $ | 59,5 | `bull_flag` |

Alle 501 Treffer: [watchlist.json](watchlist.json)

## ORB-Scan – 2026-10-28 10:10 ET

Quelle: Treffer des Morgen-Scans · 450 nutzbare Charts · **163 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | AMGN | 450,32 $ | 439,70 $ – 448,95 $ | +0,31 % |
| 9:50 AM | AMRX | 21,57 $ | 21,11 $ – 21,55 $ | +0,09 % |
| 9:50 AM | BBWI | 21,92 $ | 21,65 $ – 21,86 $ | +0,27 % |
| 9:50 AM | BEAM | 25,44 $ | 24,50 $ – 25,42 $ | +0,07 % |
| 9:50 AM | BILL | 49,59 $ | 48,39 $ – 49,56 $ | +0,06 % |
| 9:50 AM | BOX | 42,60 $ | 41,96 $ – 42,57 $ | +0,07 % |
| 9:50 AM | BRKR | 62,37 $ | 60,55 $ – 62,25 $ | +0,19 % |
| 9:50 AM | BROS | 43,10 $ | 42,05 $ – 42,90 $ | +0,48 % |
| 9:50 AM | CAI | 34,86 $ | 33,50 $ – 34,64 $ | +0,64 % |
| 9:50 AM | CCEP | 111,32 $ | 110,34 $ – 110,94 $ | +0,34 % |
| 9:50 AM | CE | 49,05 $ | 48,25 $ – 49,04 $ | +0,02 % |
| 9:50 AM | CERT | 11,33 $ | 10,84 $ – 11,26 $ | +0,62 % |
| 9:50 AM | CRL | 374,28 $ | 360,01 $ – 374,27 $ | +0,00 % |
| 9:50 AM | CXM | 6,83 $ | 6,56 $ – 6,79 $ | +0,59 % |
| 9:50 AM | DOCU | 82,79 $ | 80,63 $ – 82,57 $ | +0,27 % |
| 9:50 AM | ELF | 114,73 $ | 112,25 $ – 113,69 $ | +0,91 % |
| 9:50 AM | ELVN | 44,43 $ | 43,39 $ – 44,39 $ | +0,09 % |
| 9:50 AM | ENOV | 22,06 $ | 21,45 $ – 22,00 $ | +0,25 % |
| 9:50 AM | EW | 91,03 $ | 89,90 $ – 90,90 $ | +0,14 % |
| 9:50 AM | FND | 48,47 $ | 47,52 $ – 48,38 $ | +0,19 % |
| 9:50 AM | FTRE | 25,50 $ | 24,30 $ – 25,38 $ | +0,46 % |
| 9:50 AM | GILD | 159,40 $ | 156,04 $ – 158,95 $ | +0,29 % |
| 9:50 AM | GKOS | 186,18 $ | 180,90 $ – 185,00 $ | +0,64 % |
| 9:50 AM | GTLB | 57,49 $ | 55,77 $ – 57,46 $ | +0,05 % |
| 9:50 AM | HALO | 128,89 $ | 126,25 $ – 128,77 $ | +0,09 % |
| 9:50 AM | HLN | 10,06 $ | 9,97 $ – 10,03 $ | +0,30 % |
| 9:50 AM | HRB | 48,03 $ | 47,26 $ – 47,95 $ | +0,16 % |
| 9:50 AM | HTFL | 59,50 $ | 57,79 $ – 59,43 $ | +0,12 % |
| 9:50 AM | JNJ | 268,75 $ | 264,20 $ – 268,42 $ | +0,12 % |
| 9:50 AM | LFST | 13,36 $ | 13,05 $ – 13,34 $ | +0,15 % |

… und 133 weitere in [orb.json](orb.json).

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: **BA -10,69 %** · **CRWV +7,94 %** · GOOG +0,84 % · GOOGL +1,19 % · LLY +0,22 % · LRCX +1,41 % · **NBIS +11,22 %** · **SOFI +13,42 %** · **TSLA +4,04 %** · **TXN +3,62 %**

- 28.10. 08:31 Uhr ET · **BA** · [Boeing Sinks 12% in a Week on a Slower 737 Ramp: “Longer Than We Had Expected”](https://www.tikr.com/blog/boeing-sinks-12-in-a-week-on-a-slower-737-ramp-longer-than-we-had-expected?ref=yahoofinance&.tsrc=rss) · earnings
- 28.10. 08:23 Uhr ET · **GOOG** · [What Is Snowflake Stock's Biggest Opportunity?](https://www.trefis.com/stock/snow/articles/620992/what-is-snowflake-stocks-biggest-opportunity/2026-10-28?.tsrc=rss)
- 28.10. 08:18 Uhr ET · **GOOG** · [Vertiv stock surges as orders double amid AI build-out: 'Evolving faster than ever'](https://finance.yahoo.com/markets/stocks/article/vertiv-stock-surges-as-orders-double-amid-ai-build-out-evolving-faster-than-ever-122018206.html?.tsrc=rss)
- 28.10. 08:16 Uhr ET · **LLY** · [How Much Should One Number Worry Merck Stock Holders?](https://www.trefis.com/stock/mrk/articles/621000/how-much-should-one-number-worry-merck-stock-holders/2026-10-28?.tsrc=rss)
- 28.10. 08:15 Uhr ET · **GOOG** · [Big Tech Earnings Face a $600 Billion Question: Is AI Spending Paying Off?](https://firstformoney.com/big-tech-earnings-face-a-600-billion-question-is-ai-spending-paying-off/?.tsrc=rss) · earnings
- 28.10. 08:14 Uhr ET · **LLY** · [3 Big Pharma Earnings Reports to Watch: Eli Lilly, Merck and Gilead](https://247wallst.com/investing/2026/10/28/3-big-pharma-earnings-reports-to-watch-eli-lilly-merck-and-gilead/?.tsrc=rss) · earnings
- 28.10. 08:14 Uhr ET · **BA** · [US Stock Market Today: S&P 500 Futures Edge Higher On Fed Decision Watch](https://finance.yahoo.com/markets/stocks/articles/us-stock-market-today-p-121406952.html?.tsrc=rss) · macro
- 28.10. 08:13 Uhr ET · **GOOG** · [Stock Market Today: Dow Falls Ahead Of Rate Decision, Warsh Comments; Robinhood Plunges (Live Coverage)](https://finance.yahoo.com/m/8aa305ef-cc61-37d7-bc76-82a4a4324c5b/stock-market-today%3A-dow-falls.html?.tsrc=rss) · earnings, macro
- 28.10. 08:12 Uhr ET · **GOOG** · [Dow Jones Futures Fall, Techs Rise As SK Hynix Crushes Views; Fed, Microsoft, Google On Deck](https://finance.yahoo.com/m/7066a700-b33b-3fa1-858d-f75f49b920da/dow-jones-futures-fall%2C-techs.html?.tsrc=rss) · macro
- 28.10. 08:09 Uhr ET · **GOOG** · [Bharti Airtel Stock And 2 Indian Telecom Shares Riding The Jio IPO Shift](https://finance.yahoo.com/markets/stocks/articles/bharti-airtel-stock-2-indian-120944242.html?.tsrc=rss)
- 28.10. 08:04 Uhr ET · **GOOG** · [Morning Minute: Robinhood Misses, But Crypto Beats and Robinhood Chain Soars](https://decrypt.co/382029/morning-minute-robinhood-misses-but-crypto-beats-and-robinhood-chain-soars?.tsrc=rss)
- 28.10. 08:01 Uhr ET · **LLY** · [Why Should Pfizer Stock Holders Watch This One Number?](https://www.trefis.com/stock/pfe/articles/621004/why-should-pfizer-stock-holders-watch-this-one-number/2026-10-28?.tsrc=rss)
- 28.10. 08:01 Uhr ET · **GOOG** · [These 7 Stocks Are Analyst Favorites For Magnificent Earnings Growth; Lilly, Amazon Earnings Ahead](https://finance.yahoo.com/m/2b47c372-177e-3051-aa01-406a8d82b220/these-7-stocks-are-analyst.html?.tsrc=rss) · earnings
- 28.10. 08:00 Uhr ET · **GOOG** · [Funds Load Up On Marriott, Estee Lauder As Big Tech Earnings Loom](https://finance.yahoo.com/m/e5ed3c43-7ba7-36b0-91ee-1cf78a2797a3/funds-load-up-on-marriott%2C.html?.tsrc=rss) · earnings
- 28.10. 08:00 Uhr ET · **GOOG** · [Google Earnings: Cloud Is Booming, But Can Search Deliver Amid AI Shift?](https://finance.yahoo.com/m/87e72ddb-46f1-3633-bc3f-70cf4ac925d0/google-earnings%3A-cloud-is.html?.tsrc=rss) · earnings
- 28.10. 08:00 Uhr ET · **BA** · [Boeing: Global Freighter Fleet to Exceed 4,000 Airplanes as Air Cargo Traffic Doubles by 2045](https://finance.yahoo.com/economy/articles/boeing-global-freighter-fleet-exceed-120000853.html?.tsrc=rss) · earnings
- 28.10. 08:00 Uhr ET · **GOOG** · [How Anthropic's IPO structure could become the AI blueprint](https://finance.yahoo.com/video/anthropics-ipo-structure-could-become-120000012.html?.tsrc=rss) · people
- 28.10. 07:58 Uhr ET · **GOOG** · [Here Are Wednesday’s Top Wall Street Analyst Research Calls: Enphase Energy, F5, Marvell Technology, MSG Rangers, Pentair, Silicon Motion Technology, Spotify Technology, Texas Instruments, Whirlpool, and More](https://247wallst.com/investing/2026/10/28/here-are-wednesdays-top-wall-street-analyst-research-calls-enphase-energy-f5-marvell-technology-msg-rangers-pentair-silicon-motion-technology-spotify-technology-texas-instruments-whi/?.tsrc=rss) · macro
- 28.10. 07:51 Uhr ET · **GOOG** · [OpenAI Reportedly Plans to Purchase Google AI Chips as Demand for Computing Infrastructure Grows](https://investorshub.advfn.com/market-news/article/38763/openai-reportedly-plans-to-purchase-google-ai-chips-as-demand-for-computing-infrastructure-grows?.tsrc=rss)
- 28.10. 07:50 Uhr ET · **TSLA** · [Tesla Stock Heads for Third Day of Gains. It’s About More Than SpaceX.](https://finance.yahoo.com/m/f3514d3f-678c-31b8-b499-e6d96ed30fb3/tesla-stock-heads-for-third.html?.tsrc=rss)
- 28.10. 07:37 Uhr ET · **GOOG** · [Megacap Earnings Could Spoil the Market’s Appetite for AI](https://finance.yahoo.com/m/4e4095e2-758d-393b-8bb3-33c3b63ed415/megacap-earnings-could-spoil.html?.tsrc=rss) · earnings
- 28.10. 07:30 Uhr ET · **TSLA** · [Man repairs 2 wrecked Teslas, they pass inspection, but the carmaker cuts fast charging anyway — now he owes $15K](https://finance.yahoo.com/technology/articles/man-repairs-2-wrecked-teslas-113000365.html?.tsrc=rss)
- 28.10. 07:30 Uhr ET · **TSLA** · [BMO Launches Canada's First Single Stock Autocallable Income ETFs](https://finance.yahoo.com/markets/options/articles/bmo-launches-canadas-first-single-113000761.html?.tsrc=rss) · capital
- 28.10. 07:25 Uhr ET · **LLY** · [Micron Biomedical Appoints Anand Subramony, Ph.D., as Executive Vice President, Global Product Development and Combination Product Commercialization](https://finance.yahoo.com/healthcare/articles/micron-biomedical-appoints-anand-subramony-112500420.html?.tsrc=rss) · people
- 28.10. 07:22 Uhr ET · **GOOG** · [OpenAI Is Buying Google’s AI Chips, a Hit to Nvidia’s Biggest Customer Bond](https://247wallst.com/investing/2026/10/28/openai-is-buying-googles-ai-chips-a-hit-to-nvidias-biggest-customer-bond/?.tsrc=rss)

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

## Labor live – Fr 30.10.2026, Stand 13:47 Uhr ET

414 Aktien beobachtet · 1.925 Spielgeld-Trades aller Varianten · 1.004 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 0 | 0 | 0,00 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 2× normal | 14 | 8 | -15,20 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 0 | 0 | 0,00 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · Volumen ≥ 1,5× | 18 | 16 | -13,28 € |
| Stocks in Play (Studie): Top 10 nach Startvolumen · Stopp 10 % ATR · Ziel 2R | 8 | 0 | 1,97 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 2× normal | 4 | 3 | -6,17 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| CDE | Erholung: Lücke nach unten ≥ 3 % | 10:40 13,19 $ | 12,96 $ | 13,65 $ | Stopp 13:40 Uhr | -1,80 € |
| HPQ | Opening-Range-Ausbruch 30 Min | 10:40 29,29 $ | 26,95 $ | 33,96 $ | offen, Kurs 28,84 $ | -1,58 € |
| HPQ | Ausbruch 30 Min | 10:40 29,29 $ | 26,95 $ | 33,96 $ | offen, Kurs 28,84 $ | -1,58 € |
| MOD | Opening-Range-Ausbruch 30 Min | 10:40 134,43 $ | 126,67 $ | 149,96 $ | offen, Kurs 130,08 $ | -3,29 € |
| TSM | Erholung: Lücke nach unten ≥ 3 % | 10:40 415,25 $ | 411,45 $ | 422,84 $ | Stopp 11:15 Uhr | -0,96 € |
| AAPL | Opening-Range-Ausbruch 30 Min | 10:45 348,99 $ | 344,13 $ | 358,72 $ | offen, Kurs 346,04 $ | -0,90 € |
| TGTX | Opening-Range-Ausbruch 30 Min | 10:45 60,68 $ | 58,00 $ | 66,03 $ | offen, Kurs 61,03 $ | 0,53 € |
| OLN | Opening-Range-Ausbruch 30 Min | 10:50 17,30 $ | 15,95 $ | 20,00 $ | offen, Kurs 17,59 $ | 1,63 € |
| COIN | Erholung: Lücke nach unten ≥ 3 % | 11:00 140,67 $ | 136,90 $ | 148,20 $ | offen, Kurs 138,62 $ | -1,50 € |
| PEP | Opening-Range-Ausbruch 30 Min | 11:05 137,67 $ | 136,35 $ | 140,30 $ | offen, Kurs 138,27 $ | 0,39 € |
| AMZN | Opening-Range-Ausbruch 30 Min | 11:10 240,73 $ | 229,36 $ | 263,46 $ | offen, Kurs 239,50 $ | -0,56 € |
| AMZN | Ausbruch 30 Min | 11:10 240,73 $ | 229,36 $ | 263,46 $ | offen, Kurs 239,50 $ | -0,56 € |
| GOOG | Opening-Range-Ausbruch 30 Min | 11:10 281,01 $ | 277,62 $ | 287,79 $ | Stopp 12:55 Uhr | -1,26 € |
| MSTR | Opening-Range-Ausbruch 30 Min | 11:10 132,57 $ | 124,10 $ | 149,50 $ | offen, Kurs 129,53 $ | -2,34 € |
| CAT | Erholung: Lücke nach unten ≥ 3 % | 11:25 633,17 $ | 621,85 $ | 655,80 $ | offen, Kurs 627,21 $ | -0,99 € |
| CROX | Opening-Range-Ausbruch 30 Min | 11:30 153,64 $ | 150,26 $ | 160,39 $ | offen, Kurs 151,51 $ | -1,43 € |
| EXEL | Opening-Range-Ausbruch 30 Min | 12:00 72,11 $ | 67,50 $ | 81,33 $ | offen, Kurs 71,29 $ | -1,19 € |
| EXEL | Ausbruch 30 Min | 12:00 72,11 $ | 67,50 $ | 81,33 $ | offen, Kurs 71,29 $ | -1,19 € |
| MTZ | Erholung: Lücke nach unten ≥ 3 % | 12:05 184,35 $ | 169,00 $ | 215,04 $ | offen, Kurs 181,75 $ | -1,46 € |
| AMZN | Erholung: Lücke nach unten ≥ 3 % | 12:10 239,00 $ | 229,36 $ | 258,27 $ | offen, Kurs 239,50 $ | 0,16 € |

## Labor (Testphase, Spielgeld ohne Limit)

697 Aktien · 65 Handelstage · Lerntage Do 30.07.2026 bis Di 29.09.2026 · **Prüftage Mi 30.09.2026 bis Do 29.10.2026** · 76 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 36 | 50 % | +0,39 % | 14,06 € | -57,94 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 41 | 49 % | +0,30 % | 12,30 € | -69,70 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 36 | 50 % | +0,21 % | 7,74 € | -64,26 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 36 | 50 % | +0,20 % | 7,06 € | -64,94 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 41 | 49 % | +0,17 % | 6,87 € | -75,13 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 41 | 49 % | +0,13 % | 5,19 € | -76,81 € | möglich | **ja** |
| 7 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 2× normal | 108 | 65 % | +1,09 % | 117,82 € | -98,18 € | unwahrscheinlich | nein |
| 8 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 250 | 59 % | +0,93 % | 232,59 € | -267,41 € | unwahrscheinlich | nein |
| 9 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 49 | 61 % | +0,75 % | 36,89 € | -61,11 € | unwahrscheinlich | nein |
| 10 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R | 284 | 56 % | +0,75 % | 213,12 € | -354,88 € | unwahrscheinlich | nein |
| 11 | Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 2R | 284 | 51 % | +0,34 % | 97,82 € | -470,18 € | unwahrscheinlich | nein |
| 12 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 1R | 284 | 57 % | +0,32 % | 91,54 € | -476,46 € | unwahrscheinlich | nein |

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
