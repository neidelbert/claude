# Trader-Übersicht

Stand: Di 24.11. 13:31 Uhr ET (19:31 Uhr MEZ) · wird bei jedem Lauf neu gebaut.

NYSE heute: offen (Handelszeit 09:30 bis 16:00 Uhr ET).

## Systemstatus

| Teil | Letzter Lauf | Ergebnis |
|---|---|---|
| Morgen-Scan | Di 24.11. 07:30 Uhr ET (13:30 Uhr MEZ) | OK – 531 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45334981954)) |
| ORB-Scan | Di 24.11. 10:10 Uhr ET (16:10 Uhr MEZ) | OK – 261 Treffer ([Lauf](https://github.com/neidelbert/claude/actions/runs/45334981954)) |
| Labor live | Di 24.11. 13:30 Uhr ET (19:30 Uhr MEZ) | OK – 3.697 Trades, 2.524 offen ([Lauf](https://github.com/neidelbert/claude/actions/runs/45377035163)) |
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

## Labor live – Di 24.11.2026, Stand 13:30 Uhr ET

410 Aktien beobachtet · 3.697 Spielgeld-Trades aller Varianten · 2.524 offen

| Top-Variante | Trades | offen | € bei 100 €/Trade |
|---|---|---|---|
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 3R | 2 | 2 | 1,42 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 2R | 2 | 1 | 2,70 € |
| News-Sprung: Lücke ≥ 4 % · Volumen ≥ 3× · Ziel 1,5R | 2 | 1 | 1,92 € |
| Stocks in Play (Studie): Top 20 nach Startvolumen · Stopp 10 % ATR · bis Schluss · nur bis 12 Uhr ET und Stopp mindestens 0,5 % entfernt | 6 | 1 | -3,57 € |
| Opening-Range-Ausbruch 30 Min · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | -0,75 € |
| Ausbruch 30 Min · nur Top 20 nach Volumen · Stopp Tief der Spanne · Ziel 2R · nur bei Volumen über 4× normal | 1 | 1 | -0,75 € |
| Erholung: Lücke nach unten ≥ 3 % · Stopp Tagestief · Ziel 2R · nur bei Volumen über 4× normal | 1 | 0 | -2,89 € |
| Ausbruch 30 Min · Volumen ≥ 1,5× · nur wenn der Gesamtmarkt (SPY) im Plus ist · Ziel 2R | 15 | 13 | 9,72 € |
| Beste Signale (locker): News-Sprung ≥ 2 %, Volumen ≥ 2×, Schwankung ≥ 2 %, Einstieg bis 10:30 Uhr ET · nur der erste Kandidat des Tages · Ziel 3R | 1 | 1 | 2,49 € |

| Aktie | Regel | Einstieg | Stopp | Ziel | Stand | Ergebnis |
|---|---|---|---|---|---|---|
| SN | News-Sprung: Lücke ≥ 4 % | 9:45 225,66 $ | 222,15 $ | 236,18 $ | offen, Kurs 229,80 $ | 1,78 € |
| AAOI | Stocks in Play (Studie): Top 20 nach Startvolumen | 9:50 41,07 $ | 40,37 $ | – | Stopp 10:00 Uhr | -1,75 € |
| BOX | Ausbruch 30 Min | 10:05 46,40 $ | 45,28 $ | 48,65 $ | offen, Kurs 46,45 $ | 0,05 € |
| CAH | Ausbruch 30 Min | 10:05 275,86 $ | 269,30 $ | 288,97 $ | offen, Kurs 278,31 $ | 0,84 € |
| CPRT | Ausbruch 30 Min | 10:05 32,52 $ | 31,62 $ | 34,32 $ | offen, Kurs 32,62 $ | 0,27 € |
| SEDG | Ausbruch 30 Min | 10:05 18,05 $ | 17,37 $ | 19,41 $ | offen, Kurs 18,39 $ | 1,81 € |
| CYTK | Ausbruch 30 Min | 10:10 57,90 $ | 54,12 $ | 65,47 $ | offen, Kurs 59,59 $ | 2,86 € |
| LMT | Ausbruch 30 Min | 10:10 589,31 $ | 574,54 $ | 618,86 $ | offen, Kurs 588,22 $ | -0,24 € |
| RTX | Ausbruch 30 Min | 10:10 197,38 $ | 194,62 $ | 202,89 $ | Stopp 10:45 Uhr | -1,45 € |
| GILD | Ausbruch 30 Min | 10:15 176,34 $ | 171,14 $ | 186,73 $ | offen, Kurs 178,65 $ | 1,26 € |
| HPE | Erholung: Lücke nach unten ≥ 3 % | 10:15 41,25 $ | 40,08 $ | 43,59 $ | Stopp 11:45 Uhr | -2,89 € |
| NKE | Ausbruch 30 Min | 10:15 35,34 $ | 33,93 $ | 38,17 $ | offen, Kurs 36,05 $ | 1,96 € |
| SYM | Ausbruch 30 Min | 10:25 38,21 $ | 33,54 $ | 47,55 $ | offen, Kurs 37,41 $ | -2,14 € |
| BMRN | Opening-Range-Ausbruch 30 Min | 10:35 67,64 $ | 62,78 $ | 77,35 $ | offen, Kurs 67,17 $ | -0,75 € |
| BMRN | Ausbruch 30 Min | 10:35 67,64 $ | 62,78 $ | 77,35 $ | offen, Kurs 67,17 $ | -0,75 € |
| BMRN | Ausbruch 30 Min | 10:35 67,64 $ | 62,78 $ | 77,35 $ | offen, Kurs 67,17 $ | -0,75 € |
| RBLX | Ausbruch 30 Min | 10:35 54,29 $ | 51,46 $ | 59,94 $ | offen, Kurs 53,16 $ | -2,13 € |
| BAX | Ausbruch 30 Min | 10:55 26,98 $ | 26,22 $ | 28,51 $ | offen, Kurs 27,23 $ | 0,88 € |
| AMC | Ausbruch 30 Min | 11:25 2,90 $ | 2,81 $ | 3,06 $ | Ziel 12:45 Uhr | 5,57 € |
| SN | Ausbruch 30 Min | 11:25 227,57 $ | 217,99 $ | 246,74 $ | offen, Kurs 229,80 $ | 0,93 € |

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
