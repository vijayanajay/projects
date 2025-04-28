# Technical Analysis Report

## Portfolio-Level Report

---

## Table of Contents

1. [Cover Page](#technical-analysis-report)
2. [Table of Contents](#table-of-contents)
3. [Assumptions: Slippage and Commission](#assumptions-slippage-and-commission)
4. [Performance Metrics](#performance-metrics)
5. [Benchmark Comparison](#benchmark-comparison)
6. [Trade Log](#trade-log)
7. [Regime Summary](#regime-summary)
8. [Strategy Parameters](#strategy-parameters)
9. [Risk and Position Sizing Logic](#risk-and-position-sizing-logic)
10. [Analyst Notes and Suggestions](#analyst-notes-and-suggestions)
11. [Rationale Summary](#rationale-summary)
12. [Trade Statistics Breakdown](#trade-statistics-breakdown)
13. [Regime Breakdown](#regime-breakdown)

## Drawdown Table

![](plots/drawdown_table.png)

## Assumptions: Slippage and Commission

- **Slippage:** A slippage of 0.0 per trade is applied to all executions (entry and exit prices adjusted by ±slippage). (slippage=0.0)

- **Commission:** A fixed commission rate of 0.20% per trade is applied, as set in the backtesting engine (commission=0.002).


These assumptions may affect real-world applicability and should be reviewed for live trading scenarios.

## Performance Metrics

- **Strategy Return:** -0.07%
- **Strategy Sharpe Ratio:** -0.12
- **Strategy Max Drawdown:** 0.18%
- **Strategy Win Rate:** 37.50%

![Equity Curve](plots/portfolio_equity.png)


## Drawdown Curve

![Drawdown Curve](plots/drawdown_curve.png)


## Return Distribution

![Return Distribution](plots/return_distribution.png)

Note: Outlier(s) highlighted in red.

## Trade Log

**Ticker:** ESCORTS.NS
**Entry:** 2015-06-16 00:00:00+05:30
**Entry Price:** 99.1512222290039
**Exit:** 2015-06-18 00:00:00+05:30
**Exit Price:** 101.93208312988281
**Position Size:** 1
**PnL:** 2.38
**Rationale:** Buy: ESCORTS.NS close 99.1512222290039 > prev 98.57588958740234 at idx 34 | Sell: ESCORTS.NS close 101.93208312988281 < prev 102.12384796142578 at idx 36

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-03-13 00:00:00+05:30
**Entry Price:** 98.7574462890625
**Exit:** 2020-03-16 00:00:00+05:30
**Exit Price:** 92.54658508300781
**Position Size:** 1
**PnL:** -6.59
**Rationale:** Buy: APOLLOTYRE.NS close 98.7574462890625 > prev 94.96456146240234 at idx 1202 | Sell: APOLLOTYRE.NS close 92.54658508300781 < prev 98.7574462890625 at idx 1203

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-03-20 00:00:00+05:30
**Entry Price:** 84.24964141845703
**Exit:** 2020-03-23 00:00:00+05:30
**Exit Price:** 72.49166107177734
**Position Size:** 1
**PnL:** -12.07
**Rationale:** Buy: APOLLOTYRE.NS close 84.24964141845703 > prev 81.73684692382812 at idx 1207 | Sell: APOLLOTYRE.NS close 72.49166107177734 < prev 84.24964141845703 at idx 1208

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-03-24 00:00:00+05:30
**Entry Price:** 74.4829330444336
**Exit:** 2020-03-30 00:00:00+05:30
**Exit Price:** 77.37501525878906
**Position Size:** 1
**PnL:** 2.59
**Rationale:** Buy: APOLLOTYRE.NS close 74.4829330444336 > prev 72.49166107177734 at idx 1209 | Sell: APOLLOTYRE.NS close 77.37501525878906 < prev 78.3232421875 at idx 1213

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-03 00:00:00+05:30
**Entry Price:** 74.38809967041016
**Exit:** 2020-04-08 00:00:00+05:30
**Exit Price:** 79.08181762695312
**Position Size:** 1
**PnL:** 4.39
**Rationale:** Buy: APOLLOTYRE.NS close 74.38809967041016 > prev 73.86659240722656 at idx 1216 | Sell: APOLLOTYRE.NS close 79.08181762695312 < prev 79.1766357421875 at idx 1218

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-09 00:00:00+05:30
**Entry Price:** 85.15045166015625
**Exit:** 2020-04-13 00:00:00+05:30
**Exit Price:** 81.35755157470703
**Position Size:** 1
**PnL:** -4.13
**Rationale:** Buy: APOLLOTYRE.NS close 85.15045166015625 > prev 79.08181762695312 at idx 1219 | Sell: APOLLOTYRE.NS close 81.35755157470703 < prev 85.15045166015625 at idx 1220

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-15 00:00:00+05:30
**Entry Price:** 83.58587646484375
**Exit:** 2020-04-20 00:00:00+05:30
**Exit Price:** 92.30952453613281
**Position Size:** 1
**PnL:** 8.37
**Rationale:** Buy: APOLLOTYRE.NS close 83.58587646484375 > prev 81.35755157470703 at idx 1221 | Sell: APOLLOTYRE.NS close 92.30952453613281 < prev 93.11551666259766 at idx 1224

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-22 00:00:00+05:30
**Entry Price:** 89.4648666381836
**Exit:** 2020-04-23 00:00:00+05:30
**Exit Price:** 88.42181396484375
**Position Size:** 1
**PnL:** -1.40
**Rationale:** Buy: APOLLOTYRE.NS close 89.4648666381836 > prev 87.18913269042969 at idx 1226 | Sell: APOLLOTYRE.NS close 88.42181396484375 < prev 89.4648666381836 at idx 1227

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-04-29 00:00:00+05:30
**Entry Price:** 90.69754791259766
**Exit:** 2020-05-04 00:00:00+05:30
**Exit Price:** 84.15481567382812
**Position Size:** 1
**PnL:** -6.89
**Rationale:** Buy: APOLLOTYRE.NS close 90.69754791259766 > prev 84.86598205566406 at idx 1231 | Sell: APOLLOTYRE.NS close 84.15481567382812 < prev 91.31391143798828 at idx 1233

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-06 00:00:00+05:30
**Entry Price:** 82.59024047851562
**Exit:** 2020-05-12 00:00:00+05:30
**Exit Price:** 86.24089813232422
**Position Size:** 1
**PnL:** 3.31
**Rationale:** Buy: APOLLOTYRE.NS close 82.59024047851562 > prev 81.26272583007812 at idx 1235 | Sell: APOLLOTYRE.NS close 86.24089813232422 < prev 88.27957153320312 at idx 1239

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-13 00:00:00+05:30
**Entry Price:** 89.51228332519531
**Exit:** 2020-05-14 00:00:00+05:30
**Exit Price:** 87.80546569824219
**Position Size:** 1
**PnL:** -2.06
**Rationale:** Buy: APOLLOTYRE.NS close 89.51228332519531 > prev 86.24089813232422 at idx 1240 | Sell: APOLLOTYRE.NS close 87.80546569824219 < prev 89.51228332519531 at idx 1241

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-19 00:00:00+05:30
**Entry Price:** 87.0468978881836
**Exit:** 2020-05-20 00:00:00+05:30
**Exit Price:** 85.67196655273438
**Position Size:** 1
**PnL:** -1.72
**Rationale:** Buy: APOLLOTYRE.NS close 87.0468978881836 > prev 86.90465545654297 at idx 1244 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.0468978881836 at idx 1245

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-21 00:00:00+05:30
**Entry Price:** 87.09430694580078
**Exit:** 2020-05-22 00:00:00+05:30
**Exit Price:** 85.67196655273438
**Position Size:** 1
**PnL:** -1.77
**Rationale:** Buy: APOLLOTYRE.NS close 87.09430694580078 > prev 85.67196655273438 at idx 1246 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.09430694580078 at idx 1247

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-05-26 00:00:00+05:30
**Entry Price:** 87.56841278076172
**Exit:** 2020-05-29 00:00:00+05:30
**Exit Price:** 92.07247161865234
**Position Size:** 1
**PnL:** 4.14
**Rationale:** Buy: APOLLOTYRE.NS close 87.56841278076172 > prev 85.67196655273438 at idx 1248 | Sell: APOLLOTYRE.NS close 92.07247161865234 < prev 92.9732894897461 at idx 1251

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-06-01 00:00:00+05:30
**Entry Price:** 99.32637786865234
**Exit:** 2020-06-02 00:00:00+05:30
**Exit Price:** 98.56781005859375
**Position Size:** 1
**PnL:** -1.15
**Rationale:** Buy: APOLLOTYRE.NS close 99.32637786865234 > prev 92.07247161865234 at idx 1252 | Sell: APOLLOTYRE.NS close 98.56781005859375 < prev 99.32637786865234 at idx 1253

**Ticker:** APOLLOTYRE.NS
**Entry:** 2020-06-05 00:00:00+05:30
**Entry Price:** 99.27896881103516
**Exit:** 2020-06-09 00:00:00+05:30
**Exit Price:** 99.32637786865234
**Position Size:** 1
**PnL:** -0.35
**Rationale:** Buy: APOLLOTYRE.NS close 99.27896881103516 > prev 97.38251495361328 at idx 1256 | Sell: APOLLOTYRE.NS close 99.32637786865234 < prev 100.84354400634766 at idx 1258

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
| 2017-07-25 00:00:00+05:30 | 2017-08-21 00:00:00+05:30 | trending | 18 |
| 2017-08-21 00:00:00+05:30 | 2018-08-01 00:00:00+05:30 | ranging | 237 |
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
| 2023-06-08 00:00:00+05:30 | 2023-10-16 00:00:00+05:30 | ranging | 88 |
| 2023-10-16 00:00:00+05:30 | 2023-11-02 00:00:00+05:30 | trending | 12 |
| 2023-11-02 00:00:00+05:30 | 2023-12-27 00:00:00+05:30 | ranging | 36 |
| 2023-12-27 00:00:00+05:30 | 2024-03-13 00:00:00+05:30 | trending | 52 |
| 2024-03-13 00:00:00+05:30 | 2024-10-31 00:00:00+05:30 | ranging | 156 |
| 2024-10-31 00:00:00+05:30 | 2024-12-03 00:00:00+05:30 | trending | 21 |
| 2024-12-03 00:00:00+05:30 | 2025-04-28 00:00:00+05:30 | ranging | 99 |

## Trade Outcome Heatmap

![Trade Outcome Heatmap](plots/trade_heatmap.png)

## Strategy Parameters

- **position_size:** 100
- **initial_cash:** 10000

## Risk and Position Sizing Logic

- **% Risked Per Trade:** 1.00% of initial capital allocated to each trade (position_size=100, initial_cash=10000).
- **Allocation Rule:** Fixed allocation per trade; no leverage or short selling. Trades only executed if sufficient cash is available.
- **Max Simultaneous Positions:** No explicit maximum; limited by available cash.

Each trade allocates capital using a fixed position size. The number of shares bought is calculated as:


    qty = int(position_size // price)


This ensures that:
- No trade exceeds the specified position size or available cash.
- No leverage or short selling is used.
- Trades are only executed if sufficient cash is available.

This simple approach provides basic risk control by capping exposure per trade and preventing over-allocation. More advanced risk management (e.g., stop-loss, volatility targeting) is not implemented in this version.

## Analyst Notes and Suggestions

The strategy underperformed in ranging markets; consider parameter tuning or regime filtering.

## Rationale Summary

- Buy: ESCORTS.NS close 99.1512222290039 > prev 98.57588958740234 at idx 34 | Sell: ESCORTS.NS close 101.93208312988281 < prev 102.12384796142578 at idx 36
- Buy: APOLLOTYRE.NS close 98.7574462890625 > prev 94.96456146240234 at idx 1202 | Sell: APOLLOTYRE.NS close 92.54658508300781 < prev 98.7574462890625 at idx 1203
- Buy: APOLLOTYRE.NS close 84.24964141845703 > prev 81.73684692382812 at idx 1207 | Sell: APOLLOTYRE.NS close 72.49166107177734 < prev 84.24964141845703 at idx 1208
- Buy: APOLLOTYRE.NS close 74.4829330444336 > prev 72.49166107177734 at idx 1209 | Sell: APOLLOTYRE.NS close 77.37501525878906 < prev 78.3232421875 at idx 1213
- Buy: APOLLOTYRE.NS close 74.38809967041016 > prev 73.86659240722656 at idx 1216 | Sell: APOLLOTYRE.NS close 79.08181762695312 < prev 79.1766357421875 at idx 1218
- Buy: APOLLOTYRE.NS close 85.15045166015625 > prev 79.08181762695312 at idx 1219 | Sell: APOLLOTYRE.NS close 81.35755157470703 < prev 85.15045166015625 at idx 1220
- Buy: APOLLOTYRE.NS close 83.58587646484375 > prev 81.35755157470703 at idx 1221 | Sell: APOLLOTYRE.NS close 92.30952453613281 < prev 93.11551666259766 at idx 1224
- Buy: APOLLOTYRE.NS close 89.4648666381836 > prev 87.18913269042969 at idx 1226 | Sell: APOLLOTYRE.NS close 88.42181396484375 < prev 89.4648666381836 at idx 1227
- Buy: APOLLOTYRE.NS close 90.69754791259766 > prev 84.86598205566406 at idx 1231 | Sell: APOLLOTYRE.NS close 84.15481567382812 < prev 91.31391143798828 at idx 1233
- Buy: APOLLOTYRE.NS close 82.59024047851562 > prev 81.26272583007812 at idx 1235 | Sell: APOLLOTYRE.NS close 86.24089813232422 < prev 88.27957153320312 at idx 1239
- Buy: APOLLOTYRE.NS close 89.51228332519531 > prev 86.24089813232422 at idx 1240 | Sell: APOLLOTYRE.NS close 87.80546569824219 < prev 89.51228332519531 at idx 1241
- Buy: APOLLOTYRE.NS close 87.0468978881836 > prev 86.90465545654297 at idx 1244 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.0468978881836 at idx 1245
- Buy: APOLLOTYRE.NS close 87.09430694580078 > prev 85.67196655273438 at idx 1246 | Sell: APOLLOTYRE.NS close 85.67196655273438 < prev 87.09430694580078 at idx 1247
- Buy: APOLLOTYRE.NS close 87.56841278076172 > prev 85.67196655273438 at idx 1248 | Sell: APOLLOTYRE.NS close 92.07247161865234 < prev 92.9732894897461 at idx 1251
- Buy: APOLLOTYRE.NS close 99.32637786865234 > prev 92.07247161865234 at idx 1252 | Sell: APOLLOTYRE.NS close 98.56781005859375 < prev 99.32637786865234 at idx 1253
- Buy: APOLLOTYRE.NS close 99.27896881103516 > prev 97.38251495361328 at idx 1256 | Sell: APOLLOTYRE.NS close 99.32637786865234 < prev 100.84354400634766 at idx 1258

## Parameter Sensitivity Analysis

The plot below compares equity curves for different parameter values, illustrating the impact of parameter changes on strategy performance.

![Parameter Sensitivity](plots/parameter_sensitivity.png)

## Trade Statistics Breakdown

| Metric | Value |
|---|---|
| Average Win | 4.20 |
| Average Loss | -3.81 |
| Largest Win | 8.37 |
| Largest Loss | -12.07 |
| Profit Factor | 0.66 |
| Expectancy | -0.81 |

### Regime Breakdown

| Regime | Trades | Win Rate | Avg Win | Avg Loss | Largest Win | Largest Loss | Profit Factor | Expectancy | Mean PnL |
|---|---|---|---|---|---|---|---|---|---|
| trending | 4 | 0.50 | 2.48 | -6.21 | 2.59 | -12.07 | 0.40 | -1.86 | -1.86 |
| ranging | 12 | 0.33 | 5.05 | -3.21 | 8.37 | -6.89 | 0.79 | -0.46 | -0.46 |

![Mean PnL by Regime](plots/regime_barplot.png)


![PnL Distribution by Regime](plots/regime_boxplot.png)


## Trade Holding Duration Distribution

![Trade Holding Duration](plots/holding_duration.png)
