# Technical Analysis Report

## Portfolio-Level Report

---

## Table of Contents

1. [Cover Page](#technical-analysis-report)
2. [Table of Contents](#table-of-contents)
3. [Performance Metrics](#performance-metrics)
4. [Trade Log](#trade-log)
5. [Regime Summary](#regime-summary)
6. [Strategy Parameters](#strategy-parameters)
7. [Analyst Notes and Suggestions](#analyst-notes-and-suggestions)
8. [Rationale Summary](#rationale-summary)

## Performance Metrics

- **Return:** -0.07%
- **Sharpe Ratio:** -0.12
- **Max Drawdown:** 0.18%
- **Win Rate:** 43.75%

![Equity Curve](plots/portfolio_equity.png)


![Metric Distribution (Returns)](plots/portfolio_metric_dist.png)

Note: Outlier(s) highlighted in red.


## Drawdown Curve

![Drawdown Curve](plots/drawdown_curve.png)


## Return Distribution

![Return Distribution](plots/return_distribution.png)

Note: Outlier(s) highlighted in red.

## Regime Summary

**Regime Definitions and Classification Criteria:**

- **Trending:** A period where price exhibits a clear upward or downward movement, typically identified by the short-term SMA (window: 20) being consistently above (uptrend) or below (downtrend) the long-term SMA (window: 50) for more than 3 days.

- **Ranging:** A period where price oscillates within a horizontal channel, identified when the short-term SMA crosses above and below the long-term SMA frequently, with no sustained trend for more than 3 days.

- **Quantitative Parameters:**
**Short SMA window:** 20 days
**Long SMA window:** 50 days
**Minimum regime duration:** 4 days (regimes shorter than this are filtered out)
**RSI period:** 14
**RSI thresholds:** Overbought (70), Oversold (30)

Trending: 25%, Ranging: 75%


| Start Date | End Date | Regime | Days |
|---|---|---|---|
| 2015-04-30 00:00:00+05:30 | 2015-07-20 00:00:00+05:30 | ranging | 56 |
| 2015-07-20 00:00:00+05:30 | 2015-07-28 00:00:00+05:30 | trending | 6 |
| 2015-07-28 00:00:00+05:30 | 2015-09-14 00:00:00+05:30 | ranging | 34 |
| 2015-09-14 00:00:00+05:30 | 2015-09-30 00:00:00+05:30 | trending | 10 |
| 2015-09-30 00:00:00+05:30 | 2016-04-21 00:00:00+05:30 | ranging | 133 |
| 2016-04-26 00:00:00+05:30 | 2016-11-30 00:00:00+05:30 | ranging | 148 |
| 2016-11-30 00:00:00+05:30 | 2016-12-09 00:00:00+05:30 | trending | 7 |
| 2016-12-09 00:00:00+05:30 | 2017-01-13 00:00:00+05:30 | ranging | 25 |
| 2017-01-18 00:00:00+05:30 | 2017-03-31 00:00:00+05:30 | ranging | 49 |
| 2017-03-31 00:00:00+05:30 | 2017-04-21 00:00:00+05:30 | trending | 13 |
| 2017-04-21 00:00:00+05:30 | 2017-07-25 00:00:00+05:30 | ranging | 65 |
| 2017-07-25 00:00:00+05:30 | 2017-08-22 00:00:00+05:30 | trending | 19 |
| 2017-08-22 00:00:00+05:30 | 2018-08-01 00:00:00+05:30 | ranging | 236 |
| 2018-08-01 00:00:00+05:30 | 2018-09-18 00:00:00+05:30 | trending | 31 |
| 2018-09-18 00:00:00+05:30 | 2019-11-07 00:00:00+05:30 | ranging | 275 |
| 2019-11-07 00:00:00+05:30 | 2019-12-26 00:00:00+05:30 | trending | 33 |
| 2019-12-26 00:00:00+05:30 | 2020-05-26 00:00:00+05:30 | ranging | 100 |
| 2020-05-26 00:00:00+05:30 | 2020-06-11 00:00:00+05:30 | trending | 12 |
| 2020-06-11 00:00:00+05:30 | 2020-07-02 00:00:00+05:30 | ranging | 15 |
| 2020-07-02 00:00:00+05:30 | 2020-08-27 00:00:00+05:30 | trending | 40 |
| 2020-08-27 00:00:00+05:30 | 2021-09-22 00:00:00+05:30 | ranging | 266 |
| 2021-09-22 00:00:00+05:30 | 2021-11-02 00:00:00+05:30 | trending | 28 |
| 2021-11-02 00:00:00+05:30 | 2021-12-21 00:00:00+05:30 | ranging | 33 |
| 2021-12-24 00:00:00+05:30 | 2022-12-05 00:00:00+05:30 | ranging | 234 |
| 2022-12-05 00:00:00+05:30 | 2022-12-14 00:00:00+05:30 | trending | 7 |
| 2022-12-14 00:00:00+05:30 | 2023-02-02 00:00:00+05:30 | ranging | 35 |
| 2023-02-02 00:00:00+05:30 | 2023-02-17 00:00:00+05:30 | trending | 11 |
| 2023-02-17 00:00:00+05:30 | 2023-05-25 00:00:00+05:30 | ranging | 63 |
| 2023-05-25 00:00:00+05:30 | 2023-06-08 00:00:00+05:30 | trending | 10 |
| 2023-06-08 00:00:00+05:30 | 2023-10-17 00:00:00+05:30 | ranging | 89 |
| 2023-10-17 00:00:00+05:30 | 2023-11-02 00:00:00+05:30 | trending | 11 |
| 2023-11-02 00:00:00+05:30 | 2023-12-27 00:00:00+05:30 | ranging | 36 |
| 2023-12-27 00:00:00+05:30 | 2024-03-13 00:00:00+05:30 | trending | 52 |
| 2024-03-13 00:00:00+05:30 | 2024-10-31 00:00:00+05:30 | ranging | 156 |
| 2024-10-31 00:00:00+05:30 | 2024-12-03 00:00:00+05:30 | trending | 21 |
| 2024-12-03 00:00:00+05:30 | 2025-04-25 00:00:00+05:30 | ranging | 98 |

## Trade Outcome Heatmap

![Trade Outcome Heatmap](plots/trade_heatmap.png)

## Strategy Parameters

- **short_window:** 20
- **long_window:** 50
- **rsi_period:** 14
- **overbought:** 70
- **oversold:** 30
## Trade Log

**Ticker:** ESCORTS.NS
**Entry:** 2015-06-16 00:00:00+05:30
**Entry Price:** 99.15123748779297
**Exit:** 2015-06-18 00:00:00+05:30
**Exit Price:** 101.93206787109375
**Position Size:** 1
**PnL:** 2.78
**Rationale:** Buy: ESCORTS.NS close 99.15123748779297 > prev 98.57588958740234 at idx 35 | Sell: ESCORTS.NS close 101.93206787109375 < prev 102.12384033203125 at idx 37

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-03-13 00:00:00+05:30
**Entry Price:** 98.75745391845703
**Exit:** 2020-03-16 00:00:00+05:30
**Exit Price:** 92.54659271240234
**Position Size:** 1
**PnL:** -6.21
**Rationale:** Buy: APOLLOTYRE.NS close 98.75745391845703 > prev 94.96456146240234 at idx 1203 | Sell: APOLLOTYRE.NS close 92.54659271240234 < prev 98.75745391845703 at idx 1204

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-03-20 00:00:00+05:30
**Entry Price:** 84.24964141845703
**Exit:** 2020-03-23 00:00:00+05:30
**Exit Price:** 72.49165344238281
**Position Size:** 1
**PnL:** -11.76
**Rationale:** Buy: APOLLOTYRE.NS close 84.24964141845703 > prev 81.7368392944336 at idx 1208 | Sell: APOLLOTYRE.NS close 72.49165344238281 < prev 84.24964141845703 at idx 1209

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-03-24 00:00:00+05:30
**Entry Price:** 74.4829330444336
**Exit:** 2020-03-30 00:00:00+05:30
**Exit Price:** 77.37501525878906
**Position Size:** 1
**PnL:** 2.89
**Rationale:** Buy: APOLLOTYRE.NS close 74.4829330444336 > prev 72.49165344238281 at idx 1210 | Sell: APOLLOTYRE.NS close 77.37501525878906 < prev 78.32323455810547 at idx 1214

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-03 00:00:00+05:30
**Entry Price:** 74.38810729980469
**Exit:** 2020-04-08 00:00:00+05:30
**Exit Price:** 79.08182525634766
**Position Size:** 1
**PnL:** 4.69
**Rationale:** Buy: APOLLOTYRE.NS close 74.38810729980469 > prev 73.86659240722656 at idx 1217 | Sell: APOLLOTYRE.NS close 79.08182525634766 < prev 79.17664337158203 at idx 1219

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-09 00:00:00+05:30
**Entry Price:** 85.15044403076172
**Exit:** 2020-04-13 00:00:00+05:30
**Exit Price:** 81.35755157470703
**Position Size:** 1
**PnL:** -3.79
**Rationale:** Buy: APOLLOTYRE.NS close 85.15044403076172 > prev 79.08182525634766 at idx 1220 | Sell: APOLLOTYRE.NS close 81.35755157470703 < prev 85.15044403076172 at idx 1221

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-15 00:00:00+05:30
**Entry Price:** 83.58587646484375
**Exit:** 2020-04-20 00:00:00+05:30
**Exit Price:** 92.30953216552734
**Position Size:** 1
**PnL:** 8.72
**Rationale:** Buy: APOLLOTYRE.NS close 83.58587646484375 > prev 81.35755157470703 at idx 1222 | Sell: APOLLOTYRE.NS close 92.30953216552734 < prev 93.11551666259766 at idx 1225

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-22 00:00:00+05:30
**Entry Price:** 89.46485900878906
**Exit:** 2020-04-23 00:00:00+05:30
**Exit Price:** 88.42181396484375
**Position Size:** 1
**PnL:** -1.04
**Rationale:** Buy: APOLLOTYRE.NS close 89.46485900878906 > prev 87.18912506103516 at idx 1227 | Sell: APOLLOTYRE.NS close 88.42181396484375 < prev 89.46485900878906 at idx 1228

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-29 00:00:00+05:30
**Entry Price:** 90.69755554199219
**Exit:** 2020-05-04 00:00:00+05:30
**Exit Price:** 84.15481567382812
**Position Size:** 1
**PnL:** -6.54
**Rationale:** Buy: APOLLOTYRE.NS close 90.69755554199219 > prev 84.86598205566406 at idx 1232 | Sell: APOLLOTYRE.NS close 84.15481567382812 < prev 91.31390380859375 at idx 1234

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-06 00:00:00+05:30
**Entry Price:** 82.59024047851562
**Exit:** 2020-05-12 00:00:00+05:30
**Exit Price:** 86.24090576171875
**Position Size:** 1
**PnL:** 3.65
**Rationale:** Buy: APOLLOTYRE.NS close 82.59024047851562 > prev 81.26273345947266 at idx 1236 | Sell: APOLLOTYRE.NS close 86.24090576171875 < prev 88.27957916259766 at idx 1240

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-13 00:00:00+05:30
**Entry Price:** 89.51228332519531
**Exit:** 2020-05-14 00:00:00+05:30
**Exit Price:** 87.80547332763672
**Position Size:** 1
**PnL:** -1.71
**Rationale:** Buy: APOLLOTYRE.NS close 89.51228332519531 > prev 86.24090576171875 at idx 1241 | Sell: APOLLOTYRE.NS close 87.80547332763672 < prev 89.51228332519531 at idx 1242

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-19 00:00:00+05:30
**Entry Price:** 87.0468978881836
**Exit:** 2020-05-20 00:00:00+05:30
**Exit Price:** 85.67196655273438
**Position Size:** 1
**PnL:** -1.37
**Rationale:** Buy: APOLLOTYRE.NS close 87.0468978881836 > prev 86.90465545654297 at idx 1245 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.0468978881836 at idx 1246

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-21 00:00:00+05:30
**Entry Price:** 87.09430694580078
**Exit:** 2020-05-22 00:00:00+05:30
**Exit Price:** 85.67196655273438
**Position Size:** 1
**PnL:** -1.42
**Rationale:** Buy: APOLLOTYRE.NS close 87.09430694580078 > prev 85.67196655273438 at idx 1247 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.09430694580078 at idx 1248

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-26 00:00:00+05:30
**Entry Price:** 87.56841278076172
**Exit:** 2020-05-29 00:00:00+05:30
**Exit Price:** 92.07247161865234
**Position Size:** 1
**PnL:** 4.50
**Rationale:** Buy: APOLLOTYRE.NS close 87.56841278076172 > prev 85.67196655273438 at idx 1249 | Sell: APOLLOTYRE.NS close 92.07247161865234 < prev 92.97329711914062 at idx 1252

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-06-01 00:00:00+05:30
**Entry Price:** 99.32637786865234
**Exit:** 2020-06-02 00:00:00+05:30
**Exit Price:** 98.56780242919922
**Position Size:** 1
**PnL:** -0.76
**Rationale:** Buy: APOLLOTYRE.NS close 99.32637786865234 > prev 92.07247161865234 at idx 1253 | Sell: APOLLOTYRE.NS close 98.56780242919922 < prev 99.32637786865234 at idx 1254

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-06-05 00:00:00+05:30
**Entry Price:** 99.27897644042969
**Exit:** 2020-06-09 00:00:00+05:30
**Exit Price:** 99.32637786865234
**Position Size:** 1
**PnL:** 0.05
**Rationale:** Buy: APOLLOTYRE.NS close 99.27897644042969 > prev 97.38252258300781 at idx 1257 | Sell: APOLLOTYRE.NS close 99.32637786865234 < prev 100.84354400634766 at idx 1259

## Analyst Notes and Suggestions

The strategy underperformed in ranging markets; consider parameter tuning or regime filtering.

## Rationale Summary

- Buy: ESCORTS.NS close 99.15123748779297 > prev 98.57588958740234 at idx 35 | Sell: ESCORTS.NS close 101.93206787109375 < prev 102.12384033203125 at idx 37
- Buy: APOLLOTYRE.NS close 98.75745391845703 > prev 94.96456146240234 at idx 1203 | Sell: APOLLOTYRE.NS close 92.54659271240234 < prev 98.75745391845703 at idx 1204
- Buy: APOLLOTYRE.NS close 84.24964141845703 > prev 81.7368392944336 at idx 1208 | Sell: APOLLOTYRE.NS close 72.49165344238281 < prev 84.24964141845703 at idx 1209
- Buy: APOLLOTYRE.NS close 74.4829330444336 > prev 72.49165344238281 at idx 1210 | Sell: APOLLOTYRE.NS close 77.37501525878906 < prev 78.32323455810547 at idx 1214
- Buy: APOLLOTYRE.NS close 74.38810729980469 > prev 73.86659240722656 at idx 1217 | Sell: APOLLOTYRE.NS close 79.08182525634766 < prev 79.17664337158203 at idx 1219
- Buy: APOLLOTYRE.NS close 85.15044403076172 > prev 79.08182525634766 at idx 1220 | Sell: APOLLOTYRE.NS close 81.35755157470703 < prev 85.15044403076172 at idx 1221
- Buy: APOLLOTYRE.NS close 83.58587646484375 > prev 81.35755157470703 at idx 1222 | Sell: APOLLOTYRE.NS close 92.30953216552734 < prev 93.11551666259766 at idx 1225
- Buy: APOLLOTYRE.NS close 89.46485900878906 > prev 87.18912506103516 at idx 1227 | Sell: APOLLOTYRE.NS close 88.42181396484375 < prev 89.46485900878906 at idx 1228
- Buy: APOLLOTYRE.NS close 90.69755554199219 > prev 84.86598205566406 at idx 1232 | Sell: APOLLOTYRE.NS close 84.15481567382812 < prev 91.31390380859375 at idx 1234
- Buy: APOLLOTYRE.NS close 82.59024047851562 > prev 81.26273345947266 at idx 1236 | Sell: APOLLOTYRE.NS close 86.24090576171875 < prev 88.27957916259766 at idx 1240
- Buy: APOLLOTYRE.NS close 89.51228332519531 > prev 86.24090576171875 at idx 1241 | Sell: APOLLOTYRE.NS close 87.80547332763672 < prev 89.51228332519531 at idx 1242
- Buy: APOLLOTYRE.NS close 87.0468978881836 > prev 86.90465545654297 at idx 1245 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.0468978881836 at idx 1246
- Buy: APOLLOTYRE.NS close 87.09430694580078 > prev 85.67196655273438 at idx 1247 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.09430694580078 at idx 1248
- Buy: APOLLOTYRE.NS close 87.56841278076172 > prev 85.67196655273438 at idx 1249 | Sell: APOLLOTYRE.NS close 92.07247161865234 < prev 92.97329711914062 at idx 1252
- Buy: APOLLOTYRE.NS close 99.32637786865234 > prev 92.07247161865234 at idx 1253 | Sell: APOLLOTYRE.NS close 98.56780242919922 < prev 99.32637786865234 at idx 1254
- Buy: APOLLOTYRE.NS close 99.27897644042969 > prev 97.38252258300781 at idx 1257 | Sell: APOLLOTYRE.NS close 99.32637786865234 < prev 100.84354400634766 at idx 1259