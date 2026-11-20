# Trader-Übersicht

Stand: Fr 20.11. 07:33 Uhr ET (13:33 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: vor der Eröffnung (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Fr 20.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 260 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44689475493)) |
| ORB-Scan | Do 19.11. 10:41 Uhr ET (16:41 Uhr MEZ) | OK – 18 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44507873118)) |
| Labor live | Do 19.11. 16:00 Uhr ET (22:00 Uhr MEZ) | OK – Tagesbilanz: 968 Trades ([Lauf](https://github.com/neidelbert/claude/actions/runs/44604811557)) |
| Labor | Do 19.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 16 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/44604811557)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Do 19.11.2026

5.927 Aktien in der Liste · 5.927 Charts geladen · 1.503 liquide (ab 5 $ und 1.000.000 Aktien) · 1.502 gescannt · **260 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 20 | INSM, PDD, TGT, GME, PCG, VVV, TU, IBN |
| `bull_flag` | 52 | TMUS, CMCSA, CAH, MDLN, RKT, CMG, EW, HDB |
| `reclaim_ma20` | 17 | PANW, CRWD, COHR, PDD, UTZ, VVV, S, NRG |
| `oversold` | 160 | NVDA, GOOG, UNH, CAT, MSTR, NOW, BABA, HOOD |
| `oversold_bounce` | 30 | INTC, NTRA, AXON, FSLR, ASTS, NLY, FUTU, USAR |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| NVDA | 145,98 $ | 19,8 | `oversold` |
| GOOG | 271,02 $ | 29,6 | `oversold` |
| INTC | 55,72 $ | 31,1 | `oversold_bounce` |
| PANW | 361,73 $ | 54,5 | `reclaim_ma20` |
| UNH | 330,48 $ | 24,3 | `oversold` |
| CRWD | 243,46 $ | 53,6 | `reclaim_ma20` |
| COHR | 214,94 $ | 45,8 | `reclaim_ma20` |
| CAT | 537,37 $ | 27,0 | `oversold` |
| INSM | 144,46 $ | 77,4 | `breakout_20d` |
| MSTR | 86,13 $ | 22,9 | `oversold` |
| PDD | 86,00 $ | 63,8 | `breakout_20d`, `reclaim_ma20` |
| NOW | 88,87 $ | 24,8 | `oversold` |
| BABA | 83,31 $ | 23,3 | `oversold` |
| HOOD | 68,65 $ | 27,3 | `oversold` |
| IREN | 14,41 $ | 27,6 | `oversold` |
| CRM | 183,31 $ | 22,0 | `oversold` |
| SNDK | 94,39 $ | 29,1 | `oversold` |
| FCX | 49,12 $ | 23,8 | `oversold` |
| COF | 181,76 $ | 28,1 | `oversold` |
| BA | 160,51 $ | 27,9 | `oversold` |

Alle 260 Treffer: [watchlist.json](watchlist.json)

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

Bewegung seit gestern: **CAT -3,83 %** · COHR +0,99 % · CRWD +2,71 % · GOOG -2,93 % · **INSM +20,58 %** · INTC +1,92 % · **MSTR -4,64 %** · **NVDA -3,30 %** · **PANW +6,42 %** · **UNH -5,55 %**

- 20.11. 07:24 Uhr ET · **CRWD** · [Dow Jones Futures: Techs Tumble, Anthropic Dives After Ugly Market Reversal To New Lows](https://finance.yahoo.com/m/9e02231d-41cd-31ac-b37f-993325b8a4ca/dow-jones-futures%3A-techs.html?.tsrc=rss) · macro
- 20.11. 07:20 Uhr ET · **NVDA** · [Nasdaq Futures Slide, Anthropic Shares Reverse IPO Gains — LITE, IREN, SNDK, NVDA In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-futures-slide-anthropic-shares-reverse-ipo-gains-lite-iren-sndk-nvda-in-focus/cNbSL5RR9Ks?.tsrc=rss) · macro
- 20.11. 07:18 Uhr ET · **GOOG** · ['Miserable 7' Stocks Shed Whopping $4 Trillion In Value Overnight](https://finance.yahoo.com/m/6e6f9c49-9658-3615-8008-22c4188b1bd6/%27miserable-7%27-stocks-shed.html?.tsrc=rss)
- 20.11. 07:15 Uhr ET · **NVDA** · [Buy Broadcom Now: Get a $115 Billion AI Giant at Just 18.5x Forward Earnings](https://247wallst.com/investing/2026/11/20/buy-broadcom-now-get-a-115-billion-ai-giant-at-just-18-5x-forward-earnings/?.tsrc=rss) · earnings
- 20.11. 07:15 Uhr ET · **MSTR** · [Strategy Tumbles 37% in a Month: This Wall Street Pro Predicts 400% Gains on Its Bitcoin Exposure](https://247wallst.com/investing/2026/11/20/strategy-tumbles-37-in-a-month-this-wall-street-pro-predicts-400-gains-on-its-bitcoin-exposure/?.tsrc=rss)
- 20.11. 07:15 Uhr ET · **GOOG** · [Stanley Druckenmiller dumps Google stock in a bid to ‘not lose money’ as the outlook darkens. Here’s what he’s buying](https://finance.yahoo.com/markets/stocks/articles/stanley-druckenmiller-dumps-google-stock-121500032.html?.tsrc=rss)
- 20.11. 07:13 Uhr ET · **INTC** · [AMD Stock Drops Another 7% Before the Bell and Taiwan Semiconductor Slides 4.2% as Nasdaq Futures Fall 1.6% After Asia’s Chip Selloff](https://247wallst.com/investing/2026/11/20/amd-stock-drops-another-7-0-before-the-bell-and-taiwan-semiconductor-slides-4-2-as-nasdaq-futures-fall-1-6-after-asias-chip-selloff/?.tsrc=rss) · macro
- 20.11. 07:11 Uhr ET · **NVDA** · [3 Funds Riding Anthropic IPO Optimism Through Very Different Chip Bets](https://finance.yahoo.com/technology/articles/3-funds-riding-anthropic-ipo-121139010.html?.tsrc=rss)
- 20.11. 07:05 Uhr ET · **NVDA** · [3 Magnificent AI Chip Stocks That Could Help Set You Up for Life](https://www.fool.com/investing/2026/11/20/3-magnificent-ai-chip-stocks-that-could-help-set-you-up-for-life/?.tsrc=rss)
- 20.11. 07:01 Uhr ET · **NVDA** · [SpaceX Raises $32 Billion in Debt to Buy Nvidia Chips](https://finance.yahoo.com/markets/stocks/articles/spacex-raises-32-billion-debt-120100540.html?.tsrc=rss)
- 20.11. 07:00 Uhr ET · **NVDA** · [SpaceX's 8.26% Bond Yield Reveals the Cost of the AI Boom](https://finance.yahoo.com/technology/ai/articles/spacexs-8-26-bond-yield-120052825.html?.tsrc=rss)
- 20.11. 07:00 Uhr ET · **GOOG** · [OpenAI tried to ruin Anthropic's IPO. It backfired.](https://finance.yahoo.com/video/openai-tried-ruin-anthropics-ipo-120000298.html?.tsrc=rss)
- 20.11. 06:59 Uhr ET · **GOOG** · [Nvidia, Google and Amazon Back Anthropic as Founders Cash Out Nearly $2 Billion](https://finance.yahoo.com/technology/ai/articles/nvidia-google-amazon-back-anthropic-115953506.html?.tsrc=rss)
- 20.11. 06:58 Uhr ET · **NVDA** · [Jensen Huang Pledges $350 Million to Nvidia-Backed CoreWeave](https://finance.yahoo.com/technology/ai/articles/jensen-huang-pledges-350-million-115855482.html?.tsrc=rss)
- 20.11. 06:57 Uhr ET · **INTC** · [Can Intel Stock Jump 30%?](https://www.trefis.com/stock/intc/articles/627242/can-intel-stock-jump-30-2/2026-11-20?.tsrc=rss)
- 20.11. 06:53 Uhr ET · **INSM** · [What Is Behind The Move In Insmed Stock?](https://www.trefis.com/stock/insm/articles/627318/what-is-behind-the-move-in-insmed-stock/2026-11-20?.tsrc=rss)
- 20.11. 06:50 Uhr ET · **NVDA** · [Jensen Huang's Sudden Resignation Has Created a Flash Sale For These 3 AI Stocks](https://www.fool.com/investing/2026/11/20/jensen-huang-sudden-resignation-created-flash-sale-ai-stocks/?.tsrc=rss) · people
- 20.11. 06:40 Uhr ET · **NVDA** · [If You Had Invested $5,000 in Amazon Stock 20 Years Ago, Here's How Much You'd Have Today](https://www.fool.com/investing/2026/11/20/if-youd-invested-5000-in-company-name-stock-20-years-ago-heres-how-much-youd-have-today/?.tsrc=rss)
- 20.11. 06:37 Uhr ET · **UNH** · [TD Cowen Names UnitedHealth Its 2027 Best Idea —  Why Analyst Sees Mid-To-High-Teens EPS Growth For UNH Stock](https://stocktwits.com/news-articles/markets/equity/td-cowen-names-united-health-its-2027-best-idea-why-analyst-sees-mid-to-high-teens-eps-growth-for-unh-stock/cNbSgzzR9KA?.tsrc=rss) · earnings, analyst
- 20.11. 06:37 Uhr ET · **NVDA** · [AI Chips Today - AI Revolution Drives VR and AR Market Expansion](https://finance.yahoo.com/technology/ai/articles/ai-chips-today-ai-revolution-113737070.html?.tsrc=rss)
- 20.11. 06:36 Uhr ET · **NVDA** · [CoreWeave Gains $350 Million Computing Commitment as Debt Concerns Persist](https://finance.yahoo.com/technology/ai/articles/coreweave-gains-350-million-computing-113603215.html?.tsrc=rss)
- 20.11. 06:36 Uhr ET · **NVDA** · [These 3 ETFs Could Set You Up for Life With Next to No Effort on Your Part](https://www.fool.com/investing/2026/11/20/these-3-etfs-could-set-you-up-for-life-with-next-to-no-effort-on-your-part/?.tsrc=rss)
- 20.11. 06:35 Uhr ET · **NVDA** · [“The Open Checkbook Is Over.” Nebius, Backed by $2 Billion From Nvidia, Stands to Gain](https://www.tikr.com/blog/the-open-checkbook-is-over-nebius-backed-by-2-billion-from-nvidia-stands-to-gain?ref=yahoofinance&tlnk=yf-261120-x7v3x99j&.tsrc=rss)
- 20.11. 06:35 Uhr ET · **NVDA** · [If a Bear Market Is Coming in 2027, History Says This 1 Simple Move Can Protect Your Investments](https://www.fool.com/investing/2026/11/20/if-a-bear-market-is-coming-in-2027-history-says-this-1-simple-move-can-protect-your-investments/?.tsrc=rss)
- 20.11. 06:32 Uhr ET · **GOOG** · [Social Buzz: Wallstreetbets Stocks Mostly Lower Pre-Bell Friday; Sandisk, AMD to Decline](https://finance.yahoo.com/markets/stocks/articles/social-buzz-wallstreetbets-stocks-mostly-113227780.html?.tsrc=rss)

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

## Labor live – Do 19.11.2026, Stand 16:00 Uhr ET

224 Aktien beobachtet · 968 Spielgeld-Trades aller Varianten · 0 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 2 | 0 | -2,21 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 2 | 0 | -2,21 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 2 | 0 | -2,21 € |
| Ausbruch 30 Min · nur Top 10 nach Volumen · Stopp Tief der Spanne · Ziel 1,5R | 1 | 0 | -5,20 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 8 | 0 | -7,65 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 0 | -5,20 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 0 | 0 | 0,00 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| CRWD | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 254,13 $ | 252,62 $ | – | Stopp 9:40 Uhr | -1,22 € |
| NET | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 320,07 $ | 317,73 $ | – | Stopp 9:40 Uhr | -0,89 € |
| OKTA | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 211,99 $ | 210,51 $ | – | Stopp 9:40 Uhr | -1,28 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 90,69 $ | Schluss 15:55 Uhr | 0,37 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 92,42 $ | Schluss 15:55 Uhr | 0,37 € |
| PDD | News-Sprung: Lücke ≥ 4 % | 9:40 85,49 $ | 82,02 $ | 95,89 $ | Schluss 15:55 Uhr | 0,37 € |
| SNOW | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 295,72 $ | 294,05 $ | – | Stopp 9:40 Uhr | -0,84 € |
| ZS | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:40 214,04 $ | 212,81 $ | – | Stopp 9:45 Uhr | -0,62 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 27,58 $ | Schluss 15:55 Uhr | -2,58 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 28,25 $ | Schluss 15:55 Uhr | -2,58 € |
| NTSK | News-Sprung: Lücke ≥ 4 % | 9:45 25,58 $ | 24,25 $ | 29,58 $ | Schluss 15:55 Uhr | -2,58 € |
| NTSK | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 25,49 $ | 25,30 $ | – | Stopp 11:55 Uhr | -0,79 € |
| SAIL | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 23,03 $ | 22,90 $ | – | Stopp 9:55 Uhr | -0,64 € |
| USAR | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:45 7,12 $ | 7,03 $ | – | Stopp 10:10 Uhr | -1,37 € |
| NTSK | Opening-Range-Ausbruch 30 Min | 10:05 26,29 $ | 24,25 $ | 30,36 $ | Schluss 15:55 Uhr | -5,20 € |
| NTSK | Ausbruch 30 Min | 10:05 26,29 $ | 24,25 $ | 29,35 $ | Schluss 15:55 Uhr | -5,20 € |

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
