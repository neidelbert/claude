# Trader-Übersicht

Stand: Mo 23.11. 12:01 Uhr ET (18:01 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Mo 23.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 384 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45113296426)) |
| ORB-Scan | Mo 23.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 74 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45149217755)) |
| Labor live | Mo 23.11. 12:00 Uhr ET (18:00 Uhr MEZ) | OK – 4.074 Trades, 3.189 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/45149217755)) |
| Labor | Fr 20.11. 16:40 Uhr ET (22:40 Uhr MEZ) | OK – 16 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/44816105107)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Fr 20.11.2026

5.927 Aktien in der Liste · 5.927 Charts geladen · 1.622 liquide (ab 5 $ und 1.000.000 Aktien) · 1.620 gescannt · **384 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 12 | HDB, TSN, BIPC, IBN, TU, BIP, ADC, HRL |
| `bull_flag` | 38 | TMUS, CMG, HDB, CAH, BDX, IBN, CDW, ROL |
| `reclaim_ma20` | 25 | PEP, GPN, ADP, CME, PGR, RKT, KR, GIS |
| `oversold` | 307 | NVDA, MU, GOOGL, SNDK, TSM, INTC, GOOG, PLTR |
| `oversold_bounce` | 16 | UNH, TEAM, VEEV, CRSP, DLB, DOX, YSWY, BFAM |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| NVDA | 125,53 $ | 15,2 | `oversold` |
| MU | 594,51 $ | 29,4 | `oversold` |
| GOOGL | 265,29 $ | 27,7 | `oversold` |
| SNDK | 94,39 $ | 29,1 | `oversold` |
| TSM | 318,71 $ | 28,3 | `oversold` |
| INTC | 51,28 $ | 28,1 | `oversold` |
| GOOG | 264,00 $ | 26,8 | `oversold` |
| PLTR | 143,49 $ | 26,2 | `oversold` |
| MRVL | 122,28 $ | 27,7 | `oversold` |
| UNH | 339,85 $ | 29,8 | `oversold`, `oversold_bounce` |
| ASML | 1.266,22 $ | 28,7 | `oversold` |
| NBIS | 81,31 $ | 28,4 | `oversold` |
| NFLX | 56,73 $ | 27,4 | `oversold` |
| GS | 790,69 $ | 29,2 | `oversold` |
| DELL | 278,02 $ | 28,6 | `oversold` |
| MSTR | 77,80 $ | 20,4 | `oversold` |
| INTU | 270,44 $ | 26,4 | `oversold` |
| CAT | 510,45 $ | 23,9 | `oversold` |
| BAC | 47,04 $ | 27,9 | `oversold` |
| PEP | 140,54 $ | 53,0 | `reclaim_ma20` |

Alle 384 Treffer: [watchlist.json](watchlist.json)

## ORB-Scan – 2026-11-23 10:10 ET

Quelle: Treffer des Morgen-Scans · 365 nutzbare Charts · **74 über der Eröffnungsspanne**

| Bar-Schluss | Ticker | Kurs | Spanne | über dem Hoch |
|---|---|---|---|---|
| 9:50 AM | ALNY | 150,84 $ | 146,85 $ – 150,00 $ | +0,56 % |
| 9:50 AM | ARWR | 43,47 $ | 42,22 $ – 43,24 $ | +0,52 % |
| 9:50 AM | AUPH | 14,99 $ | 14,82 $ – 14,93 $ | +0,40 % |
| 9:50 AM | CALM | 72,33 $ | 70,66 $ – 72,17 $ | +0,24 % |
| 9:50 AM | CHD | 110,85 $ | 109,00 $ – 110,32 $ | +0,48 % |
| 9:50 AM | CME | 307,60 $ | 302,34 $ – 307,55 $ | +0,02 % |
| 9:50 AM | CYTK | 52,90 $ | 51,35 $ – 52,57 $ | +0,63 % |
| 9:50 AM | G | 41,80 $ | 41,12 $ – 41,64 $ | +0,38 % |
| 9:50 AM | GLUE | 9,16 $ | 8,78 $ – 9,09 $ | +0,83 % |
| 9:50 AM | HALO | 93,91 $ | 92,18 $ – 93,73 $ | +0,20 % |
| 9:50 AM | INVA | 18,63 $ | 18,40 $ – 18,60 $ | +0,16 % |
| 9:50 AM | IVR | 5,50 $ | 5,32 $ – 5,45 $ | +0,82 % |
| 9:50 AM | JAN | 32,20 $ | 31,27 $ – 31,99 $ | +0,66 % |
| 9:50 AM | LFST | 14,32 $ | 13,97 $ – 14,18 $ | +1,02 % |
| 9:50 AM | MIAX | 37,51 $ | 36,97 $ – 37,35 $ | +0,43 % |
| 9:50 AM | MIRM | 98,57 $ | 96,59 $ – 97,66 $ | +0,93 % |
| 9:50 AM | NIQ | 16,76 $ | 16,28 $ – 16,59 $ | +1,02 % |
| 9:50 AM | NJR | 55,78 $ | 54,91 $ – 55,55 $ | +0,41 % |
| 9:50 AM | NKTR | 31,89 $ | 30,80 $ – 31,68 $ | +0,66 % |
| 9:50 AM | NZF | 10,64 $ | 10,50 $ – 10,63 $ | +0,09 % |
| 9:50 AM | PBR | 16,11 $ | 15,90 $ – 16,08 $ | +0,16 % |
| 9:50 AM | PBR.A | 14,17 $ | 13,98 $ – 14,14 $ | +0,21 % |
| 9:50 AM | PEGA | 27,80 $ | 27,56 $ – 27,78 $ | +0,06 % |
| 9:50 AM | PFGC | 108,86 $ | 106,80 $ – 108,82 $ | +0,04 % |
| 9:50 AM | PGR | 230,16 $ | 228,34 $ – 230,07 $ | +0,04 % |
| 9:50 AM | PICS | 5,67 $ | 5,26 $ – 5,64 $ | +0,53 % |
| 9:50 AM | PRVA | 25,32 $ | 24,87 $ – 25,31 $ | +0,04 % |
| 9:50 AM | ROL | 37,86 $ | 37,28 $ – 37,85 $ | +0,03 % |
| 9:50 AM | SAP | 203,62 $ | 200,84 $ – 202,68 $ | +0,46 % |
| 9:50 AM | SSNC | 75,25 $ | 74,49 $ – 75,19 $ | +0,09 % |

… und 44 weitere in [orb.json](orb.json).

Ein späterer Treffer liegt näher am aktuellen Kurs.

## News zu den ersten 10 Treffern (letzte 24 Stunden, nur neue)

Bewegung seit gestern: GOOG -2,59 % · GOOGL -2,70 % · **INTC -7,97 %** · **MRVL -11,69 %** · **MU -13,89 %** · **NVDA -14,01 %** · **PLTR -6,63 %** · **SNDK -16,05 %** · **TSM -9,48 %** · UNH +2,84 %

- 23.11. 07:26 Uhr ET · **NVDA** · [Anthropic Just Rewrote Wall Street's IPO Record Books. Here's Where History Says Its Shares Will Head Next.](https://www.fool.com/investing/2026/11/23/anthropic-just-rewrote-wall-street-ipo-record-books-where-history-says-shares-head-next/?.tsrc=rss)
- 23.11. 07:21 Uhr ET · **NVDA** · [Could an AI selloff trigger a bear market and recession?](https://finance.yahoo.com/markets/stocks/articles/could-ai-selloff-trigger-bear-122152717.html?.tsrc=rss)
- 23.11. 07:17 Uhr ET · **NVDA** · [Down 33% YTD, Is Nvidia a Golden Buying Opportunity?](https://247wallst.com/investing/2026/11/23/down-33-ytd-is-nvidia-a-golden-buying-opportunity/?.tsrc=rss)
- 23.11. 07:15 Uhr ET · **GOOG** · [Marvell Technology’s Near 50% Plummet Within a Month Means Little to This Wall Street Pro Who Predicts 270% Gains From Here](https://247wallst.com/investing/2026/11/23/marvell-technologys-near-50-plummet-within-a-month-means-little-to-this-wall-street-pro-who-predicts-270-gains-from-here/?.tsrc=rss) · earnings, deal
- 23.11. 07:15 Uhr ET · **TSM** · [ASML Vs. Taiwan Semiconductor: Here’s Why You Choose One as Your AI-Anchor Now](https://247wallst.com/investing/2026/11/23/asml-vs-taiwan-semiconductor-heres-why-you-choose-one-as-your-ai-anchor-now/?.tsrc=rss)
- 23.11. 07:10 Uhr ET · **NVDA** · [Where Will Nvidia Stock Be in 1 Year? Wall Street's Answer Might Surprise You.](https://www.fool.com/investing/2026/11/23/where-will-nvidia-stock-be-in-1-year-wall-street-s-answer-might-surprise-you/?.tsrc=rss)
- 23.11. 07:05 Uhr ET · **MU** · [Why Is Micron Technology Stock Falling?](https://www.trefis.com/stock/mu/articles/627777/why-is-micron-technology-stock-falling/2026-11-23?.tsrc=rss) · legal
- 23.11. 07:05 Uhr ET · **NVDA** · [Disney Just Made a 52-Week High While Netflix Is Down 36.2% This Year. Here’s the Better Buy Now.](https://www.fool.com/investing/2026/11/23/disney-just-made-a-52-week-high-while-netflix-is-down-36-2-this-year-here-s-the-better-buy-now/?.tsrc=rss)
- 23.11. 07:01 Uhr ET · **GOOG** · [What Is Behind The Move In CoreWeave Stock?](https://www.trefis.com/stock/crwv/articles/627785/what-is-behind-the-move-in-coreweave-stock-2/2026-11-23?.tsrc=rss) · legal
- 23.11. 07:00 Uhr ET · **GOOG** · [The biggest investors in AI are doing this](https://finance.yahoo.com/video/biggest-investors-ai-doing-120000197.html?.tsrc=rss)
- 23.11. 06:55 Uhr ET · **NVDA** · [YieldMax® ETFs Announces Distributions on MSST, NVIT, and TEST](https://finance.yahoo.com/markets/options/articles/yieldmax-etfs-announces-distributions-msst-115500809.html?.tsrc=rss)
- 23.11. 06:52 Uhr ET · **NVDA** · [Why Did Digital Realty Stock Move?](https://www.trefis.com/stock/dlr/articles/627809/why-did-digital-realty-stock-move/2026-11-23?.tsrc=rss) · legal
- 23.11. 06:50 Uhr ET · **NVDA** · [Here’s How Many Shares of Costco You’d Need for $5,000 in Yearly Dividends.](https://www.fool.com/investing/2026/11/23/heres-how-many-shares-of-costco-youd-need-for-5000-in-yearly-dividends/?.tsrc=rss) · capital
- 23.11. 06:48 Uhr ET · **NVDA** · [Donald Trump urges Nvidia to rehire former CEO Jensen Huang](https://www.euronews.com/2026/11/23/donald-trump-urges-nvidia-to-rehire-former-ceo-jensen-huang?.tsrc=rss) · people
- 23.11. 06:48 Uhr ET · **NVDA** · [What Sent Astera Labs Stock Lower?](https://www.trefis.com/stock/alab/articles/627706/what-sent-astera-labs-stock-lower/2026-11-23?.tsrc=rss) · legal
- 23.11. 06:47 Uhr ET · **NVDA** · [JPMorgan Traders Drop Bullish View on Stocks After Selloff](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-traders-drop-bullish-view-114704931.html?.tsrc=rss)
- 23.11. 06:45 Uhr ET · **NVDA** · [Best Buy Reports Earnings Tomorrow. Here's What Investors Should Be Watching.](https://www.fool.com/investing/2026/11/23/best-buy-reports-earnings-tomorrow-here-s-what-investors-should-be-watching/?.tsrc=rss) · earnings
- 23.11. 06:44 Uhr ET · **NVDA** · [Jensen and Lori Huang Control 870 Million Nvidia Shares Through Trusts and LLCs](https://finance.yahoo.com/markets/stocks/articles/jensen-lori-huang-control-870-114440529.html?.tsrc=rss)
- 23.11. 06:41 Uhr ET · **PLTR** · [Trump's Portfolio Discloses Up to $148 Million in September Trading](https://finance.yahoo.com/markets/stocks/articles/trumps-portfolio-discloses-148-million-114128711.html?.tsrc=rss)
- 23.11. 06:41 Uhr ET · **GOOG** · [Nvidia Stock Surges as Trump Urges Board to Rehire Huang. Is the Selling Finally Over?](https://finance.yahoo.com/m/5d0863d1-3733-3b1d-9c79-9c4251c3f14a/nvidia-stock-surges-as-trump.html?.tsrc=rss)
- 23.11. 06:37 Uhr ET · **MU** · [AI Chips Update - Global Semiconductor ETF Expands International Investment Horizons](https://finance.yahoo.com/technology/ai/articles/ai-chips-global-semiconductor-etf-113725192.html?.tsrc=rss)
- 23.11. 06:20 Uhr ET · **INTC** · [CrowdStrike, Zscaler, Anthropic, Sandisk, Strategy, Robinhood, and More Stocks That Explain Today’s Market](https://finance.yahoo.com/m/76a3103b-f3de-364f-8cd8-90e453a902d8/crowdstrike%2C-zscaler%2C.html?.tsrc=rss)
- 23.11. 06:18 Uhr ET · **INTC** · [Why Did AMD Stock Move?](https://www.trefis.com/stock/amd/articles/627783/why-did-amd-stock-move/2026-11-23?.tsrc=rss) · legal
- 23.11. 06:18 Uhr ET · **INTC** · [What Triggered The Drop In Marvell Stock?](https://www.trefis.com/stock/mrvl/articles/627782/what-triggered-the-drop-in-marvell-stock/2026-11-23?.tsrc=rss) · legal
- 23.11. 06:10 Uhr ET · **GOOG** · [CrowdStrike explores acquisition of Zscaler – report](https://www.verdict.co.uk/crowdstrike-explores-acquisition-zscaler/?.tsrc=rss) · deal

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

## Labor live – Mo 23.11.2026, Stand 12:00 Uhr ET

423 Aktien beobachtet · 4.074 Spielgeld-Trades aller Varianten · 3.189 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 4 | 3 | -3,48 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 4 | 3 | -3,48 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 4 | 3 | -3,48 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 10 | 0 | -11,59 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 19 | 19 | -11,45 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 2 | 2 | -3,15 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 2 | 2 | -3,15 € |
| Beste Signale (streng): News-Sprung ≥ 2 %, Volumen ≥ 4×, Schwankung ≥ 4 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 1 | 0,80 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| PLTR | Ausbruch 30 Min | 10:25 160,61 $ | 154,57 $ | 172,69 $ | offen, Kurs 158,20 $ | -1,55 € |
| QCOM | Ausbruch 30 Min | 10:25 165,11 $ | 160,49 $ | 174,36 $ | offen, Kurs 164,85 $ | -0,21 € |
| QQQ | News-Sprung: Lücke ≥ 4 % | 10:25 656,70 $ | 648,20 $ | 669,45 $ | Stopp 11:45 Uhr | -1,34 € |
| QQQ | News-Sprung: Lücke ≥ 4 % | 10:25 656,70 $ | 648,20 $ | 673,69 $ | Stopp 11:45 Uhr | -1,34 € |
| QQQ | News-Sprung: Lücke ≥ 4 % | 10:25 656,70 $ | 648,20 $ | 682,19 $ | Stopp 11:45 Uhr | -1,34 € |
| QQQ | Opening-Range-Ausbruch 30 Min | 10:25 656,70 $ | 641,95 $ | 686,19 $ | offen, Kurs 652,11 $ | -0,75 € |
| QQQ | Ausbruch 30 Min | 10:25 656,70 $ | 641,95 $ | 686,19 $ | offen, Kurs 652,11 $ | -0,75 € |
| QQQ | Ausbruch 30 Min | 10:25 656,70 $ | 641,95 $ | 686,19 $ | offen, Kurs 652,11 $ | -0,75 € |
| SPY | Ausbruch 30 Min | 10:25 726,68 $ | 713,53 $ | 752,99 $ | offen, Kurs 723,55 $ | -0,48 € |
| CCL | Ausbruch 30 Min | 10:30 28,22 $ | 27,64 $ | 29,37 $ | offen, Kurs 28,07 $ | -0,60 € |
| F | Ausbruch 30 Min | 10:30 11,53 $ | 11,38 $ | 11,83 $ | offen, Kurs 11,61 $ | 0,64 € |
| PM | Ausbruch 30 Min | 10:35 183,92 $ | 181,80 $ | 188,15 $ | offen, Kurs 184,18 $ | 0,10 € |
| BRK.B | Ausbruch 30 Min | 10:40 574,88 $ | 568,35 $ | 587,95 $ | offen, Kurs 574,08 $ | -0,19 € |
| HON | Ausbruch 30 Min | 10:40 220,50 $ | 217,89 $ | 225,72 $ | offen, Kurs 221,64 $ | 0,47 € |
| NTNX | Ausbruch 30 Min | 10:40 58,11 $ | 56,87 $ | 60,60 $ | offen, Kurs 57,80 $ | -0,58 € |
| NTRA | Ausbruch 30 Min | 10:40 296,27 $ | 286,11 $ | 316,58 $ | offen, Kurs 292,84 $ | -1,21 € |
| GLBE | Ausbruch 30 Min | 10:45 35,01 $ | 34,10 $ | 36,82 $ | offen, Kurs 35,00 $ | -0,07 € |
| DASH | Ausbruch 30 Min | 11:20 163,64 $ | 158,52 $ | 173,89 $ | offen, Kurs 162,61 $ | -0,68 € |
| ALM | Ausbruch 30 Min | 11:25 7,33 $ | 6,94 $ | 8,12 $ | offen, Kurs 7,39 $ | 0,68 € |
| COIN | Ausbruch 30 Min | 11:25 111,27 $ | 107,20 $ | 119,40 $ | offen, Kurs 110,40 $ | -0,83 € |

## Labor (Testphase, Spielgeld ohne Limit)

767 Aktien · 81 Handelstage · Lerntage Do 30.07.2026 bis Mi 14.10.2026 · **Prüftage Do 15.10.2026 bis Fr 20.11.2026** · 80 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 47 | 66 % | +1,36 % | 63,97 € | -30,03 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 47 | 66 % | +1,20 % | 56,51 € | -37,49 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 47 | 66 % | +1,10 % | 51,65 € | -42,35 € | unwahrscheinlich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 68 | 59 % | +0,76 % | 51,69 € | -84,31 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 68 | 59 % | +0,63 % | 42,94 € | -93,06 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 68 | 59 % | +0,53 % | 36,33 € | -99,67 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 4× normal | 90 | 53 % | +0,44 % | 39,86 € | -140,14 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 3R | 89 | 53 % | +0,42 % | 37,66 € | -140,34 € | möglich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 158 | 52 % | +0,41 % | 63,95 € | -252,05 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 2R | 89 | 53 % | +0,37 % | 32,81 € | -145,19 € | möglich | **ja** |
| 11 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 169 | 51 % | +0,36 % | 61,51 € | -276,49 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 1,5R | 89 | 53 % | +0,31 % | 27,85 € | -150,15 € | möglich | **ja** |

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
