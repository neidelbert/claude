# Trader-Übersicht

Stand: Mi 28.10. 10:01 Uhr ET (15:01 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Mi 28.10. 08:39 Uhr ET (13:39 Uhr MEZ) | OK – 501 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40689559352)) |
| ORB-Scan | Di 27.10. 10:10 Uhr ET (15:10 Uhr MEZ) | OK – 64 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40504826435)) |
| Labor live | Mi 28.10. 10:00 Uhr ET (15:00 Uhr MEZ) | OK – 1.053 Trades, 979 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/40689559352)) |
| Labor | Di 27.10. 16:20 Uhr ET (21:20 Uhr MEZ) | OK – 1 von 76 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/40554495911)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

**Probleme:**
- Labor live / Antworten lesen: <urlopen error [Errno 101] Network is unreachable>

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

## ORB-Scan – 2026-10-27 10:10 ET

Quelle: Treffer des Morgen-Scans · 396 nutzbare Charts · **64 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | AEO | 19,03 $ | 18,76 $ – 18,97 $ | +0,34 % |
| 9:50 AM | AROC | 30,83 $ | 30,10 $ – 30,76 $ | +0,23 % |
| 9:50 AM | ATI | 166,57 $ | 164,90 $ – 166,38 $ | +0,11 % |
| 9:50 AM | BKR | 56,90 $ | 56,36 $ – 56,76 $ | +0,24 % |
| 9:50 AM | CCC | 7,70 $ | 7,68 $ – 7,69 $ | +0,07 % |
| 9:50 AM | COLD | 14,64 $ | 14,50 $ – 14,62 $ | +0,14 % |
| 9:50 AM | CSTM | 24,08 $ | 23,69 $ – 24,00 $ | +0,32 % |
| 9:50 AM | DOV | 204,63 $ | 201,98 $ – 204,00 $ | +0,31 % |
| 9:50 AM | EQPT | 16,79 $ | 16,47 $ – 16,75 $ | +0,24 % |
| 9:50 AM | ERIC | 11,00 $ | 10,94 $ – 10,99 $ | +0,09 % |
| 9:50 AM | FR | 55,25 $ | 55,07 $ – 55,23 $ | +0,04 % |
| 9:50 AM | FRVO | 8,60 $ | 8,14 $ – 8,55 $ | +0,58 % |
| 9:50 AM | FUN | 7,21 $ | 7,02 $ – 7,17 $ | +0,56 % |
| 9:50 AM | GGG | 67,18 $ | 66,20 $ – 66,92 $ | +0,40 % |
| 9:50 AM | GNL | 7,18 $ | 7,12 $ – 7,17 $ | +0,14 % |
| 9:50 AM | LBTYA | 7,66 $ | 7,54 $ – 7,66 $ | +0,11 % |
| 9:50 AM | LBTYK | 7,61 $ | 7,51 $ – 7,59 $ | +0,13 % |
| 9:50 AM | LKQ | 17,46 $ | 17,22 $ – 17,43 $ | +0,17 % |
| 9:50 AM | MOD | 135,62 $ | 133,03 $ – 134,90 $ | +0,54 % |
| 9:50 AM | MOS | 18,40 $ | 17,81 $ – 18,38 $ | +0,14 % |
| 9:50 AM | MRVI | 7,61 $ | 7,50 $ – 7,60 $ | +0,13 % |
| 9:50 AM | MYGN | 6,09 $ | 6,01 $ – 6,08 $ | +0,10 % |
| 9:50 AM | NZF | 11,23 $ | 11,11 $ – 11,23 $ | +0,04 % |
| 9:50 AM | PCAR | 104,81 $ | 102,01 $ – 104,46 $ | +0,33 % |
| 9:50 AM | SLB | 53,87 $ | 52,50 $ – 53,63 $ | +0,45 % |
| 9:50 AM | SUNB | 80,82 $ | 79,60 $ – 80,75 $ | +0,08 % |
| 9:50 AM | XP | 16,57 $ | 15,81 $ – 16,53 $ | +0,21 % |
| 9:55 AM | ADPT | 26,66 $ | 26,07 $ – 26,60 $ | +0,23 % |
| 9:55 AM | AMRX | 21,24 $ | 20,93 $ – 21,18 $ | +0,26 % |
| 9:55 AM | CRL | 358,48 $ | 351,95 $ – 357,18 $ | +0,36 % |

… und 34 weitere in [orb.json](orb.json).

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

## Labor live – Mi 28.10.2026, Stand 10:00 Uhr ET

414 Aktien beobachtet · 1.053 Spielgeld-Trades aller Varianten · 979 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 2× normal | 0 | 0 | 0,00 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 2× normal | 0 | 0 | 0,00 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 0 | 0 | 0,00 € |
| Stocks in Play (Studie): Top 10 nach Startvolumen · Stopp 10 % ATR · Ziel 2R | 7 | 1 | -4,48 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 1 | 1 | 0,04 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| CHKP | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:40 159,58 $ | 159,08 $ | 160,57 $ | Stopp 9:45 Uhr | -0,36 € |
| HOOD | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:40 91,69 $ | 91,17 $ | 92,72 $ | Stopp 9:40 Uhr | -1,17 € |
| NXPI | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:40 245,66 $ | 244,76 $ | 247,47 $ | Stopp 9:40 Uhr | -2,03 € |
| FTV | News-Sprung: Lücke ≥ 2 % | 9:45 66,45 $ | 64,15 $ | 71,04 $ | offen, Kurs 66,51 $ | 0,04 € |
| MDT | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:45 94,65 $ | 94,41 $ | 95,14 $ | Stopp 9:50 Uhr | -0,31 € |
| RPRX | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:45 64,73 $ | 64,59 $ | 65,03 $ | Ziel 9:50 Uhr | 0,40 € |
| CECO | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:50 54,31 $ | 53,80 $ | 55,31 $ | Stopp 9:55 Uhr | -0,98 € |
| SGRY | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:50 23,34 $ | 23,24 $ | 23,55 $ | offen, Kurs 23,35 $ | -0,03 € |

## Labor (Testphase, Spielgeld ohne Limit)

583 Aktien · 63 Handelstage · Lerntage Do 30.07.2026 bis Mo 28.09.2026 · **Prüftage Di 29.09.2026 bis Di 27.10.2026** · 76 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 2× normal | 337 | 51 % | +0,09 % | 30,13 € | -643,87 € | möglich | **ja** |
| 2 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 2× normal | 78 | 64 % | +1,18 % | 92,11 € | -63,89 € | unwahrscheinlich | nein |
| 3 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 182 | 59 % | +1,12 % | 203,18 € | -160,82 € | unwahrscheinlich | nein |
| 4 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R | 208 | 55 % | +0,88 % | 183,74 € | -232,26 € | unwahrscheinlich | nein |
| 5 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 36 | 61 % | +0,82 % | 29,39 € | -42,61 € | möglich | nein |
| 6 | Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 2R | 208 | 52 % | +0,44 % | 90,88 € | -325,12 € | unwahrscheinlich | nein |
| 7 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 1R | 208 | 55 % | +0,34 % | 71,21 € | -344,79 € | unwahrscheinlich | nein |
| 8 | Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 459 | 50 % | +0,20 % | 90,74 € | -827,26 € | unwahrscheinlich | nein |
| 9 | Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 1,5R | 459 | 50 % | +0,18 % | 82,84 € | -835,15 € | unwahrscheinlich | nein |
| 10 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · Volumen ≥ 1,5× | 712 | 50 % | +0,12 % | 87,90 € | -1.336,10 € | möglich | nein |
| 11 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 1,5R · Volumen ≥ 1,5× | 712 | 50 % | +0,11 % | 81,30 € | -1.342,69 € | möglich | nein |
| 12 | Erholung: RSI unter 30 · Stopp 1,5 % darunter · Ziel 2R | 956 | 46 % | +0,09 % | 85,54 € | -1.826,46 € | unwahrscheinlich | nein |

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
