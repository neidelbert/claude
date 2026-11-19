# Trader-Übersicht

Stand: Do 19.11. 13:00 Uhr ET (19:00 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Do 19.11. 10:41 Uhr ET (16:41 Uhr MEZ) | OK – 86 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44507873118)) |
| ORB-Scan | Do 19.11. 10:41 Uhr ET (16:41 Uhr MEZ) | OK – 18 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44507873118)) |
| Labor live | Do 19.11. 13:00 Uhr ET (19:00 Uhr MEZ) | OK – 968 Trades, 398 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/44507873118)) |
| Labor | Mi 18.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 19 von 76 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/44387313646)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Mi 18.11.2026

5.927 Aktien in der Liste · 5.927 Charts geladen · 359 liquide (ab 5 $ und 1.000.000 Aktien) · 358 gescannt · **86 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 14 | DIS, TGT, IBN, CMG, BMRN, CPB, TSCO, PCG |
| `bull_flag` | 18 | INSM, SNY, DAL, CMCSA, AAL, IBN, NCLH, CMG |
| `reclaim_ma20` | 12 | AMD, TTWO, NET, TJX, OKTA, AKAM, TECH, NTSK |
| `oversold` | 43 | NVDA, INTC, UNH, BABA, MSTR, IREN, HOOD, NOW |
| `oversold_bounce` | 4 | DDOG, DT, AESI, FLO |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| NVDA | 150,96 $ | 21,2 | `oversold` |
| AMD | 530,14 $ | 50,4 | `reclaim_ma20` |
| INTC | 54,67 $ | 29,3 | `oversold` |
| UNH | 349,91 $ | 28,6 | `oversold` |
| BABA | 84,37 $ | 24,2 | `oversold` |
| TTWO | 216,61 $ | 53,4 | `reclaim_ma20` |
| INSM | 119,80 $ | 60,9 | `bull_flag` |
| MSTR | 90,32 $ | 24,4 | `oversold` |
| IREN | 15,24 $ | 28,7 | `oversold` |
| NET | 300,91 $ | 49,5 | `reclaim_ma20` |
| HOOD | 69,17 $ | 27,6 | `oversold` |
| DIS | 122,36 $ | 69,5 | `breakout_20d` |
| NOW | 90,59 $ | 25,6 | `oversold` |
| TJX | 140,30 $ | 53,3 | `reclaim_ma20` |
| OKTA | 195,61 $ | 52,5 | `reclaim_ma20` |
| CRM | 190,40 $ | 24,5 | `oversold` |
| TGT | 165,93 $ | 60,1 | `breakout_20d` |
| FCX | 51,45 $ | 26,3 | `oversold` |
| DDOG | 167,11 $ | 27,8 | `oversold`, `oversold_bounce` |
| BA | 162,91 $ | 29,7 | `oversold` |

Alle 86 Treffer: [watchlist.json](watchlist.json)

## ORB-Scan – 2026-11-19 10:43 ET

Quelle: Treffer des Morgen-Scans · 74 nutzbare Charts · **18 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | AESI | 5,66 $ | 5,24 $ – 5,57 $ | +1,62 % |
| 9:50 AM | AKAM | 95,86 $ | 92,11 $ – 95,09 $ | +0,81 % |
| 9:50 AM | AMD | 554,47 $ | 537,09 $ – 552,00 $ | +0,45 % |
| 9:50 AM | BABA | 87,76 $ | 83,25 $ – 87,62 $ | +0,16 % |
| 9:50 AM | BMNR | 16,37 $ | 16,08 $ – 16,33 $ | +0,22 % |
| 9:50 AM | FUTU | 90,07 $ | 85,52 $ – 88,97 $ | +1,24 % |
| 9:50 AM | INTC | 59,15 $ | 57,28 $ – 59,00 $ | +0,25 % |
| 9:50 AM | NTSK | 25,85 $ | 24,25 $ – 25,81 $ | +0,14 % |
| 9:50 AM | SVRA | 5,03 $ | 4,73 $ – 4,91 $ | +2,55 % |
| 9:50 AM | TJX | 139,62 $ | 136,98 $ – 139,40 $ | +0,16 % |
| 9:50 AM | VFC | 20,92 $ | 20,60 $ – 20,81 $ | +0,53 % |
| 9:50 AM | WMG | 33,47 $ | 30,90 $ – 33,23 $ | +0,72 % |
| 9:55 AM | BMRN | 63,58 $ | 61,00 $ – 62,50 $ | +1,73 % |
| 10:05 AM | DT | 47,45 $ | 45,82 $ – 47,33 $ | +0,25 % |
| 10:05 AM | NOW | 93,49 $ | 90,79 $ – 93,32 $ | +0,17 % |
| 10:05 AM | TGT | 168,11 $ | 165,20 $ – 167,77 $ | +0,20 % |
| 10:20 AM | BRBR | 14,52 $ | 13,25 $ – 14,50 $ | +0,10 % |
| 10:20 AM | PCG | 13,84 $ | 13,62 $ – 13,77 $ | +0,50 % |

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: **AMD -7,66 %** · **BABA +3,09 %** · **INSM +15,12 %** · **INTC +3,53 %** · IREN -0,98 % · MSTR -1,75 % · **NET +5,96 %** · NVDA +1,14 % · TTWO -0,90 % · **UNH -4,50 %**

- 19.11. 10:30 Uhr ET · **INTC** · [BC-Most Active Stocks](https://finance.yahoo.com/markets/stocks/articles/bc-most-active-stocks-153021724.html?.tsrc=rss)
- 19.11. 10:29 Uhr ET · **NVDA** · [Apple Stock Polishes Breakout As Nvidia-Led AI Boom Gets Wake-Up Call](https://finance.yahoo.com/m/681ca0c6-76b1-321b-bdd4-bb83acc818fb/apple-stock-polishes-breakout.html?.tsrc=rss)
- 19.11. 10:27 Uhr ET · **NVDA** · [Jensen Huang Stepped Away From Nvidia. The Stock Has Crashed. Instead of Rushing to Buy the Dip, Here Are 2 AI Stocks Down More Than 15% to Buy Instead.](https://www.fool.com/investing/2026/11/19/jensen-huang-stepped-away-from-nvidia-the-stock-has-crashed-instead-of-rushing-to-buy-the-dip-here-are-2-ai-stocks-down-more-than-15-to-buy-instead/?.tsrc=rss)
- 19.11. 10:25 Uhr ET · **INSM** · [Billionaire Druckenmiller’s New AI Warning and Top 10 Stock Picks](https://finance.yahoo.com/markets/stocks/articles/billionaire-druckenmiller-ai-warning-top-152506734.html?.tsrc=rss)
- 19.11. 10:23 Uhr ET · **NVDA** · [Opinion: Trump May Have Finally Killed the AI Trade](https://www.tikr.com/blog/opinion-trump-may-have-finally-killed-the-ai-trade?ref=yahoofinance&tlnk=yf-261119-xjm2c5jx&.tsrc=rss)
- 19.11. 10:23 Uhr ET · **NVDA** · [Why Micron Stock Finally Popped Today](https://www.fool.com/investing/2026/11/19/why-micron-stock-finally-popped-today/?.tsrc=rss)
- 19.11. 10:21 Uhr ET · **MSTR** · [Analysts Turned Bearish on These 5 Stocks on Wednesday](https://finance.yahoo.com/markets/stocks/articles/analysts-turned-bearish-5-stocks-152114314.html?.tsrc=rss)
- 19.11. 10:20 Uhr ET · **NVDA** · [If a Market Correction Is Coming, Here's the Exact 3-Step Strategy I'm Using to Prepare](https://www.fool.com/investing/2026/11/19/if-a-market-correction-is-coming-here-the-exact-3-step-strategy-i-m-using-to-prepare/?.tsrc=rss)
- 19.11. 10:17 Uhr ET · **NVDA** · [What Could Derail Take-Two Stock?](https://www.trefis.com/stock/ttwo/articles/626761/what-could-derail-take-two-stock/2026-11-19?.tsrc=rss)
- 19.11. 10:15 Uhr ET · **INTC** · [Microsoft (MSFT) Secures New AI Chip Supply Deal For Azure Growth](https://finance.yahoo.com/technology/ai/articles/microsoft-msft-secures-ai-chip-151529450.html?.tsrc=rss) · deal
- 19.11. 10:15 Uhr ET · **NVDA** · [Claude crushes it on Wall Street](https://www.axios.com/2026/11/19/anthropic-ipo-claude-crush#utm_source=yahoo_finance&utm_medium=partner&utm_campaign=subs-partner-yahoo-finance-AI?.tsrc=rss)
- 19.11. 10:13 Uhr ET · **NVDA** · [Peter Lynch Made “Growth at a Reasonable Price” Famous. SPGP Runs the S&P 500 Through That Filter and Keeps 75 Stocks](https://247wallst.com/investing/etf/2026/11/19/peter-lynch-made-growth-at-a-reasonable-price-famous-spgp-runs-the-sp-500-through-that-filter-and-keeps-75-stocks/?.tsrc=rss)
- 19.11. 10:10 Uhr ET · **NVDA** · [Anthropic IPO mania: Could it be the biggest public debut ever?](https://finance.yahoo.com/video/anthropic-ipo-mania-could-it-be-the-biggest-public-debut-ever-151001594.html?.tsrc=rss) · capital
- 19.11. 10:08 Uhr ET · **NVDA** · [Some Fed Officials Wanted to Hike in October. A Half-Point Hike Is on the Table.](https://247wallst.com/investing/2026/11/19/some-fed-officials-wanted-to-hike-in-october-a-half-point-hike-is-on-the-table/?.tsrc=rss) · macro
- 19.11. 10:07 Uhr ET · **NET** · [Palo Alto Networks soars on Q1 earnings and Applied Compute deal](https://finance.yahoo.com/markets/stocks/article/palo-alto-networks-soars-on-q1-earnings-and-applied-compute-deal-150705343.html?.tsrc=rss) · earnings, deal
- 19.11. 10:06 Uhr ET · **NVDA** · [Nvidia’s earnings beat fails to lift chip sector as macro and policy risks weigh](https://finance.yahoo.com/markets/stocks/articles/nvidia-earnings-beat-fails-lift-150623941.html?.tsrc=rss) · earnings
- 19.11. 10:06 Uhr ET · **NVDA** · [AI giant Anthropic shares set to trade after record-breaking IPO](https://finance.yahoo.com/technology/ai/articles/anthropic-set-price-ipo-key-030309911.html?.tsrc=rss) · capital, people
- 19.11. 10:06 Uhr ET · **NVDA** · [I’m Buying Anthropic Stock, Just Not on Day 1. Here’s My Plan.](https://www.fool.com/investing/2026/11/19/i-m-buying-anthropic-stock-just-not-on-day-1-here-s-my-plan/?.tsrc=rss)
- 19.11. 10:05 Uhr ET · **NVDA** · [“Like Kicking Michael Jordan Off Your Team.” Elon Musk Blasts Nvidia Board’s Actions](https://247wallst.com/investing/2026/11/19/like-kicking-michael-jordan-off-your-team-elon-musk-blasts-nvidia-boards-actions/?.tsrc=rss)
- 19.11. 10:01 Uhr ET · **INTC** · [Intel Soars 8% on First Outside 18A Customer as CEO Says “I Just Cannot Supply Enough”](https://www.tikr.com/blog/intel-soars-8-on-first-outside-18a-customer-as-ceo-says-i-just-cannot-supply-enough?ref=yahoofinance&tlnk=yf-261119-f6cmv7fm&.tsrc=rss) · people
- 19.11. 10:01 Uhr ET · **INTC** · [Connected Logistics - Global Strategic Business Report 2026: Capitalize on a $100.8 Billion Market by 2032 with Cisco, IBM, SAP, Intel, and AT&T](https://finance.yahoo.com/technology/articles/connected-logistics-global-strategic-business-150100808.html?.tsrc=rss) · capital
- 19.11. 09:56 Uhr ET · **AMD** · [Intel Climbs 7% on First 18A Customer, NVIDIA Gains 4% as Trump Floats Blackwell Sales to China and Dan Ives Hails Anthropic IPO; AMD Rises 3%](https://247wallst.com/investing/2026/11/19/intel-climbs-7-on-first-18a-customer-nvidia-gains-4-as-trump-floats-blackwell-sales-to-china-and-dan-ives-hails-anthropic-ipo-amd-rises-3/?.tsrc=rss) · deal
- 19.11. 09:54 Uhr ET · **AMD** · [Anthropic’s IPO puts AI’s circular financing boom to the test](https://finance.yahoo.com/technology/ai/articles/anthropic-ipo-puts-ai-circular-145439533.html?.tsrc=rss)
- 19.11. 09:54 Uhr ET · **BABA** · [Anthropic IPO gives boost to AI trade: AlphaCheck](https://finance.yahoo.com/markets/article/ai-trade-soars-with-anthropic-ipo-in-spotlight-alphacheck-145421789.html?.tsrc=rss)
- 19.11. 09:51 Uhr ET · **MSTR** · [Strategy Stock Lives and Dies by Bitcoin. The Crypto’s Slump Takes a Toll.](https://finance.yahoo.com/m/cd85da47-be7b-3609-83c8-4365ba2c6453/strategy-stock-lives-and-dies.html?.tsrc=rss) · analyst

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

## Labor live – Do 19.11.2026, Stand 13:00 Uhr ET

224 Aktien beobachtet · 968 Spielgeld-Trades aller Varianten · 398 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 2 | 2 | -0,57 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 2 | 2 | -0,57 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 2 | 2 | -0,57 € |
| Ausbruch 30 Min · nur Top 10 nach Volumen · Stopp Tief der Spanne · Ziel 1,5R | 1 | 1 | -3,85 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 8 | 0 | -7,65 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | -3,85 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 0 | 0 | 0,00 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| CRWD | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 254,13 $ | 252,62 $ | – | Stopp 9:40 Uhr | -1,22 € |
| NET | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 320,07 $ | 317,73 $ | – | Stopp 9:40 Uhr | -0,89 € |
| OKTA | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 211,99 $ | 210,51 $ | – | Stopp 9:40 Uhr | -1,28 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 90,69 $ | offen, Kurs 86,06 $ | 0,62 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 92,42 $ | offen, Kurs 86,06 $ | 0,62 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 95,89 $ | offen, Kurs 86,06 $ | 0,62 € |
| SNOW | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 295,72 $ | 294,05 $ | – | Stopp 9:40 Uhr | -0,84 € |
| ZS | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 214,04 $ | 212,81 $ | – | Stopp 9:45 Uhr | -0,62 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 27,58 $ | offen, Kurs 25,29 $ | -1,19 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 28,25 $ | offen, Kurs 25,29 $ | -1,19 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 29,58 $ | offen, Kurs 25,29 $ | -1,19 € |
| NTSK | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 25,49 $ | 25,30 $ | – | Stopp 11:55 Uhr | -0,79 € |
| SAIL | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 23,03 $ | 22,90 $ | – | Stopp 9:55 Uhr | -0,64 € |
| USAR | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 7,12 $ | 7,03 $ | – | Stopp 10:10 Uhr | -1,37 € |
| NTSK | Opening-Range-Ausbruch 30 Min | 10:05 26,29 $ | 24,25 $ | 30,36 $ | offen, Kurs 25,29 $ | -3,85 € |
| NTSK | Ausbruch 30 Min | 10:05 26,29 $ | 24,25 $ | 29,35 $ | offen, Kurs 25,29 $ | -3,85 € |

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
