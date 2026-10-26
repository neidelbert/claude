# Trader-Übersicht

Stand: Mo 26.10. 13:41 Uhr ET (18:41 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Fr 23.10. 08:25 Uhr ET (14:25 Uhr MESZ) | OK – 823 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/39953208409)) |
| ORB-Scan | Mo 26.10. 10:35 Uhr ET (15:35 Uhr MEZ) | OK – 396 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40340972956)) |
| Labor live | Mo 26.10. 13:40 Uhr ET (18:40 Uhr MEZ) | OK – 3.937 Trades, 2.196 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/40340972956)) |
| Labor | Fr 23.10. 13:09 Uhr ET (19:09 Uhr MESZ) | OK – 0 von 58 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/39992696989)) |
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

## ORB-Scan – 2026-10-26 10:35 ET

Quelle: Treffer des Morgen-Scans · 723 nutzbare Charts · **396 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | ACI | 14,16 $ | 13,83 $ – 14,13 $ | +0,21 % |
| 9:50 AM | ADC | 67,35 $ | 66,68 $ – 67,23 $ | +0,17 % |
| 9:50 AM | AEE | 108,58 $ | 107,64 $ – 108,58 $ | +0,00 % |
| 9:50 AM | AESI | 8,79 $ | 8,53 $ – 8,73 $ | +0,69 % |
| 9:50 AM | AMAT | 385,42 $ | 378,20 $ – 384,28 $ | +0,30 % |
| 9:50 AM | AMGN | 447,22 $ | 444,25 $ – 447,18 $ | +0,01 % |
| 9:50 AM | AMH | 32,19 $ | 31,95 $ – 32,18 $ | +0,03 % |
| 9:50 AM | AMN | 48,43 $ | 47,60 $ – 48,42 $ | +0,02 % |
| 9:50 AM | ATI | 159,73 $ | 156,10 $ – 158,58 $ | +0,72 % |
| 9:50 AM | BAC | 51,46 $ | 50,72 $ – 51,25 $ | +0,40 % |
| 9:50 AM | BHVN | 14,06 $ | 13,69 $ – 13,97 $ | +0,61 % |
| 9:50 AM | BJ | 106,73 $ | 105,43 $ – 106,42 $ | +0,29 % |
| 9:50 AM | BNL | 17,52 $ | 17,37 $ – 17,50 $ | +0,09 % |
| 9:50 AM | BRUN | 7,31 $ | 6,97 $ – 7,19 $ | +1,67 % |
| 9:50 AM | BRX | 28,33 $ | 28,13 $ – 28,32 $ | +0,04 % |
| 9:50 AM | BYD | 73,10 $ | 71,50 $ – 73,07 $ | +0,04 % |
| 9:50 AM | CAH | 252,36 $ | 249,96 $ – 252,36 $ | +0,00 % |
| 9:50 AM | CCI | 88,74 $ | 86,00 $ – 88,61 $ | +0,14 % |
| 9:50 AM | CHD | 105,63 $ | 104,97 $ – 105,55 $ | +0,08 % |
| 9:50 AM | CMG | 28,35 $ | 27,66 $ – 28,29 $ | +0,24 % |
| 9:50 AM | CNQ | 54,92 $ | 54,27 $ – 54,72 $ | +0,37 % |
| 9:50 AM | COHR | 215,12 $ | 208,86 $ – 214,51 $ | +0,28 % |
| 9:50 AM | COP | 151,20 $ | 149,24 $ – 151,05 $ | +0,10 % |
| 9:50 AM | CRBG | 35,12 $ | 34,38 $ – 35,06 $ | +0,17 % |
| 9:50 AM | CRS | 282,84 $ | 275,60 $ – 281,26 $ | +0,56 % |
| 9:50 AM | CRWV | 53,32 $ | 51,24 $ – 52,87 $ | +0,85 % |
| 9:50 AM | CUZ | 29,03 $ | 28,62 $ – 29,01 $ | +0,07 % |
| 9:50 AM | DINO | 126,06 $ | 121,66 $ – 124,42 $ | +1,32 % |
| 9:50 AM | DOCN | 95,00 $ | 92,35 $ – 94,69 $ | +0,33 % |
| 9:50 AM | DOW | 33,96 $ | 32,28 $ – 33,81 $ | +0,46 % |

… und 366 weitere in [orb.json](orb.json).

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: AAPL +1,23 % · **AMAT -8,16 %** · BRK.B +1,48 % · **CRWV -10,06 %** · **KLAC -9,55 %** · LLY +2,83 % · **LRCX -11,76 %** · **PG +5,58 %** · **SKHY -8,07 %** · WMT +2,82 %

- 23.10. 08:01 Uhr ET · **SKHY** · [MU, SNDK, SKHY Stocks Bounce After Thursday’s Markdown, But Strategists Split: ‘Great Buying Opportunity’ Versus ‘The Kospi Has Peaked’](https://stocktwits.com/news-articles/markets/equity/mu-sndk-skhynix-stocks-rebound-semiconductor-selloff-strategists/cZxyh1rRBxL?.tsrc=rss)
- 23.10. 07:30 Uhr ET · **AAPL** · [Apple Is Just $42 Billion Away From Passing Nvidia as the World’s Most Valuable Company](https://247wallst.com/investing/2026/10/23/apple-is-just-42-billion-away-from-passing-nvidia-as-the-worlds-most-valuable-company/?.tsrc=rss)
- 23.10. 07:26 Uhr ET · **CRWV** · [The Bond Market Is Sending a Dire Warning to Wall Street About the AI Infrastructure Build-Out, but Is Anyone Paying Attention?](https://www.fool.com/investing/2026/10/23/bond-market-sending-dire-warning-to-wall-street-about-ai-infrastructure-build-out/?.tsrc=rss)
- 23.10. 07:16 Uhr ET · **AAPL** · [3 Investment Grade Bond Ideas Riding Big Tech AI Capex Plans](https://finance.yahoo.com/markets/stocks/articles/3-investment-grade-bond-ideas-111614808.html?.tsrc=rss)
- 23.10. 07:15 Uhr ET · **CRWV** · [Nebius Has Cratered Over The Last 3 Months: This Wall Street Ratings Firm Says 2.5X Returns Will Materialize Soon](https://247wallst.com/investing/2026/10/23/nebius-has-cratered-over-the-last-3-months-this-wall-street-ratings-firm-says-2-5x-returns-will-materialize-soon/?.tsrc=rss) · earnings
- 23.10. 07:06 Uhr ET · **CRWV** · [Two Critical Nvidia Stock Flaws and Other Reasons This Analyst Says Sell](https://finance.yahoo.com/m/9cdb41d6-a291-37eb-bff7-347d06660a9d/two-critical-nvidia-stock.html?.tsrc=rss)
- 23.10. 07:00 Uhr ET · **AAPL** · [Develop A Critical Thinking Mindset When You Make Decisions](https://finance.yahoo.com/m/4941c14e-8ac8-3d05-85f5-a6d29d520931/develop-a-critical-thinking.html?.tsrc=rss)
- 23.10. 06:56 Uhr ET · **CRWV** · [BofA sees growing investor reluctance to fund AI infrastructure](https://finance.yahoo.com/technology/ai/articles/bofa-sees-growing-investor-reluctance-105636342.html?.tsrc=rss)
- 23.10. 06:45 Uhr ET · **CRWV** · [Moderna, Meta, SpaceX, AT&T, CoreWeave, Sandisk, and More Stocks That Explain Today’s Market](https://finance.yahoo.com/m/f96806d8-9583-3620-89cf-a7ccb8de8237/moderna%2C-meta%2C-spacex%2C-at%26t%2C.html?.tsrc=rss) · macro
- 23.10. 06:38 Uhr ET · **AAPL** · [Apple could be about to dethrone Nvidia as world's most valuable company](https://finance.yahoo.com/markets/stocks/article/apple-could-be-about-to-dethrone-nvidia-as-worlds-most-valuable-company-103826475.html?.tsrc=rss)
- 23.10. 06:35 Uhr ET · **SKHY** · [History Says This Is What Happens to Mega-IPO Stocks in Their First 12 Months](https://www.fool.com/investing/2026/10/23/history-what-happens-mega-ipo-stock-12-months/?.tsrc=rss)
- 23.10. 06:29 Uhr ET · **SKHY** · [Stock Market Today: Futures Head Lower at End of Wild Week as Oil Prices Rise Further on Middle East Tensions; Chip Stocks Rebound](https://www.investopedia.com/stock-market-today-dow-jones-s-and-p-500-10232026-12189475?.tsrc=rss) · macro
- 23.10. 06:25 Uhr ET · **CRWV** · [SK Hynix Scraps U.S. IPO of Memory-Chip Unit. Why the Stock Is Jumping.](https://finance.yahoo.com/m/824ab6e9-a4f8-30cc-98f6-d256584e0ccc/sk-hynix-scraps-u.s.-ipo-of.html?.tsrc=rss)
- 23.10. 06:14 Uhr ET · **LLY** · [What Sent Eli Lilly Stock Higher Over The Past Year?](https://www.trefis.com/articles/620216/what-sent-eli-lilly-stock-higher-over-the-past-year/2026-10-23?.tsrc=rss)
- 23.10. 06:13 Uhr ET · **CRWV** · [Nasdaq, Dow, S&P 500 Futures Drop Premarket: NVDA, AMD, META, CRWV, MRNA, WDC, BE In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-dow-s-and-p-500-futures-drop-premarket-nvda-amd-meta-crwv-mrna-wdc-be-in-focus/cZxyfNARBxI?.tsrc=rss) · macro
- 23.10. 06:00 Uhr ET · **PG** · [Wall Street's safest stock just had its biggest day since the pandemic crash: Chart of the Day](https://finance.yahoo.com/markets/article/wall-streets-safest-stock-just-had-its-biggest-day-since-the-pandemic-crash-chart-of-the-day-100000879.html?.tsrc=rss)
- 23.10. 05:35 Uhr ET · **SKHY** · [Better Memory Stock: SK Hynix vs. Micron](https://www.fool.com/investing/2026/10/23/better-memory-stock-sk-hynix-vs-micron/?.tsrc=rss)
- 23.10. 05:30 Uhr ET · **CRWV** · [Stocktwits Wall Street Wrap: Analysts Turn Bullish On SpaceX, Tesla, But Netflix And Chipotle Face Fresh Downgrades Amid Growth Concerns](https://stocktwits.com/news-articles/markets/equity/stocktwits-wall-street-wrap-analysts-turn-bullish-on-space-x-tesla-but-netflix-and-chipotle-face-fresh-downgrades-amid-growth-concerns/cZxyaiCRBx4?.tsrc=rss) · earnings, analyst
- 23.10. 05:30 Uhr ET · **CRWV** · [Stock market today: Dow, S&P 500, Nasdaq futures wobble after sharp tech sell-off](https://finance.yahoo.com/markets/live/stock-market-today-friday-october-23-dow-sp-500-nasdaq-tesla-meta-093000521.html?.tsrc=rss) · macro
- 23.10. 05:26 Uhr ET · **AAPL** · [Warren Buffett's Successor, Greg Abel, Has 32% of Berkshire Hathaway's $364 Billion Portfolio Invested in 3 Unstoppable AI Stocks](https://www.fool.com/investing/2026/10/23/warren-buffett-successor-greg-abel-32-berkshire-hathaway-364-billion-portfolio-invested-3-unstoppable-ai-stocks/?.tsrc=rss)
- 23.10. 05:01 Uhr ET · **AAPL** · [Could You Have Seen The Run In Microsoft Stock Coming?](https://www.trefis.com/articles/620174/could-you-have-seen-the-run-in-microsoft-stock-coming/2026-10-23?.tsrc=rss)
- 23.10. 04:50 Uhr ET · **CRWV** · [If I Could Only Buy 1 AI Stock in November After This Sell-Off, It Would Be This One.](https://www.fool.com/investing/2026/10/23/if-only-buy-ai-stock-in-november-sell-off-alab/?.tsrc=rss) · earnings
- 23.10. 04:44 Uhr ET · **SKHY** · [Nasdaq Futures Steady as AI Selloff Pauses](https://www.wsj.com/finance/stocks/nasdaq-futures-steady-as-ai-selloff-pauses-275c6454?.tsrc=rss) · macro
- 23.10. 04:22 Uhr ET · **BRK.B** · [The S&P 500 May Depend on the Fortunes of These 3 Companies Right Now. Here’s the Good News and the Bad News for Investors.](https://www.fool.com/investing/2026/10/23/the-s-and-p-500-may-depend-on-the-fortunes-of-these-3-companies-right-now-here-s-the-good-news-and-the-bad-news-for-investors/?.tsrc=rss)
- 23.10. 04:21 Uhr ET · **PG** · [Company News for Oct 23, 2026](https://finance.yahoo.com/markets/stocks/articles/company-news-oct-23-2026-082100335.html?.tsrc=rss)

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

## Labor live – Mo 26.10.2026, Stand 13:40 Uhr ET

397 Aktien beobachtet · 3.937 Spielgeld-Trades aller Varianten · 2.196 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R | 14 | 10 | 19,33 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 2R | 14 | 5 | 12,29 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 1R | 14 | 6 | 11,64 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · Volumen ≥ 1,5× | 21 | 19 | -4,80 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 21 | 19 | -4,80 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R | 10 | 9 | 0,59 € |
| Stocks in Play (Studie): Top 10 nach Startvolumen · Stopp 10 % ATR · Ziel 2R | 7 | 0 | 1,60 € |
| News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R | 0 | 0 | 0,00 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| RIG | Ausbruch 30 Min | 10:45 6,55 $ | 6,33 $ | 7,01 $ | offen, Kurs 6,54 $ | -0,26 € |
| MTZ | Opening-Range-Ausbruch 30 Min | 11:00 176,89 $ | 171,52 $ | 187,63 $ | offen, Kurs 174,41 $ | -1,45 € |
| MTZ | Ausbruch 30 Min | 11:00 176,89 $ | 171,52 $ | 187,63 $ | offen, Kurs 174,41 $ | -1,45 € |
| NET | Opening-Range-Ausbruch 30 Min | 11:00 331,96 $ | 316,00 $ | 363,88 $ | offen, Kurs 330,30 $ | -0,55 € |
| NET | Ausbruch 30 Min | 11:00 331,96 $ | 316,00 $ | 363,88 $ | offen, Kurs 330,30 $ | -0,55 € |
| NET | Ausbruch 30 Min | 11:00 331,96 $ | 316,00 $ | 363,88 $ | offen, Kurs 330,30 $ | -0,55 € |
| ITUB | Erholung: Lücke nach unten ≥ 3 % | 11:10 7,50 $ | 7,23 $ | 7,77 $ | offen, Kurs 7,64 $ | 1,90 € |
| ITUB | Erholung: Lücke nach unten ≥ 3 % | 11:10 7,50 $ | 7,23 $ | 8,04 $ | offen, Kurs 7,64 $ | 1,90 € |
| ITUB | Erholung: Lücke nach unten ≥ 3 % | 11:10 7,50 $ | 7,38 $ | 7,73 $ | offen, Kurs 7,64 $ | 1,90 € |
| MU | Opening-Range-Ausbruch 30 Min | 11:25 910,91 $ | 883,73 $ | 965,26 $ | offen, Kurs 911,06 $ | -0,03 € |
| MU | Ausbruch 30 Min | 11:25 910,91 $ | 883,73 $ | 965,26 $ | offen, Kurs 911,06 $ | -0,03 € |
| PBR | Erholung: Lücke nach unten ≥ 3 % | 11:30 21,85 $ | 21,36 $ | 22,35 $ | Ziel 13:15 Uhr | 2,22 € |
| PBR | Erholung: Lücke nach unten ≥ 3 % | 11:30 21,85 $ | 21,36 $ | 22,84 $ | offen, Kurs 22,16 $ | 1,39 € |
| PBR | Erholung: Lücke nach unten ≥ 3 % | 11:30 21,85 $ | 21,51 $ | 22,53 $ | offen, Kurs 22,16 $ | 1,39 € |
| NVS | Opening-Range-Ausbruch 30 Min | 11:40 153,97 $ | 152,02 $ | 157,88 $ | offen, Kurs 153,65 $ | -0,26 € |
| NVS | Ausbruch 30 Min | 11:40 153,97 $ | 152,02 $ | 157,88 $ | offen, Kurs 153,65 $ | -0,26 € |
| NVS | Ausbruch 30 Min | 11:40 153,97 $ | 152,02 $ | 157,88 $ | offen, Kurs 153,65 $ | -0,26 € |
| SE | Erholung: Lücke nach unten ≥ 3 % | 12:55 74,25 $ | 71,53 $ | 76,96 $ | offen, Kurs 73,70 $ | -0,79 € |
| SE | Erholung: Lücke nach unten ≥ 3 % | 12:55 74,25 $ | 71,53 $ | 79,68 $ | offen, Kurs 73,70 $ | -0,79 € |
| SE | Erholung: Lücke nach unten ≥ 3 % | 12:55 74,25 $ | 73,10 $ | 76,55 $ | offen, Kurs 73,70 $ | -0,79 € |

## Labor (Testphase, Spielgeld ohne Limit)

397 Aktien · 61 Handelstage · Lerntage Do 30.07.2026 bis Fr 25.09.2026 · **Prüftage Mo 28.09.2026 bis Fr 23.10.2026** · 58 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R | 146 | 53 % | +0,73 % | 106,55 € | -185,45 € | unwahrscheinlich | nein |
| 2 | Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 2R | 146 | 50 % | +0,36 % | 52,66 € | -239,34 € | unwahrscheinlich | nein |
| 3 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 1R | 146 | 54 % | +0,28 % | 41,49 € | -250,51 € | möglich | nein |
| 4 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · Volumen ≥ 1,5× | 465 | 50 % | +0,10 % | 46,13 € | -883,87 € | möglich | nein |
| 5 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 1,5R · Volumen ≥ 1,5× | 465 | 50 % | +0,09 % | 43,84 € | -886,16 € | möglich | nein |
| 6 | Erholung: RSI unter 30 · Stopp 1,5 % darunter · Ziel 2R | 562 | 48 % | +0,09 % | 50,75 € | -1.073,25 € | möglich | nein |
| 7 | Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 268 | 47 % | +0,08 % | 21,43 € | -514,57 € | möglich | nein |
| 8 | Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 1,5R | 268 | 47 % | +0,07 % | 20,23 € | -515,77 € | möglich | nein |
| 9 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 1R · Volumen ≥ 1,5× | 465 | 50 % | +0,06 % | 27,57 € | -902,43 € | möglich | nein |
| 10 | Erholung: RSI unter 30 · Stopp 1,5 % darunter · Ziel 1R | 562 | 49 % | +0,06 % | 31,85 € | -1.092,15 € | möglich | nein |
| 11 | Opening-Range-Ausbruch 30 Min · Stopp Mitte der Spanne · Ziel 2R · Volumen ≥ 1,5× | 465 | 47 % | +0,06 % | 25,54 € | -904,46 € | möglich | nein |
| 12 | Opening-Range-Ausbruch 30 Min · Stopp Mitte der Spanne · Ziel 1,5R · Volumen ≥ 1,5× | 465 | 48 % | +0,04 % | 19,79 € | -910,21 € | möglich | nein |

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
