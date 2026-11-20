# Trader-Übersicht

Stand: Fr 20.11. 12:40 Uhr ET (18:40 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Fr 20.11. 11:41 Uhr ET (17:41 Uhr MEZ) | OK – 108 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44729531561)) |
| ORB-Scan | Fr 20.11. 11:41 Uhr ET (17:41 Uhr MEZ) | OK – 59 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44729531561)) |
| Labor live | Fr 20.11. 12:40 Uhr ET (18:40 Uhr MEZ) | OK – 2.167 Trades, 811 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/44729531561)) |
| Labor | Do 19.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 16 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/44604811557)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Do 19.11.2026

5.927 Aktien in der Liste · 5.927 Charts geladen · 605 liquide (ab 5 $ und 1.000.000 Aktien) · 604 gescannt · **108 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 9 | PDD, TGT, INSM, IBN, GME, PCG, TU, VVV |
| `bull_flag` | 13 | CMCSA, HDB, TMUS, CMG, RKT, IBN, MDLN, MWH |
| `reclaim_ma20` | 8 | PANW, COHR, CRWD, PDD, UTZ, VVV, YMM, S |
| `oversold` | 75 | NVDA, SNDK, GOOG, UNH, MSTR, CAT, IREN, HOOD |
| `oversold_bounce` | 11 | INTC, ASTS, AGNC, USAR, NLY, DX, UMAC, ARR |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| NVDA | 145,98 $ | 19,8 | `oversold` |
| SNDK | 94,39 $ | 29,1 | `oversold` |
| INTC | 55,72 $ | 31,1 | `oversold_bounce` |
| GOOG | 271,02 $ | 29,6 | `oversold` |
| UNH | 330,48 $ | 24,3 | `oversold` |
| PANW | 361,73 $ | 54,5 | `reclaim_ma20` |
| COHR | 214,94 $ | 45,8 | `reclaim_ma20` |
| MSTR | 86,13 $ | 22,9 | `oversold` |
| CAT | 537,37 $ | 27,0 | `oversold` |
| CRWD | 243,46 $ | 53,6 | `reclaim_ma20` |
| IREN | 14,41 $ | 27,6 | `oversold` |
| PDD | 86,00 $ | 63,8 | `breakout_20d`, `reclaim_ma20` |
| HOOD | 68,65 $ | 27,3 | `oversold` |
| NOW | 88,87 $ | 24,8 | `oversold` |
| COIN | 108,87 $ | 25,4 | `oversold` |
| FCX | 49,12 $ | 23,8 | `oversold` |
| CRM | 183,31 $ | 22,0 | `oversold` |
| BABA | 83,31 $ | 23,3 | `oversold` |
| BA | 160,51 $ | 27,9 | `oversold` |
| UTZ | 14,29 $ | 55,5 | `reclaim_ma20` |

Alle 108 Treffer: [watchlist.json](watchlist.json)

## ORB-Scan – 2026-11-20 11:43 ET

Quelle: Treffer des Morgen-Scans · 88 nutzbare Charts · **59 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | BABA | 84,08 $ | 82,98 $ – 84,07 $ | +0,01 % |
| 9:50 AM | BHP | 68,98 $ | 67,86 $ – 68,69 $ | +0,42 % |
| 9:50 AM | CAT | 533,66 $ | 524,50 $ – 529,63 $ | +0,76 % |
| 9:50 AM | CLM | 5,31 $ | 5,20 $ – 5,28 $ | +0,47 % |
| 9:50 AM | CNQ | 44,70 $ | 44,09 $ – 44,61 $ | +0,20 % |
| 9:50 AM | IE | 5,70 $ | 5,55 $ – 5,70 $ | +0,09 % |
| 9:50 AM | INSM | 149,10 $ | 142,42 $ – 147,47 $ | +1,11 % |
| 9:50 AM | INTC | 54,78 $ | 53,48 $ – 54,48 $ | +0,55 % |
| 9:50 AM | MDLN | 38,24 $ | 37,44 $ – 38,22 $ | +0,05 % |
| 9:50 AM | MWH | 26,80 $ | 26,00 $ – 26,72 $ | +0,30 % |
| 9:50 AM | NAVI | 6,05 $ | 5,83 $ – 6,02 $ | +0,42 % |
| 9:50 AM | RIO | 74,53 $ | 74,14 $ – 74,49 $ | +0,05 % |
| 9:50 AM | SAP | 203,12 $ | 200,90 $ – 203,04 $ | +0,04 % |
| 9:50 AM | TEAM | 138,91 $ | 131,04 $ – 136,00 $ | +2,14 % |
| 9:50 AM | VALE | 9,78 $ | 9,65 $ – 9,77 $ | +0,15 % |
| 9:55 AM | ALB | 83,58 $ | 81,16 $ – 83,43 $ | +0,18 % |
| 9:55 AM | ASTS | 25,50 $ | 24,27 $ – 25,25 $ | +0,99 % |
| 9:55 AM | BA | 163,48 $ | 160,15 $ – 163,41 $ | +0,04 % |
| 9:55 AM | BILI | 11,02 $ | 10,83 $ – 10,98 $ | +0,32 % |
| 9:55 AM | CDE | 11,36 $ | 11,16 $ – 11,35 $ | +0,04 % |
| 9:55 AM | EC | 13,35 $ | 13,08 $ – 13,30 $ | +0,36 % |
| 9:55 AM | GDS | 14,19 $ | 13,70 $ – 14,10 $ | +0,67 % |
| 9:55 AM | GOOG | 277,87 $ | 271,06 $ – 277,19 $ | +0,25 % |
| 9:55 AM | HL | 11,08 $ | 10,85 $ – 11,07 $ | +0,11 % |
| 9:55 AM | NOW | 91,09 $ | 87,33 $ – 90,82 $ | +0,30 % |
| 9:55 AM | PBR | 16,18 $ | 16,02 $ – 16,17 $ | +0,06 % |
| 9:55 AM | UEC | 5,67 $ | 5,44 $ – 5,64 $ | +0,50 % |
| 9:55 AM | UMC | 12,77 $ | 12,43 $ – 12,75 $ | +0,20 % |
| 9:55 AM | UUUU | 5,34 $ | 5,20 $ – 5,33 $ | +0,09 % |
| 10:00 AM | ARR | 11,16 $ | 10,86 $ – 11,15 $ | +0,09 % |

… und 29 weitere in [orb.json](orb.json).

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: **CAT -3,61 %** · **COHR -14,90 %** · **CRWD -5,15 %** · GOOG +0,67 % · **INTC -3,86 %** · **MSTR -6,05 %** · **NVDA -7,06 %** · **PANW -3,23 %** · **SNDK -14,89 %** · **UNH +4,80 %**

- 20.11. 11:35 Uhr ET · **NVDA** · [Prediction: $5,000 in SpaceX Will Be Worth This Much by 2040 If Elon Musk Solves Its Power Problem](https://www.fool.com/investing/2026/11/20/prediction-5000-in-spacex-will-be-worth-this-much/?.tsrc=rss)
- 20.11. 11:34 Uhr ET · **GOOG** · [Investors Might Be Making a Big Mistake by Overlooking This Growth Stock](https://247wallst.com/investing/2026/11/20/investors-might-be-making-a-big-mistake-by-overlooking-this-growth-stock/?.tsrc=rss) · earnings
- 20.11. 11:34 Uhr ET · **NVDA** · [Why Sandisk Stock Dropped Again Today](https://www.fool.com/investing/2026/11/20/why-sandisk-stock-dropped-again-today/?.tsrc=rss)
- 20.11. 11:32 Uhr ET · **GOOG** · [Scott Bessent Says Trump-Xi Talks Did Not Address Jensen Huang, Left Nvidia H200 Policy Unchanged](https://stocktwits.com/news-articles/markets/equity/scott-bessent-says-trump-xi-talks-did-not-address-jensen-huang-left-nvidia-h200-policy-unchanged/cNbSZuYR915?.tsrc=rss)
- 20.11. 11:31 Uhr ET · **NVDA** · [How Low Nvidia Stock Can Go Now](https://finance.yahoo.com/m/4bbf9581-d9bc-3f2e-9760-2221f5e509cc/how-low-nvidia-stock-can-go.html?.tsrc=rss)
- 20.11. 11:27 Uhr ET · **GOOG** · [Nvidia Stock Falls 40% From Its High. It’s Getting Ugly but There’s Hope.](https://finance.yahoo.com/m/30e2a4ab-b95f-395f-9f4d-e4058f562e01/nvidia-stock-falls-40%25-from.html?.tsrc=rss)
- 20.11. 11:26 Uhr ET · **NVDA** · [The Hot ‘Toothpaste Trade’ Is Another Sign AI Stock Fears Are Getting Worse](https://finance.yahoo.com/m/27d8735d-c51d-33d5-8083-094abc7a7ba3/the-hot-%E2%80%98toothpaste-trade%E2%80%99-is.html?.tsrc=rss)
- 20.11. 11:22 Uhr ET · **NVDA** · [The Nasdaq Is In Its Third Correction of 2026. Here’s the Lesson Most Investors Are Missing.](https://www.fool.com/investing/2026/11/20/the-nasdaq-is-in-its-third-correction-of-2026-here-s-the-lesson-most-investors-are-missing/?.tsrc=rss)
- 20.11. 11:20 Uhr ET · **NVDA** · [Don't Try to Time the Market. Buy This ETF Instead.](https://www.fool.com/investing/2026/11/20/don-t-try-to-time-the-market-buy-this-etf-instead/?.tsrc=rss)
- 20.11. 11:17 Uhr ET · **NVDA** · [Why SpaceX Stock Dropped After the Anthropic IPO](https://www.fool.com/investing/2026/11/20/why-spacex-stock-dropped-after-the-anthropic-ipo/?.tsrc=rss)
- 20.11. 11:16 Uhr ET · **GOOG** · [Veteran investors talk new book, 'demystifying' financial jargon to invest sooner and smarter](https://finance.yahoo.com/video/veteran-investors-talk-new-book-demystifying-financial-jargon-to-invest-sooner-and-smarter-161606156.html?.tsrc=rss) · people
- 20.11. 11:13 Uhr ET · **NVDA** · [Which Baidu ETFs Change What Chip News Means For You?](https://finance.yahoo.com/markets/stocks/articles/baidu-etfs-change-chip-news-161322634.html?.tsrc=rss) · earnings
- 20.11. 11:11 Uhr ET · **SNDK** · [MU, SNDK, Other Chipmakers Plunge Amid AI Trade Weakness — UBS Says Risk-Reward In Equities Has Become ‘More Balanced’](https://stocktwits.com/news-articles/markets/equity/mu-sndk-other-chipmakers-plunge-amid-ai-trade-weakness-ubs-says-risk-reward-in-equities-has-become-more-balanced/cNbSZa1R91c?.tsrc=rss)
- 20.11. 11:05 Uhr ET · **CAT** · [Caterpillar Sinks 11% in a Week to a New 52-Week Low. Is the Selling Overdone?](https://www.tikr.com/blog/caterpillar-sinks-11-in-a-week-to-a-new-52-week-low-is-the-selling-overdone?ref=yahoofinance&tlnk=yf-261120-w3r4pmj4&.tsrc=rss)
- 20.11. 11:02 Uhr ET · **NVDA** · [Apollo and Goldman Sachs Announce Pricing of $44 Billion SpaceX GPU Financing](https://finance.yahoo.com/markets/stocks/articles/apollo-goldman-sachs-announce-pricing-160200875.html?.tsrc=rss)
- 20.11. 10:59 Uhr ET · **NVDA** · [Anthropic, Nvidia, AMD, Micron, Sandisk, Bloom Energy, and More Stocks That Explain Today’s Market](https://finance.yahoo.com/m/801603d1-8318-3eb0-99a6-10147f0d5ed5/anthropic%2C-nvidia%2C-amd%2C.html?.tsrc=rss)
- 20.11. 10:58 Uhr ET · **NVDA** · [Nvidia falls below Alphabet to become fourth most valuable U.S. company](https://finance.yahoo.com/markets/stocks/articles/nvidia-falls-below-alphabet-become-155838605.html?.tsrc=rss)
- 20.11. 10:58 Uhr ET · **UNH** · [TD Cowen lifts UnitedHealth, Humana to Buy on improved earnings outlook](https://finance.yahoo.com/healthcare/articles/td-cowen-lifts-unitedhealth-humana-155813927.html?.tsrc=rss) · earnings, analyst
- 20.11. 10:57 Uhr ET · **GOOG** · [SDMC's Third Consecutive Year at Google's TV Summit, Showcasing Home Physical AI](https://finance.yahoo.com/technology/ai/articles/sdmcs-third-consecutive-googles-tv-155700409.html?.tsrc=rss)
- 20.11. 10:55 Uhr ET · **NVDA** · [Is Micron's Record Inventory A Risk For The Stock?](https://www.trefis.com/stock/mu/articles/627203/is-micron-s-record-inventory-a-risk-for-the-stock/2026-11-20?.tsrc=rss)
- 20.11. 10:51 Uhr ET · **GOOG** · [Nvidia Falls Behind Alphabet, Loses $2.3 Trillion In Market Value Since October Peak](https://stocktwits.com/news-articles/markets/equity/nvidia-falls-behind-alphabet-loses-2-3-trillion-in-market-value-since-october-peak/cNbSlqeR91T?.tsrc=rss)
- 20.11. 10:50 Uhr ET · **NVDA** · [Costco Just Made a New All-Time High After Announcing a $30-Per-Share Special Dividend. Is the Stock a Buy Before Dec. 10?](https://www.fool.com/investing/2026/11/20/costco-just-made-a-new-all-time-high-after-announcing-a-30-per-share-special-dividend-is-the-stock-a-buy-before-dec-10/?.tsrc=rss) · capital
- 20.11. 10:48 Uhr ET · **NVDA** · [How Anthropic compares to other tech companies](https://finance.yahoo.com/video/how-anthropic-compares-to-other-tech-companies-154845765.html?.tsrc=rss)
- 20.11. 10:45 Uhr ET · **CAT** · [Caterpillar’s 35% 3-Month Downturn: This Sell-Side Firm Predicts 90% Returns From Here With Another Close Behind](https://247wallst.com/investing/2026/11/20/caterpillars-35-3-month-downturn-this-sell-side-firm-predicts-90-returns-from-here-with-another-close-behind/?.tsrc=rss)
- 20.11. 10:45 Uhr ET · **NVDA** · [Between IREN and CoreWeave Here’s Who Has the Cleaner Path to a Sustained 30% Rebound](https://247wallst.com/investing/2026/11/20/between-iren-and-coreweave-heres-who-has-the-cleaner-path-to-a-sustained-30-rebound/?.tsrc=rss)

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

## Labor live – Fr 20.11.2026, Stand 12:40 Uhr ET

245 Aktien beobachtet · 2.167 Spielgeld-Trades aller Varianten · 811 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 0 | 0 | 0,00 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 1 | 0 | -1,09 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 19 | 13 | -31,94 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 1 | -1,58 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| UUUU | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:55 5,33 $ | 5,28 $ | – | Stopp 10:20 Uhr | -1,09 € |
| ABBV | Ausbruch 30 Min | 10:05 288,64 $ | 286,39 $ | 293,15 $ | offen, Kurs 288,40 $ | -0,13 € |
| BA | Ausbruch 30 Min | 10:05 164,13 $ | 160,15 $ | 172,10 $ | Stopp 11:40 Uhr | -2,48 € |
| BHP | Ausbruch 30 Min | 10:05 69,55 $ | 67,86 $ | 72,94 $ | Stopp 12:40 Uhr | -2,48 € |
| BMY | Ausbruch 30 Min | 10:05 59,56 $ | 58,73 $ | 61,22 $ | offen, Kurs 59,25 $ | -0,57 € |
| CMCSA | Ausbruch 30 Min | 10:05 25,36 $ | 25,07 $ | 25,95 $ | offen, Kurs 25,26 $ | -0,47 € |
| DX | Ausbruch 30 Min | 10:05 10,07 $ | 9,87 $ | 10,47 $ | Stopp 12:25 Uhr | -2,04 € |
| EBAY | Ausbruch 30 Min | 10:05 120,08 $ | 117,71 $ | 124,82 $ | offen, Kurs 118,17 $ | -1,64 € |
| F | Ausbruch 30 Min | 10:05 11,64 $ | 11,21 $ | 12,50 $ | offen, Kurs 11,34 $ | -2,68 € |
| IBM | Ausbruch 30 Min | 10:05 232,08 $ | 223,77 $ | 248,71 $ | offen, Kurs 229,50 $ | -1,16 € |
| MRK | Ausbruch 30 Min | 10:05 136,84 $ | 133,79 $ | 142,94 $ | offen, Kurs 134,62 $ | -1,67 € |
| PATH | Ausbruch 30 Min | 10:05 11,43 $ | 11,12 $ | 12,05 $ | Stopp 11:45 Uhr | -2,77 € |
| PINS | Ausbruch 30 Min | 10:05 17,60 $ | 16,81 $ | 19,19 $ | offen, Kurs 16,91 $ | -4,02 € |
| PLTR | Ausbruch 30 Min | 10:05 152,45 $ | 147,55 $ | 162,25 $ | Stopp 10:40 Uhr | -3,26 € |
| PYPL | Ausbruch 30 Min | 10:05 55,05 $ | 53,31 $ | 58,52 $ | offen, Kurs 54,22 $ | -1,55 € |
| UNH | Ausbruch 30 Min | 10:05 345,45 $ | 338,24 $ | 359,88 $ | offen, Kurs 344,50 $ | -0,33 € |
| GME | Ausbruch 30 Min | 10:10 27,52 $ | 26,74 $ | 29,09 $ | Stopp 11:40 Uhr | -2,90 € |
| RKT | Ausbruch 30 Min | 10:10 13,84 $ | 13,12 $ | 15,29 $ | offen, Kurs 13,47 $ | -2,70 € |
| T | Ausbruch 30 Min | 10:10 22,45 $ | 22,08 $ | 23,19 $ | offen, Kurs 22,64 $ | 0,81 € |
| TMUS | Ausbruch 30 Min | 10:10 166,93 $ | 164,27 $ | 172,25 $ | offen, Kurs 167,17 $ | 0,10 € |

## Labor (Testphase, Spielgeld ohne Limit)

731 Aktien · 80 Handelstage · Lerntage Do 30.07.2026 bis Di 13.10.2026 · **Prüftage Mi 14.10.2026 bis Do 19.11.2026** · 80 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 44 | 64 % | +1,25 % | 55,05 € | -32,95 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 44 | 64 % | +1,08 % | 47,59 € | -40,41 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 44 | 64 % | +0,98 % | 43,19 € | -44,81 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 61 | 57 % | +0,72 % | 43,97 € | -78,03 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 61 | 57 % | +0,57 % | 34,55 € | -87,45 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 61 | 57 % | +0,48 % | 29,17 € | -92,83 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 4× normal | 82 | 52 % | +0,46 % | 37,57 € | -126,43 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 3R | 81 | 52 % | +0,43 % | 34,75 € | -127,25 € | möglich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 144 | 52 % | +0,41 % | 59,57 € | -228,43 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 154 | 51 % | +0,38 % | 59,17 € | -248,83 € | möglich | **ja** |
| 11 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 2R | 81 | 52 % | +0,37 % | 29,90 € | -132,10 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 153 | 51 % | +0,34 % | 52,03 € | -253,97 € | möglich | **ja** |

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
