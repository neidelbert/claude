# Trader-Übersicht

Stand: Di 24.11. 07:33 Uhr ET (13:33 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: vor der Eröffnung (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Di 24.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 531 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45334981954)) |
| ORB-Scan | Mo 23.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 74 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45149217755)) |
| Labor live | Mo 23.11. 16:00 Uhr ET (22:00 Uhr MEZ) | OK – Tagesbilanz: 4.102 Trades ([Lauf](https://github.com/neidelbert/claude/actions/runs/45196902629)) |
| Labor | Mo 23.11. 16:20 Uhr ET (22:20 Uhr MEZ) | OK – 14 von 80 bestanden ([Lauf](https://github.com/neidelbert/claude/actions/runs/45196902629)) |
| Preisalarme | noch nie | – |
| Ticker-Analyse | Do 22.10. 18:34 Uhr ET (00:34 Uhr MESZ) | OK – AAPL: abgelaufen ([Lauf](https://github.com/neidelbert/claude/actions/runs/39865972957)) |
| Test-Push | Do 22.10. 19:24 Uhr ET (01:24 Uhr MESZ) | OK – Push gesendet ([Lauf](https://github.com/neidelbert/claude/actions/runs/39871573010)) |

Zeitplan (Mo–Fr, an Handelstagen): Morgen-Scan ab ca. 8:00 Uhr ET, ORB-Scan ab ca. 10:15 Uhr ET, Labor live und Preisalarme alle 10 Minuten während der Handelszeit, Tagesbilanz nach Schluss, Labor-Rangliste nach Börsenschluss (ab ca. 16:20 Uhr ET).

## Morgen-Scan – Schlusskurse vom Mo 23.11.2026

5.927 Aktien in der Liste · 5.927 Charts geladen · 1.500 liquide (ab 5 $ und 1.000.000 Aktien) · 1.499 gescannt · **531 passen zu einer Regel**

| Regel | Anzahl | Meistgehandelt |
|---|---|---|
| `breakout_20d` | 51 | WMT, KYMR, PDD, TGT, INSM, ORLY, VIK, BIPC |
| `bull_flag` | 31 | CAH, IBN, HDB, EW, TSN, CLX, FWONK, CDW |
| `reclaim_ma20` | 171 | AAPL, TSLA, ZS, PANW, COHR, HD, MPWR, LIN |
| `oversold` | 82 | SNDK, UNH, MSTR, INTU, COIN, CRM, COF, OXY |
| `oversold_bounce` | 253 | NVDA, MU, GOOGL, TSM, INTC, GOOG, DELL, MRVL |

**Die 20 meistgehandelten Treffer** (Kurs × Umsatz):

| Ticker | Kurs | RSI | Regeln |
|---|---|---|---|
| NVDA | 165,05 $ | 43,0 | `oversold_bounce` |
| MU | 707,70 $ | 42,5 | `oversold_bounce` |
| AAPL | 349,08 $ | 52,8 | `reclaim_ma20` |
| TSLA | 385,46 $ | 52,1 | `reclaim_ma20` |
| GOOGL | 282,10 $ | 40,9 | `oversold_bounce` |
| TSM | 363,60 $ | 43,1 | `oversold_bounce` |
| SNDK | 94,39 $ | 29,3 | `oversold` |
| INTC | 59,66 $ | 40,1 | `oversold_bounce` |
| GOOG | 279,53 $ | 40,2 | `oversold_bounce` |
| DELL | 334,91 $ | 41,7 | `oversold_bounce` |
| MRVL | 144,74 $ | 38,5 | `oversold_bounce` |
| PLTR | 159,36 $ | 41,6 | `oversold_bounce` |
| NBIS | 97,80 $ | 36,0 | `oversold_bounce` |
| ZS | 229,24 $ | 59,1 | `reclaim_ma20` |
| UNH | 336,08 $ | 28,7 | `oversold` |
| PANW | 353,43 $ | 51,8 | `reclaim_ma20` |
| WMT | 129,58 $ | 67,3 | `breakout_20d` |
| GS | 823,62 $ | 37,7 | `oversold_bounce` |
| ASML | 1.383,78 $ | 40,8 | `oversold_bounce` |
| NFLX | 58,10 $ | 33,3 | `oversold_bounce` |

Alle 531 Treffer: [watchlist.json](watchlist.json)

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

Bewegung seit gestern: AAPL +1,90 % · **DELL +20,46 %** · **GOOG +5,88 %** · **GOOGL +6,34 %** · **INTC +16,34 %** · **MU +19,04 %** · **NVDA +31,48 %** · **SNDK +10,69 %** · **TSLA +11,46 %** · **TSM +14,08 %**

- 24.11. 07:28 Uhr ET · **NVDA** · [Anthropic Falls Below IPO Price. The Threat Wasn’t Nvidia, It Came From Inside](https://beincrypto.com/anthropic-stock-below-ipo-price-employees/?.tsrc=rss)
- 24.11. 07:24 Uhr ET · **NVDA** · [Premarket movers: Nvidia slips; HPE, Semtech fall](https://finance.yahoo.com/markets/stocks/articles/premarket-movers-nvidia-slips-hpe-122424595.html?.tsrc=rss) · macro
- 24.11. 07:22 Uhr ET · **GOOG** · [Elon Musk Reportedly Told Staff SpaceX Is Falling Behind in AI](https://247wallst.com/investing/2026/11/24/elon-musk-reportedly-told-staff-spacex-is-falling-behind-in-ai/?.tsrc=rss)
- 24.11. 07:17 Uhr ET · **NVDA** · [NVIDIA Added About $1 Trillion in Minutes on Huang’s Return. Where Does the Price Target Go Now?](https://247wallst.com/investing/2026/11/24/nvidia-added-about-1-trillion-in-minutes-on-huangs-return-where-does-the-price-target-go-now/?.tsrc=rss) · analyst, legal, people
- 24.11. 07:15 Uhr ET · **NVDA** · [ASML Stock What Changed After Nvidia CEO Return](https://finance.yahoo.com/markets/stocks/articles/asml-stock-changed-nvidia-ceo-121558672.html?.tsrc=rss) · capital, people
- 24.11. 07:15 Uhr ET · **NVDA** · [Can Earnings Beat Change The Case For Navitas Stock](https://finance.yahoo.com/markets/stocks/articles/earnings-beat-change-case-navitas-121547987.html?.tsrc=rss) · earnings, deal
- 24.11. 07:15 Uhr ET · **NVDA** · [Anthropic’s Frenemy Squeeze: Pledging Up to $49B to Microsoft While Building Its Own Landlord Escape Hatch](https://247wallst.com/investing/2026/11/24/anthropics-frenemy-squeeze-pledging-up-to-49b-to-microsoft-while-building-its-own-landlord-escape-hatch/?.tsrc=rss)
- 24.11. 07:15 Uhr ET · **INTC** · [Intel Has Plummeted 30% Over 30 Days: This Pro Analyst Reiterated His Buy Status, Predicting 133% Gains](https://247wallst.com/investing/2026/11/24/intel-has-plummeted-30-over-30-days-this-pro-analyst-reiterated-his-buy-status-predicting-133-gains/?.tsrc=rss) · earnings
- 24.11. 07:14 Uhr ET · **INTC** · [U.S. chip stocks fall premarket after Nvidia-led rally on Huang’s return](https://finance.yahoo.com/markets/stocks/articles/u-chip-stocks-fall-premarket-121456516.html?.tsrc=rss)
- 24.11. 07:14 Uhr ET · **NVDA** · [Nvidia reinstates Jensen Huang as CEO and president](https://www.verdict.co.uk/nvidia-brings-back-jensen-huang-ceo/?.tsrc=rss) · people
- 24.11. 07:14 Uhr ET · **NVDA** · [Ansell And 2 Australian Undervalued Stocks To Improve Your Portfolio](https://finance.yahoo.com/markets/stocks/articles/ansell-2-australian-undervalued-stocks-121408597.html?.tsrc=rss) · people
- 24.11. 07:11 Uhr ET · **NVDA** · [Acutaas Chemicals And 2 Other Indian Growth Stocks To Watch](https://finance.yahoo.com/markets/stocks/articles/acutaas-chemicals-2-other-indian-121146498.html?.tsrc=rss) · people
- 24.11. 07:10 Uhr ET · **NVDA** · [Nvidia's Role as AI Industry Advocate Likely to Continue Following Huang's Return Amid Focus on Regulatory Policy, Wedbush Says](https://finance.yahoo.com/technology/ai/articles/nvidia-apos-role-ai-industry-121020908.html?.tsrc=rss)
- 24.11. 07:09 Uhr ET · **TSLA** · [Tesla, SpaceX Name Five Directors for Potential $3.5 Trillion Merger](https://finance.yahoo.com/markets/stocks/articles/tesla-spacex-name-five-directors-120918069.html?.tsrc=rss) · deal
- 24.11. 07:05 Uhr ET · **GOOG** · [OpenAI’s Greg Brockman: “The World Is Not Building Enough Compute.” Wall Street Just Stopped Raising Capex Forecasts](https://www.tikr.com/blog/openais-greg-brockman-the-world-is-not-building-enough-compute-wall-street-just-stopped-raising-capex-forecasts?ref=yahoofinance&tlnk=yf-261124-777pg8fq&.tsrc=rss) · earnings
- 24.11. 07:05 Uhr ET · **NVDA** · [Bitcoin or Gold? Cathie Wood of Ark Invest Makes a Compelling Case for Buying Bitcoin.](https://www.fool.com/investing/2026/11/24/bitcoin-or-gold-cathie-wood-of-ark-invest-makes-a-compelling-case-for-buying-bitcoin/?.tsrc=rss)
- 24.11. 07:04 Uhr ET · **NVDA** · [China Just Fired A Warning Shot At Nvidia As Jensen Huang Returns](https://finance.yahoo.com/technology/ai/articles/china-just-fired-warning-shot-120411505.html?.tsrc=rss)
- 24.11. 07:03 Uhr ET · **NVDA** · [Dan Ives Calls Jensen Huang's Return To Nvidia The Start of  ‘AI Godfather Part 2,’ But Warns Of More ‘Noise’ Ahead](https://stocktwits.com/news-articles/markets/equity/dan-ives-calls-jensen-huang-return-to-nvidia-the-start-of-ai-godfather-part-2-but-warns-of-more-noise-ahead/cNbsIBLR9kL?.tsrc=rss) · analyst
- 24.11. 07:03 Uhr ET · **NVDA** · [TSMC and SK Hynix Stocks Jump After Nvidia Reinstates Jensen Huang as CEO](https://finance.yahoo.com/markets/stocks/articles/tsmc-sk-hynix-stocks-jump-120300756.html?.tsrc=rss) · people
- 24.11. 07:02 Uhr ET · **DELL** · [HPE Expects Thinner AI Margins. Is Dell Next?](https://www.trefis.com/stock/hpe/articles/628212/hpe-expects-thinner-ai-margins-is-dell-next/2026-11-24?.tsrc=rss)
- 24.11. 07:02 Uhr ET · **AAPL** · [Nvidia Regains Nearly $1 Trillion in Value -- Apple Still Holds the Top Spot](https://finance.yahoo.com/markets/stocks/articles/nvidia-regains-nearly-1-trillion-120207012.html?.tsrc=rss)
- 24.11. 07:02 Uhr ET · **AAPL** · [Not Apple. Not Microsoft. This Is the "Magnificent Seven" Stock I’d Buy for a 10-Year Hold.](https://www.fool.com/investing/2026/11/24/not-apple-not-microsoft-this-is-the-magnificent-seven-stock-id-buy-for-a-10-year-hold/?.tsrc=rss)
- 24.11. 07:00 Uhr ET · **MU** · [SanDisk Stock At $937 Looked Cheap. Where Is The Floor?](https://www.trefis.com/stock/sndk/articles/627524/sandisk-stock-at-937-looked-cheap-where-is-the-floor/2026-11-24?.tsrc=rss)
- 24.11. 07:00 Uhr ET · **AAPL** · [How to short an AI bubble](https://uk.finance.yahoo.com/news/short-ai-bubble-120000844.html?.tsrc=rss)
- 24.11. 06:55 Uhr ET · **TSLA** · [Tesla Jumped 11% on FSD v15. Wall Street Still Sees $418](https://www.tikr.com/blog/tesla-jumped-11-on-fsd-v15-wall-street-still-sees-418?ref=yahoofinance&tlnk=yf-261124-55wvcq4q&.tsrc=rss)

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

## Labor live – Mo 23.11.2026, Stand 16:00 Uhr ET

423 Aktien beobachtet · 4.102 Spielgeld-Trades aller Varianten · 0 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 4 | 0 | -6,38 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 4 | 0 | -6,38 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 4 | 0 | -6,38 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 10 | 0 | -11,59 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 0 | 0 | 0,00 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 19 | 0 | -17,93 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 2 | 0 | -4,75 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 2 | 0 | -4,75 € |
| Beste Signale (streng): News-Sprung ≥ 2 %, Volumen ≥ 4×, Schwankung ≥ 4 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 0 | -0,44 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| PLTR | Ausbruch 30 Min | 10:25 160,61 $ | 154,57 $ | 172,69 $ | Schluss 15:55 Uhr | -0,89 € |
| QCOM | Ausbruch 30 Min | 10:25 165,11 $ | 160,49 $ | 174,36 $ | Schluss 15:55 Uhr | -0,57 € |
| QQQ | News-Sprung: Lücke ≥ 4 % | 10:25 656,70 $ | 648,20 $ | 669,45 $ | Stopp 11:45 Uhr | -1,34 € |
| QQQ | News-Sprung: Lücke ≥ 4 % | 10:25 656,70 $ | 648,20 $ | 673,69 $ | Stopp 11:45 Uhr | -1,34 € |
| QQQ | News-Sprung: Lücke ≥ 4 % | 10:25 656,70 $ | 648,20 $ | 682,19 $ | Stopp 11:45 Uhr | -1,34 € |
| QQQ | Opening-Range-Ausbruch 30 Min | 10:25 656,70 $ | 641,95 $ | 686,19 $ | Schluss 15:55 Uhr | -1,07 € |
| QQQ | Ausbruch 30 Min | 10:25 656,70 $ | 641,95 $ | 686,19 $ | Schluss 15:55 Uhr | -1,07 € |
| QQQ | Ausbruch 30 Min | 10:25 656,70 $ | 641,95 $ | 686,19 $ | Schluss 15:55 Uhr | -1,07 € |
| SPY | Ausbruch 30 Min | 10:25 726,68 $ | 713,53 $ | 752,99 $ | Schluss 15:55 Uhr | -0,68 € |
| CCL | Ausbruch 30 Min | 10:30 28,22 $ | 27,64 $ | 29,37 $ | Schluss 15:55 Uhr | -1,11 € |
| F | Ausbruch 30 Min | 10:30 11,53 $ | 11,38 $ | 11,83 $ | Schluss 15:55 Uhr | 0,77 € |
| PM | Ausbruch 30 Min | 10:35 183,92 $ | 181,80 $ | 188,15 $ | Schluss 15:55 Uhr | -0,57 € |
| BRK.B | Ausbruch 30 Min | 10:40 574,88 $ | 568,35 $ | 587,95 $ | Schluss 15:55 Uhr | -0,30 € |
| HON | Ausbruch 30 Min | 10:40 220,50 $ | 217,89 $ | 225,72 $ | Schluss 15:55 Uhr | 0,34 € |
| NTNX | Ausbruch 30 Min | 10:40 58,11 $ | 56,87 $ | 60,60 $ | Schluss 15:55 Uhr | -1,25 € |
| NTRA | Ausbruch 30 Min | 10:40 296,27 $ | 286,11 $ | 316,58 $ | Schluss 15:55 Uhr | -1,36 € |
| GLBE | Ausbruch 30 Min | 10:45 35,01 $ | 34,10 $ | 36,82 $ | Schluss 15:55 Uhr | -0,70 € |
| DASH | Ausbruch 30 Min | 11:20 163,64 $ | 158,52 $ | 173,89 $ | Schluss 15:55 Uhr | -1,36 € |
| ALM | Ausbruch 30 Min | 11:25 7,33 $ | 6,94 $ | 8,12 $ | Schluss 15:55 Uhr | -1,67 € |
| COIN | Ausbruch 30 Min | 11:25 111,27 $ | 107,20 $ | 119,40 $ | Schluss 15:55 Uhr | -2,33 € |

## Labor (Testphase, Spielgeld ohne Limit)

895 Aktien · 82 Handelstage · Lerntage Do 30.07.2026 bis Do 15.10.2026 · **Prüftage Fr 16.10.2026 bis Mo 23.11.2026** · 80 Varianten

| # | Variante | Prüftage: Trades | Treffer | Ø je Trade | € bei 100 €/Trade | nach Gebühren | Zufall? | bestanden |
|---|---|---|---|---|---|---|---|---|
| 1 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 57 | 58 % | +0,77 % | 44,04 € | -69,96 € | möglich | **ja** |
| 2 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 57 | 58 % | +0,64 % | 36,58 € | -77,42 € | möglich | **ja** |
| 3 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 57 | 58 % | +0,56 % | 31,71 € | -82,29 € | möglich | **ja** |
| 4 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 3R | 102 | 54 % | +0,32 % | 32,70 € | -171,30 € | möglich | **ja** |
| 5 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 2R | 102 | 54 % | +0,23 % | 23,72 € | -180,28 € | möglich | **ja** |
| 6 | News-Sprung: Lücke ≥ 4 % · Volumen ≥ 2× · Ziel 1,5R | 102 | 54 % | +0,18 % | 18,23 € | -185,77 € | möglich | **ja** |
| 7 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bei Volumen über 2× normal | 191 | 50 % | +0,14 % | 27,54 € | -354,46 € | möglich | **ja** |
| 8 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 3R | 207 | 49 % | +0,14 % | 28,37 € | -385,63 € | möglich | **ja** |
| 9 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 206 | 49 % | +0,09 % | 18,99 € | -393,01 € | möglich | **ja** |
| 10 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 2× · Ziel 2R | 207 | 49 % | +0,09 % | 18,82 € | -395,18 € | möglich | **ja** |
| 11 | Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 98 | 20 % | +0,09 % | 8,47 € | -187,53 € | möglich | **ja** |
| 12 | News-Sprung: Lücke ≥ 2 % · Volumen ≥ 3× · Ziel 3R | 102 | 49 % | +0,07 % | 7,61 € | -196,39 € | möglich | **ja** |

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
