# Trader-Übersicht

Stand: Mi 25.11. 09:50 Uhr ET (15:50 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Mi 25.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 371 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45562375663)) |
| ORB-Scan | Di 24.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 261 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45334981954)) |
| Labor live | Mi 25.11. 09:50 Uhr ET (15:50 Uhr MEZ) | OK – 214 Trades, 171 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/45562375663)) |
| Labor | Di 24.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 16 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/45428441399)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Di 24.11.2026

5.927 Aktien in der Liste · 5.927 Charts geladen · 1.467 liquide (ab 5 $ und 1.000.000 Aktien) · 1.466 gescannt · **371 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 115 | INSM, WMT, ABBV, GILD, DIS, KYMR, DLTR, T |
| `bull_flag` | 28 | CAH, EW, PFGC, IBN, HDB, CLX, TSN, TFX |
| `reclaim_ma20` | 146 | LLY, MRNA, KO, JNJ, ABBV, MA, AMGN, PEP |
| `oversold` | 70 | SNDK, MSTR, FCX, COIN, VALE, BMNR, CRCL, ADM |
| `oversold_bounce` | 40 | UNH, CRM, INTU, COF, OXY, TEAM, IP, SHEL |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| INSM | 170,15 $ | 82,9 | `breakout_20d` |
| SNDK | 94,39 $ | 29,3 | `oversold` |
| LLY | 1.407,59 $ | 59,0 | `reclaim_ma20` |
| WMT | 132,31 $ | 71,8 | `breakout_20d` |
| UNH | 341,88 $ | 32,2 | `oversold_bounce` |
| MRNA | 227,38 $ | 53,3 | `reclaim_ma20` |
| KO | 97,62 $ | 58,6 | `reclaim_ma20` |
| JNJ | 276,46 $ | 54,0 | `reclaim_ma20` |
| MSTR | 77,55 $ | 24,7 | `oversold` |
| ABBV | 300,28 $ | 63,8 | `breakout_20d`, `reclaim_ma20` |
| MA | 647,44 $ | 55,6 | `reclaim_ma20` |
| GILD | 178,29 $ | 68,7 | `breakout_20d` |
| CRM | 193,26 $ | 35,3 | `oversold_bounce` |
| AMGN | 473,94 $ | 61,8 | `reclaim_ma20` |
| DIS | 122,51 $ | 64,2 | `breakout_20d` |
| PEP | 142,68 $ | 57,0 | `reclaim_ma20` |
| KYMR | 173,92 $ | 76,5 | `breakout_20d` |
| INTU | 279,42 $ | 31,8 | `oversold_bounce` |
| DLTR | 154,65 $ | 68,2 | `breakout_20d` |
| T | 22,88 $ | 57,5 | `breakout_20d` |

Alle 371 Treffer: [watchlist.json](watchlist.json)

## ORB-Scan – 2026-11-24 10:10 ET

Quelle: Treffer des Morgen-Scans · 503 nutzbare Charts · **261 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | AAPL | 352,95 $ | 345,88 $ – 352,50 $ | +0,13 % |
| 9:50 AM | ACIW | 52,88 $ | 51,66 $ – 52,47 $ | +0,80 % |
| 9:50 AM | ADC | 71,57 $ | 70,71 $ – 71,51 $ | +0,08 % |
| 9:50 AM | ADEA | 13,73 $ | 13,45 $ – 13,67 $ | +0,44 % |
| 9:50 AM | AFRM | 59,83 $ | 57,50 $ – 59,80 $ | +0,05 % |
| 9:50 AM | AG | 11,24 $ | 10,95 $ – 11,23 $ | +0,17 % |
| 9:50 AM | AGNC | 7,99 $ | 7,83 $ – 7,98 $ | +0,19 % |
| 9:50 AM | AKAM | 90,77 $ | 87,78 $ – 89,90 $ | +0,97 % |
| 9:50 AM | ARIS | 12,82 $ | 12,42 $ – 12,77 $ | +0,43 % |
| 9:50 AM | B | 34,24 $ | 33,35 $ – 34,21 $ | +0,09 % |
| 9:50 AM | BAC | 48,52 $ | 47,81 $ – 48,49 $ | +0,06 % |
| 9:50 AM | BBAR | 9,24 $ | 8,99 $ – 9,21 $ | +0,33 % |
| 9:50 AM | BEKE | 18,24 $ | 17,86 $ – 18,21 $ | +0,16 % |
| 9:50 AM | BOX | 46,21 $ | 45,28 $ – 46,03 $ | +0,40 % |
| 9:50 AM | CAH | 273,40 $ | 269,30 $ – 272,95 $ | +0,17 % |
| 9:50 AM | CDE | 11,48 $ | 11,11 $ – 11,43 $ | +0,52 % |
| 9:50 AM | CHYM | 32,60 $ | 31,63 $ – 32,30 $ | +0,93 % |
| 9:50 AM | CNQ | 44,51 $ | 43,83 $ – 44,34 $ | +0,38 % |
| 9:50 AM | CRK | 11,66 $ | 11,41 $ – 11,64 $ | +0,17 % |
| 9:50 AM | CRM | 192,07 $ | 183,89 $ – 190,50 $ | +0,83 % |
| 9:50 AM | CRSP | 44,47 $ | 42,68 $ – 44,44 $ | +0,07 % |
| 9:50 AM | CTRE | 37,61 $ | 37,18 $ – 37,53 $ | +0,20 % |
| 9:50 AM | CUE | 6,78 $ | 5,56 $ – 6,57 $ | +3,27 % |
| 9:50 AM | CZR | 29,33 $ | 29,24 $ – 29,31 $ | +0,08 % |
| 9:50 AM | DBX | 36,28 $ | 35,15 $ – 36,03 $ | +0,69 % |
| 9:50 AM | DDOG | 169,69 $ | 165,06 $ – 167,98 $ | +1,02 % |
| 9:50 AM | DOX | 41,95 $ | 41,28 $ – 41,86 $ | +0,22 % |
| 9:50 AM | DT | 46,31 $ | 45,52 $ – 46,17 $ | +0,31 % |
| 9:50 AM | EGO | 26,90 $ | 26,01 $ – 26,85 $ | +0,19 % |
| 9:50 AM | EPAM | 162,44 $ | 158,54 $ – 162,36 $ | +0,05 % |

… und 231 weitere in [orb.json](orb.json).

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: **ABBV +4,10 %** · **INSM +14,13 %** · JNJ +2,88 % · KO +1,81 % · **LLY +3,15 %** · **MRNA +7,21 %** · **MSTR -8,12 %** · **SNDK -11,13 %** · UNH +1,73 % · WMT +2,11 %

- 25.11. 07:18 Uhr ET · **SNDK** · [Dow Jones Futures Fall, Techs Dive; Trump Says 'Not Too Late' For U.S. To Take Nvidia Stake](https://finance.yahoo.com/m/d96603c1-fe7f-3bf3-8158-0728b464d469/dow-jones-futures-fall%2C-techs.html?.tsrc=rss) · macro
- 25.11. 07:12 Uhr ET · **SNDK** · [Sandisk (SNDK) Shares Dropped, So What Is Driving Attention Now?](https://finance.yahoo.com/markets/stocks/articles/sandisk-sndk-shares-dropped-driving-121239819.html?.tsrc=rss) · capital
- 25.11. 07:11 Uhr ET · **WMT** · [Market Chatter: Walmart-Backed PhonePe Resumes IPO Process; Seeks Up to $15 Billion in Valuation](https://finance.yahoo.com/markets/stocks/articles/market-chatter-walmart-backed-phonepe-121130205.html?.tsrc=rss) · capital
- 25.11. 06:57 Uhr ET · **ABBV** · [What Could Still Lift AbbVie Stock?](https://www.trefis.com/stock/abbv/articles/628894/what-could-still-lift-abbvie-stock/2026-11-25?.tsrc=rss)
- 25.11. 06:46 Uhr ET · **SNDK** · [Tradr to Launch Six New Leveraged ETFs](https://finance.yahoo.com/markets/options/articles/tradr-launch-six-leveraged-etfs-114600732.html?.tsrc=rss)
- 25.11. 06:21 Uhr ET · **UNH** · [How Much Could You Lose In UNH Stock?](https://www.trefis.com/stock/unh/articles/628754/how-much-could-you-lose-in-unh-stock/2026-11-25?.tsrc=rss)
- 25.11. 06:05 Uhr ET · **MRNA** · [Invesco S&P 500 High Beta (SPHB) Buys $13.4 Million More Bloom Energy on Monday](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-high-beta-110539855.html?.tsrc=rss)
- 25.11. 06:05 Uhr ET · **KO** · [State Street Consumer Staples SPDR (XLP) Adds Walmart and Costco on Nov. 23](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-staples-spdr-110513471.html?.tsrc=rss)
- 25.11. 06:04 Uhr ET · **MRNA** · [What Invesco S&P 500 Equal Weight ETF (RSP) Sold: Moderna Leads on Nov. 23](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-equal-weight-110443601.html?.tsrc=rss)
- 25.11. 06:04 Uhr ET · **SNDK** · [What Direxion Daily Technology Bull 3X ETF (TECL) Sold: Apple Leads on Monday](https://finance.yahoo.com/markets/stocks/articles/direxion-daily-technology-bull-3x-110437163.html?.tsrc=rss)
- 25.11. 06:03 Uhr ET · **ABBV** · [Forget the P/E Ratio. DSTL Picks 100 Large Stocks by the Cash They Generate and the Debt They Don’t Carry](https://247wallst.com/investing/etf/2026/11/25/forget-the-p-e-ratio-dstl-picks-100-large-stocks-by-the-cash-they-generate-and-the-debt-they-dont-carry/?.tsrc=rss)
- 25.11. 05:50 Uhr ET · **INSM** · [International Biotechnology Trust: Sanofi deal highlights accelerating biotech M&A wave](https://finance.yahoo.com/video/international-biotechnology-trust-sanofi-deal-105025941.html?.tsrc=rss) · deal, capital
- 25.11. 05:22 Uhr ET · **MSTR** · [Michael Saylor Bought $100M In Bitcoin Before Strategy Did, Says The Man Who Convinced Him To Buy It — Now That Bet Is Around $589M](https://stocktwits.com/news-articles/markets/equity/michael-saylor-100m-bitcoin-purchase-589m-bet/cNbHOY3R9lH?.tsrc=rss)
- 25.11. 04:43 Uhr ET · **WMT** · [A Walton Beat the IRS in Tax Court in 2000. The Trust She Won With Is How Billionaires Now Pass Stock Gains to Their Kids With No Gift Tax](https://247wallst.com/personal-finance/2026/11/25/a-walton-beat-the-irs-in-tax-court-in-2000-the-trust-she-won-with-is-how-billionaires-now-pass-stock-gains-to-their-kids-with-no-gift-tax/?.tsrc=rss) · legal
- 25.11. 04:25 Uhr ET · **SNDK** · [SanDisk Trades at 4.6x Earnings—And Still Got Cut in Half](https://finance.yahoo.com/markets/stocks/articles/sandisk-trades-4-6x-earnings-092502421.html?.tsrc=rss) · earnings
- 25.11. 04:24 Uhr ET · **UNH** · [Skip insurance whiplash: How this surgical leader climbed 16%](https://finance.yahoo.com/healthcare/articles/skip-insurance-whiplash-surgical-leader-092408778.html?.tsrc=rss)
- 25.11. 04:24 Uhr ET · **KO** · [Up 41% at Just Over Half Costco’s P/E: Inside Coca-Cola’s Quiet Rally](https://finance.yahoo.com/markets/stocks/articles/41-just-over-half-costco-092400539.html?.tsrc=rss)
- 25.11. 04:08 Uhr ET · **MRNA** · [Is Moderna (MRNA) Stock Reasonable After Its Huge Run And Vaccine Data?](https://finance.yahoo.com/markets/stocks/articles/moderna-mrna-stock-reasonable-huge-090844311.html?.tsrc=rss) · earnings
- 25.11. 03:32 Uhr ET · **WMT** · [Walmart’s shopper base is shifting: High earners lead its gains as low-income shoppers turn to Amazon](https://finance.yahoo.com/markets/stocks/articles/walmart-shopper-shifting-high-earners-083200748.html?.tsrc=rss)
- 25.11. 03:27 Uhr ET · **SNDK** · [MU, SKHY, SNDK Stocks In Focus After TrendForce Lowers DRAM Pricing Forecast](https://stocktwits.com/news-articles/markets/equity/mu-skhy-sndk-stocks-in-focus-after-trend-force-lowers-dram-pricing-forecast/cNbH7VLR9l8?.tsrc=rss) · earnings
- 25.11. 00:12 Uhr ET · **WMT** · [Symbotic: 3 Key Takeaways for Long-Term Investors](https://www.fool.com/earnings/takeaways/2026/11/24/symbotic-3-key-takeaways-for-long-term-investors/?.tsrc=rss)
- 24.11. 22:20 Uhr ET · **MSTR** · [Dow, S&P 500, Nasdaq Futures Edge Lower Amid Tech Selloff Ahead Of Key Inflation Data: DELL, AMBA, SOXL, MSTR In Focus](https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-nasdaq-futures-edge-lower-amid-tech-selloff-ahead-of-key-inflation-data-dell-amba-soxl-mstr-in-focus/cNbHbLoR9lJ?.tsrc=rss) · macro
- 24.11. 21:47 Uhr ET · **KO** · [Warren Buffett Finished Buying Coca-Cola in August 1994 and Never Bought Another Share. Under Greg Abel, Berkshire Now Collects $2.3 Million a Day From It](https://247wallst.com/investing/2026/11/24/warren-buffett-finished-buying-coca-cola-in-august-1994-and-never-bought-another-share-under-greg-abel-berkshire-now-collects-2-3-million-a-day-from-it/?.tsrc=rss) · capital
- 24.11. 21:22 Uhr ET · **WMT** · [e.l.f. Beauty vs. Hershey: Which Consumer Goods Stock Is a Better Buy for 2027?](https://www.fool.com/coverage/better-buy/2026/11/24/elf-beauty-vs-hershey-which-consumer-goods-stock-is-a-better-buy-for-2027/?.tsrc=rss)
- 24.11. 21:09 Uhr ET · **MSTR** · [Strategy (MSTR) Stock Trades At A Discount To Book Value](https://finance.yahoo.com/markets/stocks/articles/strategy-mstr-stock-trades-discount-020908385.html?.tsrc=rss)

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

## Labor live – Mi 25.11.2026, Stand 09:50 Uhr ET

431 Aktien beobachtet · 214 Spielgeld-Trades aller Varianten · 171 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 0 | 0 | 0,00 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 3 | 1 | -2,36 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 0 | 0 | 0,00 € |
| Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 0 | 0 | 0,00 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| ERO | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 20,82 $ | 20,62 $ | – | Stopp 9:50 Uhr | -1,18 € |
| DELL | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:50 278,05 $ | 274,02 $ | – | Stopp 9:50 Uhr | -1,52 € |
| PINS | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:50 18,30 $ | 18,21 $ | – | offen, Kurs 18,37 $ | 0,34 € |

## Labor (Testphase, Spielgeld ohne Limit)

960 Aktien · 83 Handelstage · Lerntage Do 30.07.2026 bis Do 15.10.2026 · **Prüftage Fr 16.10.2026 bis Di 24.11.2026** · 80 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 67 | 61 % | +0,83 % | 55,39 € | -78,61 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 67 | 61 % | +0,82 % | 55,05 € | -78,95 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 67 | 61 % | +0,73 % | 48,84 € | -85,16 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 116 | 54 % | +0,37 % | 42,64 € | -189,36 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 116 | 54 % | +0,35 % | 40,78 € | -191,22 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 4× normal | 115 | 53 % | +0,31 % | 35,93 € | -194,07 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 116 | 54 % | +0,29 % | 33,94 € | -198,06 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 2R | 118 | 52 % | +0,23 % | 27,70 € | -208,30 € | möglich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 213 | 51 % | +0,23 % | 49,26 € | -376,74 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 3R | 118 | 52 % | +0,21 % | 25,42 € | -210,57 € | möglich | **ja** |
| 11 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 231 | 50 % | +0,20 % | 46,90 € | -415,10 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 230 | 50 % | +0,19 % | 44,62 € | -415,38 € | möglich | **ja** |

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
