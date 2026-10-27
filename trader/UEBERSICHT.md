# Trader-Übersicht

Stand: Di 27.10. 13:50 Uhr ET (18:50 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Di 27.10. 08:34 Uhr ET (13:34 Uhr MEZ) | OK – 443 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40504826435)) |
| ORB-Scan | Di 27.10. 10:10 Uhr ET (15:10 Uhr MEZ) | OK – 64 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/40504826435)) |
| Labor live | Di 27.10. 13:50 Uhr ET (18:50 Uhr MEZ) | OK – 2.931 Trades, 2.082 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/40504826435)) |
| Labor | Mo 26.10. 16:20 Uhr ET (21:20 Uhr MEZ) | OK – 4 von 76 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/40391446088)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Mo 26.10.2026

5.945 Aktien in der Liste · 5.943 Charts geladen · 1.433 liquide (ab 5 $ und 1.000.000 Aktien) · 1.430 gescannt · **443 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 217 | TSLA, BRK.B, TXN, XOM, CART, LMT, RRC, SGRY |
| `bull_flag` | 63 | WMT, HD, COP, CI, EBAY, AJG, BP, EL |
| `reclaim_ma20` | 52 | MSFT, JPM, PANW, QCOM, GS, ADI, DDOG, RCL |
| `oversold` | 104 | GOOG, NBIS, CRWV, LRCX, XP, GE, BAC, CAT |
| `oversold_bounce` | 64 | CRWV, LRCX, AMAT, GE, CAT, KLAC, IREN, HWM |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| TSLA | 391,62 $ | 60,6 | `breakout_20d` |
| MSFT | 532,60 $ | 58,0 | `reclaim_ma20` |
| GOOG | 314,19 $ | 29,8 | `oversold` |
| NBIS | 153,27 $ | 29,1 | `oversold` |
| CRWV | 55,19 $ | 28,1 | `oversold`, `oversold_bounce` |
| LRCX | 237,50 $ | 29,3 | `oversold`, `oversold_bounce` |
| BRK.B | 548,56 $ | 76,9 | `breakout_20d` |
| AMAT | 387,59 $ | 30,8 | `oversold_bounce` |
| TXN | 298,12 $ | 64,6 | `breakout_20d` |
| XP | 15,71 $ | 28,8 | `oversold` |
| JPM | 334,04 $ | 44,9 | `reclaim_ma20` |
| XOM | 184,54 $ | 77,3 | `breakout_20d` |
| PANW | 390,46 $ | 55,5 | `reclaim_ma20` |
| CART | 60,88 $ | 82,7 | `breakout_20d` |
| GE | 288,43 $ | 29,7 | `oversold`, `oversold_bounce` |
| WMT | 120,29 $ | 70,4 | `bull_flag` |
| QCOM | 179,60 $ | 51,8 | `reclaim_ma20` |
| LMT | 635,20 $ | 82,6 | `breakout_20d` |
| GS | 893,28 $ | 44,1 | `reclaim_ma20` |
| BAC | 50,52 $ | 26,1 | `oversold` |

Alle 443 Treffer: [watchlist.json](watchlist.json)

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

Bewegung seit gestern: AMAT +2,74 % · BRK.B +1,17 % · CRWV +1,76 % · GOOG -0,97 % · **LRCX +3,22 %** · MSFT +1,54 % · **NBIS -3,45 %** · **TSLA +5,21 %** · **TXN +4,72 %** · **XP -48,36 %**

- 27.10. 08:30 Uhr ET · **GOOG** · [Big Tech Is About to Report. Nvidia Investors Should Watch One Number.](https://www.fool.com/investing/2026/10/27/big-tech-is-about-to-report-nvidia-investors-should-watch-one-number/?.tsrc=rss)
- 27.10. 08:21 Uhr ET · **GOOG** · [Anthropic’s Founders Will Keep Control With a Single Share of Stock](https://247wallst.com/investing/2026/10/27/anthropics-founders-will-keep-control-with-a-single-share-of-stock/?.tsrc=rss)
- 27.10. 08:18 Uhr ET · **MSFT** · [Azure and Copilot Reacceleration Reinforce Microsoft’s (MSFT) AI Leadership](https://finance.yahoo.com/technology/ai/articles/azure-copilot-reacceleration-reinforce-microsoft-121852027.html?.tsrc=rss)
- 27.10. 08:12 Uhr ET · **AMAT** · [What Does Applied Materials (AMAT) Owning About 20% Mean For Its AI Push?](https://finance.yahoo.com/technology/ai/articles/does-applied-materials-amat-owning-121235879.html?.tsrc=rss)
- 27.10. 08:10 Uhr ET · **MSFT** · [What Few Investors Realize About QQQ’s Dividend](https://247wallst.com/investing/etf/2026/10/27/what-few-investors-realize-about-qqqs-dividend/?.tsrc=rss) · capital
- 27.10. 08:10 Uhr ET · **TSLA** · [Only 5 of 60 Analysts Still Say Sell Tesla, the Fewest in 11 Years](https://247wallst.com/investing/2026/10/27/only-5-of-60-analysts-still-say-sell-tesla-the-fewest-in-11-years/?.tsrc=rss) · deal
- 27.10. 08:04 Uhr ET · **AMAT** · [Semiconductor Equipment Selloff Challenges Applied Materials (AMAT)](https://finance.yahoo.com/markets/stocks/articles/semiconductor-equipment-selloff-challenges-applied-120417903.html?.tsrc=rss)
- 27.10. 08:00 Uhr ET · **GOOG** · [OuterBox Connects Its Proprietary Lead Tracking to Google Ads, HubSpot, and Salesforce](https://finance.yahoo.com/media-advertising/articles/outerbox-connects-proprietary-lead-tracking-120000093.html?.tsrc=rss)
- 27.10. 07:52 Uhr ET · **LRCX** · [Lam Research Corp. (LRCX) Shares Decline as Investors Reassess AI Spending](https://finance.yahoo.com/markets/stocks/articles/lam-research-corp-lrcx-shares-115245954.html?.tsrc=rss)
- 27.10. 07:37 Uhr ET · **TSLA** · [This Week In Energy Transition - SunPower Expands in Texas with Strategic Solar Collaborations](https://finance.yahoo.com/energy/articles/week-energy-transition-sunpower-expands-113719902.html?.tsrc=rss)
- 27.10. 07:26 Uhr ET · **TSLA** · [2 Standout AI Stocks That Can Plunge Up to 93%, According to Select Wall Street Analysts](https://www.fool.com/investing/2026/10/27/2-standout-ai-stocks-can-plunge-up-to-93-according-to-wall-street-analysts/?.tsrc=rss)
- 27.10. 07:24 Uhr ET · **TSLA** · [Humanoid Robots Could Need 20 Times More Memory Chips by 2030](https://247wallst.com/investing/2026/10/27/humanoid-robots-could-need-20-times-more-memory-chips-by-2030/?.tsrc=rss) · earnings
- 27.10. 07:22 Uhr ET · **GOOG** · [What Mattered Most In IBM's Latest Quarter?](https://www.trefis.com/stock/ibm/articles/620769/what-mattered-most-in-ibms-latest-quarter/2026-10-27?.tsrc=rss)
- 27.10. 07:15 Uhr ET · **MSFT** · [Several Important Factors Protect Amazon’s Margins and Secure Its AI Moat](https://247wallst.com/investing/2026/10/27/several-important-factors-protect-amazons-margins-and-secure-its-ai-moat/?.tsrc=rss)
- 27.10. 07:15 Uhr ET · **CRWV** · [CoreWeave Vs. Nvidia: Demand For Silicon is Not The Same Thing as Solvent, Credit-Backed Demand for Physical Infrastructure](https://247wallst.com/investing/2026/10/27/coreweave-vs-nvidia-demand-for-silicon-is-not-the-same-thing-as-solvent-credit-backed-demand-for-physical-infrastructure/?.tsrc=rss)
- 27.10. 07:15 Uhr ET · **GOOG** · [Prediction: Broadcom Stock Could Be Worth Twice as Much by 2030](https://247wallst.com/investing/2026/10/27/prediction-broadcom-stock-could-be-worth-twice-as-much-by-2030/?.tsrc=rss) · earnings
- 27.10. 07:15 Uhr ET · **GOOG** · [Can Adobe Stock Jump 50%?](https://www.trefis.com/stock/adbe/articles/620782/can-adobe-stock-jump-50/2026-10-27?.tsrc=rss)
- 27.10. 07:15 Uhr ET · **GOOG** · [Is Broadcom Stock Too Dependent On One Business?](https://www.trefis.com/stock/avgo/articles/620733/is-broadcom-stock-too-dependent-on-one-business/2026-10-27?.tsrc=rss)
- 27.10. 07:15 Uhr ET · **MSFT** · [Microsoft Is Paying Workers to Leave So It Can Pay for AI](https://247wallst.com/investing/2026/10/27/microsoft-is-paying-workers-to-leave-so-it-can-pay-for-ai/?.tsrc=rss)
- 27.10. 07:11 Uhr ET · **GOOG** · [Entergy (ETR) Stock Appears Rich On A 150% Three Year Run](https://finance.yahoo.com/markets/stocks/articles/entergy-etr-stock-appears-rich-111154138.html?.tsrc=rss) · capital
- 27.10. 07:00 Uhr ET · **GOOG** · [Anthropic's S-1 is out. Is it actually making money?](https://finance.yahoo.com/video/anthropics-1-actually-making-money-110000352.html?.tsrc=rss)
- 27.10. 06:54 Uhr ET · **CRWV** · [CoreWeave Expands AI Cloud Footprint With Denmark Data Center — Plans Global Network Expansion Across 4 Continents](https://stocktwits.com/news-articles/markets/equity/core-weave-expands-ai-cloud-footprint-with-denmark-data-center-plans-global-network-expansion-across-4-continents/cZUedJLRBC2?.tsrc=rss)
- 27.10. 06:53 Uhr ET · **TSLA** · [SpaceX CEO Elon Musk Just Gave Telecoms Some Great News](https://finance.yahoo.com/m/d5e05259-96b6-3ef4-a519-1bee6a11d20d/spacex-ceo-elon-musk-just.html?.tsrc=rss) · people
- 27.10. 06:50 Uhr ET · **TSLA** · [In a SpaceX-Tesla Merger, Tesla Shareholders Might Be the Junior Partner](https://www.fool.com/investing/2026/10/27/in-a-spacex-tesla-merger-tsla-shareholders-might/?.tsrc=rss) · deal
- 27.10. 06:45 Uhr ET · **GOOG** · [Ex-Google CEO Eric Schmidt Says AI Could Eliminate 20% of Jobs at Large Companies](https://finance.yahoo.com/technology/ai/articles/ex-google-ceo-eric-schmidt-104506199.html?.tsrc=rss) · people

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

## Labor live – Di 27.10.2026, Stand 13:50 Uhr ET

419 Aktien beobachtet · 2.931 Spielgeld-Trades aller Varianten · 2.082 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | 0,88 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 2× normal | 7 | 7 | 3,88 € |
| Opening-Range-Ausbruch 15 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | 1,57 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | 0,88 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 2× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 7 | 7 | 2,32 € |
| Stocks in Play (Studie): Top 10 nach Startvolumen · Stopp 10 % ATR · Ziel 2R | 6 | 0 | -4,40 € |
| News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 2 | 2 | 2,54 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| KO | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:45 92,77 $ | 92,60 $ | 93,10 $ | Stopp 9:45 Uhr | -0,49 € |
| FPS | Stocks in Play (Studie): Top 10 nach Startvolumen | 9:50 26,61 $ | 26,33 $ | 27,19 $ | Stopp 9:55 Uhr | -1,12 € |
| SOFI | News-Sprung: Lücke ≥ 2 % | 9:55 16,19 $ | 15,67 $ | 17,24 $ | offen, Kurs 16,45 $ | 1,57 € |
| SOFI | Opening-Range-Ausbruch 15 Min | 9:55 16,19 $ | 15,67 $ | 17,24 $ | offen, Kurs 16,45 $ | 1,57 € |
| UPS | Opening-Range-Ausbruch 30 Min | 10:05 103,09 $ | 99,61 $ | 110,04 $ | offen, Kurs 105,02 $ | 1,82 € |
| SOFI | Opening-Range-Ausbruch 30 Min | 10:25 16,30 $ | 15,67 $ | 17,57 $ | offen, Kurs 16,45 $ | 0,88 € |
| SOFI | Opening-Range-Ausbruch 30 Min | 10:25 16,30 $ | 15,67 $ | 17,57 $ | offen, Kurs 16,45 $ | 0,88 € |
| SOFI | Ausbruch 30 Min | 10:25 16,30 $ | 15,67 $ | 17,57 $ | offen, Kurs 16,45 $ | 0,88 € |
| FLEX | Ausbruch 30 Min | 10:35 80,60 $ | 77,75 $ | 86,30 $ | offen, Kurs 81,26 $ | 0,77 € |
| GM | Opening-Range-Ausbruch 30 Min | 10:50 80,83 $ | 78,37 $ | 85,74 $ | offen, Kurs 80,56 $ | -0,38 € |
| GM | Ausbruch 30 Min | 10:50 80,83 $ | 78,37 $ | 85,74 $ | offen, Kurs 80,56 $ | -0,38 € |
| GOOGL | Opening-Range-Ausbruch 30 Min | 10:50 320,34 $ | 316,90 $ | 327,21 $ | offen, Kurs 322,10 $ | 0,50 € |
| GOOGL | Ausbruch 30 Min | 10:50 320,34 $ | 316,90 $ | 327,21 $ | offen, Kurs 322,10 $ | 0,50 € |
| FDX | Opening-Range-Ausbruch 30 Min | 11:00 305,29 $ | 299,13 $ | 317,62 $ | offen, Kurs 306,00 $ | 0,18 € |
| FDX | Ausbruch 30 Min | 11:00 305,29 $ | 299,13 $ | 317,62 $ | offen, Kurs 306,00 $ | 0,18 € |
| CCL | Ausbruch 30 Min | 11:05 27,77 $ | 27,14 $ | 29,04 $ | offen, Kurs 27,89 $ | 0,37 € |
| DASH | Opening-Range-Ausbruch 30 Min | 11:05 170,59 $ | 165,50 $ | 180,76 $ | offen, Kurs 174,00 $ | 1,95 € |
| DASH | Ausbruch 30 Min | 11:05 170,59 $ | 165,50 $ | 180,76 $ | offen, Kurs 174,00 $ | 1,95 € |
| AMKR | Opening-Range-Ausbruch 30 Min | 11:25 39,27 $ | 37,36 $ | 43,09 $ | offen, Kurs 38,87 $ | -1,07 € |
| AMKR | Ausbruch 30 Min | 11:25 39,27 $ | 37,36 $ | 43,09 $ | offen, Kurs 38,87 $ | -1,07 € |

## Labor (Testphase, Spielgeld ohne Limit)

397 Aktien · 62 Handelstage · Lerntage Do 30.07.2026 bis Fr 25.09.2026 · **Prüftage Mo 28.09.2026 bis Mo 26.10.2026** · 76 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 42 | 69 % | +0,30 % | 12,62 € | -71,38 € | möglich | **ja** |
| 2 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 2× normal | 202 | 52 % | +0,10 % | 20,82 € | -383,18 € | möglich | **ja** |
| 3 | Opening-Range-Ausbruch 15 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 62 | 55 % | +0,08 % | 4,68 € | -119,31 € | möglich | **ja** |
| 4 | Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 38 | 66 % | +0,02 % | 0,86 € | -75,14 € | möglich | **ja** |
| 5 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 2× normal | 56 | 64 % | +1,10 % | 61,91 € | -50,09 € | unwahrscheinlich | nein |
| 6 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 133 | 61 % | +1,08 % | 143,75 € | -122,25 € | unwahrscheinlich | nein |
| 7 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R | 153 | 55 % | +0,81 % | 124,51 € | -181,49 € | unwahrscheinlich | nein |
| 8 | Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 2R | 153 | 52 % | +0,45 % | 68,50 € | -237,50 € | unwahrscheinlich | nein |
| 9 | Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 1R | 153 | 56 % | +0,35 % | 53,72 € | -252,28 € | unwahrscheinlich | nein |
| 10 | Erholung: RSI unter 30 · Stopp 1,5 % darunter · Ziel 2R | 598 | 48 % | +0,10 % | 62,97 € | -1.133,03 € | möglich | nein |
| 11 | Erholung: Lücke nach unten ≥ 3 % · Stopp 1,5 % darunter · Ziel 1R | 153 | 54 % | +0,08 % | 12,48 € | -293,52 € | möglich | nein |
| 12 | Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · Volumen ≥ 1,5× | 483 | 48 % | +0,07 % | 36,10 € | -929,90 € | möglich | nein |

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
