# Trader-Übersicht

Stand: Fr 20.11. 10:51 Uhr ET (16:51 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Fr 20.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 260 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44689475493)) |
| ORB-Scan | Fr 20.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 134 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/44689475493)) |
| Labor live | Fr 20.11. 10:50 Uhr ET (16:50 Uhr MEZ) | OK – 3.118 Trades, 2.141 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/44689475493)) |
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

## ORB-Scan – 2026-11-20 10:10 ET

Quelle: Treffer des Morgen-Scans · 240 nutzbare Charts · **134 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | BABA | 84,08 $ | 82,98 $ – 84,07 $ | +0,01 % |
| 9:50 AM | BBAR | 9,05 $ | 8,81 $ – 9,03 $ | +0,17 % |
| 9:50 AM | BHP | 68,98 $ | 67,86 $ – 68,69 $ | +0,42 % |
| 9:50 AM | CAT | 533,66 $ | 524,50 $ – 529,63 $ | +0,76 % |
| 9:50 AM | CLM | 5,31 $ | 5,20 $ – 5,28 $ | +0,47 % |
| 9:50 AM | CLMT | 30,71 $ | 30,15 $ – 30,64 $ | +0,23 % |
| 9:50 AM | CMI | 419,57 $ | 412,05 $ – 418,94 $ | +0,15 % |
| 9:50 AM | CNQ | 44,70 $ | 44,09 $ – 44,61 $ | +0,20 % |
| 9:50 AM | DD | 150,58 $ | 147,84 $ – 150,56 $ | +0,01 % |
| 9:50 AM | DLB | 57,58 $ | 54,39 $ – 57,14 $ | +0,78 % |
| 9:50 AM | IE | 5,70 $ | 5,55 $ – 5,70 $ | +0,09 % |
| 9:50 AM | INSM | 149,10 $ | 142,42 $ – 147,47 $ | +1,11 % |
| 9:50 AM | INTC | 54,78 $ | 53,48 $ – 54,48 $ | +0,55 % |
| 9:50 AM | KMT | 22,17 $ | 21,92 $ – 22,12 $ | +0,18 % |
| 9:50 AM | LNTH | 102,32 $ | 102,08 $ – 102,21 $ | +0,11 % |
| 9:50 AM | LQDT | 32,92 $ | 32,24 $ – 32,87 $ | +0,18 % |
| 9:50 AM | MAGN | 13,00 $ | 12,31 $ – 12,82 $ | +1,40 % |
| 9:50 AM | MDLN | 38,24 $ | 37,44 $ – 38,22 $ | +0,05 % |
| 9:50 AM | MLYS | 14,10 $ | 13,58 $ – 14,05 $ | +0,39 % |
| 9:50 AM | MWH | 26,80 $ | 26,00 $ – 26,72 $ | +0,30 % |
| 9:50 AM | NAVI | 6,05 $ | 5,83 $ – 6,02 $ | +0,42 % |
| 9:50 AM | NRG | 93,19 $ | 91,15 $ – 93,10 $ | +0,10 % |
| 9:50 AM | NZF | 10,59 $ | 10,45 $ – 10,53 $ | +0,52 % |
| 9:50 AM | OTEX | 22,75 $ | 22,18 $ – 22,72 $ | +0,13 % |
| 9:50 AM | RIO | 74,53 $ | 74,14 $ – 74,49 $ | +0,05 % |
| 9:50 AM | SARO | 27,14 $ | 26,81 $ – 27,13 $ | +0,04 % |
| 9:50 AM | SLM | 16,12 $ | 15,66 $ – 16,09 $ | +0,21 % |
| 9:50 AM | TEAM | 138,91 $ | 131,04 $ – 136,00 $ | +2,14 % |
| 9:50 AM | VALE | 9,78 $ | 9,65 $ – 9,77 $ | +0,15 % |
| 9:50 AM | YMM | 9,10 $ | 8,90 $ – 9,09 $ | +0,17 % |

… und 104 weitere in [orb.json](orb.json).

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

## Labor live – Fr 20.11.2026, Stand 10:50 Uhr ET

397 Aktien beobachtet · 3.118 Spielgeld-Trades aller Varianten · 2.141 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 0 | 0 | 0,00 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 0 | 0 | 0,00 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 2 | 0 | -1,71 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | -0,10 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 21 | 20 | -15,33 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 1 | -0,73 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| BA | Ausbruch 30 Min | 10:05 164,13 $ | 160,15 $ | 172,10 $ | offen, Kurs 162,72 $ | -0,91 € |
| BHP | Ausbruch 30 Min | 10:05 69,55 $ | 67,86 $ | 72,94 $ | offen, Kurs 68,84 $ | -1,07 € |
| BMY | Ausbruch 30 Min | 10:05 59,56 $ | 58,73 $ | 61,22 $ | offen, Kurs 59,52 $ | -0,12 € |
| CMCSA | Ausbruch 30 Min | 10:05 25,36 $ | 25,07 $ | 25,95 $ | offen, Kurs 25,43 $ | 0,20 € |
| DX | Ausbruch 30 Min | 10:05 10,07 $ | 9,87 $ | 10,47 $ | offen, Kurs 10,04 $ | -0,40 € |
| EBAY | Ausbruch 30 Min | 10:05 120,08 $ | 117,71 $ | 124,82 $ | offen, Kurs 119,68 $ | -0,38 € |
| F | Ausbruch 30 Min | 10:05 11,64 $ | 11,21 $ | 12,50 $ | offen, Kurs 11,51 $ | -1,22 € |
| IBM | Ausbruch 30 Min | 10:05 232,08 $ | 223,77 $ | 248,71 $ | offen, Kurs 231,83 $ | -0,16 € |
| MRK | Ausbruch 30 Min | 10:05 136,84 $ | 133,79 $ | 142,94 $ | offen, Kurs 136,15 $ | -0,56 € |
| PINS | Ausbruch 30 Min | 10:05 17,60 $ | 16,81 $ | 19,19 $ | offen, Kurs 17,24 $ | -2,12 € |
| PLTR | Ausbruch 30 Min | 10:05 152,45 $ | 147,55 $ | 162,25 $ | Stopp 10:40 Uhr | -3,26 € |
| PYPL | Ausbruch 30 Min | 10:05 55,05 $ | 53,31 $ | 58,52 $ | offen, Kurs 55,28 $ | 0,37 € |
| TW | Ausbruch 30 Min | 10:05 128,91 $ | 126,77 $ | 133,21 $ | offen, Kurs 129,40 $ | 0,33 € |
| UNH | Ausbruch 30 Min | 10:05 345,45 $ | 338,24 $ | 359,88 $ | offen, Kurs 344,69 $ | -0,27 € |
| GME | Ausbruch 30 Min | 10:10 27,52 $ | 26,74 $ | 29,09 $ | offen, Kurs 27,03 $ | -1,84 € |
| LLY | Ausbruch 30 Min | 10:10 1.369,06 $ | 1.354,23 $ | 1.398,73 $ | offen, Kurs 1.362,42 $ | -0,54 € |
| RKT | Ausbruch 30 Min | 10:10 13,84 $ | 13,12 $ | 15,29 $ | offen, Kurs 13,54 $ | -2,27 € |
| T | Ausbruch 30 Min | 10:10 22,45 $ | 22,08 $ | 23,19 $ | offen, Kurs 22,51 $ | 0,19 € |
| TMUS | Ausbruch 30 Min | 10:10 166,93 $ | 164,27 $ | 172,25 $ | offen, Kurs 166,82 $ | -0,11 € |
| SVRA | Erholung: Lücke nach unten ≥ 3 % | 10:50 4,36 $ | 4,00 $ | 5,09 $ | offen, Kurs 4,36 $ | -0,10 € |

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
