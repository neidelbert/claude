# Trader-Übersicht

Stand: Do 19.11. 10:00 Uhr ET (16:00 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Do 19.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 410 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44466796616)) |
| ORB-Scan | Mi 28.10. 10:10 Uhr ET (15:10 Uhr MEZ) | OK – 163 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40689559352)) |
| Labor live | Do 19.11. 10:00 Uhr ET (16:00 Uhr MEZ) | OK – 688 Trades, 566 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/44466796616)) |
| Labor | Mi 18.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 19 von 76 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/44387313646)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Mi 18.11.2026

5.926 Aktien in der Liste · 5.925 Charts geladen · 1.471 liquide (ab 5 $ und 1.000.000 Aktien) · 1.470 gescannt · **410 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 77 | DIS, TGT, VIK, TSCO, ORLY, CMG, SN, FROG |
| `bull_flag` | 139 | LLY, COST, HD, HWM, LOW, GE, TMUS, SHW |
| `reclaim_ma20` | 67 | AMD, TTWO, TJX, NET, OKTA, UNP, HON, AKAM |
| `oversold` | 133 | NVDA, UNH, INTC, MSTR, CAT, CRM, NOW, FCX |
| `oversold_bounce` | 31 | DDOG, NTRA, AXON, DT, CRSP, ARWR, NTNX, IONS |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| NVDA | 150,96 $ | 21,2 | `oversold` |
| AMD | 530,14 $ | 50,4 | `reclaim_ma20` |
| UNH | 349,91 $ | 28,6 | `oversold` |
| INTC | 54,67 $ | 29,3 | `oversold` |
| LLY | 1.382,75 $ | 55,6 | `bull_flag` |
| TTWO | 216,61 $ | 53,4 | `reclaim_ma20` |
| TJX | 140,30 $ | 53,3 | `reclaim_ma20` |
| COST | 1.096,62 $ | 68,9 | `bull_flag` |
| MSTR | 90,32 $ | 24,4 | `oversold` |
| DIS | 122,36 $ | 69,5 | `breakout_20d` |
| TGT | 165,93 $ | 60,1 | `breakout_20d` |
| CAT | 558,77 $ | 29,7 | `oversold` |
| CRM | 190,40 $ | 24,5 | `oversold` |
| NOW | 90,59 $ | 25,6 | `oversold` |
| HD | 337,64 $ | 53,9 | `bull_flag` |
| FCX | 51,45 $ | 26,3 | `oversold` |
| BABA | 84,37 $ | 24,2 | `oversold` |
| IREN | 15,24 $ | 28,7 | `oversold` |
| COF | 184,30 $ | 29,9 | `oversold` |
| HWM | 221,15 $ | 53,4 | `bull_flag` |

Alle 410 Treffer: [watchlist.json](watchlist.json)

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

Bewegung seit gestern: **AMD +5,31 %** · COST -1,21 % · **DIS +4,63 %** · INTC -0,91 % · LLY -2,32 % · **MSTR -6,40 %** · NVDA -2,89 % · **TJX +8,05 %** · **TTWO +6,22 %** · **UNH -10,21 %**

- 19.11. 07:27 Uhr ET · **NVDA** · [President Trump Just Delivered Good News for Nvidia Stock Investors](https://finance.yahoo.com/markets/stocks/articles/president-trump-just-delivered-good-122719225.html?.tsrc=rss)
- 19.11. 07:25 Uhr ET · **UNH** · [UnitedHealth Shares Sink as New Federal Fraud Crackdown Sparks Healthcare Sell-Off](https://finance.yahoo.com/healthcare/articles/unitedhealth-shares-sink-federal-fraud-122529002.html?.tsrc=rss)
- 19.11. 07:23 Uhr ET · **NVDA** · [Dow Jones Futures Rise, Techs Jump 2%: Anthropic To Debut After Record IPO; Palo Alto, Everpure Rally, Walmart Beats](https://finance.yahoo.com/m/107e5a2c-4fba-3df3-b2fd-5d1160e65516/dow-jones-futures-rise%2C-techs.html?.tsrc=rss) · macro
- 19.11. 07:22 Uhr ET · **AMD** · [OpenAI Says Its AI Improved AMD’s Best Chip Design by Up to 14%](https://247wallst.com/investing/2026/11/19/openai-says-its-ai-improved-amds-best-chip-design-by-up-to-14/?.tsrc=rss)
- 19.11. 07:16 Uhr ET · **NVDA** · [TJX Beat Its Own Sales Forecast With 4% Comparable Growth, but Management Is Bracing for a Slower Holiday Quarter.](https://www.fool.com/investing/2026/11/19/tjx-beat-its-own-sales-forecast-with-4-comparable-growth-but-management-is-bracing-for-a-slower-holiday-quarter/?.tsrc=rss) · earnings
- 19.11. 07:15 Uhr ET · **NVDA** · [Stalemates over semiconductors and rare earth minerals appear little changed as Trump heads home from China](https://finance.yahoo.com/markets/article/stalemates-over-semiconductors-and-rare-earth-minerals-appear-little-changed-as-trump-heads-home-from-china-121555352.html?.tsrc=rss)
- 19.11. 07:15 Uhr ET · **NVDA** · [IonQ Has a $3.7 Billion Runway That Could Send Prices to $65 or Higher in 2027](https://247wallst.com/investing/2026/11/19/ionq-has-a-3-7-billion-runway-that-could-send-prices-to-65-or-higher-in-2027/?.tsrc=rss)
- 19.11. 07:15 Uhr ET · **AMD** · [Why Did David Tepper Exit AMD and Open a $172M Oracle Position? Here’s What May Have Driven the Shift](https://247wallst.com/investing/2026/11/19/why-did-david-tepper-exit-amd-and-open-a-172m-oracle-position-heres-what-may-have-driven-the-shift/?.tsrc=rss)
- 19.11. 07:14 Uhr ET · **AMD** · [Advanced Micro Devices (AMD) Closes $8.2 Billion World Labs Acquisition](https://finance.yahoo.com/technology/ai/articles/advanced-micro-devices-amd-closes-121439912.html?.tsrc=rss) · deal
- 19.11. 07:12 Uhr ET · **AMD** · [Anthropic Tops SpaceX For The Biggest IPO Ever](https://finance.yahoo.com/markets/stocks/articles/anthropic-tops-spacex-biggest-ipo-121239477.html?.tsrc=rss)
- 19.11. 07:08 Uhr ET · **LLY** · [Which Dates Could Move Bristol Myers Squibb Stock Most?](https://www.trefis.com/stock/bmy/articles/626791/which-dates-could-move-bristol-myers-squibb-stock-most/2026-11-19?.tsrc=rss)
- 19.11. 07:08 Uhr ET · **NVDA** · [History Says a Bear Market Is Coming. Here's Exactly How I'm Preparing.](https://www.fool.com/investing/2026/11/19/history-says-a-bear-market-is-coming-heres-exactly-how-im-preparing/?.tsrc=rss)
- 19.11. 07:04 Uhr ET · **NVDA** · [Dan Ives Says Anthropic IPO Is ‘A Big Win For The Tech Sector’ After ‘A White Knuckle Time With Nvidia’](https://stocktwits.com/news-articles/markets/equity/dan-ives-says-anthropic-ipo-big-win-for-the-tech-sector-after-a-white-knuckle-time-with-nvidia/cNbielNR9iz?.tsrc=rss) · earnings
- 19.11. 07:02 Uhr ET · **NVDA** · [Moody’s Says Jensen Huang’s Exit Is “Credit Negative” for Nvidia](https://247wallst.com/investing/2026/11/19/moodys-says-jensen-huangs-exit-is-credit-negative-for-nvidia/?.tsrc=rss) · analyst, people
- 19.11. 07:00 Uhr ET · **AMD** · [NexusIgnite Plans Sovereign AI Cloud in Jordan, Starting With Its Universities](https://finance.yahoo.com/technology/ai/articles/nexusignite-plans-sovereign-ai-cloud-120000648.html?.tsrc=rss)
- 19.11. 07:00 Uhr ET · **NVDA** · [Everything you need to know about the Anthropic IPO](https://finance.yahoo.com/video/everything-know-anthropic-ipo-120000799.html?.tsrc=rss)
- 19.11. 07:00 Uhr ET · **TTWO** · [GTA VI: Why the 13-year wait could be worth $8 billion](https://finance.yahoo.com/video/gta-vi-why-13-wait-120000877.html?.tsrc=rss)
- 19.11. 07:00 Uhr ET · **TTWO** · [Rockstar Games Announces Grand Theft Auto VI Now Available](https://finance.yahoo.com/technology/articles/rockstar-games-announces-grand-theft-120000642.html?.tsrc=rss)
- 19.11. 06:54 Uhr ET · **NVDA** · [The Biggest Investing Lesson I Learned From My First Bear Market](https://www.fool.com/investing/2026/11/19/the-biggest-investing-lesson-i-learned-from-my-first-bear-market/?.tsrc=rss)
- 19.11. 06:51 Uhr ET · **DIS** · [What Are Netflix Stock Bears Missing?](https://www.trefis.com/stock/nflx/articles/626821/what-are-netflix-stock-bears-missing/2026-11-19?.tsrc=rss)
- 19.11. 06:47 Uhr ET · **DIS** · [Netflix Is 48% Below Its High While Guiding to Record Revenue of $51.1 Billion, Up 13%, for 2026](https://www.tikr.com/blog/netflix-is-48-below-its-high-while-guiding-to-record-revenue-of-51-1-billion-up-13-for-2026?ref=yahoofinance&tlnk=yf-261119-c55xxvxf&.tsrc=rss)
- 19.11. 06:47 Uhr ET · **AMD** · [Dividend Stocks Or AI Stocks: Which Fits Now?](https://www.trefis.com/stock/smh/articles/626520/dividend-stocks-or-ai-stocks-which-fits-now/2026-11-19?.tsrc=rss) · capital
- 19.11. 06:43 Uhr ET · **NVDA** · [How Much Gold Should A $1 Million Portfolio Own?](https://www.trefis.com/stock/gld/articles/624818/how-much-gold-should-a-1-million-portfolio-own/2026-11-19?.tsrc=rss)
- 19.11. 06:35 Uhr ET · **NVDA** · [Jim Cramer Isn't Buying SpaceX Stock Yet. Cathie Wood Keeps Buying. Here’s Who’s Right.](https://www.fool.com/investing/2026/11/19/jim-cramer-not-buying-spacex-stock-cathie-wood-buying-who-is-right/?.tsrc=rss)
- 19.11. 06:32 Uhr ET · **NVDA** · [This "Unstoppable" Cryptocurrency Is Ready to Deliver Massive Gains in 2027](https://www.fool.com/investing/2026/11/19/this-unstoppable-cryptocurrency-is-ready-to-deliver-massive-gains-in-2027/?.tsrc=rss)

## Pelosi-Tracker (pelosi)

- Fr 06.11.2026 · Hon. Nancy Pelosi (CA11) · [PDF](https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2026/20035780.pdf)

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

## Labor live – Do 19.11.2026, Stand 10:00 Uhr ET

421 Aktien beobachtet · 688 Spielgeld-Trades aller Varianten · 566 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 2 | 2 | 2,05 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 2 | 2 | 2,05 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 2 | 2 | 2,05 € |
| Ausbruch 30 Min · nur Top 10 nach Volumen · Stopp Tief der Spanne · Ziel 1,5R | 0 | 0 | 0,00 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 8 | 3 | -1,08 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 0 | 0 | 0,00 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| CRWD | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 254,13 $ | 252,62 $ | – | Stopp 9:40 Uhr | -1,22 € |
| OKTA | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 211,99 $ | 210,51 $ | – | Stopp 9:40 Uhr | -1,28 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 90,69 $ | offen, Kurs 86,40 $ | 1,02 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 92,42 $ | offen, Kurs 86,40 $ | 1,02 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 95,89 $ | offen, Kurs 86,40 $ | 1,02 € |
| SNOW | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 295,72 $ | 294,05 $ | – | Stopp 9:40 Uhr | -0,84 € |
| ZS | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 214,04 $ | 212,81 $ | – | Stopp 9:45 Uhr | -0,62 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 27,58 $ | offen, Kurs 25,86 $ | 1,03 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 28,25 $ | offen, Kurs 25,86 $ | 1,03 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 29,58 $ | offen, Kurs 25,86 $ | 1,03 € |
| NTSK | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 25,49 $ | 25,30 $ | – | offen, Kurs 25,86 $ | 1,39 € |
| SAIL | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 23,03 $ | 22,90 $ | – | Stopp 9:55 Uhr | -0,64 € |
| USAR | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 7,12 $ | 7,03 $ | – | offen, Kurs 7,23 $ | 1,47 € |
| NTRA | Stocks in Play (Studie): Top 20 nach Startvolumen | 10:00 300,62 $ | 298,95 $ | – | offen, Kurs 302,75 $ | 0,66 € |

## Labor (Testphase, Spielgeld ohne Limit)

697 Aktien · 79 Handelstage · Lerntage Do 30.07.2026 bis Di 13.10.2026 · **Prüftage Mi 14.10.2026 bis Mi 18.11.2026** · 76 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 37 | 62 % | +1,49 % | 55,22 € | -18,78 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 37 | 62 % | +1,29 % | 47,76 € | -26,24 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 37 | 62 % | +1,09 % | 40,46 € | -33,54 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 50 | 56 % | +0,94 % | 47,16 € | -52,84 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 4× normal | 66 | 56 % | +0,78 % | 51,55 € | -80,45 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 50 | 56 % | +0,76 % | 37,73 € | -62,27 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 3R | 68 | 54 % | +0,70 % | 47,78 € | -88,22 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 118 | 54 % | +0,65 % | 76,56 € | -159,44 € | unwahrscheinlich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 124 | 53 % | +0,64 % | 79,45 € | -168,55 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 2R | 68 | 54 % | +0,63 % | 42,93 € | -93,07 € | möglich | **ja** |
| 11 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 50 | 56 % | +0,59 % | 29,46 € | -70,54 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 123 | 54 % | +0,57 % | 70,72 € | -175,28 € | möglich | **ja** |

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
