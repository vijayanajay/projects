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

## Assumptions: Slippage and Commission

- **Slippage:** A slippage of 0.0 per trade is applied to all executions (entry and exit prices adjusted by ±slippage). (slippage=0.0)

- **Commission:** A fixed commission rate of 0.20% per trade is applied, as set in the backtesting engine (commission=0.002).


These assumptions may affect real-world applicability and should be reviewed for live trading scenarios.

## Performance Metrics

- **Strategy Return:** 0.00%
- **Strategy Sharpe Ratio:** 0.00
- **Strategy Max Drawdown:** 0.00%
- **Strategy Win Rate:** 40.06%

![Equity Curve](plots/portfolio_equity.png)


## Drawdown Curve

![Drawdown Curve](plots/drawdown_curve.png)


## Return Distribution

![Return Distribution](plots/return_distribution.png)

## Trade Log

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 194.54
**Exit:** 
**Exit Price:** 206.76
**Position Size:** 
**PnL:** 11.41
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.76 | 5.12 |
| ATR | 5.29 | 4.65 |
| Volume | 12329713.00 | 9340350.00 |
| SMA (Short) | 194.04 | 216.09 |
| SMA (Long) | 193.31 | 217.29 |
| RSI |  | 13.38 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 200.19
**Exit:** 
**Exit Price:** 212.9
**Position Size:** 
**PnL:** 11.88
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-10-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.45 | 5.37 |
| ATR | 5.12 | 5.60 |
| Volume | 9048478.00 | 12078110.00 |
| SMA (Short) | 197.89 | 220.94 |
| SMA (Long) | 197.45 | 221.11 |
| RSI | 69.27 | 37.39 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 224.13
**Exit:** 
**Exit Price:** 216.67
**Position Size:** 
**PnL:** -8.34
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-05-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 7.39 | 5.58 |
| ATR | 6.45 | 4.70 |
| Volume | 20706353.00 | 13546285.00 |
| SMA (Short) | 220.28 | 222.71 |
| SMA (Long) | 220.26 | 223.92 |
| RSI | 69.17 | 27.71 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 220.0
**Exit:** 
**Exit Price:** 226.79
**Position Size:** 
**PnL:** 5.9
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-07-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.09 | 4.17 |
| ATR | 3.47 | 4.80 |
| Volume | 11359882.00 | 7039997.00 |
| SMA (Short) | 215.22 | 234.72 |
| SMA (Long) | 215.03 | 234.99 |
| RSI | 54.03 | 29.82 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 235.38
**Exit:** 
**Exit Price:** 227.09
**Position Size:** 
**PnL:** -9.22
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-01-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 5.54 | 6.04 |
| ATR | 4.35 | 3.65 |
| Volume | 15009634.00 | 21861796.00 |
| SMA (Short) | 229.33 | 230.07 |
| SMA (Long) | 228.45 | 230.13 |
| RSI | 77.80 | 31.48 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 267.49
**Exit:** 
**Exit Price:** 289.21
**Position Size:** 
**PnL:** 20.61
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-02-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.41 | 4.11 |
| ATR | 4.11 | 6.76 |
| Volume | 73183771.60 | 9223001.00 |
| SMA (Short) | 237.21 | 296.81 |
| SMA (Long) | 234.43 | 296.97 |
| RSI | 86.82 | 31.65 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 312.87
**Exit:** 
**Exit Price:** 411.03
**Position Size:** 
**PnL:** 96.71
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-06-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.31 | 1.67 |
| ATR | 6.17 | 8.98 |
| Volume | 10142474.00 | 10658428.00 |
| SMA (Short) | 301.10 | 410.23 |
| SMA (Long) | 300.41 | 410.66 |
| RSI | 68.47 | 61.45 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 420.2
**Exit:** 
**Exit Price:** 400.96
**Position Size:** 
**PnL:** -20.89
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-02-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.98 | 13.89 |
| ATR | 7.91 | 8.65 |
| Volume | 14294571.00 | 11580639.00 |
| SMA (Short) | 411.64 | 411.54 |
| SMA (Long) | 411.21 | 413.87 |
| RSI | 59.15 | 40.91 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 424.47
**Exit:** 
**Exit Price:** 407.03
**Position Size:** 
**PnL:** -19.1
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-03-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.39 | 8.75 |
| ATR | 8.44 | 8.49 |
| Volume | 14021366.00 | 13283967.00 |
| SMA (Short) | 416.02 | 414.73 |
| SMA (Long) | 415.10 | 415.29 |
| RSI | 73.88 | 42.24 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 418.46
**Exit:** 
**Exit Price:** 411.03
**Position Size:** 
**PnL:** -9.09
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 7.31 | 11.26 |
| ATR | 8.18 | 7.67 |
| Volume | 8934275.00 | 11369679.00 |
| SMA (Short) | 410.05 | 417.17 |
| SMA (Long) | 409.33 | 417.28 |
| RSI | 72.21 | 28.40 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 438.82
**Exit:** 
**Exit Price:** 471.52
**Position Size:** 
**PnL:** 30.87
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-06-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 11.59 | 28.73 |
| ATR | 7.62 | 14.06 |
| Volume | 15018718.00 | 47998260.00 |
| SMA (Short) | 422.76 | 541.77 |
| SMA (Long) | 421.63 | 545.53 |
| RSI | 78.61 | 16.31 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 524.88
**Exit:** 
**Exit Price:** 493.91
**Position Size:** 
**PnL:** -33.01
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.33 | 6.41 |
| ATR | 16.41 | 12.04 |
| Volume | 23443212.00 | 18516544.00 |
| SMA (Short) | 510.57 | 497.82 |
| SMA (Long) | 507.85 | 498.40 |
| RSI | 68.31 | 45.40 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 532.43
**Exit:** 
**Exit Price:** 566.64
**Position Size:** 
**PnL:** 32.01
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-01-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 11.78 | 31.76 |
| ATR | 11.31 | 14.13 |
| Volume | 56181172.00 | 28438234.00 |
| SMA (Short) | 503.81 | 594.97 |
| SMA (Long) | 503.38 | 596.84 |
| RSI | 70.88 | 35.99 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 577.01
**Exit:** 
**Exit Price:** 552.75
**Position Size:** 
**PnL:** -26.52
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-09-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.35 | 13.40 |
| ATR | 13.85 | 14.01 |
| Volume | 21307915.00 | 11747929.00 |
| SMA (Short) | 566.11 | 558.36 |
| SMA (Long) | 564.07 | 559.63 |
| RSI | 64.07 | 32.92 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 586.49
**Exit:** 
**Exit Price:** 684.33
**Position Size:** 
**PnL:** 95.3
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.39 | 7.18 |
| ATR | 15.52 | 13.52 |
| Volume | 18350457.00 | 16047902.00 |
| SMA (Short) | 559.31 | 689.12 |
| SMA (Long) | 556.24 | 690.23 |
| RSI | 67.12 | 39.18 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 640.85
**Exit:** 
**Exit Price:** 930.14
**Position Size:** 
**PnL:** 286.15
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-04-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 40.68 | 35.87 |
| ATR | 32.43 | 26.37 |
| Volume | 73183771.60 | 37324416.00 |
| SMA (Short) | 569.10 | 992.73 |
| SMA (Long) | 560.15 | 1000.51 |
| RSI | 77.23 | 27.15 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 901.26
**Exit:** 
**Exit Price:** 876.07
**Position Size:** 
**PnL:** -28.74
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-01-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.31 | 15.19 |
| ATR | 24.19 | 23.74 |
| Volume | 24123091.00 | 32325918.00 |
| SMA (Short) | 907.33 | 904.80 |
| SMA (Long) | 907.26 | 905.07 |
| RSI | 47.92 | 34.59 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 962.37
**Exit:** 
**Exit Price:** 882.79
**Position Size:** 
**PnL:** -83.27
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-02-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 28.48 | 38.62 |
| ATR | 21.81 | 22.82 |
| Volume | 39087742.00 | 41470034.00 |
| SMA (Short) | 906.68 | 898.27 |
| SMA (Long) | 904.39 | 899.77 |
| RSI | 63.10 | 47.24 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 931.75
**Exit:** 
**Exit Price:** 918.22
**Position Size:** 
**PnL:** -17.22
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 25.08 | 17.92 |
| ATR | 23.14 | 28.03 |
| Volume | 15791099.00 | 16250796.00 |
| SMA (Short) | 903.80 | 933.40 |
| SMA (Long) | 902.24 | 935.33 |
| RSI | 63.10 | 29.56 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 960.26
**Exit:** 
**Exit Price:** 965.51
**Position Size:** 
**PnL:** 1.41
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-05-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.41 | 10.31 |
| ATR | 20.69 | 19.26 |
| Volume | 56469931.00 | 8354449.00 |
| SMA (Short) | 913.27 | 964.26 |
| SMA (Long) | 908.80 | 967.01 |
| RSI | 75.78 | 52.18 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 988.19
**Exit:** 
**Exit Price:** 1185.79
**Position Size:** 
**PnL:** 193.24
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-08-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 16.10 | 16.02 |
| ATR | 18.12 | 25.99 |
| Volume | 9426282.00 | 4803269.00 |
| SMA (Short) | 979.17 | 1164.72 |
| SMA (Long) | 978.41 | 1164.79 |
| RSI | 68.33 | 46.71 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1159.7
**Exit:** 
**Exit Price:** 1096.43
**Position Size:** 
**PnL:** -67.79
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.52 | 32.21 |
| ATR | 26.89 | 27.07 |
| Volume | 14800442.00 | 10017691.00 |
| SMA (Short) | 1118.99 | 1106.34 |
| SMA (Long) | 1118.94 | 1111.69 |
| RSI | 72.02 | 27.95 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1164.33
**Exit:** 
**Exit Price:** 1116.51
**Position Size:** 
**PnL:** -52.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 42.14 | 66.95 |
| ATR | 27.51 | 30.84 |
| Volume | 22557065.00 | 13437911.00 |
| SMA (Short) | 1106.15 | 1169.83 |
| SMA (Long) | 1104.33 | 1176.36 |
| RSI | 63.47 | 26.64 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1253.18
**Exit:** 
**Exit Price:** 1152.57
**Position Size:** 
**PnL:** -105.41
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 27.55 | 40.69 |
| ATR | 32.09 | 35.41 |
| Volume | 22126569.00 | 10617206.00 |
| SMA (Short) | 1208.72 | 1204.42 |
| SMA (Long) | 1203.65 | 1209.87 |
| RSI | 74.99 | 32.67 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1187.95
**Exit:** 
**Exit Price:** 1125.83
**Position Size:** 
**PnL:** -66.75
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-09-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.37 | 25.89 |
| ATR | 29.97 | 22.49 |
| Volume | 10724688.00 | 9528051.00 |
| SMA (Short) | 1168.73 | 1168.00 |
| SMA (Long) | 1166.69 | 1172.93 |
| RSI | 59.30 | 29.23 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1174.82
**Exit:** 
**Exit Price:** 1174.38
**Position Size:** 
**PnL:** -5.14
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.01 | 18.41 |
| ATR | 23.80 | 23.09 |
| Volume | 8981896.00 | 5763271.00 |
| SMA (Short) | 1153.28 | 1186.69 |
| SMA (Long) | 1152.55 | 1191.85 |
| RSI | 73.11 | 34.21 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1092.58
**Exit:** 
**Exit Price:** 1203.5
**Position Size:** 
**PnL:** 106.33
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 19.40 | 26.62 |
| ATR | 20.50 | 22.85 |
| Volume | 17929479.00 | 21638600.00 |
| SMA (Short) | 1075.08 | 1237.79 |
| SMA (Long) | 1075.05 | 1241.90 |
| RSI | 64.73 | 24.54 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1194.1
**Exit:** 
**Exit Price:** 1450.18
**Position Size:** 
**PnL:** 250.79
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.29 | 10.21 |
| ATR | 15.32 | 24.93 |
| Volume | 8534814.00 | 10462776.00 |
| SMA (Short) | 1173.25 | 1466.47 |
| SMA (Long) | 1172.16 | 1467.51 |
| RSI | 73.14 | 38.00 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1424.85
**Exit:** 
**Exit Price:** 1420.75
**Position Size:** 
**PnL:** -9.79
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-06-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.34 | 33.10 |
| ATR | 24.52 | 28.75 |
| Volume | 13206858.00 | 17464890.00 |
| SMA (Short) | 1451.22 | 1451.31 |
| SMA (Long) | 1450.78 | 1451.67 |
| RSI | 59.03 | 50.63 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1465.25
**Exit:** 
**Exit Price:** 1474.3
**Position Size:** 
**PnL:** 3.17
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-06-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.52 | 27.02 |
| ATR | 28.67 | 29.97 |
| Volume | 9181160.00 | 6249776.00 |
| SMA (Short) | 1451.69 | 1482.95 |
| SMA (Long) | 1451.43 | 1483.71 |
| RSI | 47.87 | 42.50 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1498.3
**Exit:** 
**Exit Price:** 1461.53
**Position Size:** 
**PnL:** -42.69
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-09-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.89 | 20.75 |
| ATR | 24.23 | 23.27 |
| Volume | 9610286.00 | 10768260.00 |
| SMA (Short) | 1493.10 | 1493.20 |
| SMA (Long) | 1492.43 | 1495.18 |
| RSI | 63.68 | 30.49 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1273.7
**Exit:** 
**Exit Price:** 1265.1
**Position Size:** 
**PnL:** -13.68
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.91 | 25.98 |
| ATR | 24.80 | 23.77 |
| Volume | 14562976.00 | 6584612.00 |
| SMA (Short) | 1264.09 | 1258.36 |
| SMA (Long) | 1261.49 | 1260.06 |
| RSI | 61.12 | 56.77 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1266.7
**Exit:** 
**Exit Price:** 1217.25
**Position Size:** 
**PnL:** -54.42
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-02-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.82 | 26.67 |
| ATR | 23.35 | 23.66 |
| Volume | 8764283.00 | 10298145.00 |
| SMA (Short) | 1261.02 | 1249.59 |
| SMA (Long) | 1258.42 | 1249.69 |
| RSI | 47.95 | 44.84 |

---

**Ticker:** RELIANCE.NS  
**Entry:** 
**Entry Price:** 1269.15
**Exit:** 
**Exit Price:** 1185.35
**Position Size:** 
**PnL:** -88.71
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-04-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 25.38 | 43.79 |
| ATR | 23.69 | 24.86 |
| Volume | 15971477.00 | 10223104.00 |
| SMA (Short) | 1244.41 | 1231.67 |
| SMA (Long) | 1241.16 | 1236.93 |
| RSI | 64.66 | 36.04 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1036.74
**Exit:** 
**Exit Price:** 1073.66
**Position Size:** 
**PnL:** 32.69
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.86 | 21.75 |
| ATR | 23.94 | 19.03 |
| Volume | 1309050.00 | 1070526.00 |
| SMA (Short) | 1040.88 | 1067.67 |
| SMA (Long) | 1040.05 | 1069.30 |
| RSI |  | 46.73 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1120.99
**Exit:** 
**Exit Price:** 1068.85
**Position Size:** 
**PnL:** -56.51
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-09-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 23.10 | 15.39 |
| ATR | 18.55 | 23.34 |
| Volume | 3479784.00 | 2426396.00 |
| SMA (Short) | 1071.20 | 1078.92 |
| SMA (Long) | 1069.14 | 1079.25 |
| RSI | 80.75 | 33.06 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1137.75
**Exit:** 
**Exit Price:** 1044.23
**Position Size:** 
**PnL:** -97.89
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-10-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 22.71 | 38.61 |
| ATR | 23.20 | 24.89 |
| Volume | 4807306.00 | 3130642.00 |
| SMA (Short) | 1085.38 | 1079.19 |
| SMA (Long) | 1081.17 | 1086.74 |
| RSI | 82.48 | 37.08 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1016.88
**Exit:** 
**Exit Price:** 987.72
**Position Size:** 
**PnL:** -33.17
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.57 | 14.66 |
| ATR | 15.09 | 15.27 |
| Volume | 1605762.00 | 2678020.00 |
| SMA (Short) | 1022.35 | 1016.49 |
| SMA (Long) | 1021.48 | 1018.44 |
| RSI | 58.78 | 46.33 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1020.87
**Exit:** 
**Exit Price:** 926.46
**Position Size:** 
**PnL:** -98.31
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-02-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 25.16 | 31.56 |
| ATR | 17.29 | 18.96 |
| Volume | 1402996.00 | 1962408.00 |
| SMA (Short) | 999.05 | 993.14 |
| SMA (Long) | 995.89 | 993.36 |
| RSI | 88.55 | 42.94 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 992.65
**Exit:** 
**Exit Price:** 1034.81
**Position Size:** 
**PnL:** 38.1
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 28.33 | 31.62 |
| ATR | 23.30 | 21.18 |
| Volume | 1636742.00 | 3316800.00 |
| SMA (Short) | 981.40 | 1070.89 |
| SMA (Long) | 976.12 | 1080.26 |
| RSI | 54.92 | 38.14 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1156.38
**Exit:** 
**Exit Price:** 1072.29
**Position Size:** 
**PnL:** -88.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-08-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 34.86 | 19.72 |
| ATR | 22.50 | 22.74 |
| Volume | 3961704.00 | 3231668.00 |
| SMA (Short) | 1092.76 | 1092.91 |
| SMA (Long) | 1084.15 | 1094.58 |
| RSI | 78.45 | 33.91 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 979.61
**Exit:** 
**Exit Price:** 963.73
**Position Size:** 
**PnL:** -19.77
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-02-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 22.11 | 27.50 |
| ATR | 23.53 | 20.60 |
| Volume | 1118954.00 | 1814638.00 |
| SMA (Short) | 971.67 | 974.00 |
| SMA (Long) | 970.72 | 976.24 |
| RSI | 67.96 | 46.28 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1033.13
**Exit:** 
**Exit Price:** 1027.55
**Position Size:** 
**PnL:** -9.7
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-04-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 37.06 | 7.32 |
| ATR | 20.75 | 20.46 |
| Volume | 2033328.00 | 1050538.00 |
| SMA (Short) | 983.22 | 1038.79 |
| SMA (Long) | 981.66 | 1039.49 |
| RSI | 59.09 | 29.48 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1086.84
**Exit:** 
**Exit Price:** 1020.28
**Position Size:** 
**PnL:** -70.78
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-06-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 34.42 | 18.24 |
| ATR | 18.42 | 22.50 |
| Volume | 1663940.00 | 1789726.00 |
| SMA (Short) | 1039.87 | 1042.56 |
| SMA (Long) | 1033.10 | 1046.54 |
| RSI | 82.34 | 18.79 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1119.57
**Exit:** 
**Exit Price:** 1082.76
**Position Size:** 
**PnL:** -41.22
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 24.97 | 7.32 |
| ATR | 23.83 | 20.26 |
| Volume | 2678832.00 | 1081510.00 |
| SMA (Short) | 1067.55 | 1075.38 |
| SMA (Long) | 1066.59 | 1076.01 |
| RSI | 74.46 | 47.82 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1091.07
**Exit:** 
**Exit Price:** 1087.68
**Position Size:** 
**PnL:** -7.75
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.00 | 8.08 |
| ATR | 20.35 | 20.27 |
| Volume | 2944072.00 | 782754.00 |
| SMA (Short) | 1077.54 | 1080.01 |
| SMA (Long) | 1077.38 | 1080.26 |
| RSI | 54.06 | 53.28 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1085.63
**Exit:** 
**Exit Price:** 1060.55
**Position Size:** 
**PnL:** -29.37
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.24 | 10.25 |
| ATR | 19.63 | 19.31 |
| Volume | 1334642.00 | 1985014.00 |
| SMA (Short) | 1081.76 | 1084.62 |
| SMA (Long) | 1080.83 | 1084.81 |
| RSI | 49.31 | 46.21 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1129.61
**Exit:** 
**Exit Price:** 1116.64
**Position Size:** 
**PnL:** -17.46
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-12-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 27.28 | 11.50 |
| ATR | 17.94 | 20.68 |
| Volume | 1443016.00 | 5504150.00 |
| SMA (Short) | 1089.22 | 1144.20 |
| SMA (Long) | 1084.49 | 1144.54 |
| RSI | 71.74 | 27.78 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1185.0
**Exit:** 
**Exit Price:** 1238.84
**Position Size:** 
**PnL:** 48.99
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-01-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 13.70 | 44.22 |
| ATR | 21.64 | 34.10 |
| Volume | 1242220.00 | 3489940.00 |
| SMA (Short) | 1160.10 | 1289.18 |
| SMA (Long) | 1158.51 | 1296.92 |
| RSI | 69.50 | 28.69 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1379.87
**Exit:** 
**Exit Price:** 1735.17
**Position Size:** 
**PnL:** 349.07
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 42.22 | 88.54 |
| ATR | 30.11 | 38.06 |
| Volume | 8179118.00 | 2815425.00 |
| SMA (Short) | 1304.40 | 1799.75 |
| SMA (Long) | 1301.76 | 1816.72 |
| RSI | 88.38 | 33.01 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1767.98
**Exit:** 
**Exit Price:** 1686.1
**Position Size:** 
**PnL:** -88.79
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 60.55 | 35.63 |
| ATR | 50.68 | 41.36 |
| Volume | 1680420.00 | 1094883.00 |
| SMA (Short) | 1740.06 | 1702.65 |
| SMA (Long) | 1738.19 | 1702.88 |
| RSI | 64.58 | 31.21 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1759.51
**Exit:** 
**Exit Price:** 1871.54
**Position Size:** 
**PnL:** 104.76
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-01-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 35.01 | 26.04 |
| ATR | 37.16 | 42.87 |
| Volume | 2429575.00 | 3281320.00 |
| SMA (Short) | 1707.00 | 1854.01 |
| SMA (Long) | 1705.57 | 1854.55 |
| RSI | 65.33 | 39.65 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1905.95
**Exit:** 
**Exit Price:** 1920.84
**Position Size:** 
**PnL:** 7.23
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-05-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.32 | 53.39 |
| ATR | 43.08 | 42.25 |
| Volume | 4971725.00 | 2900415.00 |
| SMA (Short) | 1857.35 | 1939.75 |
| SMA (Long) | 1857.14 | 1941.71 |
| RSI | 51.66 | 29.15 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 2026.18
**Exit:** 
**Exit Price:** 1918.91
**Position Size:** 
**PnL:** -115.16
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-09-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 43.88 | 41.07 |
| ATR | 40.20 | 42.34 |
| Volume | 2073298.00 | 1454663.00 |
| SMA (Short) | 1969.05 | 1945.49 |
| SMA (Long) | 1962.96 | 1949.85 |
| RSI | 74.36 | 27.77 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 2061.72
**Exit:** 
**Exit Price:** 1849.63
**Position Size:** 
**PnL:** -219.92
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-12-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 71.73 | 34.72 |
| ATR | 44.01 | 44.82 |
| Volume | 5195136.00 | 3809860.00 |
| SMA (Short) | 1920.65 | 1898.20 |
| SMA (Long) | 1917.14 | 1907.10 |
| RSI | 87.00 | 39.25 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 2039.99
**Exit:** 
**Exit Price:** 1968.94
**Position Size:** 
**PnL:** -79.06
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-02-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 62.51 | 36.97 |
| ATR | 46.41 | 42.70 |
| Volume | 6251505.00 | 2439322.00 |
| SMA (Short) | 1923.66 | 1968.04 |
| SMA (Long) | 1922.69 | 1970.24 |
| RSI | 67.45 | 36.55 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 2032.42
**Exit:** 
**Exit Price:** 1940.33
**Position Size:** 
**PnL:** -100.04
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-02-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 30.51 | 27.78 |
| ATR | 41.46 | 41.03 |
| Volume | 2486223.00 | 3092877.00 |
| SMA (Short) | 1989.78 | 1995.02 |
| SMA (Long) | 1987.62 | 1995.08 |
| RSI | 60.87 | 52.27 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 1758.85
**Exit:** 
**Exit Price:** 2754.97
**Position Size:** 
**PnL:** 987.09
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-05-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 72.99 | 89.96 |
| ATR | 91.04 | 68.97 |
| Volume | 3517431.00 | 3774549.00 |
| SMA (Short) | 1741.56 | 2872.11 |
| SMA (Long) | 1727.10 | 2878.54 |
| RSI | 61.79 | 25.87 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3026.72
**Exit:** 
**Exit Price:** 2849.96
**Position Size:** 
**PnL:** -188.51
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-05-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 58.53 | 40.35 |
| ATR | 73.96 | 72.71 |
| Volume | 5317862.00 | 1990777.00 |
| SMA (Short) | 2926.41 | 2893.88 |
| SMA (Long) | 2910.73 | 2895.49 |
| RSI | 67.57 | 30.97 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 2938.75
**Exit:** 
**Exit Price:** 3026.94
**Position Size:** 
**PnL:** 76.26
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-06-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 44.55 | 25.85 |
| ATR | 62.31 | 47.74 |
| Volume | 2240078.00 | 2859334.00 |
| SMA (Short) | 2931.27 | 3014.51 |
| SMA (Long) | 2930.13 | 3015.28 |
| RSI | 58.94 | 27.38 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3127.03
**Exit:** 
**Exit Price:** 3330.86
**Position Size:** 
**PnL:** 190.91
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-08-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 52.64 | 117.03 |
| ATR | 47.70 | 74.61 |
| Volume | 1510489.00 | 4871211.00 |
| SMA (Short) | 3052.84 | 3471.85 |
| SMA (Long) | 3050.13 | 3500.64 |
| RSI | 74.02 | 34.62 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3429.2
**Exit:** 
**Exit Price:** 3387.62
**Position Size:** 
**PnL:** -55.21
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 60.79 | 62.04 |
| ATR | 66.70 | 70.59 |
| Volume | 1510718.00 | 5408531.00 |
| SMA (Short) | 3383.06 | 3539.74 |
| SMA (Long) | 3375.43 | 3554.02 |
| RSI | 68.44 | 27.09 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3532.66
**Exit:** 
**Exit Price:** 3359.66
**Position Size:** 
**PnL:** -186.78
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-04-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 34.61 | 99.93 |
| ATR | 74.74 | 72.48 |
| Volume | 2168110.00 | 2640370.00 |
| SMA (Short) | 3500.09 | 3452.06 |
| SMA (Long) | 3495.09 | 3465.21 |
| RSI | 63.45 | 36.78 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3198.77
**Exit:** 
**Exit Price:** 2984.67
**Position Size:** 
**PnL:** -226.46
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-09-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 77.17 | 91.96 |
| ATR | 71.16 | 62.77 |
| Volume | 2150567.00 | 2052900.00 |
| SMA (Short) | 3097.74 | 3082.16 |
| SMA (Long) | 3087.24 | 3090.68 |
| RSI | 85.80 | 19.77 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3018.2
**Exit:** 
**Exit Price:** 3109.49
**Position Size:** 
**PnL:** 79.03
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-10-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 27.54 | 45.59 |
| ATR | 56.78 | 52.32 |
| Volume | 2438421.00 | 870157.00 |
| SMA (Short) | 2995.90 | 3125.68 |
| SMA (Long) | 2995.11 | 3131.75 |
| RSI | 59.38 | 35.98 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3237.14
**Exit:** 
**Exit Price:** 3230.86
**Position Size:** 
**PnL:** -19.21
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-03-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 44.04 | 52.68 |
| ATR | 57.12 | 56.03 |
| Volume | 1688475.00 | 1334132.00 |
| SMA (Short) | 3174.56 | 3232.22 |
| SMA (Long) | 3171.20 | 3242.87 |
| RSI | 63.15 | 37.55 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3144.91
**Exit:** 
**Exit Price:** 3086.44
**Position Size:** 
**PnL:** -70.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-06-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 36.78 | 22.27 |
| ATR | 54.57 | 41.64 |
| Volume | 1719623.00 | 863542.00 |
| SMA (Short) | 3100.76 | 3104.10 |
| SMA (Long) | 3091.30 | 3104.90 |
| RSI | 81.00 | 41.78 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3158.79
**Exit:** 
**Exit Price:** 3237.74
**Position Size:** 
**PnL:** 66.15
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-07-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 36.54 | 75.09 |
| ATR | 42.32 | 50.42 |
| Volume | 1687264.00 | 1984471.00 |
| SMA (Short) | 3120.68 | 3364.46 |
| SMA (Long) | 3115.20 | 3380.11 |
| RSI | 56.91 | 24.40 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3409.49
**Exit:** 
**Exit Price:** 3769.97
**Position Size:** 
**PnL:** 346.13
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 58.25 | 137.57 |
| ATR | 51.53 | 82.61 |
| Volume | 1441634.00 | 4311783.00 |
| SMA (Short) | 3387.78 | 3890.87 |
| SMA (Long) | 3381.04 | 3903.59 |
| RSI | 67.55 | 35.74 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 3854.04
**Exit:** 
**Exit Price:** 4197.44
**Position Size:** 
**PnL:** 327.29
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-06-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 40.20 | 87.59 |
| ATR | 68.71 | 80.46 |
| Volume | 4526556.00 | 2713073.00 |
| SMA (Short) | 3758.90 | 4277.97 |
| SMA (Long) | 3758.76 | 4281.23 |
| RSI | 62.65 | 6.33 |

---

**Ticker:** TCS.NS  
**Entry:** 
**Entry Price:** 4264.57
**Exit:** 
**Exit Price:** 4047.92
**Position Size:** 
**PnL:** -233.27
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 114.14 | 81.78 |
| ATR | 80.47 | 85.55 |
| Volume | 1558993.00 | 763161.00 |
| SMA (Short) | 4121.35 | 4117.15 |
| SMA (Long) | 4108.66 | 4134.53 |
| RSI | 73.52 | 16.33 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 473.64
**Exit:** 
**Exit Price:** 474.88
**Position Size:** 
**PnL:** -0.67
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.38 | 10.64 |
| ATR | 9.88 | 9.47 |
| Volume | 2004420.00 | 7343164.00 |
| SMA (Short) | 458.28 | 501.38 |
| SMA (Long) | 457.88 | 502.16 |
| RSI | 58.48 | 28.00 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 511.83
**Exit:** 
**Exit Price:** 499.01
**Position Size:** 
**PnL:** -14.84
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.40 | 5.46 |
| ATR | 10.57 | 9.34 |
| Volume | 4026686.00 | 2324080.00 |
| SMA (Short) | 493.02 | 495.93 |
| SMA (Long) | 492.47 | 496.22 |
| RSI | 77.58 | 33.76 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 504.28
**Exit:** 
**Exit Price:** 493.31
**Position Size:** 
**PnL:** -12.97
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.24 | 4.83 |
| ATR | 7.37 | 7.38 |
| Volume | 4645004.00 | 1644456.00 |
| SMA (Short) | 501.17 | 498.63 |
| SMA (Long) | 501.09 | 498.83 |
| RSI | 61.98 | 40.73 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 480.19
**Exit:** 
**Exit Price:** 589.86
**Position Size:** 
**PnL:** 107.53
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.22 | 7.78 |
| ATR | 9.89 | 8.12 |
| Volume | 2401774.00 | 1600178.00 |
| SMA (Short) | 476.12 | 595.12 |
| SMA (Long) | 475.01 | 596.73 |
| RSI | 84.07 | 33.70 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 579.06
**Exit:** 
**Exit Price:** 854.94
**Position Size:** 
**PnL:** 273.02
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.18 | 5.14 |
| ATR | 9.45 | 11.59 |
| Volume | 1925206.00 | 2006486.00 |
| SMA (Short) | 566.77 | 859.94 |
| SMA (Long) | 565.43 | 860.23 |
| RSI | 77.67 | 58.42 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 877.43
**Exit:** 
**Exit Price:** 869.3
**Position Size:** 
**PnL:** -11.63
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-12-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.33 | 7.83 |
| ATR | 11.28 | 11.40 |
| Volume | 2830398.00 | 1841546.00 |
| SMA (Short) | 862.60 | 864.63 |
| SMA (Long) | 862.38 | 864.87 |
| RSI | 66.19 | 46.28 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 886.04
**Exit:** 
**Exit Price:** 888.47
**Position Size:** 
**PnL:** -1.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-02-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.48 | 18.93 |
| ATR | 11.76 | 13.82 |
| Volume | 6225062.00 | 1791760.00 |
| SMA (Short) | 865.82 | 893.02 |
| SMA (Long) | 865.58 | 893.21 |
| RSI | 53.81 | 30.71 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 909.66
**Exit:** 
**Exit Price:** 987.96
**Position Size:** 
**PnL:** 74.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.14 | 11.31 |
| ATR | 14.01 | 13.75 |
| Volume | 1860004.00 | 5312580.00 |
| SMA (Short) | 895.95 | 1005.37 |
| SMA (Long) | 895.71 | 1006.56 |
| RSI | 57.39 | 20.67 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 954.55
**Exit:** 
**Exit Price:** 989.98
**Position Size:** 
**PnL:** 31.55
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.30 | 16.71 |
| ATR | 18.54 | 15.20 |
| Volume | 6487276.00 | 8289702.00 |
| SMA (Short) | 941.55 | 998.30 |
| SMA (Long) | 940.01 | 1000.74 |
| RSI | 71.66 | 42.83 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1004.38
**Exit:** 
**Exit Price:** 995.46
**Position Size:** 
**PnL:** -12.92
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-02-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.85 | 8.28 |
| ATR | 14.67 | 14.44 |
| Volume | 3720694.00 | 4445354.00 |
| SMA (Short) | 1005.78 | 1003.93 |
| SMA (Long) | 1004.22 | 1004.73 |
| RSI | 51.87 | 50.29 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1033.32
**Exit:** 
**Exit Price:** 1137.75
**Position Size:** 
**PnL:** 100.09
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-03-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.45 | 12.48 |
| ATR | 13.57 | 18.68 |
| Volume | 7548646.00 | 4469614.00 |
| SMA (Short) | 1005.68 | 1147.00 |
| SMA (Long) | 1004.62 | 1150.86 |
| RSI | 68.32 | 25.89 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1206.93
**Exit:** 
**Exit Price:** 1194.74
**Position Size:** 
**PnL:** -17.0
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-01-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 46.31 | 19.91 |
| ATR | 23.18 | 17.69 |
| Volume | 20960205.00 | 5915878.00 |
| SMA (Short) | 1093.81 | 1214.86 |
| SMA (Long) | 1088.12 | 1217.84 |
| RSI | 77.99 | 51.57 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 960.94
**Exit:** 
**Exit Price:** 1002.07
**Position Size:** 
**PnL:** 37.21
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 61.32 | 30.90 |
| ATR | 52.68 | 34.07 |
| Volume | 20811797.00 | 12418392.00 |
| SMA (Short) | 866.64 | 1005.09 |
| SMA (Long) | 863.64 | 1009.19 |
| RSI | 64.85 | 30.98 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1074.89
**Exit:** 
**Exit Price:** 1007.31
**Position Size:** 
**PnL:** -71.75
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-09-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 27.25 | 20.50 |
| ATR | 30.12 | 28.57 |
| Volume | 13800869.00 | 9921439.00 |
| SMA (Short) | 1026.64 | 1035.86 |
| SMA (Long) | 1026.07 | 1038.23 |
| RSI | 76.31 | 26.65 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1115.73
**Exit:** 
**Exit Price:** 1410.35
**Position Size:** 
**PnL:** 289.57
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-10-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 43.54 | 28.60 |
| ATR | 26.79 | 41.86 |
| Volume | 10624389.00 | 7007816.00 |
| SMA (Short) | 1041.06 | 1457.58 |
| SMA (Long) | 1034.26 | 1464.37 |
| RSI | 65.68 | 31.66 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1417.94
**Exit:** 
**Exit Price:** 1391.0
**Position Size:** 
**PnL:** -32.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-07-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 39.88 | 30.03 |
| ATR | 37.61 | 25.36 |
| Volume | 6141995.00 | 6563342.00 |
| SMA (Short) | 1397.49 | 1430.64 |
| SMA (Long) | 1394.55 | 1430.90 |
| RSI | 62.51 | 42.25 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1471.46
**Exit:** 
**Exit Price:** 1499.47
**Position Size:** 
**PnL:** 22.07
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-08-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 34.39 | 27.54 |
| ATR | 23.55 | 28.99 |
| Volume | 8329214.00 | 6857063.00 |
| SMA (Short) | 1430.22 | 1536.29 |
| SMA (Long) | 1428.40 | 1543.17 |
| RSI | 77.03 | 22.77 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1509.74
**Exit:** 
**Exit Price:** 1432.41
**Position Size:** 
**PnL:** -83.21
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-01-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 42.99 | 24.72 |
| ATR | 26.69 | 30.05 |
| Volume | 4194599.00 | 6421273.00 |
| SMA (Short) | 1467.71 | 1446.05 |
| SMA (Long) | 1464.43 | 1449.70 |
| RSI | 80.57 | 32.48 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1463.36
**Exit:** 
**Exit Price:** 1461.39
**Position Size:** 
**PnL:** -7.83
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.96 | 24.16 |
| ATR | 31.44 | 31.44 |
| Volume | 6567533.00 | 5016132.00 |
| SMA (Short) | 1449.44 | 1447.95 |
| SMA (Long) | 1448.22 | 1448.03 |
| RSI | 54.40 | 56.24 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1467.51
**Exit:** 
**Exit Price:** 1403.87
**Position Size:** 
**PnL:** -69.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 22.33 | 31.45 |
| ATR | 31.44 | 33.45 |
| Volume | 3734033.00 | 9159327.00 |
| SMA (Short) | 1451.17 | 1439.96 |
| SMA (Long) | 1446.83 | 1444.39 |
| RSI | 54.09 | 48.18 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1451.98
**Exit:** 
**Exit Price:** 1325.06
**Position Size:** 
**PnL:** -132.48
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-04-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 24.29 | 83.61 |
| ATR | 38.83 | 43.57 |
| Volume | 7284278.00 | 26223135.00 |
| SMA (Short) | 1414.51 | 1398.30 |
| SMA (Long) | 1412.25 | 1407.49 |
| RSI | 69.09 | 40.50 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1343.73
**Exit:** 
**Exit Price:** 1317.79
**Position Size:** 
**PnL:** -31.27
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.18 | 14.60 |
| ATR | 35.17 | 35.25 |
| Volume | 3655908.00 | 4577715.00 |
| SMA (Short) | 1348.80 | 1344.80 |
| SMA (Long) | 1348.76 | 1347.12 |
| RSI | 65.73 | 62.39 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1320.37
**Exit:** 
**Exit Price:** 1348.27
**Position Size:** 
**PnL:** 22.56
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 18.70 | 52.18 |
| ATR | 27.99 | 24.46 |
| Volume | 5736226.00 | 7205194.00 |
| SMA (Short) | 1309.47 | 1421.95 |
| SMA (Long) | 1307.65 | 1422.38 |
| RSI | 58.76 | 26.02 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1475.94
**Exit:** 
**Exit Price:** 1559.96
**Position Size:** 
**PnL:** 77.95
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-11-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 22.48 | 22.30 |
| ATR | 27.17 | 25.13 |
| Volume | 9536878.00 | 4625035.00 |
| SMA (Short) | 1426.43 | 1566.06 |
| SMA (Long) | 1425.91 | 1566.96 |
| RSI | 76.71 | 50.49 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1653.69
**Exit:** 
**Exit Price:** 1560.16
**Position Size:** 
**PnL:** -99.96
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-02-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 39.67 | 31.86 |
| ATR | 24.31 | 29.08 |
| Volume | 12491970.00 | 9496996.00 |
| SMA (Short) | 1589.43 | 1587.49 |
| SMA (Long) | 1580.89 | 1587.90 |
| RSI | 70.76 | 29.75 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1622.29
**Exit:** 
**Exit Price:** 1582.39
**Position Size:** 
**PnL:** -46.31
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-06-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 41.48 | 15.70 |
| ATR | 28.15 | 24.43 |
| Volume | 21180771.00 | 25183469.00 |
| SMA (Short) | 1575.96 | 1603.45 |
| SMA (Long) | 1575.39 | 1603.82 |
| RSI | 77.33 | 32.98 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1678.48
**Exit:** 
**Exit Price:** 1596.99
**Position Size:** 
**PnL:** -88.04
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-08-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 34.68 | 12.21 |
| ATR | 22.84 | 24.03 |
| Volume | 20349508.00 | 14112911.00 |
| SMA (Short) | 1618.77 | 1621.96 |
| SMA (Long) | 1612.13 | 1624.69 |
| RSI | 76.80 | 33.61 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1537.8
**Exit:** 
**Exit Price:** 1408.12
**Position Size:** 
**PnL:** -135.57
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-01-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 19.83 | 92.74 |
| ATR | 21.80 | 26.04 |
| Volume | 34745720.00 | 40913568.68 |
| SMA (Short) | 1504.37 | 1565.65 |
| SMA (Long) | 1499.71 | 1583.24 |
| RSI | 80.75 | 15.55 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1450.69
**Exit:** 
**Exit Price:** 1464.1
**Position Size:** 
**PnL:** 7.58
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-04-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.81 | 24.26 |
| ATR | 28.63 | 24.11 |
| Volume | 12599785.00 | 10460095.00 |
| SMA (Short) | 1425.75 | 1459.56 |
| SMA (Long) | 1423.52 | 1462.37 |
| RSI | 57.31 | 44.00 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1527.7
**Exit:** 
**Exit Price:** 1607.8
**Position Size:** 
**PnL:** 73.83
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-05-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.60 | 22.09 |
| ATR | 24.96 | 34.08 |
| Volume | 14692720.00 | 16167214.00 |
| SMA (Short) | 1473.45 | 1630.24 |
| SMA (Long) | 1469.56 | 1630.73 |
| RSI | 55.57 | 48.22 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1646.5
**Exit:** 
**Exit Price:** 1699.8
**Position Size:** 
**PnL:** 46.61
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-09-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.17 | 31.15 |
| ATR | 27.74 | 24.84 |
| Volume | 11896457.00 | 10235341.00 |
| SMA (Short) | 1638.53 | 1662.71 |
| SMA (Long) | 1638.35 | 1664.74 |
| RSI | 54.84 | 37.55 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1728.7
**Exit:** 
**Exit Price:** 1713.4
**Position Size:** 
**PnL:** -22.18
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.42 | 33.05 |
| ATR | 25.55 | 33.81 |
| Volume | 23274177.00 | 6763953.00 |
| SMA (Short) | 1675.33 | 1768.74 |
| SMA (Long) | 1669.06 | 1771.05 |
| RSI | 49.51 | 27.38 |

---

**Ticker:** HDFCBANK.NS  
**Entry:** 
**Entry Price:** 1710.0
**Exit:** 
**Exit Price:** 1690.0
**Position Size:** 
**PnL:** -26.8
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-03-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.83 | 18.79 |
| ATR | 30.20 | 30.26 |
| Volume | 9960479.00 | 10791936.00 |
| SMA (Short) | 1703.39 | 1700.09 |
| SMA (Long) | 1702.60 | 1700.43 |
| RSI | 52.10 | 46.18 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 380.66
**Exit:** 
**Exit Price:** 386.74
**Position Size:** 
**PnL:** 4.54
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.29 | 4.69 |
| ATR | 8.74 | 8.62 |
| Volume | 5189344.00 | 6469976.00 |
| SMA (Short) | 379.82 | 379.82 |
| SMA (Long) | 379.63 | 380.18 |
| RSI |  |  |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 397.26
**Exit:** 
**Exit Price:** 369.54
**Position Size:** 
**PnL:** -29.25
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-07-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.50 | 7.44 |
| ATR | 8.50 | 8.41 |
| Volume | 5882188.00 | 8587772.00 |
| SMA (Short) | 383.40 | 386.67 |
| SMA (Long) | 382.14 | 388.08 |
| RSI | 60.69 | 33.58 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 434.61
**Exit:** 
**Exit Price:** 405.55
**Position Size:** 
**PnL:** -30.74
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.74 | 15.58 |
| ATR | 9.31 | 11.43 |
| Volume | 12665660.00 | 10125252.00 |
| SMA (Short) | 393.53 | 439.12 |
| SMA (Long) | 391.02 | 441.42 |
| RSI | 73.89 | 17.06 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 439.24
**Exit:** 
**Exit Price:** 422.76
**Position Size:** 
**PnL:** -18.2
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.78 | 7.73 |
| ATR | 9.32 | 9.17 |
| Volume | 5526952.00 | 3156716.00 |
| SMA (Short) | 434.26 | 431.10 |
| SMA (Long) | 434.06 | 431.68 |
| RSI | 65.32 | 44.32 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 450.04
**Exit:** 
**Exit Price:** 448.19
**Position Size:** 
**PnL:** -3.65
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-02-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.57 | 12.17 |
| ATR | 10.38 | 10.67 |
| Volume | 10066612.00 | 3974018.00 |
| SMA (Short) | 431.44 | 439.33 |
| SMA (Long) | 429.56 | 440.30 |
| RSI | 56.30 | 39.47 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 447.47
**Exit:** 
**Exit Price:** 486.19
**Position Size:** 
**PnL:** 36.85
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.12 | 11.02 |
| ATR | 11.20 | 9.63 |
| Volume | 6386154.00 | 6229566.00 |
| SMA (Short) | 443.93 | 480.78 |
| SMA (Long) | 442.55 | 482.35 |
| RSI | 53.97 | 41.52 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 408.63
**Exit:** 
**Exit Price:** 389.5
**Position Size:** 
**PnL:** -20.72
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-01-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 6.18 | 6.50 |
| ATR | 9.11 | 8.86 |
| Volume | 6436742.00 | 8876480.00 |
| SMA (Short) | 399.76 | 393.45 |
| SMA (Long) | 399.33 | 394.92 |
| RSI | 61.91 | 30.87 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 410.7
**Exit:** 
**Exit Price:** 393.87
**Position Size:** 
**PnL:** -18.44
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-04-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 11.87 | 11.53 |
| ATR | 9.28 | 8.69 |
| Volume | 4650662.00 | 6696752.00 |
| SMA (Short) | 397.16 | 404.70 |
| SMA (Long) | 395.99 | 405.50 |
| RSI | 76.45 | 28.23 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 404.99
**Exit:** 
**Exit Price:** 383.96
**Position Size:** 
**PnL:** -22.61
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-06-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.98 | 4.37 |
| ATR | 7.46 | 7.36 |
| Volume | 3716910.00 | 15914040.00 |
| SMA (Short) | 394.60 | 386.95 |
| SMA (Long) | 394.01 | 388.13 |
| RSI | 71.13 | 37.25 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 401.36
**Exit:** 
**Exit Price:** 361.34
**Position Size:** 
**PnL:** -41.54
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-08-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.91 | 19.20 |
| ATR | 7.63 | 9.64 |
| Volume | 6275976.00 | 30443048.40 |
| SMA (Short) | 392.87 | 394.26 |
| SMA (Long) | 391.48 | 397.37 |
| RSI | 60.98 | 26.18 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 384.08
**Exit:** 
**Exit Price:** 480.29
**Position Size:** 
**PnL:** 94.48
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-10-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.72 | 6.29 |
| ATR | 7.95 | 10.79 |
| Volume | 5625102.00 | 7763544.00 |
| SMA (Short) | 381.39 | 480.76 |
| SMA (Long) | 380.12 | 481.26 |
| RSI | 64.37 | 39.26 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 483.2
**Exit:** 
**Exit Price:** 594.5
**Position Size:** 
**PnL:** 109.15
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.67 | 18.85 |
| ATR | 11.35 | 14.52 |
| Volume | 8526216.00 | 6222176.00 |
| SMA (Short) | 481.15 | 603.22 |
| SMA (Long) | 480.17 | 603.60 |
| RSI | 55.79 | 44.75 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 580.08
**Exit:** 
**Exit Price:** 566.7
**Position Size:** 
**PnL:** -15.67
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-12-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.93 | 16.99 |
| ATR | 17.91 | 16.16 |
| Volume | 7120933.00 | 3373319.00 |
| SMA (Short) | 578.52 | 568.88 |
| SMA (Long) | 577.26 | 569.62 |
| RSI | 61.10 | 45.86 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 581.45
**Exit:** 
**Exit Price:** 612.54
**Position Size:** 
**PnL:** 28.7
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-01-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 7.82 | 11.43 |
| ATR | 15.25 | 12.58 |
| Volume | 18130292.00 | 6415187.00 |
| SMA (Short) | 572.32 | 623.61 |
| SMA (Long) | 570.65 | 626.66 |
| RSI | 56.83 | 35.44 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 651.41
**Exit:** 
**Exit Price:** 636.84
**Position Size:** 
**PnL:** -17.15
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-04-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.86 | 14.53 |
| ATR | 12.39 | 12.11 |
| Volume | 6897127.00 | 8285120.00 |
| SMA (Short) | 640.13 | 636.28 |
| SMA (Long) | 636.99 | 637.59 |
| RSI | 71.83 | 39.62 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 651.58
**Exit:** 
**Exit Price:** 695.91
**Position Size:** 
**PnL:** 41.63
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.78 | 18.34 |
| ATR | 12.18 | 14.90 |
| Volume | 4435148.00 | 5881438.00 |
| SMA (Short) | 635.02 | 698.98 |
| SMA (Long) | 633.08 | 699.39 |
| RSI | 66.16 | 41.99 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 640.7
**Exit:** 
**Exit Price:** 663.09
**Position Size:** 
**PnL:** 19.78
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-12-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.83 | 22.70 |
| ATR | 17.07 | 14.08 |
| Volume | 5616324.00 | 9216022.00 |
| SMA (Short) | 638.67 | 684.39 |
| SMA (Long) | 636.95 | 687.32 |
| RSI | 63.76 | 32.37 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 597.54
**Exit:** 
**Exit Price:** 1152.19
**Position Size:** 
**PnL:** 551.15
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-05-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.21 | 16.61 |
| ATR | 31.74 | 29.34 |
| Volume | 7934250.00 | 15132388.00 |
| SMA (Short) | 602.10 | 1176.63 |
| SMA (Long) | 599.36 | 1181.22 |
| RSI | 55.43 | 30.61 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1237.0
**Exit:** 
**Exit Price:** 1222.15
**Position Size:** 
**PnL:** -19.77
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-05-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 32.07 | 9.10 |
| ATR | 29.70 | 29.97 |
| Volume | 6518173.00 | 4887060.00 |
| SMA (Short) | 1199.31 | 1238.93 |
| SMA (Long) | 1195.32 | 1239.70 |
| RSI | 64.95 | 19.71 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1295.14
**Exit:** 
**Exit Price:** 1601.88
**Position Size:** 
**PnL:** 300.95
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-05-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 28.62 | 26.80 |
| ATR | 26.29 | 27.65 |
| Volume | 4429904.00 | 4738376.00 |
| SMA (Short) | 1258.91 | 1570.50 |
| SMA (Long) | 1255.03 | 1574.86 |
| RSI | 75.75 | 56.31 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1665.35
**Exit:** 
**Exit Price:** 1589.31
**Position Size:** 
**PnL:** -82.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-12-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 32.41 | 21.99 |
| ATR | 30.78 | 37.09 |
| Volume | 13438109.00 | 3991449.00 |
| SMA (Short) | 1584.66 | 1607.78 |
| SMA (Long) | 1582.85 | 1610.15 |
| RSI | 61.48 | 32.87 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1643.73
**Exit:** 
**Exit Price:** 1627.66
**Position Size:** 
**PnL:** -22.62
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-01-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 20.32 | 92.70 |
| ATR | 37.20 | 37.13 |
| Volume | 3029169.00 | 8788872.00 |
| SMA (Short) | 1610.79 | 1677.78 |
| SMA (Long) | 1609.96 | 1685.18 |
| RSI | 44.61 | 35.94 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1724.31
**Exit:** 
**Exit Price:** 1464.35
**Position Size:** 
**PnL:** -266.34
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-04-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 58.68 | 99.27 |
| ATR | 41.83 | 43.09 |
| Volume | 7140443.00 | 17044923.00 |
| SMA (Short) | 1673.99 | 1653.67 |
| SMA (Long) | 1669.06 | 1670.82 |
| RSI | 64.16 | 10.74 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1434.81
**Exit:** 
**Exit Price:** 1384.45
**Position Size:** 
**PnL:** -55.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-09-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 18.69 | 46.62 |
| ATR | 36.56 | 31.78 |
| Volume | 3652582.00 | 3669352.00 |
| SMA (Short) | 1404.82 | 1423.81 |
| SMA (Long) | 1399.72 | 1434.05 |
| RSI | 74.01 | 25.52 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1438.03
**Exit:** 
**Exit Price:** 1445.79
**Position Size:** 
**PnL:** 2.0
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-10-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 33.15 | 38.06 |
| ATR | 30.70 | 29.39 |
| Volume | 982837.00 | 6236361.00 |
| SMA (Short) | 1396.96 | 1482.15 |
| SMA (Long) | 1396.47 | 1482.86 |
| RSI | 73.45 | 20.42 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1531.85
**Exit:** 
**Exit Price:** 1416.82
**Position Size:** 
**PnL:** -120.92
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-03-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 22.81 | 43.16 |
| ATR | 27.90 | 26.61 |
| Volume | 7040194.00 | 4615015.00 |
| SMA (Short) | 1484.00 | 1463.41 |
| SMA (Long) | 1479.59 | 1469.97 |
| RSI | 72.68 | 28.55 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1266.2
**Exit:** 
**Exit Price:** 1367.29
**Position Size:** 
**PnL:** 95.82
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-06-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.22 | 27.70 |
| ATR | 23.80 | 21.65 |
| Volume | 5002553.00 | 2636516.00 |
| SMA (Short) | 1258.03 | 1404.79 |
| SMA (Long) | 1254.51 | 1406.63 |
| RSI | 73.97 | 42.83 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1418.46
**Exit:** 
**Exit Price:** 1584.33
**Position Size:** 
**PnL:** 159.86
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.46 | 27.27 |
| ATR | 23.23 | 33.10 |
| Volume | 3755373.00 | 5688997.00 |
| SMA (Short) | 1408.85 | 1602.86 |
| SMA (Long) | 1401.60 | 1607.28 |
| RSI | 61.75 | 37.02 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1482.87
**Exit:** 
**Exit Price:** 1842.37
**Position Size:** 
**PnL:** 352.86
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 42.55 | 40.13 |
| ATR | 26.28 | 36.80 |
| Volume | 6810606.00 | 2906475.00 |
| SMA (Short) | 1430.04 | 1881.30 |
| SMA (Long) | 1427.67 | 1885.50 |
| RSI | 62.49 | 40.43 |

---

**Ticker:** INFY.NS  
**Entry:** 
**Entry Price:** 1924.5
**Exit:** 
**Exit Price:** 1800.7
**Position Size:** 
**PnL:** -131.25
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 37.72 | 54.98 |
| ATR | 40.95 | 41.82 |
| Volume | 4447143.00 | 7169109.00 |
| SMA (Short) | 1871.26 | 1891.75 |
| SMA (Long) | 1865.03 | 1897.20 |
| RSI | 74.23 | 29.14 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 264.95
**Exit:** 
**Exit Price:** 244.92
**Position Size:** 
**PnL:** -21.05
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-07-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 7.73 | 11.02 |
| ATR | 6.93 | 5.94 |
| Volume | 18385230.00 | 13705803.00 |
| SMA (Short) | 258.18 | 255.13 |
| SMA (Long) | 257.62 | 256.94 |
| RSI | 80.10 | 31.34 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 245.46
**Exit:** 
**Exit Price:** 254.68
**Position Size:** 
**PnL:** 8.22
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-08-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.97 | 6.72 |
| ATR | 6.37 | 6.42 |
| Volume | 10292540.00 | 9669851.00 |
| SMA (Short) | 257.24 | 257.33 |
| SMA (Long) | 257.20 | 257.54 |
| RSI | 36.61 | 58.39 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 241.0
**Exit:** 
**Exit Price:** 221.48
**Position Size:** 
**PnL:** -20.45
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.73 | 5.85 |
| ATR | 7.78 | 6.94 |
| Volume | 6759388.00 | 13448248.00 |
| SMA (Short) | 237.56 | 230.27 |
| SMA (Long) | 237.45 | 231.59 |
| RSI | 63.40 | 24.87 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 190.55
**Exit:** 
**Exit Price:** 188.48
**Position Size:** 
**PnL:** -2.82
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-05-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.63 | 8.45 |
| ATR | 7.23 | 6.99 |
| Volume | 17144832.00 | 32481385.00 |
| SMA (Short) | 184.36 | 189.14 |
| SMA (Long) | 182.23 | 189.60 |
| RSI | 80.17 | 23.69 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 205.91
**Exit:** 
**Exit Price:** 208.47
**Position Size:** 
**PnL:** 1.73
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-05-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.24 | 8.68 |
| ATR | 6.79 | 6.12 |
| Volume | 18249239.00 | 9477854.00 |
| SMA (Short) | 195.78 | 211.20 |
| SMA (Long) | 194.99 | 213.47 |
| RSI | 70.91 | 35.17 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 220.11
**Exit:** 
**Exit Price:** 215.25
**Position Size:** 
**PnL:** -5.72
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-10-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.84 | 5.45 |
| ATR | 5.91 | 5.94 |
| Volume | 15251016.00 | 10506728.00 |
| SMA (Short) | 215.11 | 219.67 |
| SMA (Long) | 214.96 | 221.22 |
| RSI | 62.98 | 29.17 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 244.42
**Exit:** 
**Exit Price:** 223.41
**Position Size:** 
**PnL:** -21.94
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.01 | 8.22 |
| ATR | 6.20 | 8.03 |
| Volume | 22219428.00 | 16611698.00 |
| SMA (Short) | 224.81 | 227.87 |
| SMA (Long) | 222.81 | 229.62 |
| RSI | 70.90 | 43.15 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 230.54
**Exit:** 
**Exit Price:** 237.93
**Position Size:** 
**PnL:** 6.45
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 5.47 | 6.26 |
| ATR | 6.51 | 5.87 |
| Volume | 6968061.00 | 13884032.00 |
| SMA (Short) | 225.41 | 236.57 |
| SMA (Long) | 224.70 | 237.43 |
| RSI | 74.74 | 50.84 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 241.24
**Exit:** 
**Exit Price:** 231.19
**Position Size:** 
**PnL:** -10.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-04-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.96 | 3.99 |
| ATR | 5.92 | 5.55 |
| Volume | 17014957.00 | 18165879.00 |
| SMA (Short) | 239.19 | 239.69 |
| SMA (Long) | 238.90 | 240.03 |
| RSI | 47.01 | 37.92 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 260.22
**Exit:** 
**Exit Price:** 279.16
**Position Size:** 
**PnL:** 17.86
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-05-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.88 | 4.31 |
| ATR | 5.75 | 6.17 |
| Volume | 30347849.00 | 8168684.00 |
| SMA (Short) | 242.08 | 279.38 |
| SMA (Long) | 239.80 | 280.26 |
| RSI | 65.32 | 36.45 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 285.21
**Exit:** 
**Exit Price:** 276.92
**Position Size:** 
**PnL:** -9.41
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.81 | 3.28 |
| ATR | 6.05 | 5.71 |
| Volume | 12737088.00 | 7639794.00 |
| SMA (Short) | 281.61 | 282.03 |
| SMA (Long) | 281.46 | 282.43 |
| RSI | 49.04 | 43.97 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 298.44
**Exit:** 
**Exit Price:** 294.73
**Position Size:** 
**PnL:** -4.9
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-01-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.85 | 2.03 |
| ATR | 6.88 | 6.35 |
| Volume | 38829935.00 | 8366713.00 |
| SMA (Short) | 273.33 | 297.57 |
| SMA (Long) | 272.56 | 297.73 |
| RSI | 74.44 | 39.90 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 302.54
**Exit:** 
**Exit Price:** 303.97
**Position Size:** 
**PnL:** 0.22
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-01-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.39 | 5.71 |
| ATR | 6.36 | 8.48 |
| Volume | 11699345.00 | 9974873.00 |
| SMA (Short) | 297.92 | 308.94 |
| SMA (Long) | 297.75 | 309.91 |
| RSI | 51.51 | 24.18 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 292.21
**Exit:** 
**Exit Price:** 272.73
**Position Size:** 
**PnL:** -20.6
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-06-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.70 | 4.16 |
| ATR | 8.29 | 8.29 |
| Volume | 16239386.00 | 16876061.00 |
| SMA (Short) | 276.67 | 273.32 |
| SMA (Long) | 276.33 | 274.66 |
| RSI | 61.48 | 46.00 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 286.3
**Exit:** 
**Exit Price:** 265.73
**Position Size:** 
**PnL:** -21.67
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-06-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.26 | 6.11 |
| ATR | 7.70 | 7.98 |
| Volume | 17490606.00 | 25318055.00 |
| SMA (Short) | 277.06 | 276.32 |
| SMA (Long) | 276.98 | 276.78 |
| RSI | 65.27 | 39.65 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 286.63
**Exit:** 
**Exit Price:** 302.06
**Position Size:** 
**PnL:** 14.24
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-08-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 16.51 | 7.22 |
| ATR | 7.35 | 9.41 |
| Volume | 15581508.00 | 21104376.00 |
| SMA (Short) | 271.82 | 302.22 |
| SMA (Long) | 269.51 | 303.38 |
| RSI | 67.10 | 32.93 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 332.55
**Exit:** 
**Exit Price:** 341.16
**Position Size:** 
**PnL:** 7.26
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-10-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.78 | 9.36 |
| ATR | 11.24 | 8.20 |
| Volume | 34460428.00 | 25605469.00 |
| SMA (Short) | 312.98 | 346.84 |
| SMA (Long) | 312.05 | 347.30 |
| RSI | 67.96 | 36.35 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 373.43
**Exit:** 
**Exit Price:** 362.71
**Position Size:** 
**PnL:** -12.2
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 12.97 | 10.55 |
| ATR | 8.31 | 8.82 |
| Volume | 37108265.00 | 16183425.00 |
| SMA (Short) | 350.04 | 372.05 |
| SMA (Long) | 347.54 | 372.67 |
| RSI | 83.17 | 37.99 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 415.33
**Exit:** 
**Exit Price:** 394.88
**Position Size:** 
**PnL:** -22.07
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 16.84 | 7.06 |
| ATR | 9.81 | 9.10 |
| Volume | 37708344.00 | 16505930.00 |
| SMA (Short) | 381.10 | 403.17 |
| SMA (Long) | 378.90 | 405.40 |
| RSI | 63.89 | 23.84 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 419.72
**Exit:** 
**Exit Price:** 508.12
**Position Size:** 
**PnL:** 86.55
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.93 | 4.22 |
| ATR | 11.73 | 9.50 |
| Volume | 19987241.00 | 16292578.00 |
| SMA (Short) | 401.53 | 512.35 |
| SMA (Long) | 398.23 | 512.83 |
| RSI | 63.78 | 39.50 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 522.96
**Exit:** 
**Exit Price:** 480.67
**Position Size:** 
**PnL:** -44.3
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-02-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.74 | 14.95 |
| ATR | 9.72 | 10.56 |
| Volume | 9227235.00 | 32737933.00 |
| SMA (Short) | 517.47 | 514.02 |
| SMA (Long) | 517.39 | 517.03 |
| RSI | 53.82 | 28.99 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 345.29
**Exit:** 
**Exit Price:** 346.79
**Position Size:** 
**PnL:** 0.11
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 23.45 | 15.03 |
| ATR | 23.71 | 14.53 |
| Volume | 37251097.00 | 48021824.00 |
| SMA (Short) | 320.06 | 342.24 |
| SMA (Long) | 319.40 | 343.57 |
| RSI | 63.26 | 52.32 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 355.78
**Exit:** 
**Exit Price:** 339.01
**Position Size:** 
**PnL:** -18.16
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-09-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 9.00 | 6.65 |
| ATR | 13.48 | 12.00 |
| Volume | 26257336.00 | 28932482.00 |
| SMA (Short) | 345.65 | 356.09 |
| SMA (Long) | 345.49 | 356.15 |
| RSI | 40.13 | 24.44 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 388.11
**Exit:** 
**Exit Price:** 548.58
**Position Size:** 
**PnL:** 158.59
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-10-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 18.44 | 19.08 |
| ATR | 11.26 | 19.02 |
| Volume | 41641237.00 | 24434219.00 |
| SMA (Short) | 359.40 | 572.17 |
| SMA (Long) | 357.44 | 577.82 |
| RSI | 62.93 | 27.21 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 582.7
**Exit:** 
**Exit Price:** 681.94
**Position Size:** 
**PnL:** 96.71
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-05-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.55 | 12.34 |
| ATR | 19.70 | 12.83 |
| Volume | 17253943.00 | 9383924.00 |
| SMA (Short) | 577.42 | 682.74 |
| SMA (Long) | 574.28 | 683.78 |
| RSI | 63.82 | 46.92 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 722.71
**Exit:** 
**Exit Price:** 692.55
**Position Size:** 
**PnL:** -32.98
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 15.72 | 19.77 |
| ATR | 12.95 | 18.42 |
| Volume | 15345601.00 | 23965914.00 |
| SMA (Short) | 688.05 | 723.07 |
| SMA (Long) | 686.65 | 724.15 |
| RSI | 56.36 | 14.75 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 769.05
**Exit:** 
**Exit Price:** 731.43
**Position Size:** 
**PnL:** -40.62
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 24.40 | 20.96 |
| ATR | 17.38 | 17.57 |
| Volume | 12250210.00 | 10967164.00 |
| SMA (Short) | 735.58 | 750.30 |
| SMA (Long) | 731.40 | 752.85 |
| RSI | 91.12 | 32.18 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 736.42
**Exit:** 
**Exit Price:** 674.57
**Position Size:** 
**PnL:** -64.68
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 14.82 | 15.74 |
| ATR | 19.97 | 18.52 |
| Volume | 13216391.00 | 16685166.00 |
| SMA (Short) | 717.93 | 701.46 |
| SMA (Long) | 716.24 | 701.84 |
| RSI | 72.82 | 21.43 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 726.87
**Exit:** 
**Exit Price:** 664.58
**Position Size:** 
**PnL:** -65.07
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 21.49 | 23.32 |
| ATR | 16.14 | 16.40 |
| Volume | 10949759.00 | 13348598.00 |
| SMA (Short) | 709.10 | 706.22 |
| SMA (Long) | 708.34 | 709.41 |
| RSI | 79.24 | 38.22 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 719.36
**Exit:** 
**Exit Price:** 860.76
**Position Size:** 
**PnL:** 138.24
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.91 | 18.50 |
| ATR | 15.92 | 17.05 |
| Volume | 10374018.00 | 9705750.00 |
| SMA (Short) | 694.39 | 842.20 |
| SMA (Long) | 693.81 | 845.50 |
| RSI | 74.39 | 42.28 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 874.75
**Exit:** 
**Exit Price:** 868.66
**Position Size:** 
**PnL:** -9.58
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 14.08 | 15.49 |
| ATR | 17.91 | 15.25 |
| Volume | 8097552.00 | 9788367.00 |
| SMA (Short) | 854.59 | 889.94 |
| SMA (Long) | 854.56 | 890.88 |
| RSI | 64.53 | 27.03 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 861.98
**Exit:** 
**Exit Price:** 900.7
**Position Size:** 
**PnL:** 35.19
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.19 | 7.26 |
| ATR | 17.22 | 12.64 |
| Volume | 26416933.00 | 8767733.00 |
| SMA (Short) | 836.07 | 907.30 |
| SMA (Long) | 831.86 | 907.42 |
| RSI | 78.04 | 30.90 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 935.71
**Exit:** 
**Exit Price:** 934.55
**Position Size:** 
**PnL:** -4.9
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-09-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 12.28 | 20.99 |
| ATR | 12.19 | 14.35 |
| Volume | 16334427.00 | 25991282.00 |
| SMA (Short) | 915.76 | 957.54 |
| SMA (Long) | 914.31 | 959.05 |
| RSI | 74.55 | 37.78 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 1004.8
**Exit:** 
**Exit Price:** 1113.27
**Position Size:** 
**PnL:** 104.23
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-12-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.44 | 20.66 |
| ATR | 14.11 | 24.36 |
| Volume | 31378461.00 | 18306176.00 |
| SMA (Short) | 937.20 | 1101.48 |
| SMA (Long) | 931.24 | 1103.16 |
| RSI | 77.80 | 49.22 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 1134.68
**Exit:** 
**Exit Price:** 1168.35
**Position Size:** 
**PnL:** 29.06
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-06-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.67 | 18.65 |
| ATR | 24.98 | 27.39 |
| Volume | 34309514.00 | 13117927.00 |
| SMA (Short) | 1108.72 | 1173.00 |
| SMA (Long) | 1104.49 | 1176.30 |
| RSI | 58.21 | 33.22 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 1221.9
**Exit:** 
**Exit Price:** 1249.1
**Position Size:** 
**PnL:** 22.26
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-08-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 22.64 | 17.77 |
| ATR | 23.52 | 25.53 |
| Volume | 10806748.00 | 11537317.00 |
| SMA (Short) | 1199.74 | 1268.97 |
| SMA (Long) | 1196.18 | 1269.50 |
| RSI | 75.79 | 24.93 |

---

**Ticker:** ICICIBANK.NS  
**Entry:** 
**Entry Price:** 1300.1
**Exit:** 
**Exit Price:** 1290.6
**Position Size:** 
**PnL:** -14.68
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.46 | 9.85 |
| ATR | 25.90 | 24.12 |
| Volume | 11397228.00 | 7433222.00 |
| SMA (Short) | 1278.11 | 1292.48 |
| SMA (Long) | 1275.10 | 1293.20 |
| RSI | 57.24 | 30.48 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 722.57
**Exit:** 
**Exit Price:** 721.12
**Position Size:** 
**PnL:** -4.34
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-05-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.67 | 14.63 |
| ATR | 24.81 | 22.19 |
| Volume | 1458520.00 | 1115144.00 |
| SMA (Short) | 734.73 | 730.55 |
| SMA (Long) | 734.50 | 732.12 |
| RSI |  |  |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 727.95
**Exit:** 
**Exit Price:** 709.76
**Position Size:** 
**PnL:** -21.06
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.45 | 10.39 |
| ATR | 19.70 | 19.81 |
| Volume | 928603.00 | 1074518.00 |
| SMA (Short) | 733.15 | 731.09 |
| SMA (Long) | 732.55 | 731.64 |
| RSI | 54.37 | 44.99 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 773.41
**Exit:** 
**Exit Price:** 752.79
**Position Size:** 
**PnL:** -23.67
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 27.30 | 16.40 |
| ATR | 18.72 | 17.47 |
| Volume | 1812148.00 | 373170.00 |
| SMA (Short) | 730.11 | 767.73 |
| SMA (Long) | 727.39 | 768.83 |
| RSI | 82.32 | 32.78 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 706.27
**Exit:** 
**Exit Price:** 704.53
**Position Size:** 
**PnL:** -4.56
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.27 | 15.50 |
| ATR | 14.88 | 15.38 |
| Volume | 1188716.00 | 1525578.00 |
| SMA (Short) | 693.67 | 715.60 |
| SMA (Long) | 693.65 | 718.87 |
| RSI | 55.37 | 30.13 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 739.28
**Exit:** 
**Exit Price:** 750.29
**Position Size:** 
**PnL:** 8.02
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-02-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 16.54 | 11.78 |
| ATR | 17.40 | 15.50 |
| Volume | 1191495.00 | 697299.00 |
| SMA (Short) | 722.27 | 746.90 |
| SMA (Long) | 719.39 | 749.30 |
| RSI | 57.38 | 29.85 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 780.3
**Exit:** 
**Exit Price:** 802.98
**Position Size:** 
**PnL:** 19.52
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-06-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 18.41 | 13.08 |
| ATR | 15.74 | 14.58 |
| Volume | 2185954.00 | 1102665.00 |
| SMA (Short) | 751.44 | 808.65 |
| SMA (Long) | 749.71 | 808.71 |
| RSI | 76.55 | 45.56 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 738.41
**Exit:** 
**Exit Price:** 723.73
**Position Size:** 
**PnL:** -17.6
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-12-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.40 | 8.89 |
| ATR | 15.29 | 14.98 |
| Volume | 317031.00 | 552176.00 |
| SMA (Short) | 744.22 | 739.27 |
| SMA (Long) | 743.70 | 741.18 |
| RSI | 55.46 | 41.76 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 736.59
**Exit:** 
**Exit Price:** 1082.04
**Position Size:** 
**PnL:** 341.81
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.10 | 17.59 |
| ATR | 14.63 | 21.62 |
| Volume | 337793.00 | 802675.00 |
| SMA (Short) | 732.60 | 1074.54 |
| SMA (Long) | 730.79 | 1077.75 |
| RSI | 71.59 | 32.33 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1117.29
**Exit:** 
**Exit Price:** 1215.35
**Position Size:** 
**PnL:** 93.39
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-10-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.35 | 23.14 |
| ATR | 21.59 | 23.45 |
| Volume | 840717.00 | 857401.00 |
| SMA (Short) | 1081.84 | 1212.56 |
| SMA (Long) | 1081.76 | 1213.16 |
| RSI | 52.38 | 44.32 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1244.89
**Exit:** 
**Exit Price:** 1487.09
**Position Size:** 
**PnL:** 236.74
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 21.66 | 67.22 |
| ATR | 21.62 | 33.49 |
| Volume | 588716.00 | 1571003.00 |
| SMA (Short) | 1203.18 | 1550.08 |
| SMA (Long) | 1203.06 | 1550.39 |
| RSI | 74.28 | 28.17 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1526.47
**Exit:** 
**Exit Price:** 1594.28
**Position Size:** 
**PnL:** 61.57
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 35.42 | 14.98 |
| ATR | 40.58 | 33.83 |
| Volume | 1125863.00 | 1628067.00 |
| SMA (Short) | 1474.86 | 1613.56 |
| SMA (Long) | 1470.00 | 1618.68 |
| RSI | 69.77 | 32.68 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1647.12
**Exit:** 
**Exit Price:** 1582.05
**Position Size:** 
**PnL:** -71.53
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-02-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 33.41 | 33.72 |
| ATR | 31.06 | 28.32 |
| Volume | 797453.00 | 1430235.00 |
| SMA (Short) | 1639.80 | 1630.58 |
| SMA (Long) | 1639.55 | 1633.58 |
| RSI | 62.51 | 50.04 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1582.69
**Exit:** 
**Exit Price:** 1540.02
**Position Size:** 
**PnL:** -48.91
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.42 | 27.66 |
| ATR | 23.02 | 23.81 |
| Volume | 1704890.00 | 1000696.00 |
| SMA (Short) | 1578.63 | 1560.84 |
| SMA (Long) | 1574.70 | 1562.50 |
| RSI | 75.63 | 38.04 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1629.28
**Exit:** 
**Exit Price:** 1578.27
**Position Size:** 
**PnL:** -57.42
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 33.64 | 30.23 |
| ATR | 24.98 | 29.33 |
| Volume | 1337466.00 | 725180.00 |
| SMA (Short) | 1563.72 | 1611.62 |
| SMA (Long) | 1558.57 | 1617.25 |
| RSI | 54.34 | 38.36 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1690.51
**Exit:** 
**Exit Price:** 1887.93
**Position Size:** 
**PnL:** 190.27
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-08-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 43.53 | 20.41 |
| ATR | 31.61 | 40.38 |
| Volume | 1910376.00 | 1600494.00 |
| SMA (Short) | 1633.12 | 1896.15 |
| SMA (Long) | 1626.04 | 1896.89 |
| RSI | 79.01 | 42.53 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 1899.2
**Exit:** 
**Exit Price:** 1851.76
**Position Size:** 
**PnL:** -54.95
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 51.66 | 81.78 |
| ATR | 29.40 | 53.27 |
| Volume | 750000.00 | 3732382.00 |
| SMA (Short) | 1854.62 | 1946.05 |
| SMA (Long) | 1851.60 | 1952.67 |
| RSI | 83.21 | 30.23 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2259.1
**Exit:** 
**Exit Price:** 1840.67
**Position Size:** 
**PnL:** -426.64
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-05-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 137.10 | 129.67 |
| ATR | 88.68 | 109.62 |
| Volume | 5896665.88 | 5896665.88 |
| SMA (Short) | 1994.25 | 2011.02 |
| SMA (Long) | 1979.22 | 2024.77 |
| RSI | 65.76 | 16.17 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2030.83
**Exit:** 
**Exit Price:** 2039.37
**Position Size:** 
**PnL:** 0.4
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 45.10 | 10.64 |
| ATR | 59.87 | 38.81 |
| Volume | 3295039.00 | 2148146.00 |
| SMA (Short) | 1969.28 | 2048.02 |
| SMA (Long) | 1955.92 | 2050.12 |
| RSI | 65.53 | 39.15 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2009.24
**Exit:** 
**Exit Price:** 1976.92
**Position Size:** 
**PnL:** -40.29
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-11-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.45 | 41.42 |
| ATR | 34.80 | 39.30 |
| Volume | 1640399.00 | 2083827.00 |
| SMA (Short) | 1999.81 | 1983.50 |
| SMA (Long) | 1999.78 | 1984.45 |
| RSI | 65.99 | 43.95 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2054.97
**Exit:** 
**Exit Price:** 2111.63
**Position Size:** 
**PnL:** 48.32
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 44.83 | 67.97 |
| ATR | 39.77 | 48.60 |
| Volume | 2799165.00 | 2908003.00 |
| SMA (Short) | 1989.95 | 2171.21 |
| SMA (Long) | 1985.80 | 2178.99 |
| RSI | 55.57 | 28.22 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2180.27
**Exit:** 
**Exit Price:** 2213.56
**Position Size:** 
**PnL:** 24.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-03-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 55.21 | 20.13 |
| ATR | 45.13 | 50.45 |
| Volume | 1762743.00 | 811095.00 |
| SMA (Short) | 2129.88 | 2215.16 |
| SMA (Long) | 2120.69 | 2221.95 |
| RSI | 67.81 | 43.07 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2351.66
**Exit:** 
**Exit Price:** 2218.59
**Position Size:** 
**PnL:** -142.21
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-07-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 45.76 | 34.73 |
| ATR | 42.99 | 34.95 |
| Volume | 3937751.00 | 1656945.00 |
| SMA (Short) | 2252.30 | 2268.62 |
| SMA (Long) | 2243.51 | 2272.97 |
| RSI | 83.60 | 20.27 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2480.95
**Exit:** 
**Exit Price:** 2412.18
**Position Size:** 
**PnL:** -78.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-10-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 72.45 | 39.73 |
| ATR | 39.57 | 51.43 |
| Volume | 5779927.00 | 5431133.00 |
| SMA (Short) | 2305.41 | 2512.06 |
| SMA (Long) | 2295.17 | 2518.53 |
| RSI | 90.78 | 24.43 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2302.5
**Exit:** 
**Exit Price:** 2187.39
**Position Size:** 
**PnL:** -124.1
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-01-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 45.17 | 49.69 |
| ATR | 37.09 | 41.59 |
| Volume | 1026186.00 | 2620474.00 |
| SMA (Short) | 2247.95 | 2224.34 |
| SMA (Long) | 2245.19 | 2230.83 |
| RSI | 85.39 | 38.85 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2075.22
**Exit:** 
**Exit Price:** 2063.79
**Position Size:** 
**PnL:** -19.71
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 39.12 | 45.79 |
| ATR | 46.86 | 56.11 |
| Volume | 1828131.00 | 1353485.00 |
| SMA (Short) | 2045.19 | 2103.93 |
| SMA (Long) | 2041.00 | 2107.12 |
| RSI | 84.43 | 14.23 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2228.14
**Exit:** 
**Exit Price:** 2461.51
**Position Size:** 
**PnL:** 223.99
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-06-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 71.86 | 14.99 |
| ATR | 58.93 | 51.38 |
| Volume | 1404108.00 | 1199906.00 |
| SMA (Short) | 2134.47 | 2480.98 |
| SMA (Long) | 2122.60 | 2484.88 |
| RSI | 74.04 | 47.25 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2557.79
**Exit:** 
**Exit Price:** 2476.32
**Position Size:** 
**PnL:** -91.54
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-10-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 51.01 | 48.71 |
| ATR | 51.84 | 52.45 |
| Volume | 2678551.00 | 1001536.00 |
| SMA (Short) | 2506.15 | 2508.27 |
| SMA (Long) | 2504.92 | 2515.08 |
| RSI | 64.46 | 36.46 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2530.97
**Exit:** 
**Exit Price:** 2500.58
**Position Size:** 
**PnL:** -40.45
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-01-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 68.52 | 33.27 |
| ATR | 51.85 | 42.22 |
| Volume | 2101890.00 | 2008493.00 |
| SMA (Short) | 2490.49 | 2493.58 |
| SMA (Long) | 2484.00 | 2499.57 |
| RSI | 69.83 | 34.15 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2581.73
**Exit:** 
**Exit Price:** 2485.53
**Position Size:** 
**PnL:** -106.34
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-01-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 38.73 | 39.48 |
| ATR | 43.75 | 46.49 |
| Volume | 1892865.00 | 2744039.00 |
| SMA (Short) | 2519.85 | 2530.76 |
| SMA (Long) | 2513.19 | 2532.97 |
| RSI | 61.83 | 44.28 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2450.68
**Exit:** 
**Exit Price:** 2372.82
**Position Size:** 
**PnL:** -87.51
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-05-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 36.99 | 31.74 |
| ATR | 42.32 | 39.31 |
| Volume | 853322.00 | 1760370.00 |
| SMA (Short) | 2444.26 | 2413.97 |
| SMA (Long) | 2442.91 | 2417.79 |
| RSI | 59.46 | 31.07 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2509.0
**Exit:** 
**Exit Price:** 2505.83
**Position Size:** 
**PnL:** -13.2
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-07-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 37.44 | 45.21 |
| ATR | 39.16 | 42.08 |
| Volume | 1749356.00 | 1653775.00 |
| SMA (Short) | 2421.37 | 2585.40 |
| SMA (Long) | 2416.79 | 2593.03 |
| RSI | 69.99 | 24.33 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2496.22
**Exit:** 
**Exit Price:** 2418.74
**Position Size:** 
**PnL:** -87.3
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-10-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 34.95 | 38.31 |
| ATR | 30.38 | 30.45 |
| Volume | 954899.00 | 875135.00 |
| SMA (Short) | 2465.12 | 2449.49 |
| SMA (Long) | 2460.82 | 2453.74 |
| RSI | 68.09 | 39.87 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2435.75
**Exit:** 
**Exit Price:** 2334.9
**Position Size:** 
**PnL:** -110.39
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-01-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.82 | 57.53 |
| ATR | 30.58 | 37.05 |
| Volume | 760809.00 | 4369332.00 |
| SMA (Short) | 2444.52 | 2499.63 |
| SMA (Long) | 2443.87 | 2503.68 |
| RSI | 53.46 | 20.59 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2309.39
**Exit:** 
**Exit Price:** 2718.01
**Position Size:** 
**PnL:** 398.56
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 64.58 | 26.81 |
| ATR | 34.55 | 46.91 |
| Volume | 689430.00 | 1368242.00 |
| SMA (Short) | 2265.45 | 2763.73 |
| SMA (Long) | 2257.42 | 2770.34 |
| RSI | 63.27 | 23.44 |

---

**Ticker:** HINDUNILVR.NS  
**Entry:** 
**Entry Price:** 2441.95
**Exit:** 
**Exit Price:** 2318.35
**Position Size:** 
**PnL:** -133.12
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-02-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 56.64 | 61.25 |
| ATR | 48.66 | 49.93 |
| Volume | 2528480.00 | 1135380.00 |
| SMA (Short) | 2402.40 | 2365.67 |
| SMA (Long) | 2396.19 | 2373.90 |
| RSI | 60.13 | 39.91 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 659.41
**Exit:** 
**Exit Price:** 684.51
**Position Size:** 
**PnL:** 22.41
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.88 | 15.84 |
| ATR | 23.35 | 21.54 |
| Volume | 1692246.00 | 1568460.00 |
| SMA (Short) | 666.47 | 666.04 |
| SMA (Long) | 665.96 | 668.32 |
| RSI |  |  |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 694.55
**Exit:** 
**Exit Price:** 636.6
**Position Size:** 
**PnL:** -60.61
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 14.30 | 15.89 |
| ATR | 20.45 | 17.98 |
| Volume | 1083812.00 | 1574396.00 |
| SMA (Short) | 672.14 | 671.83 |
| SMA (Long) | 671.20 | 673.57 |
| RSI | 58.86 | 26.74 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 689.21
**Exit:** 
**Exit Price:** 687.07
**Position Size:** 
**PnL:** -4.89
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.51 | 9.72 |
| ATR | 18.65 | 18.06 |
| Volume | 1879370.00 | 592486.00 |
| SMA (Short) | 676.03 | 693.20 |
| SMA (Long) | 672.14 | 693.45 |
| RSI | 59.32 | 34.53 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 713.88
**Exit:** 
**Exit Price:** 644.15
**Position Size:** 
**PnL:** -72.44
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.89 | 20.11 |
| ATR | 18.48 | 19.07 |
| Volume | 822516.00 | 2496993.00 |
| SMA (Short) | 695.41 | 693.25 |
| SMA (Long) | 694.24 | 698.68 |
| RSI | 51.06 | 36.62 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 650.57
**Exit:** 
**Exit Price:** 659.12
**Position Size:** 
**PnL:** 5.93
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-10-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.20 | 13.97 |
| ATR | 20.86 | 15.48 |
| Volume | 964026.00 | 710377.00 |
| SMA (Short) | 653.47 | 679.09 |
| SMA (Long) | 653.34 | 682.67 |
| RSI | 51.92 | 20.62 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 667.93
**Exit:** 
**Exit Price:** 778.99
**Position Size:** 
**PnL:** 108.17
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 12.09 | 6.48 |
| ATR | 19.16 | 13.89 |
| Volume | 1966330.00 | 740458.00 |
| SMA (Short) | 653.37 | 779.50 |
| SMA (Long) | 651.29 | 780.04 |
| RSI | 53.08 | 36.64 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 801.78
**Exit:** 
**Exit Price:** 766.0
**Position Size:** 
**PnL:** -38.92
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 17.53 | 22.09 |
| ATR | 14.39 | 17.03 |
| Volume | 1175512.00 | 1700599.00 |
| SMA (Short) | 788.46 | 787.96 |
| SMA (Long) | 787.19 | 789.04 |
| RSI | 59.81 | 34.51 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 791.48
**Exit:** 
**Exit Price:** 952.77
**Position Size:** 
**PnL:** 157.8
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.24 | 7.17 |
| ATR | 14.46 | 14.88 |
| Volume | 8772524.00 | 1664448.00 |
| SMA (Short) | 733.21 | 953.36 |
| SMA (Long) | 728.55 | 953.38 |
| RSI | 84.56 | 33.19 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 958.2
**Exit:** 
**Exit Price:** 972.09
**Position Size:** 
**PnL:** 10.03
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-07-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.92 | 10.56 |
| ATR | 14.94 | 18.14 |
| Volume | 2787244.00 | 621906.00 |
| SMA (Short) | 954.78 | 977.67 |
| SMA (Long) | 954.29 | 977.71 |
| RSI | 32.86 | 40.55 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1003.46
**Exit:** 
**Exit Price:** 1009.19
**Position Size:** 
**PnL:** 1.7
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-09-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.09 | 15.44 |
| ATR | 18.60 | 21.69 |
| Volume | 2076538.00 | 1850889.00 |
| SMA (Short) | 980.41 | 1015.35 |
| SMA (Long) | 978.42 | 1017.17 |
| RSI | 59.56 | 28.55 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1029.06
**Exit:** 
**Exit Price:** 1034.58
**Position Size:** 
**PnL:** 1.4
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-01-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.63 | 20.64 |
| ATR | 15.40 | 21.72 |
| Volume | 1158187.00 | 1961492.00 |
| SMA (Short) | 1009.31 | 1060.67 |
| SMA (Long) | 1009.16 | 1060.90 |
| RSI | 60.70 | 25.79 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1114.66
**Exit:** 
**Exit Price:** 1302.21
**Position Size:** 
**PnL:** 182.72
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.55 | 34.85 |
| ATR | 23.39 | 26.58 |
| Volume | 1293385.00 | 1827739.00 |
| SMA (Short) | 1070.09 | 1323.08 |
| SMA (Long) | 1068.94 | 1327.37 |
| RSI | 58.52 | 21.21 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1166.45
**Exit:** 
**Exit Price:** 1221.6
**Position Size:** 
**PnL:** 50.38
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.30 | 30.33 |
| ATR | 36.61 | 24.16 |
| Volume | 1257089.00 | 2162834.00 |
| SMA (Short) | 1156.72 | 1246.22 |
| SMA (Long) | 1155.19 | 1247.84 |
| RSI | 67.78 | 22.79 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1338.88
**Exit:** 
**Exit Price:** 1491.29
**Position Size:** 
**PnL:** 146.75
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-03-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 37.53 | 20.83 |
| ATR | 24.51 | 32.36 |
| Volume | 5384740.00 | 2257753.00 |
| SMA (Short) | 1262.48 | 1491.28 |
| SMA (Long) | 1252.93 | 1492.55 |
| RSI | 80.06 | 52.08 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1455.7
**Exit:** 
**Exit Price:** 1471.85
**Position Size:** 
**PnL:** 10.3
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-08-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.10 | 16.92 |
| ATR | 32.30 | 32.50 |
| Volume | 3864546.00 | 2362381.00 |
| SMA (Short) | 1492.73 | 1489.77 |
| SMA (Long) | 1491.71 | 1490.17 |
| RSI | 43.53 | 40.23 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1498.22
**Exit:** 
**Exit Price:** 1446.48
**Position Size:** 
**PnL:** -57.63
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-08-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.09 | 18.26 |
| ATR | 32.80 | 33.19 |
| Volume | 1932121.00 | 3931367.00 |
| SMA (Short) | 1491.54 | 1485.86 |
| SMA (Long) | 1489.96 | 1488.15 |
| RSI | 50.63 | 45.02 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1635.66
**Exit:** 
**Exit Price:** 1601.01
**Position Size:** 
**PnL:** -41.12
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-01-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 57.21 | 40.72 |
| ATR | 38.81 | 27.34 |
| Volume | 6854029.00 | 3495683.00 |
| SMA (Short) | 1486.34 | 1651.23 |
| SMA (Long) | 1483.24 | 1653.12 |
| RSI | 75.66 | 40.42 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1709.73
**Exit:** 
**Exit Price:** 1621.4
**Position Size:** 
**PnL:** -95.0
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.46 | 33.89 |
| ATR | 31.30 | 33.33 |
| Volume | 3010537.00 | 2918386.00 |
| SMA (Short) | 1672.25 | 1657.69 |
| SMA (Long) | 1667.67 | 1662.36 |
| RSI | 67.93 | 39.92 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1382.37
**Exit:** 
**Exit Price:** 1303.51
**Position Size:** 
**PnL:** -84.23
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-08-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 82.36 | 19.99 |
| ATR | 81.98 | 44.02 |
| Volume | 12344415.00 | 3331502.00 |
| SMA (Short) | 1223.56 | 1331.27 |
| SMA (Long) | 1218.63 | 1332.80 |
| RSI | 74.92 | 47.12 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1323.55
**Exit:** 
**Exit Price:** 1319.96
**Position Size:** 
**PnL:** -8.88
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-09-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 17.92 | 43.41 |
| ATR | 43.55 | 40.87 |
| Volume | 2831340.00 | 5029913.00 |
| SMA (Short) | 1333.16 | 1348.36 |
| SMA (Long) | 1332.61 | 1351.64 |
| RSI | 37.27 | 32.69 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1389.1
**Exit:** 
**Exit Price:** 1852.2
**Position Size:** 
**PnL:** 456.62
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-10-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 28.01 | 39.73 |
| ATR | 38.50 | 44.59 |
| Volume | 4280446.00 | 5668862.00 |
| SMA (Short) | 1339.56 | 1886.93 |
| SMA (Long) | 1334.88 | 1891.74 |
| RSI | 72.40 | 26.93 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1945.17
**Exit:** 
**Exit Price:** 1839.09
**Position Size:** 
**PnL:** -113.65
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 83.49 | 69.64 |
| ATR | 46.59 | 52.57 |
| Volume | 1690753.00 | 3837149.00 |
| SMA (Short) | 1912.07 | 1891.61 |
| SMA (Long) | 1899.53 | 1903.36 |
| RSI | 63.42 | 39.06 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1912.87
**Exit:** 
**Exit Price:** 1807.19
**Position Size:** 
**PnL:** -113.12
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 57.30 | 58.76 |
| ATR | 55.71 | 58.08 |
| Volume | 2643553.00 | 4250856.00 |
| SMA (Short) | 1906.47 | 1881.13 |
| SMA (Long) | 1897.89 | 1883.10 |
| RSI | 47.04 | 45.08 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1777.73
**Exit:** 
**Exit Price:** 1732.67
**Position Size:** 
**PnL:** -52.08
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-06-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.43 | 19.39 |
| ATR | 47.74 | 40.73 |
| Volume | 3098849.00 | 3595393.00 |
| SMA (Short) | 1762.65 | 1757.11 |
| SMA (Long) | 1761.76 | 1758.58 |
| RSI | 62.09 | 26.54 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1783.2
**Exit:** 
**Exit Price:** 1731.48
**Position Size:** 
**PnL:** -58.75
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-08-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 62.28 | 36.82 |
| ATR | 32.95 | 33.25 |
| Volume | 1641690.00 | 2561253.00 |
| SMA (Short) | 1741.61 | 1724.63 |
| SMA (Long) | 1739.47 | 1727.72 |
| RSI | 60.03 | 40.78 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1787.34
**Exit:** 
**Exit Price:** 1959.36
**Position Size:** 
**PnL:** 164.52
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-09-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 32.71 | 47.76 |
| ATR | 32.50 | 51.69 |
| Volume | 4845134.00 | 2647553.00 |
| SMA (Short) | 1729.08 | 2023.05 |
| SMA (Long) | 1728.64 | 2023.60 |
| RSI | 50.81 | 39.90 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1932.57
**Exit:** 
**Exit Price:** 1742.45
**Position Size:** 
**PnL:** -197.47
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 41.36 | 52.06 |
| ATR | 50.31 | 52.48 |
| Volume | 1676473.00 | 3026821.00 |
| SMA (Short) | 1916.59 | 1849.50 |
| SMA (Long) | 1913.15 | 1854.63 |
| RSI | 73.45 | 41.39 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1792.63
**Exit:** 
**Exit Price:** 1671.58
**Position Size:** 
**PnL:** -127.97
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 22.90 | 69.27 |
| ATR | 50.56 | 44.58 |
| Volume | 1989854.00 | 2973292.00 |
| SMA (Short) | 1768.35 | 1793.28 |
| SMA (Long) | 1766.01 | 1796.17 |
| RSI | 67.84 | 13.88 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1796.02
**Exit:** 
**Exit Price:** 1815.71
**Position Size:** 
**PnL:** 12.47
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 44.33 | 63.46 |
| ATR | 40.82 | 45.62 |
| Volume | 2186674.00 | 2804653.00 |
| SMA (Short) | 1776.88 | 1851.30 |
| SMA (Long) | 1772.55 | 1861.06 |
| RSI | 72.87 | 32.28 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1898.3
**Exit:** 
**Exit Price:** 1837.02
**Position Size:** 
**PnL:** -68.75
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 22.54 | 33.14 |
| ATR | 43.72 | 30.42 |
| Volume | 1874348.00 | 2487828.00 |
| SMA (Short) | 1871.11 | 1884.52 |
| SMA (Long) | 1867.76 | 1888.54 |
| RSI | 67.01 | 22.76 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1842.96
**Exit:** 
**Exit Price:** 1829.99
**Position Size:** 
**PnL:** -20.32
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-06-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 45.95 | 41.20 |
| ATR | 31.36 | 36.14 |
| Volume | 9293763.00 | 4838188.00 |
| SMA (Short) | 1737.73 | 1891.78 |
| SMA (Long) | 1728.96 | 1900.80 |
| RSI | 84.82 | 34.85 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1966.42
**Exit:** 
**Exit Price:** 1819.76
**Position Size:** 
**PnL:** -154.24
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-08-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 38.04 | 47.30 |
| ATR | 32.55 | 33.25 |
| Volume | 3849750.00 | 7015292.00 |
| SMA (Short) | 1893.55 | 1870.64 |
| SMA (Long) | 1892.30 | 1879.15 |
| RSI | 80.79 | 42.53 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1765.27
**Exit:** 
**Exit Price:** 1782.55
**Position Size:** 
**PnL:** 10.19
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.38 | 30.30 |
| ATR | 24.91 | 28.40 |
| Volume | 2705765.00 | 6780824.00 |
| SMA (Short) | 1756.16 | 1808.89 |
| SMA (Long) | 1755.40 | 1813.71 |
| RSI | 63.56 | 28.25 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1783.55
**Exit:** 
**Exit Price:** 1622.17
**Position Size:** 
**PnL:** -168.18
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-04-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.90 | 90.50 |
| ATR | 34.63 | 35.71 |
| Volume | 6630072.00 | 14494212.72 |
| SMA (Short) | 1757.77 | 1733.41 |
| SMA (Long) | 1756.87 | 1744.61 |
| RSI | 58.10 | 30.92 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1724.46
**Exit:** 
**Exit Price:** 1747.9
**Position Size:** 
**PnL:** 16.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-06-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 32.67 | 18.73 |
| ATR | 39.62 | 40.01 |
| Volume | 6016145.00 | 2585649.00 |
| SMA (Short) | 1713.19 | 1773.18 |
| SMA (Long) | 1708.99 | 1779.29 |
| RSI | 53.53 | 42.74 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1803.35
**Exit:** 
**Exit Price:** 1783.8
**Position Size:** 
**PnL:** -26.72
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-09-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 26.39 | 17.00 |
| ATR | 36.21 | 34.50 |
| Volume | 4541696.00 | 3192443.00 |
| SMA (Short) | 1793.26 | 1795.26 |
| SMA (Long) | 1793.19 | 1797.41 |
| RSI | 62.41 | 64.30 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1846.65
**Exit:** 
**Exit Price:** 1749.85
**Position Size:** 
**PnL:** -103.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 26.27 | 62.77 |
| ATR | 30.87 | 33.50 |
| Volume | 3674862.00 | 3302148.00 |
| SMA (Short) | 1802.27 | 1810.77 |
| SMA (Long) | 1796.79 | 1825.32 |
| RSI | 69.39 | 41.37 |

---

**Ticker:** KOTAKBANK.NS  
**Entry:** 
**Entry Price:** 1804.45
**Exit:** 
**Exit Price:** 1740.7
**Position Size:** 
**PnL:** -70.84
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-12-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.91 | 23.78 |
| ATR | 34.23 | 31.70 |
| Volume | 2989393.00 | 5502772.00 |
| SMA (Short) | 1781.39 | 1762.20 |
| SMA (Long) | 1779.05 | 1762.52 |
| RSI | 56.74 | 36.53 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 922.08
**Exit:** 
**Exit Price:** 991.36
**Position Size:** 
**PnL:** 65.45
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.80 | 16.18 |
| ATR | 20.21 | 22.96 |
| Volume | 2059530.00 | 3087904.00 |
| SMA (Short) | 919.83 | 1017.64 |
| SMA (Long) | 917.96 | 1022.42 |
| RSI | 59.68 | 43.52 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 682.73
**Exit:** 
**Exit Price:** 853.71
**Position Size:** 
**PnL:** 167.9
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 28.80 | 24.85 |
| ATR | 23.68 | 19.33 |
| Volume | 2932767.00 | 1683261.00 |
| SMA (Short) | 663.17 | 868.24 |
| SMA (Long) | 661.13 | 874.03 |
| RSI | 55.59 | 36.18 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 864.73
**Exit:** 
**Exit Price:** 827.26
**Position Size:** 
**PnL:** -40.85
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 14.20 | 15.83 |
| ATR | 17.17 | 17.27 |
| Volume | 838206.00 | 10392624.08 |
| SMA (Short) | 861.28 | 856.61 |
| SMA (Long) | 860.29 | 858.77 |
| RSI | 53.33 | 35.64 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 822.92
**Exit:** 
**Exit Price:** 991.52
**Position Size:** 
**PnL:** 164.96
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 13.01 | 10.30 |
| ATR | 16.42 | 20.48 |
| Volume | 1514451.00 | 2317045.00 |
| SMA (Short) | 801.48 | 1013.06 |
| SMA (Long) | 798.20 | 1014.62 |
| RSI | 81.76 | 34.00 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1045.06
**Exit:** 
**Exit Price:** 1000.9
**Position Size:** 
**PnL:** -48.25
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-08-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 22.15 | 12.24 |
| ATR | 20.60 | 19.13 |
| Volume | 1827242.00 | 1361351.00 |
| SMA (Short) | 1021.85 | 1018.29 |
| SMA (Long) | 1016.93 | 1020.50 |
| RSI | 80.91 | 22.57 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1090.59
**Exit:** 
**Exit Price:** 1013.75
**Position Size:** 
**PnL:** -81.04
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-10-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.29 | 33.95 |
| ATR | 19.20 | 21.27 |
| Volume | 4364705.00 | 1303081.00 |
| SMA (Short) | 1024.41 | 1035.09 |
| SMA (Long) | 1023.63 | 1038.56 |
| RSI | 75.61 | 26.87 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1096.68
**Exit:** 
**Exit Price:** 1165.68
**Position Size:** 
**PnL:** 64.47
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-10-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 32.07 | 25.98 |
| ATR | 21.10 | 27.87 |
| Volume | 2036609.00 | 2176017.00 |
| SMA (Short) | 1042.71 | 1180.48 |
| SMA (Long) | 1038.27 | 1181.59 |
| RSI | 79.96 | 26.57 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1215.6
**Exit:** 
**Exit Price:** 1232.61
**Position Size:** 
**PnL:** 12.12
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.64 | 22.79 |
| ATR | 27.33 | 24.74 |
| Volume | 1695410.00 | 2127978.00 |
| SMA (Short) | 1191.62 | 1202.20 |
| SMA (Long) | 1187.54 | 1203.15 |
| RSI | 60.23 | 53.09 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1228.99
**Exit:** 
**Exit Price:** 1223.61
**Position Size:** 
**PnL:** -10.28
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-06-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 23.51 | 12.88 |
| ATR | 25.02 | 24.61 |
| Volume | 2234018.00 | 1853562.00 |
| SMA (Short) | 1209.45 | 1214.24 |
| SMA (Long) | 1209.45 | 1215.28 |
| RSI | 47.03 | 61.58 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1226.22
**Exit:** 
**Exit Price:** 1129.54
**Position Size:** 
**PnL:** -101.39
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-10-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 35.52 | 32.02 |
| ATR | 24.63 | 25.32 |
| Volume | 8248115.00 | 4302314.00 |
| SMA (Short) | 1158.66 | 1182.29 |
| SMA (Long) | 1155.20 | 1184.75 |
| RSI | 66.52 | 25.75 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1238.83
**Exit:** 
**Exit Price:** 1209.76
**Position Size:** 
**PnL:** -33.96
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 59.80 | 28.30 |
| ATR | 27.27 | 25.31 |
| Volume | 255086.00 | 3080984.00 |
| SMA (Short) | 1178.47 | 1260.52 |
| SMA (Long) | 1174.63 | 1269.49 |
| RSI | 82.56 | 29.10 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1259.64
**Exit:** 
**Exit Price:** 1195.03
**Position Size:** 
**PnL:** -69.53
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 33.84 | 11.80 |
| ATR | 26.10 | 23.90 |
| Volume | 6631152.00 | 3422913.00 |
| SMA (Short) | 1197.35 | 1227.84 |
| SMA (Long) | 1196.48 | 1229.47 |
| RSI | 82.88 | 33.69 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1325.13
**Exit:** 
**Exit Price:** 1301.64
**Position Size:** 
**PnL:** -28.74
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 48.08 | 41.36 |
| ATR | 26.62 | 35.17 |
| Volume | 3304912.00 | 2342881.00 |
| SMA (Short) | 1247.75 | 1344.93 |
| SMA (Long) | 1242.43 | 1357.19 |
| RSI | 69.78 | 29.03 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1404.19
**Exit:** 
**Exit Price:** 1254.67
**Position Size:** 
**PnL:** -154.83
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-11-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 57.86 | 31.29 |
| ATR | 34.63 | 31.46 |
| Volume | 10392624.08 | 2396206.00 |
| SMA (Short) | 1255.13 | 1290.66 |
| SMA (Long) | 1255.01 | 1298.80 |
| RSI | 74.75 | 19.49 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1238.92
**Exit:** 
**Exit Price:** 1191.79
**Position Size:** 
**PnL:** -51.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-02-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.38 | 32.04 |
| ATR | 22.03 | 22.14 |
| Volume | 2510013.00 | 2568696.00 |
| SMA (Short) | 1214.43 | 1204.75 |
| SMA (Long) | 1213.39 | 1204.89 |
| RSI | 57.06 | 42.11 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 864.6
**Exit:** 
**Exit Price:** 858.83
**Position Size:** 
**PnL:** -9.22
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-07-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 44.79 | 9.02 |
| ATR | 43.55 | 26.32 |
| Volume | 7617144.00 | 7245021.00 |
| SMA (Short) | 793.97 | 855.66 |
| SMA (Long) | 787.03 | 856.58 |
| RSI | 66.78 | 40.64 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 903.87
**Exit:** 
**Exit Price:** 862.05
**Position Size:** 
**PnL:** -45.35
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-09-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.69 | 21.24 |
| ATR | 23.58 | 20.95 |
| Volume | 5427516.00 | 2632298.00 |
| SMA (Short) | 867.28 | 879.16 |
| SMA (Long) | 866.44 | 883.39 |
| RSI | 68.80 | 26.15 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 922.71
**Exit:** 
**Exit Price:** 1311.45
**Position Size:** 
**PnL:** 384.28
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-10-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 26.61 | 50.25 |
| ATR | 21.13 | 42.87 |
| Volume | 9638520.00 | 4237815.00 |
| SMA (Short) | 869.57 | 1382.60 |
| SMA (Long) | 869.44 | 1395.51 |
| RSI | 75.48 | 26.63 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1382.43
**Exit:** 
**Exit Price:** 1726.86
**Position Size:** 
**PnL:** 338.21
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-05-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.00 | 43.13 |
| ATR | 35.96 | 45.35 |
| Volume | 5035538.00 | 1566109.00 |
| SMA (Short) | 1346.55 | 1750.25 |
| SMA (Long) | 1338.16 | 1752.73 |
| RSI | 73.05 | 22.38 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1807.31
**Exit:** 
**Exit Price:** 1742.69
**Position Size:** 
**PnL:** -71.71
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 40.69 | 52.96 |
| ATR | 44.70 | 44.05 |
| Volume | 1685243.00 | 2290199.00 |
| SMA (Short) | 1769.11 | 1847.79 |
| SMA (Long) | 1765.60 | 1849.17 |
| RSI | 50.59 | 37.90 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1610.95
**Exit:** 
**Exit Price:** 1812.79
**Position Size:** 
**PnL:** 194.99
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 47.76 | 38.03 |
| ATR | 42.02 | 38.61 |
| Volume | 1316037.00 | 2339518.00 |
| SMA (Short) | 1539.66 | 1832.26 |
| SMA (Long) | 1532.25 | 1833.77 |
| RSI | 75.99 | 30.22 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1881.86
**Exit:** 
**Exit Price:** 1841.29
**Position Size:** 
**PnL:** -48.02
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-10-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.15 | 17.44 |
| ATR | 40.81 | 41.18 |
| Volume | 1401849.00 | 2225676.00 |
| SMA (Short) | 1863.90 | 1861.62 |
| SMA (Long) | 1857.89 | 1863.55 |
| RSI | 59.53 | 53.76 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 1912.28
**Exit:** 
**Exit Price:** 2100.7
**Position Size:** 
**PnL:** 180.4
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-10-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.76 | 43.04 |
| ATR | 41.92 | 47.13 |
| Volume | 2136147.00 | 1821012.00 |
| SMA (Short) | 1868.51 | 2106.47 |
| SMA (Long) | 1866.23 | 2112.64 |
| RSI | 60.25 | 39.77 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 2136.41
**Exit:** 
**Exit Price:** 2156.13
**Position Size:** 
**PnL:** 11.14
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-03-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.42 | 63.46 |
| ATR | 50.10 | 45.96 |
| Volume | 1996773.00 | 2265389.00 |
| SMA (Short) | 2125.53 | 2189.23 |
| SMA (Long) | 2125.48 | 2194.31 |
| RSI | 62.47 | 25.76 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 2318.36
**Exit:** 
**Exit Price:** 2938.2
**Position Size:** 
**PnL:** 609.33
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-06-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 55.72 | 31.91 |
| ATR | 39.93 | 53.61 |
| Volume | 2501720.00 | 1112206.00 |
| SMA (Short) | 2222.05 | 2897.17 |
| SMA (Long) | 2212.72 | 2902.03 |
| RSI | 79.62 | 37.66 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3001.26
**Exit:** 
**Exit Price:** 3298.62
**Position Size:** 
**PnL:** 284.76
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 47.30 | 130.79 |
| ATR | 52.72 | 77.86 |
| Volume | 1719911.00 | 3121873.00 |
| SMA (Short) | 2921.04 | 3414.74 |
| SMA (Long) | 2915.68 | 3427.40 |
| RSI | 46.78 | 34.04 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3584.42
**Exit:** 
**Exit Price:** 3436.29
**Position Size:** 
**PnL:** -162.18
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-05-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 117.25 | 61.21 |
| ATR | 77.97 | 77.53 |
| Volume | 1981370.00 | 2614667.00 |
| SMA (Short) | 3459.11 | 3562.63 |
| SMA (Long) | 3450.33 | 3566.66 |
| RSI | 72.60 | 31.14 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3759.43
**Exit:** 
**Exit Price:** 3516.11
**Position Size:** 
**PnL:** -257.87
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 107.25 | 118.41 |
| ATR | 81.11 | 95.73 |
| Volume | 5767666.00 | 3151257.00 |
| SMA (Short) | 3586.91 | 3547.81 |
| SMA (Long) | 3562.37 | 3554.84 |
| RSI | 92.58 | 55.58 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3659.04
**Exit:** 
**Exit Price:** 3660.43
**Position Size:** 
**PnL:** -13.25
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-06-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 123.35 | 124.81 |
| ATR | 94.94 | 93.92 |
| Volume | 1746508.00 | 1936792.00 |
| SMA (Short) | 3550.14 | 3540.24 |
| SMA (Long) | 3548.71 | 3546.73 |
| RSI | 52.02 | 51.76 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3561.95
**Exit:** 
**Exit Price:** 3545.2
**Position Size:** 
**PnL:** -30.96
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-08-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 106.07 | 82.99 |
| ATR | 95.10 | 90.47 |
| Volume | 2936151.00 | 1584372.00 |
| SMA (Short) | 3558.76 | 3598.21 |
| SMA (Long) | 3542.91 | 3598.93 |
| RSI | 47.66 | 44.33 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3683.45
**Exit:** 
**Exit Price:** 3622.0
**Position Size:** 
**PnL:** -76.06
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-09-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 56.32 | 55.60 |
| ATR | 72.14 | 72.33 |
| Volume | 2165489.00 | 3751523.00 |
| SMA (Short) | 3621.43 | 3626.10 |
| SMA (Long) | 3615.17 | 3626.80 |
| RSI | 71.32 | 52.58 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3759.43
**Exit:** 
**Exit Price:** 3532.4
**Position Size:** 
**PnL:** -241.61
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 70.39 | 120.58 |
| ATR | 72.47 | 73.25 |
| Volume | 5401701.00 | 2249452.00 |
| SMA (Short) | 3647.74 | 3630.53 |
| SMA (Long) | 3634.42 | 3638.89 |
| RSI | 57.11 | 34.13 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3591.35
**Exit:** 
**Exit Price:** 3603.5
**Position Size:** 
**PnL:** -2.24
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-11-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 95.26 | 61.95 |
| ATR | 77.38 | 80.88 |
| Volume | 1116206.00 | 2534018.00 |
| SMA (Short) | 3597.88 | 3573.63 |
| SMA (Long) | 3586.44 | 3576.34 |
| RSI | 60.69 | 48.00 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3753.0
**Exit:** 
**Exit Price:** 3643.3
**Position Size:** 
**PnL:** -124.49
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 79.33 | 36.89 |
| ATR | 82.28 | 81.90 |
| Volume | 4753829.00 | 1453540.00 |
| SMA (Short) | 3584.28 | 3635.13 |
| SMA (Long) | 3580.66 | 3638.70 |
| RSI | 60.28 | 38.07 |

---

**Ticker:** LT.NS  
**Entry:** 
**Entry Price:** 3501.6
**Exit:** 
**Exit Price:** 3115.95
**Position Size:** 
**PnL:** -398.89
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-04-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 134.34 | 177.31 |
| ATR | 81.22 | 88.00 |
| Volume | 3467864.00 | 3979116.00 |
| SMA (Short) | 3351.86 | 3293.06 |
| SMA (Long) | 3340.27 | 3297.61 |
| RSI | 73.05 | 37.22 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 261.36
**Exit:** 
**Exit Price:** 237.18
**Position Size:** 
**PnL:** -25.18
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.39 | 8.44 |
| ATR | 7.52 | 7.47 |
| Volume | 18247889.00 | 20210546.00 |
| SMA (Short) | 247.64 | 250.37 |
| SMA (Long) | 247.41 | 251.09 |
| RSI |  | 22.87 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 249.1
**Exit:** 
**Exit Price:** 238.65
**Position Size:** 
**PnL:** -11.43
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-07-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.48 | 4.22 |
| ATR | 6.59 | 6.08 |
| Volume | 8788162.00 | 10788886.00 |
| SMA (Short) | 246.45 | 245.15 |
| SMA (Long) | 246.30 | 245.27 |
| RSI | 56.06 | 40.33 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 265.72
**Exit:** 
**Exit Price:** 225.94
**Position Size:** 
**PnL:** -40.76
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.76 | 11.09 |
| ATR | 6.24 | 7.64 |
| Volume | 28858887.00 | 29561705.00 |
| SMA (Short) | 245.79 | 246.66 |
| SMA (Long) | 244.30 | 246.80 |
| RSI | 64.52 | 30.42 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 234.64
**Exit:** 
**Exit Price:** 223.73
**Position Size:** 
**PnL:** -11.83
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.27 | 6.17 |
| ATR | 7.92 | 6.39 |
| Volume | 8811740.00 | 30821077.00 |
| SMA (Short) | 228.15 | 221.42 |
| SMA (Long) | 227.86 | 221.70 |
| RSI | 69.59 | 35.06 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 228.2
**Exit:** 
**Exit Price:** 215.82
**Position Size:** 
**PnL:** -13.27
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-12-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.54 | 4.89 |
| ATR | 6.29 | 5.61 |
| Volume | 11273394.00 | 7408777.00 |
| SMA (Short) | 222.12 | 223.44 |
| SMA (Long) | 221.31 | 223.94 |
| RSI | 46.61 | 39.72 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 170.61
**Exit:** 
**Exit Price:** 173.55
**Position Size:** 
**PnL:** 2.26
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.70 | 3.53 |
| ATR | 7.34 | 5.75 |
| Volume | 22369600.00 | 17398341.00 |
| SMA (Short) | 166.53 | 170.83 |
| SMA (Long) | 163.85 | 171.26 |
| RSI | 73.55 | 37.21 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 183.39
**Exit:** 
**Exit Price:** 235.72
**Position Size:** 
**PnL:** 51.49
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-06-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 13.15 | 5.99 |
| ATR | 6.05 | 5.55 |
| Volume | 24568749.00 | 11224419.00 |
| SMA (Short) | 174.46 | 237.66 |
| SMA (Long) | 173.45 | 237.95 |
| RSI | 68.16 | 49.53 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 262.4
**Exit:** 
**Exit Price:** 237.03
**Position Size:** 
**PnL:** -26.37
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-12-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.34 | 5.93 |
| ATR | 6.32 | 7.38 |
| Volume | 50227559.00 | 21139754.00 |
| SMA (Short) | 238.66 | 239.77 |
| SMA (Long) | 238.60 | 240.64 |
| RSI | 64.67 | 31.06 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 248.27
**Exit:** 
**Exit Price:** 232.41
**Position Size:** 
**PnL:** -16.82
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-12-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 4.41 | 6.12 |
| ATR | 7.52 | 7.33 |
| Volume | 9084137.00 | 10557157.00 |
| SMA (Short) | 242.16 | 241.88 |
| SMA (Long) | 241.67 | 241.99 |
| RSI | 57.96 | 41.55 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 248.55
**Exit:** 
**Exit Price:** 270.18
**Position Size:** 
**PnL:** 20.6
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.26 | 5.82 |
| ATR | 5.80 | 6.36 |
| Volume | 18039379.00 | 12004368.00 |
| SMA (Short) | 239.28 | 270.15 |
| SMA (Long) | 238.10 | 271.07 |
| RSI | 77.22 | 40.20 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 273.86
**Exit:** 
**Exit Price:** 258.51
**Position Size:** 
**PnL:** -16.41
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-08-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 4.43 | 12.60 |
| ATR | 5.53 | 5.94 |
| Volume | 6256500.00 | 9247153.00 |
| SMA (Short) | 271.59 | 271.97 |
| SMA (Long) | 270.79 | 272.12 |
| RSI | 74.37 | 22.55 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 292.77
**Exit:** 
**Exit Price:** 291.69
**Position Size:** 
**PnL:** -2.25
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-12-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.95 | 3.67 |
| ATR | 6.70 | 10.24 |
| Volume | 27580765.00 | 11939569.00 |
| SMA (Short) | 254.01 | 297.00 |
| SMA (Long) | 252.59 | 297.92 |
| RSI | 74.20 | 45.96 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 247.74
**Exit:** 
**Exit Price:** 242.09
**Position Size:** 
**PnL:** -6.63
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-07-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.30 | 5.36 |
| ATR | 6.92 | 6.63 |
| Volume | 71202072.00 | 16174019.00 |
| SMA (Short) | 234.00 | 244.85 |
| SMA (Long) | 233.81 | 245.28 |
| RSI | 69.36 | 22.75 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 269.9
**Exit:** 
**Exit Price:** 255.55
**Position Size:** 
**PnL:** -15.4
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-09-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 10.96 | 8.14 |
| ATR | 6.78 | 7.97 |
| Volume | 32175436.00 | 40759431.00 |
| SMA (Short) | 251.44 | 269.07 |
| SMA (Long) | 250.80 | 271.13 |
| RSI | 71.47 | 16.25 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 266.61
**Exit:** 
**Exit Price:** 264.11
**Position Size:** 
**PnL:** -3.56
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 14.57 | 7.14 |
| ATR | 9.29 | 6.16 |
| Volume | 19201007.00 | 17435611.00 |
| SMA (Short) | 262.89 | 273.01 |
| SMA (Long) | 261.32 | 273.55 |
| RSI | 65.18 | 13.13 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 280.87
**Exit:** 
**Exit Price:** 323.6
**Position Size:** 
**PnL:** 41.52
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-03-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 8.52 | 10.75 |
| ATR | 6.26 | 8.42 |
| Volume | 37928480.00 | 17060483.00 |
| SMA (Short) | 268.08 | 331.01 |
| SMA (Long) | 268.06 | 331.61 |
| RSI | 83.35 | 38.39 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 294.04
**Exit:** 
**Exit Price:** 305.2
**Position Size:** 
**PnL:** 9.96
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-10-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.45 | 6.56 |
| ATR | 10.79 | 8.21 |
| Volume | 108587116.76 | 32625740.00 |
| SMA (Short) | 262.59 | 308.32 |
| SMA (Long) | 259.68 | 308.96 |
| RSI | 81.92 | 45.27 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 166.74
**Exit:** 
**Exit Price:** 174.88
**Position Size:** 
**PnL:** 7.46
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.74 | 5.62 |
| ATR | 8.11 | 6.15 |
| Volume | 91726802.00 | 57611375.00 |
| SMA (Short) | 167.02 | 185.47 |
| SMA (Long) | 166.09 | 186.13 |
| RSI | 71.84 | 20.04 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 191.78
**Exit:** 
**Exit Price:** 178.13
**Position Size:** 
**PnL:** -14.39
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-10-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.51 | 5.80 |
| ATR | 6.46 | 6.31 |
| Volume | 54515523.00 | 41519686.00 |
| SMA (Short) | 186.73 | 186.05 |
| SMA (Long) | 186.66 | 186.36 |
| RSI | 70.14 | 39.00 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 205.8
**Exit:** 
**Exit Price:** 342.9
**Position Size:** 
**PnL:** 135.99
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.54 | 6.63 |
| ATR | 6.69 | 13.72 |
| Volume | 108587116.76 | 38651025.00 |
| SMA (Short) | 187.21 | 342.94 |
| SMA (Long) | 186.53 | 343.38 |
| RSI | 70.75 | 32.56 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 359.79
**Exit:** 
**Exit Price:** 386.34
**Position Size:** 
**PnL:** 25.06
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-05-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.44 | 8.79 |
| ATR | 11.90 | 9.73 |
| Volume | 70917710.00 | 25541790.00 |
| SMA (Short) | 342.66 | 404.16 |
| SMA (Long) | 341.17 | 406.11 |
| RSI | 70.56 | 35.52 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 410.66
**Exit:** 
**Exit Price:** 451.5
**Position Size:** 
**PnL:** 39.12
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-09-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.29 | 13.73 |
| ATR | 8.71 | 14.06 |
| Volume | 9662128.00 | 17156956.00 |
| SMA (Short) | 406.20 | 459.44 |
| SMA (Long) | 406.07 | 460.76 |
| RSI | 78.96 | 28.27 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 484.7
**Exit:** 
**Exit Price:** 450.51
**Position Size:** 
**PnL:** -36.07
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-03-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 19.89 | 17.56 |
| ATR | 12.43 | 13.53 |
| Volume | 14489616.00 | 22003848.00 |
| SMA (Short) | 461.82 | 471.83 |
| SMA (Long) | 461.63 | 475.56 |
| RSI | 80.49 | 28.94 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 489.17
**Exit:** 
**Exit Price:** 452.07
**Position Size:** 
**PnL:** -38.98
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 9.78 | 10.28 |
| ATR | 14.61 | 12.90 |
| Volume | 19620958.00 | 13544947.00 |
| SMA (Short) | 477.81 | 466.59 |
| SMA (Long) | 476.28 | 467.17 |
| RSI | 60.40 | 33.66 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 463.04
**Exit:** 
**Exit Price:** 511.52
**Position Size:** 
**PnL:** 46.53
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 9.50 | 13.34 |
| ATR | 11.77 | 12.02 |
| Volume | 12059857.00 | 11065307.00 |
| SMA (Short) | 448.47 | 513.98 |
| SMA (Long) | 446.10 | 517.72 |
| RSI | 76.91 | 35.49 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 535.83
**Exit:** 
**Exit Price:** 573.94
**Position Size:** 
**PnL:** 35.89
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-10-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 12.95 | 6.97 |
| ATR | 12.16 | 10.84 |
| Volume | 11225588.00 | 8183715.00 |
| SMA (Short) | 519.59 | 583.07 |
| SMA (Long) | 519.09 | 583.27 |
| RSI | 64.13 | 63.43 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 521.26
**Exit:** 
**Exit Price:** 556.76
**Position Size:** 
**PnL:** 33.35
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.77 | 6.75 |
| ATR | 11.77 | 8.55 |
| Volume | 21156372.00 | 10694768.00 |
| SMA (Short) | 513.94 | 556.43 |
| SMA (Long) | 513.74 | 557.60 |
| RSI | 75.64 | 29.34 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 582.73
**Exit:** 
**Exit Price:** 564.68
**Position Size:** 
**PnL:** -20.34
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-08-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.57 | 19.54 |
| ATR | 8.39 | 9.13 |
| Volume | 11323509.00 | 18221179.00 |
| SMA (Short) | 564.65 | 576.03 |
| SMA (Long) | 562.96 | 576.63 |
| RSI | 71.92 | 22.26 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 593.99
**Exit:** 
**Exit Price:** 553.81
**Position Size:** 
**PnL:** -42.47
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-10-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 11.30 | 9.51 |
| ATR | 9.99 | 9.22 |
| Volume | 19305055.00 | 11110988.00 |
| SMA (Short) | 578.55 | 569.09 |
| SMA (Long) | 576.96 | 571.95 |
| RSI | 69.96 | 26.35 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 601.61
**Exit:** 
**Exit Price:** 808.65
**Position Size:** 
**PnL:** 204.22
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-12-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 21.38 | 22.78 |
| ATR | 8.90 | 20.58 |
| Volume | 10725706.00 | 17692355.00 |
| SMA (Short) | 571.71 | 839.63 |
| SMA (Long) | 568.40 | 840.47 |
| RSI | 65.45 | 22.06 |

---

**Ticker:** SBIN.NS  
**Entry:** 
**Entry Price:** 813.95
**Exit:** 
**Exit Price:** 788.3
**Position Size:** 
**PnL:** -28.85
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-12-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 14.24 | 23.14 |
| ATR | 14.13 | 19.84 |
| Volume | 10359618.00 | 21515438.00 |
| SMA (Short) | 803.64 | 822.35 |
| SMA (Long) | 801.94 | 827.57 |
| RSI | 63.26 | 13.23 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 330.42
**Exit:** 
**Exit Price:** 353.75
**Position Size:** 
**PnL:** 21.96
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.62 | 9.97 |
| ATR | 12.08 | 9.67 |
| Volume | 5484794.00 | 5116932.00 |
| SMA (Short) | 333.77 | 361.21 |
| SMA (Long) | 333.57 | 361.37 |
| RSI |  | 43.58 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 303.18
**Exit:** 
**Exit Price:** 288.59
**Position Size:** 
**PnL:** -15.77
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.25 | 6.54 |
| ATR | 10.84 | 9.30 |
| Volume | 7353435.00 | 3630757.00 |
| SMA (Short) | 305.63 | 298.75 |
| SMA (Long) | 304.93 | 299.58 |
| RSI | 54.01 | 28.91 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 276.49
**Exit:** 
**Exit Price:** 297.11
**Position Size:** 
**PnL:** 19.47
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-02-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 5.50 | 7.09 |
| ATR | 8.45 | 9.35 |
| Volume | 2569038.00 | 2293594.00 |
| SMA (Short) | 271.15 | 302.11 |
| SMA (Long) | 271.02 | 302.19 |
| RSI | 75.36 | 36.30 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 308.3
**Exit:** 
**Exit Price:** 294.96
**Position Size:** 
**PnL:** -14.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-06-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.42 | 6.47 |
| ATR | 9.37 | 8.97 |
| Volume | 3677399.00 | 3358585.00 |
| SMA (Short) | 304.87 | 303.48 |
| SMA (Long) | 304.52 | 303.94 |
| RSI | 54.09 | 42.32 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 307.4
**Exit:** 
**Exit Price:** 298.23
**Position Size:** 
**PnL:** -10.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-08-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.38 | 7.43 |
| ATR | 8.31 | 8.21 |
| Volume | 3541398.00 | 1704178.00 |
| SMA (Short) | 307.66 | 309.23 |
| SMA (Long) | 306.53 | 310.12 |
| RSI | 53.29 | 31.16 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 282.38
**Exit:** 
**Exit Price:** 255.42
**Position Size:** 
**PnL:** -28.04
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-12-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 9.59 | 12.43 |
| ATR | 7.64 | 7.69 |
| Volume | 2481220.00 | 2047449.00 |
| SMA (Short) | 271.33 | 268.59 |
| SMA (Long) | 270.07 | 269.11 |
| RSI | 64.97 | 20.17 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 276.63
**Exit:** 
**Exit Price:** 294.48
**Position Size:** 
**PnL:** 16.7
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 7.30 | 8.43 |
| ATR | 7.91 | 9.71 |
| Volume | 1058176.00 | 2316105.00 |
| SMA (Short) | 269.32 | 299.59 |
| SMA (Long) | 268.91 | 301.18 |
| RSI | 66.17 | 29.13 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 298.37
**Exit:** 
**Exit Price:** 351.06
**Position Size:** 
**PnL:** 51.39
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-05-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.58 | 10.45 |
| ATR | 8.59 | 8.80 |
| Volume | 3126657.00 | 2583110.00 |
| SMA (Short) | 303.00 | 356.40 |
| SMA (Long) | 302.86 | 356.83 |
| RSI | 57.19 | 35.96 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 400.23
**Exit:** 
**Exit Price:** 428.86
**Position Size:** 
**PnL:** 26.98
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-10-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 30.96 | 11.17 |
| ATR | 9.35 | 12.89 |
| Volume | 9015866.00 | 7912892.00 |
| SMA (Short) | 358.64 | 441.29 |
| SMA (Long) | 354.08 | 441.87 |
| RSI | 79.30 | 33.27 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 352.64
**Exit:** 
**Exit Price:** 337.12
**Position Size:** 
**PnL:** -16.9
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.91 | 6.53 |
| ATR | 10.51 | 11.14 |
| Volume | 4124205.00 | 25555353.00 |
| SMA (Short) | 354.61 | 351.28 |
| SMA (Long) | 354.44 | 352.36 |
| RSI | 68.97 | 40.77 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 328.7
**Exit:** 
**Exit Price:** 313.17
**Position Size:** 
**PnL:** -16.82
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-09-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.03 | 8.76 |
| ATR | 9.92 | 11.27 |
| Volume | 3647704.00 | 4483893.00 |
| SMA (Short) | 322.74 | 324.00 |
| SMA (Long) | 322.14 | 324.46 |
| RSI | 65.66 | 39.87 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 296.09
**Exit:** 
**Exit Price:** 272.15
**Position Size:** 
**PnL:** -25.08
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 15.44 | 12.98 |
| ATR | 12.82 | 10.90 |
| Volume | 6623860.00 | 6040052.00 |
| SMA (Short) | 282.87 | 281.05 |
| SMA (Long) | 282.09 | 281.55 |
| RSI | 73.46 | 36.89 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 311.36
**Exit:** 
**Exit Price:** 326.67
**Position Size:** 
**PnL:** 14.04
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-03-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 12.14 | 7.36 |
| ATR | 9.29 | 8.99 |
| Volume | 30070085.00 | 4840787.00 |
| SMA (Short) | 281.49 | 334.66 |
| SMA (Long) | 279.06 | 335.85 |
| RSI | 79.99 | 26.96 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 357.75
**Exit:** 
**Exit Price:** 324.69
**Position Size:** 
**PnL:** -34.43
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-09-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 16.57 | 7.45 |
| ATR | 10.09 | 10.76 |
| Volume | 7844936.00 | 4305439.00 |
| SMA (Short) | 339.38 | 337.75 |
| SMA (Long) | 338.38 | 338.23 |
| RSI | 64.70 | 27.58 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 363.63
**Exit:** 
**Exit Price:** 474.1
**Position Size:** 
**PnL:** 108.79
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-10-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.49 | 19.42 |
| ATR | 13.33 | 17.10 |
| Volume | 48555442.00 | 24254296.00 |
| SMA (Short) | 338.85 | 488.92 |
| SMA (Long) | 337.45 | 489.65 |
| RSI | 66.33 | 31.45 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 478.1
**Exit:** 
**Exit Price:** 544.22
**Position Size:** 
**PnL:** 64.08
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-04-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.16 | 8.20 |
| ATR | 27.63 | 18.02 |
| Volume | 12767355.00 | 14210206.00 |
| SMA (Short) | 478.50 | 545.23 |
| SMA (Long) | 477.62 | 547.75 |
| RSI | 68.07 | 51.80 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 451.18
**Exit:** 
**Exit Price:** 528.47
**Position Size:** 
**PnL:** 75.33
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.22 | 19.40 |
| ATR | 17.21 | 17.43 |
| Volume | 9800899.00 | 24669015.00 |
| SMA (Short) | 439.85 | 545.05 |
| SMA (Long) | 439.43 | 545.39 |
| RSI | 69.75 | 28.87 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 541.68
**Exit:** 
**Exit Price:** 502.84
**Position Size:** 
**PnL:** -40.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-05-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.27 | 14.70 |
| ATR | 14.04 | 12.59 |
| Volume | 12095639.00 | 22783169.00 |
| SMA (Short) | 523.20 | 515.09 |
| SMA (Long) | 520.47 | 518.04 |
| RSI | 62.29 | 27.65 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 519.23
**Exit:** 
**Exit Price:** 511.4
**Position Size:** 
**PnL:** -9.9
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-06-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.31 | 5.44 |
| ATR | 11.63 | 11.62 |
| Volume | 10045600.00 | 10214732.00 |
| SMA (Short) | 521.66 | 521.33 |
| SMA (Long) | 521.65 | 521.66 |
| RSI | 63.15 | 53.67 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 521.17
**Exit:** 
**Exit Price:** 518.9
**Position Size:** 
**PnL:** -4.35
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-06-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.06 | 4.66 |
| ATR | 11.81 | 11.80 |
| Volume | 15000348.00 | 9114558.00 |
| SMA (Short) | 521.92 | 521.22 |
| SMA (Long) | 521.78 | 521.62 |
| RSI | 52.85 | 55.21 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 530.41
**Exit:** 
**Exit Price:** 675.53
**Position Size:** 
**PnL:** 142.71
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-07-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.14 | 13.94 |
| ATR | 10.45 | 19.68 |
| Volume | 33200836.00 | 7674319.00 |
| SMA (Short) | 517.72 | 696.50 |
| SMA (Long) | 515.91 | 700.08 |
| RSI | 63.36 | 20.83 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 710.17
**Exit:** 
**Exit Price:** 676.57
**Position Size:** 
**PnL:** -36.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.94 | 15.35 |
| ATR | 16.72 | 17.75 |
| Volume | 5344096.00 | 8301523.00 |
| SMA (Short) | 699.22 | 692.09 |
| SMA (Long) | 698.90 | 692.71 |
| RSI | 75.47 | 43.12 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 696.13
**Exit:** 
**Exit Price:** 679.92
**Position Size:** 
**PnL:** -18.96
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.57 | 16.67 |
| ATR | 19.33 | 17.87 |
| Volume | 3597143.00 | 11938252.00 |
| SMA (Short) | 696.75 | 707.73 |
| SMA (Long) | 695.65 | 713.23 |
| RSI | 62.72 | 28.55 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 687.44
**Exit:** 
**Exit Price:** 802.82
**Position Size:** 
**PnL:** 112.39
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-08-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.02 | 10.40 |
| ATR | 16.12 | 14.65 |
| Volume | 8812526.00 | 6023206.00 |
| SMA (Short) | 668.24 | 815.29 |
| SMA (Long) | 665.48 | 816.00 |
| RSI | 64.74 | 37.95 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 764.51
**Exit:** 
**Exit Price:** 864.63
**Position Size:** 
**PnL:** 96.87
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.09 | 8.01 |
| ATR | 14.19 | 14.22 |
| Volume | 2355441.00 | 2842728.00 |
| SMA (Short) | 759.04 | 861.75 |
| SMA (Long) | 757.78 | 862.86 |
| RSI | 56.95 | 51.05 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 910.08
**Exit:** 
**Exit Price:** 1578.4
**Position Size:** 
**PnL:** 663.34
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-09-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 17.49 | 38.78 |
| ATR | 14.23 | 34.90 |
| Volume | 5222561.00 | 6473278.00 |
| SMA (Short) | 874.26 | 1636.27 |
| SMA (Long) | 870.79 | 1646.47 |
| RSI | 73.53 | 6.32 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 1599.5
**Exit:** 
**Exit Price:** 1586.9
**Position Size:** 
**PnL:** -18.97
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-12-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 33.19 | 33.26 |
| ATR | 36.93 | 36.77 |
| Volume | 3400479.00 | 4438130.00 |
| SMA (Short) | 1612.08 | 1601.52 |
| SMA (Long) | 1611.75 | 1606.65 |
| RSI | 47.17 | 47.12 |

---

**Ticker:** BHARTIARTL.NS  
**Entry:** 
**Entry Price:** 1599.2
**Exit:** 
**Exit Price:** 1575.35
**Position Size:** 
**PnL:** -30.2
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-03-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.70 | 36.25 |
| ATR | 36.29 | 35.46 |
| Volume | 3674564.00 | 5219668.00 |
| SMA (Short) | 1595.67 | 1623.13 |
| SMA (Long) | 1593.58 | 1628.56 |
| RSI | 48.87 | 30.51 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 562.88
**Exit:** 
**Exit Price:** 519.4
**Position Size:** 
**PnL:** -45.65
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-05-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.31 | 20.61 |
| ATR | 18.64 | 18.60 |
| Volume | 215685.00 | 336534.00 |
| SMA (Short) | 548.05 | 543.07 |
| SMA (Long) | 545.93 | 543.15 |
| RSI |  | 38.99 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 530.76
**Exit:** 
**Exit Price:** 518.97
**Position Size:** 
**PnL:** -13.88
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-07-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.93 | 6.51 |
| ATR | 15.23 | 15.01 |
| Volume | 174437.00 | 138245.00 |
| SMA (Short) | 525.61 | 522.28 |
| SMA (Long) | 524.37 | 522.85 |
| RSI | 56.13 | 52.09 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 519.02
**Exit:** 
**Exit Price:** 531.42
**Position Size:** 
**PnL:** 10.3
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-07-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.79 | 10.23 |
| ATR | 14.72 | 16.51 |
| Volume | 167000.00 | 210935.00 |
| SMA (Short) | 522.47 | 531.85 |
| SMA (Long) | 521.97 | 532.17 |
| RSI | 51.74 | 45.85 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 546.83
**Exit:** 
**Exit Price:** 513.82
**Position Size:** 
**PnL:** -35.13
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.06 | 10.31 |
| ATR | 16.15 | 13.79 |
| Volume | 277534.00 | 244921.00 |
| SMA (Short) | 539.65 | 535.58 |
| SMA (Long) | 538.48 | 537.66 |
| RSI | 54.91 | 24.71 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 530.37
**Exit:** 
**Exit Price:** 513.82
**Position Size:** 
**PnL:** -18.64
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.71 | 8.91 |
| ATR | 11.36 | 11.24 |
| Volume | 735318.00 | 317478.00 |
| SMA (Short) | 523.76 | 517.88 |
| SMA (Long) | 523.20 | 519.18 |
| RSI | 77.47 | 39.21 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 542.41
**Exit:** 
**Exit Price:** 669.78
**Position Size:** 
**PnL:** 124.95
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-02-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.31 | 8.76 |
| ATR | 11.81 | 14.74 |
| Volume | 671437.00 | 476124.00 |
| SMA (Short) | 524.63 | 682.78 |
| SMA (Long) | 522.38 | 683.86 |
| RSI | 63.20 | 32.82 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 698.99
**Exit:** 
**Exit Price:** 664.85
**Position Size:** 
**PnL:** -36.87
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.58 | 8.94 |
| ATR | 16.61 | 15.42 |
| Volume | 174998.00 | 708243.00 |
| SMA (Short) | 680.82 | 677.58 |
| SMA (Long) | 680.04 | 677.85 |
| RSI | 56.03 | 26.84 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 608.73
**Exit:** 
**Exit Price:** 772.74
**Position Size:** 
**PnL:** 161.25
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 13.18 | 10.75 |
| ATR | 16.66 | 17.67 |
| Volume | 129900.00 | 314026.00 |
| SMA (Short) | 596.69 | 768.64 |
| SMA (Long) | 595.49 | 769.00 |
| RSI | 91.67 | 50.02 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 785.91
**Exit:** 
**Exit Price:** 765.34
**Position Size:** 
**PnL:** -23.67
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.04 | 28.20 |
| ATR | 17.46 | 16.59 |
| Volume | 397771.00 | 347273.00 |
| SMA (Short) | 776.51 | 785.04 |
| SMA (Long) | 776.35 | 786.40 |
| RSI | 63.31 | 32.07 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 817.89
**Exit:** 
**Exit Price:** 843.08
**Position Size:** 
**PnL:** 21.87
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-11-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.53 | 10.80 |
| ATR | 17.24 | 22.73 |
| Volume | 531172.00 | 524002.00 |
| SMA (Short) | 782.99 | 852.28 |
| SMA (Long) | 777.79 | 853.16 |
| RSI | 71.76 | 38.20 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 874.34
**Exit:** 
**Exit Price:** 1038.49
**Position Size:** 
**PnL:** 160.32
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-03-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.22 | 16.44 |
| ATR | 18.39 | 27.22 |
| Volume | 235720.00 | 351245.00 |
| SMA (Short) | 860.63 | 1038.65 |
| SMA (Long) | 859.98 | 1042.05 |
| RSI | 57.75 | 25.20 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1082.22
**Exit:** 
**Exit Price:** 1028.44
**Position Size:** 
**PnL:** -58.0
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-09-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 35.28 | 23.43 |
| ATR | 28.86 | 28.99 |
| Volume | 480797.00 | 395613.00 |
| SMA (Short) | 1046.66 | 1075.10 |
| SMA (Long) | 1042.68 | 1080.17 |
| RSI | 60.14 | 35.42 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1089.24
**Exit:** 
**Exit Price:** 1068.99
**Position Size:** 
**PnL:** -24.57
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 47.68 | 4.21 |
| ATR | 39.70 | 31.02 |
| Volume | 396935.00 | 626835.00 |
| SMA (Short) | 1020.69 | 1075.87 |
| SMA (Long) | 1008.22 | 1077.70 |
| RSI | 77.20 | 15.54 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1124.53
**Exit:** 
**Exit Price:** 1076.53
**Position Size:** 
**PnL:** -52.4
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 25.21 | 22.37 |
| ATR | 29.25 | 28.60 |
| Volume | 329568.00 | 313627.00 |
| SMA (Short) | 1103.79 | 1104.01 |
| SMA (Long) | 1102.52 | 1107.89 |
| RSI | 70.76 | 51.87 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1103.89
**Exit:** 
**Exit Price:** 1136.89
**Position Size:** 
**PnL:** 28.52
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-03-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.52 | 26.69 |
| ATR | 29.03 | 27.44 |
| Volume | 310567.00 | 303672.00 |
| SMA (Short) | 1094.70 | 1163.57 |
| SMA (Long) | 1089.98 | 1167.25 |
| RSI | 55.91 | 22.31 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1235.06
**Exit:** 
**Exit Price:** 1194.32
**Position Size:** 
**PnL:** -45.6
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 39.07 | 12.13 |
| ATR | 30.10 | 28.02 |
| Volume | 660117.00 | 755871.00 |
| SMA (Short) | 1193.76 | 1189.67 |
| SMA (Long) | 1187.87 | 1191.38 |
| RSI | 69.42 | 41.44 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1245.76
**Exit:** 
**Exit Price:** 1328.16
**Position Size:** 
**PnL:** 77.25
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-08-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.05 | 25.85 |
| ATR | 26.85 | 35.49 |
| Volume | 1115406.00 | 1002807.00 |
| SMA (Short) | 1207.89 | 1335.59 |
| SMA (Long) | 1202.99 | 1336.37 |
| RSI | 64.53 | 33.73 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1347.63
**Exit:** 
**Exit Price:** 1253.33
**Position Size:** 
**PnL:** -99.51
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 24.81 | 128.87 |
| ATR | 26.74 | 56.66 |
| Volume | 244310.00 | 901892.00 |
| SMA (Short) | 1315.67 | 1457.74 |
| SMA (Long) | 1312.40 | 1488.32 |
| RSI | 72.31 | 35.45 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1514.19
**Exit:** 
**Exit Price:** 1353.93
**Position Size:** 
**PnL:** -166.0
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-05-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 61.24 | 74.89 |
| ATR | 74.70 | 80.91 |
| Volume | 922147.00 | 660493.00 |
| SMA (Short) | 1461.04 | 1423.99 |
| SMA (Long) | 1455.17 | 1431.03 |
| RSI | 74.62 | 40.69 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1447.99
**Exit:** 
**Exit Price:** 1367.25
**Position Size:** 
**PnL:** -86.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-06-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 40.90 | 31.16 |
| ATR | 73.20 | 52.04 |
| Volume | 924436.00 | 1069601.00 |
| SMA (Short) | 1383.42 | 1400.25 |
| SMA (Long) | 1382.58 | 1410.64 |
| RSI | 65.37 | 26.00 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1425.04
**Exit:** 
**Exit Price:** 1657.16
**Position Size:** 
**PnL:** 225.95
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-08-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 34.67 | 32.89 |
| ATR | 34.42 | 46.20 |
| Volume | 1058823.00 | 1045945.00 |
| SMA (Short) | 1372.59 | 1719.40 |
| SMA (Long) | 1362.87 | 1720.84 |
| RSI | 67.68 | 40.20 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 1734.27
**Exit:** 
**Exit Price:** 2197.71
**Position Size:** 
**PnL:** 455.57
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-03-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 28.83 | 19.39 |
| ATR | 43.47 | 44.12 |
| Volume | 422753.00 | 337985.00 |
| SMA (Short) | 1715.59 | 2193.37 |
| SMA (Long) | 1715.51 | 2193.88 |
| RSI | 50.71 | 46.19 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2231.69
**Exit:** 
**Exit Price:** 2331.14
**Position Size:** 
**PnL:** 90.32
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-08-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.62 | 69.48 |
| ATR | 44.66 | 53.55 |
| Volume | 461816.00 | 216399.00 |
| SMA (Short) | 2199.27 | 2321.13 |
| SMA (Long) | 2198.70 | 2336.29 |
| RSI | 55.32 | 39.31 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2411.83
**Exit:** 
**Exit Price:** 2232.63
**Position Size:** 
**PnL:** -188.49
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 40.55 | 59.46 |
| ATR | 55.54 | 59.43 |
| Volume | 452443.00 | 794035.00 |
| SMA (Short) | 2370.51 | 2363.08 |
| SMA (Long) | 2365.13 | 2367.97 |
| RSI | 63.33 | 42.41 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2377.55
**Exit:** 
**Exit Price:** 2447.2
**Position Size:** 
**PnL:** 60.0
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-12-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 75.53 | 45.82 |
| ATR | 59.15 | 55.18 |
| Volume | 451100.00 | 363447.00 |
| SMA (Short) | 2328.31 | 2437.28 |
| SMA (Long) | 2323.52 | 2450.68 |
| RSI | 81.52 | 32.16 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2407.44
**Exit:** 
**Exit Price:** 2375.92
**Position Size:** 
**PnL:** -41.09
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-04-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 39.97 | 58.78 |
| ATR | 69.08 | 66.86 |
| Volume | 393851.00 | 293372.00 |
| SMA (Short) | 2413.16 | 2369.56 |
| SMA (Long) | 2411.00 | 2373.12 |
| RSI | 69.61 | 40.87 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2391.46
**Exit:** 
**Exit Price:** 2206.39
**Position Size:** 
**PnL:** -194.27
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 36.70 | 67.70 |
| ATR | 64.99 | 67.46 |
| Volume | 181102.00 | 386579.00 |
| SMA (Short) | 2376.80 | 2352.98 |
| SMA (Long) | 2371.45 | 2362.81 |
| RSI | 38.72 | 36.40 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2238.01
**Exit:** 
**Exit Price:** 2587.92
**Position Size:** 
**PnL:** 340.26
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 61.20 | 64.18 |
| ATR | 61.52 | 59.93 |
| Volume | 259144.00 | 230529.00 |
| SMA (Short) | 2151.45 | 2664.56 |
| SMA (Long) | 2137.57 | 2688.21 |
| RSI | 71.29 | 11.91 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2702.8
**Exit:** 
**Exit Price:** 2552.95
**Position Size:** 
**PnL:** -160.37
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 18.98 | 73.92 |
| ATR | 55.99 | 50.68 |
| Volume | 401963.00 | 148058.00 |
| SMA (Short) | 2666.85 | 2638.76 |
| SMA (Long) | 2660.12 | 2641.00 |
| RSI | 65.26 | 17.96 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2342.75
**Exit:** 
**Exit Price:** 2571.48
**Position Size:** 
**PnL:** 218.9
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-03-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.44 | 24.42 |
| ATR | 42.76 | 46.49 |
| Volume | 270195.00 | 206189.00 |
| SMA (Short) | 2322.19 | 2604.33 |
| SMA (Long) | 2320.27 | 2607.09 |
| RSI | 60.16 | 44.16 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2446.71
**Exit:** 
**Exit Price:** 2497.8
**Position Size:** 
**PnL:** 41.2
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.46 | 97.76 |
| ATR | 39.30 | 54.32 |
| Volume | 175004.00 | 356002.00 |
| SMA (Short) | 2434.36 | 2589.80 |
| SMA (Long) | 2433.88 | 2613.41 |
| RSI | 69.90 | 30.92 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 2697.49
**Exit:** 
**Exit Price:** 3047.1
**Position Size:** 
**PnL:** 338.12
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-02-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 45.99 | 50.70 |
| ATR | 58.52 | 68.01 |
| Volume | 363955.00 | 181637.00 |
| SMA (Short) | 2653.70 | 3112.32 |
| SMA (Long) | 2642.33 | 3113.71 |
| RSI | 66.30 | 43.40 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 3192.06
**Exit:** 
**Exit Price:** 3090.7
**Position Size:** 
**PnL:** -113.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 42.91 | 29.69 |
| ATR | 61.18 | 65.18 |
| Volume | 955844.00 | 162497.00 |
| SMA (Short) | 3123.47 | 3143.33 |
| SMA (Long) | 3115.16 | 3150.60 |
| RSI | 75.15 | 36.08 |

---

**Ticker:** PIDILITIND.NS  
**Entry:** 
**Entry Price:** 3192.06
**Exit:** 
**Exit Price:** 2951.8
**Position Size:** 
**PnL:** -252.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-12-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 67.66 | 97.73 |
| ATR | 70.85 | 69.18 |
| Volume | 293172.00 | 379460.00 |
| SMA (Short) | 3133.64 | 3100.72 |
| SMA (Long) | 3120.53 | 3104.61 |
| RSI | 74.75 | 22.59 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 643.65
**Exit:** 
**Exit Price:** 614.37
**Position Size:** 
**PnL:** -31.8
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.96 | 12.41 |
| ATR | 31.69 | 25.84 |
| Volume | 1564356.00 | 1793974.00 |
| SMA (Short) | 623.66 | 630.60 |
| SMA (Long) | 622.29 | 631.78 |
| RSI |  | 31.69 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 685.81
**Exit:** 
**Exit Price:** 698.87
**Position Size:** 
**PnL:** 10.28
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-06-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 26.20 | 27.46 |
| ATR | 23.34 | 28.09 |
| Volume | 4626832.00 | 1157450.00 |
| SMA (Short) | 636.23 | 707.06 |
| SMA (Long) | 632.06 | 710.34 |
| RSI | 75.87 | 45.09 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 718.12
**Exit:** 
**Exit Price:** 770.0
**Position Size:** 
**PnL:** 48.89
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-10-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 21.94 | 11.40 |
| ATR | 29.59 | 20.98 |
| Volume | 1957795.00 | 2404805.00 |
| SMA (Short) | 709.73 | 769.70 |
| SMA (Long) | 707.73 | 769.86 |
| RSI | 70.67 | 41.41 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 799.97
**Exit:** 
**Exit Price:** 762.19
**Position Size:** 
**PnL:** -40.91
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 16.25 | 18.91 |
| ATR | 19.72 | 21.66 |
| Volume | 1038012.00 | 1547207.00 |
| SMA (Short) | 781.10 | 786.33 |
| SMA (Long) | 779.48 | 792.30 |
| RSI | 58.14 | 32.14 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 716.79
**Exit:** 
**Exit Price:** 726.99
**Position Size:** 
**PnL:** 7.31
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.63 | 18.37 |
| ATR | 32.60 | 20.97 |
| Volume | 1517858.00 | 1396088.00 |
| SMA (Short) | 697.34 | 726.29 |
| SMA (Long) | 694.37 | 728.57 |
| RSI | 77.22 | 32.51 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 736.04
**Exit:** 
**Exit Price:** 714.34
**Position Size:** 
**PnL:** -24.59
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-06-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 16.83 | 16.59 |
| ATR | 20.74 | 20.57 |
| Volume | 865612.00 | 1721319.00 |
| SMA (Short) | 737.19 | 735.77 |
| SMA (Long) | 735.57 | 736.03 |
| RSI | 51.20 | 58.23 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 738.23
**Exit:** 
**Exit Price:** 699.85
**Position Size:** 
**PnL:** -41.26
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-08-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 18.29 | 14.75 |
| ATR | 19.24 | 19.63 |
| Volume | 1051423.00 | 1666669.00 |
| SMA (Short) | 728.32 | 719.41 |
| SMA (Long) | 728.20 | 723.47 |
| RSI | 68.39 | 33.92 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 753.25
**Exit:** 
**Exit Price:** 733.56
**Position Size:** 
**PnL:** -22.66
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.82 | 16.88 |
| ATR | 20.38 | 22.29 |
| Volume | 1998554.00 | 1491112.00 |
| SMA (Short) | 725.03 | 770.96 |
| SMA (Long) | 724.71 | 774.16 |
| RSI | 56.14 | 30.55 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 682.62
**Exit:** 
**Exit Price:** 658.83
**Position Size:** 
**PnL:** -26.47
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-02-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.38 | 15.80 |
| ATR | 20.54 | 18.68 |
| Volume | 1149041.00 | 4560953.00 |
| SMA (Short) | 672.54 | 665.80 |
| SMA (Long) | 672.32 | 665.82 |
| RSI | 71.50 | 48.48 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 669.72
**Exit:** 
**Exit Price:** 648.85
**Position Size:** 
**PnL:** -23.51
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-02-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.33 | 13.16 |
| ATR | 18.58 | 18.89 |
| Volume | 1914897.00 | 3609171.00 |
| SMA (Short) | 664.60 | 660.00 |
| SMA (Long) | 664.00 | 661.29 |
| RSI | 48.29 | 44.81 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 640.06
**Exit:** 
**Exit Price:** 652.34
**Position Size:** 
**PnL:** 9.69
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-03-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.04 | 10.17 |
| ATR | 18.04 | 17.35 |
| Volume | 2714444.00 | 1420567.00 |
| SMA (Short) | 653.17 | 649.24 |
| SMA (Long) | 653.02 | 650.05 |
| RSI | 50.94 | 58.34 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 625.71
**Exit:** 
**Exit Price:** 668.73
**Position Size:** 
**PnL:** 40.44
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-06-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.66 | 12.14 |
| ATR | 18.84 | 20.81 |
| Volume | 9785718.00 | 1618248.00 |
| SMA (Short) | 583.65 | 670.11 |
| SMA (Long) | 580.32 | 670.87 |
| RSI | 88.66 | 37.22 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 700.8
**Exit:** 
**Exit Price:** 646.86
**Position Size:** 
**PnL:** -56.63
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 13.26 | 30.45 |
| ATR | 21.19 | 22.27 |
| Volume | 4300438.00 | 6471303.00 |
| SMA (Short) | 674.76 | 695.63 |
| SMA (Long) | 673.32 | 699.00 |
| RSI | 46.95 | 29.76 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 713.57
**Exit:** 
**Exit Price:** 678.45
**Position Size:** 
**PnL:** -37.91
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-11-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 22.84 | 39.76 |
| ATR | 21.71 | 22.94 |
| Volume | 1426272.00 | 1479177.00 |
| SMA (Short) | 698.87 | 710.48 |
| SMA (Long) | 696.66 | 710.91 |
| RSI | 55.97 | 34.30 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 593.48
**Exit:** 
**Exit Price:** 543.37
**Position Size:** 
**PnL:** -52.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 23.58 | 16.03 |
| ATR | 17.66 | 16.33 |
| Volume | 1845242.00 | 1032294.00 |
| SMA (Short) | 571.73 | 575.53 |
| SMA (Long) | 571.10 | 576.34 |
| RSI | 68.90 | 20.71 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 584.73
**Exit:** 
**Exit Price:** 567.2
**Position Size:** 
**PnL:** -19.84
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-07-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.58 | 18.15 |
| ATR | 18.50 | 18.94 |
| Volume | 2093121.00 | 2173137.00 |
| SMA (Short) | 576.74 | 567.68 |
| SMA (Long) | 575.35 | 567.87 |
| RSI | 78.27 | 34.79 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 590.74
**Exit:** 
**Exit Price:** 722.36
**Position Size:** 
**PnL:** 129.0
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-08-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.80 | 32.53 |
| ATR | 18.27 | 24.99 |
| Volume | 3191427.00 | 2447845.00 |
| SMA (Short) | 570.52 | 740.80 |
| SMA (Long) | 569.41 | 741.31 |
| RSI | 54.12 | 38.52 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 741.08
**Exit:** 
**Exit Price:** 682.55
**Position Size:** 
**PnL:** -61.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-02-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.15 | 21.78 |
| ATR | 20.40 | 19.54 |
| Volume | 2473473.00 | 1579099.00 |
| SMA (Short) | 737.70 | 719.25 |
| SMA (Long) | 733.37 | 722.88 |
| RSI | 64.90 | 37.03 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 749.35
**Exit:** 
**Exit Price:** 689.15
**Position Size:** 
**PnL:** -63.08
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 20.91 | 35.62 |
| ATR | 20.19 | 20.62 |
| Volume | 1210629.00 | 2081793.00 |
| SMA (Short) | 727.65 | 737.37 |
| SMA (Long) | 727.07 | 739.70 |
| RSI | 75.71 | 30.85 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 568.27
**Exit:** 
**Exit Price:** 443.29
**Position Size:** 
**PnL:** -127.0
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-10-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.95 | 43.69 |
| ATR | 20.61 | 20.17 |
| Volume | 1292240.00 | 12794693.84 |
| SMA (Short) | 570.46 | 560.88 |
| SMA (Long) | 570.01 | 568.39 |
| RSI | 64.08 | 12.39 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 454.74
**Exit:** 
**Exit Price:** 363.27
**Position Size:** 
**PnL:** -93.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.50 | 43.37 |
| ATR | 16.73 | 22.66 |
| Volume | 3213708.00 | 6593812.00 |
| SMA (Short) | 437.00 | 473.85 |
| SMA (Long) | 436.44 | 479.84 |
| RSI | 61.41 | 14.80 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 524.72
**Exit:** 
**Exit Price:** 771.35
**Position Size:** 
**PnL:** 244.04
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-04-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 59.50 | 31.11 |
| ATR | 37.13 | 29.30 |
| Volume | 7893425.00 | 2557918.00 |
| SMA (Short) | 462.20 | 811.60 |
| SMA (Long) | 453.12 | 813.30 |
| RSI | 84.92 | 26.60 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 827.79
**Exit:** 
**Exit Price:** 831.85
**Position Size:** 
**PnL:** 0.74
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 34.59 | 35.98 |
| ATR | 29.07 | 32.25 |
| Volume | 490650.00 | 3021328.00 |
| SMA (Short) | 780.10 | 888.86 |
| SMA (Long) | 778.32 | 897.81 |
| RSI | 63.21 | 31.19 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 891.88
**Exit:** 
**Exit Price:** 968.97
**Position Size:** 
**PnL:** 73.36
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-04-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 28.73 | 17.26 |
| ATR | 25.62 | 28.78 |
| Volume | 2974446.00 | 3167944.00 |
| SMA (Short) | 870.18 | 947.46 |
| SMA (Long) | 864.16 | 950.07 |
| RSI | 75.63 | 41.98 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 669.17
**Exit:** 
**Exit Price:** 596.75
**Position Size:** 
**PnL:** -74.96
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-01-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 15.67 | 36.23 |
| ATR | 19.23 | 19.78 |
| Volume | 1995987.00 | 3355188.00 |
| SMA (Short) | 675.30 | 665.63 |
| SMA (Long) | 674.26 | 675.51 |
| RSI | 51.70 | 17.27 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 707.4
**Exit:** 
**Exit Price:** 617.06
**Position Size:** 
**PnL:** -92.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-04-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 32.18 | 21.05 |
| ATR | 22.51 | 21.45 |
| Volume | 4971872.00 | 1078875.00 |
| SMA (Short) | 645.86 | 649.20 |
| SMA (Long) | 641.84 | 649.77 |
| RSI | 79.79 | 14.96 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 546.82
**Exit:** 
**Exit Price:** 533.81
**Position Size:** 
**PnL:** -15.17
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-09-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.47 | 10.84 |
| ATR | 19.38 | 15.09 |
| Volume | 1449496.00 | 718490.00 |
| SMA (Short) | 535.60 | 541.77 |
| SMA (Long) | 531.65 | 543.74 |
| RSI | 64.67 | 23.10 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 552.41
**Exit:** 
**Exit Price:** 487.01
**Position Size:** 
**PnL:** -67.48
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-11-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.53 | 32.79 |
| ATR | 12.62 | 14.87 |
| Volume | 567255.00 | 3099612.00 |
| SMA (Short) | 529.28 | 520.85 |
| SMA (Long) | 527.00 | 522.04 |
| RSI | 77.97 | 40.15 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 468.96
**Exit:** 
**Exit Price:** 855.41
**Position Size:** 
**PnL:** 383.8
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-02-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 28.26 | 19.31 |
| ATR | 11.23 | 21.67 |
| Volume | 1096959.00 | 2290941.00 |
| SMA (Short) | 437.52 | 862.59 |
| SMA (Long) | 436.31 | 867.39 |
| RSI | 77.94 | 34.59 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 946.55
**Exit:** 
**Exit Price:** 1001.7
**Position Size:** 
**PnL:** 51.26
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 35.84 | 70.01 |
| ATR | 22.85 | 36.46 |
| Volume | 2550759.00 | 3018985.00 |
| SMA (Short) | 875.96 | 1062.22 |
| SMA (Long) | 874.31 | 1072.03 |
| RSI | 68.95 | 26.63 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 1137.65
**Exit:** 
**Exit Price:** 1466.05
**Position Size:** 
**PnL:** 323.19
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-04-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 47.56 | 26.85 |
| ATR | 38.58 | 44.59 |
| Volume | 2589939.00 | 923928.00 |
| SMA (Short) | 1062.03 | 1483.89 |
| SMA (Long) | 1057.41 | 1484.03 |
| RSI | 66.25 | 35.92 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 1312.8
**Exit:** 
**Exit Price:** 1147.55
**Position Size:** 
**PnL:** -170.17
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 40.70 | 76.30 |
| ATR | 33.16 | 34.85 |
| Volume | 732526.00 | 974366.00 |
| SMA (Short) | 1300.87 | 1249.16 |
| SMA (Long) | 1291.59 | 1263.40 |
| RSI | 63.66 | 33.48 |

---

**Ticker:** AUROPHARMA.NS  
**Entry:** 
**Entry Price:** 1157.45
**Exit:** 
**Exit Price:** 1058.0
**Position Size:** 
**PnL:** -103.88
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-04-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 44.85 | 42.13 |
| ATR | 38.22 | 43.53 |
| Volume | 811910.00 | 2530340.00 |
| SMA (Short) | 1152.63 | 1130.49 |
| SMA (Long) | 1145.94 | 1134.97 |
| RSI | 63.27 | 32.44 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 718.38
**Exit:** 
**Exit Price:** 710.07
**Position Size:** 
**PnL:** -11.17
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-05-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.37 | 6.96 |
| ATR | 15.08 | 14.54 |
| Volume | 507318.00 | 191165.00 |
| SMA (Short) | 716.79 | 713.45 |
| SMA (Long) | 715.95 | 714.11 |
| RSI | 48.91 | 45.02 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 766.94
**Exit:** 
**Exit Price:** 896.77
**Position Size:** 
**PnL:** 126.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.35 | 12.90 |
| ATR | 17.10 | 42.27 |
| Volume | 571193.00 | 125539.00 |
| SMA (Short) | 718.80 | 917.90 |
| SMA (Long) | 716.51 | 920.73 |
| RSI | 70.34 | 38.83 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 875.36
**Exit:** 
**Exit Price:** 847.05
**Position Size:** 
**PnL:** -31.76
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.96 | 8.12 |
| ATR | 26.17 | 26.58 |
| Volume | 34420.00 | 124496.00 |
| SMA (Short) | 866.24 | 861.42 |
| SMA (Long) | 865.50 | 861.75 |
| RSI | 69.77 | 41.93 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 752.41
**Exit:** 
**Exit Price:** 720.39
**Position Size:** 
**PnL:** -34.97
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-05-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 17.35 | 13.28 |
| ATR | 28.59 | 23.63 |
| Volume | 179126.00 | 327263.00 |
| SMA (Short) | 739.66 | 731.84 |
| SMA (Long) | 739.30 | 731.91 |
| RSI | 52.26 | 39.86 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 698.02
**Exit:** 
**Exit Price:** 736.21
**Position Size:** 
**PnL:** 35.31
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-07-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.00 | 25.21 |
| ATR | 18.28 | 20.19 |
| Volume | 234065.00 | 361227.00 |
| SMA (Short) | 703.32 | 768.47 |
| SMA (Long) | 701.91 | 771.11 |
| RSI | 59.19 | 39.85 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 707.15
**Exit:** 
**Exit Price:** 805.62
**Position Size:** 
**PnL:** 95.45
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.33 | 50.33 |
| ATR | 21.19 | 27.95 |
| Volume | 74747.00 | 204901.00 |
| SMA (Short) | 690.48 | 832.68 |
| SMA (Long) | 689.00 | 838.05 |
| RSI | 71.30 | 29.15 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 864.71
**Exit:** 
**Exit Price:** 799.91
**Position Size:** 
**PnL:** -68.13
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-08-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 26.86 | 29.73 |
| ATR | 24.17 | 22.44 |
| Volume | 531469.00 | 259570.00 |
| SMA (Short) | 810.35 | 804.10 |
| SMA (Long) | 807.38 | 804.84 |
| RSI | 90.98 | 36.68 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 793.0
**Exit:** 
**Exit Price:** 700.9
**Position Size:** 
**PnL:** -95.09
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-02-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 27.20 | 31.80 |
| ATR | 16.93 | 20.89 |
| Volume | 533797.00 | 821469.00 |
| SMA (Short) | 762.73 | 772.63 |
| SMA (Long) | 760.00 | 775.03 |
| RSI | 68.00 | 13.38 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 679.88
**Exit:** 
**Exit Price:** 628.95
**Position Size:** 
**PnL:** -53.56
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.48 | 16.18 |
| ATR | 19.40 | 19.95 |
| Volume | 402267.00 | 578180.00 |
| SMA (Short) | 663.94 | 649.22 |
| SMA (Long) | 660.99 | 652.29 |
| RSI | 66.19 | 36.79 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 623.82
**Exit:** 
**Exit Price:** 593.44
**Position Size:** 
**PnL:** -32.81
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-10-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 19.03 | 25.24 |
| ATR | 16.68 | 22.33 |
| Volume | 990578.00 | 226979.00 |
| SMA (Short) | 588.72 | 617.32 |
| SMA (Long) | 585.06 | 624.66 |
| RSI | 86.07 | 23.96 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 688.88
**Exit:** 
**Exit Price:** 699.13
**Position Size:** 
**PnL:** 7.47
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 42.37 | 18.65 |
| ATR | 24.48 | 21.09 |
| Volume | 700286.00 | 532524.00 |
| SMA (Short) | 636.35 | 724.74 |
| SMA (Long) | 636.06 | 725.71 |
| RSI | 67.11 | 34.30 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 671.86
**Exit:** 
**Exit Price:** 629.98
**Position Size:** 
**PnL:** -44.49
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.54 | 14.01 |
| ATR | 20.75 | 19.59 |
| Volume | 339295.00 | 254972.00 |
| SMA (Short) | 657.98 | 648.92 |
| SMA (Long) | 657.00 | 650.76 |
| RSI | 48.93 | 37.03 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 706.4
**Exit:** 
**Exit Price:** 662.54
**Position Size:** 
**PnL:** -46.59
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.23 | 6.76 |
| ATR | 19.70 | 20.32 |
| Volume | 1025360.00 | 114109.00 |
| SMA (Short) | 655.23 | 669.95 |
| SMA (Long) | 654.97 | 671.87 |
| RSI | 70.39 | 40.25 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 504.79
**Exit:** 
**Exit Price:** 507.14
**Position Size:** 
**PnL:** 0.32
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-12-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 10.76 | 12.98 |
| ATR | 13.37 | 15.23 |
| Volume | 395366.00 | 455991.00 |
| SMA (Short) | 503.21 | 513.71 |
| SMA (Long) | 503.00 | 513.78 |
| RSI | 58.80 | 45.89 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 353.69
**Exit:** 
**Exit Price:** 413.93
**Position Size:** 
**PnL:** 58.71
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 18.72 | 5.16 |
| ATR | 21.00 | 14.06 |
| Volume | 2628854.00 | 357445.00 |
| SMA (Short) | 335.71 | 418.79 |
| SMA (Long) | 334.55 | 419.04 |
| RSI | 71.02 | 26.18 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 447.16
**Exit:** 
**Exit Price:** 782.52
**Position Size:** 
**PnL:** 332.9
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 13.70 | 20.45 |
| ATR | 14.44 | 31.47 |
| Volume | 1179898.00 | 1104127.00 |
| SMA (Short) | 426.25 | 803.18 |
| SMA (Long) | 426.02 | 808.49 |
| RSI | 64.45 | 47.06 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 778.0
**Exit:** 
**Exit Price:** 839.8
**Position Size:** 
**PnL:** 58.57
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-06-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 10.81 | 52.69 |
| ATR | 26.26 | 31.44 |
| Volume | 583316.00 | 1533500.00 |
| SMA (Short) | 786.33 | 913.95 |
| SMA (Long) | 786.02 | 922.64 |
| RSI | 70.03 | 21.60 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 899.32
**Exit:** 
**Exit Price:** 901.89
**Position Size:** 
**PnL:** -1.03
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 26.42 | 24.64 |
| ATR | 28.45 | 26.19 |
| Volume | 506043.00 | 1896737.00 |
| SMA (Short) | 869.93 | 888.86 |
| SMA (Long) | 865.72 | 890.73 |
| RSI | 60.06 | 44.49 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 927.53
**Exit:** 
**Exit Price:** 976.03
**Position Size:** 
**PnL:** 44.69
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-02-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 23.73 | 30.93 |
| ATR | 27.09 | 33.65 |
| Volume | 1473610.00 | 219580.00 |
| SMA (Short) | 898.38 | 990.78 |
| SMA (Long) | 897.49 | 998.17 |
| RSI | 60.87 | 32.45 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 1026.63
**Exit:** 
**Exit Price:** 1144.92
**Position Size:** 
**PnL:** 113.95
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 31.95 | 27.46 |
| ATR | 26.33 | 38.35 |
| Volume | 512099.00 | 461834.00 |
| SMA (Short) | 973.68 | 1168.91 |
| SMA (Long) | 966.96 | 1169.64 |
| RSI | 72.09 | 39.23 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 1250.93
**Exit:** 
**Exit Price:** 1367.93
**Position Size:** 
**PnL:** 111.76
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 30.45 | 20.47 |
| ATR | 36.40 | 38.09 |
| Volume | 1089188.00 | 472768.00 |
| SMA (Short) | 1179.65 | 1344.69 |
| SMA (Long) | 1175.63 | 1348.78 |
| RSI | 63.37 | 47.86 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 1406.54
**Exit:** 
**Exit Price:** 1380.41
**Position Size:** 
**PnL:** -31.7
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-02-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.55 | 35.97 |
| ATR | 37.34 | 36.44 |
| Volume | 284204.00 | 508254.00 |
| SMA (Short) | 1355.90 | 1378.88 |
| SMA (Long) | 1355.40 | 1384.21 |
| RSI | 42.34 | 45.68 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 1527.35
**Exit:** 
**Exit Price:** 1461.09
**Position Size:** 
**PnL:** -72.24
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-04-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 52.70 | 38.82 |
| ATR | 39.16 | 40.19 |
| Volume | 3782820.28 | 1045243.00 |
| SMA (Short) | 1400.78 | 1538.92 |
| SMA (Long) | 1394.95 | 1545.89 |
| RSI | 69.86 | 29.63 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 1587.0
**Exit:** 
**Exit Price:** 1732.14
**Position Size:** 
**PnL:** 138.49
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-05-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 24.83 | 89.63 |
| ATR | 35.79 | 41.85 |
| Volume | 394578.00 | 1420634.00 |
| SMA (Short) | 1563.45 | 1808.65 |
| SMA (Long) | 1561.77 | 1818.45 |
| RSI | 68.68 | 35.36 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 1745.68
**Exit:** 
**Exit Price:** 3587.5
**Position Size:** 
**PnL:** 1831.15
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 38.67 | 135.33 |
| ATR | 35.82 | 134.99 |
| Volume | 488247.00 | 1111742.00 |
| SMA (Short) | 1693.86 | 3682.61 |
| SMA (Long) | 1685.97 | 3696.85 |
| RSI | 67.01 | 25.37 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 3808.72
**Exit:** 
**Exit Price:** 3684.47
**Position Size:** 
**PnL:** -139.23
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 81.32 | 93.90 |
| ATR | 119.63 | 107.62 |
| Volume | 522503.00 | 265947.00 |
| SMA (Short) | 3731.32 | 3726.89 |
| SMA (Long) | 3728.09 | 3736.59 |
| RSI | 49.22 | 41.98 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 3647.81
**Exit:** 
**Exit Price:** 3355.5
**Position Size:** 
**PnL:** -306.32
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-12-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 74.84 | 124.06 |
| ATR | 113.04 | 111.31 |
| Volume | 385473.00 | 309606.00 |
| SMA (Short) | 3527.39 | 3474.10 |
| SMA (Long) | 3507.40 | 3475.54 |
| RSI | 68.75 | 38.79 |

---

**Ticker:** CUMMINSIND.NS  
**Entry:** 
**Entry Price:** 2862.1
**Exit:** 
**Exit Price:** 2914.6
**Position Size:** 
**PnL:** 40.95
**Rationale:** Buy: short SMA crossed above long SMA at index 2025-03-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 63.39 | 108.20 |
| ATR | 101.96 | 105.54 |
| Volume | 205971.00 | 322569.00 |
| SMA (Short) | 2871.78 | 2855.33 |
| SMA (Long) | 2860.09 | 2867.20 |
| RSI | 52.03 | 43.84 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 345.57
**Exit:** 
**Exit Price:** 341.17
**Position Size:** 
**PnL:** -5.78
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-05-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.51 | 7.59 |
| ATR | 14.67 | 14.32 |
| Volume | 389862.00 | 189710.00 |
| SMA (Short) | 347.86 | 346.57 |
| SMA (Long) | 347.35 | 346.84 |
| RSI |  |  |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 312.03
**Exit:** 
**Exit Price:** 306.17
**Position Size:** 
**PnL:** -7.1
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-10-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 8.18 | 3.68 |
| ATR | 9.88 | 9.07 |
| Volume | 22440.00 | 44472.00 |
| SMA (Short) | 306.50 | 305.62 |
| SMA (Long) | 306.13 | 305.98 |
| RSI | 78.57 | 36.55 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 304.02
**Exit:** 
**Exit Price:** 295.19
**Position Size:** 
**PnL:** -10.03
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 1.56 | 4.21 |
| ATR | 8.52 | 8.02 |
| Volume | 15970.00 | 48392.00 |
| SMA (Short) | 303.35 | 303.01 |
| SMA (Long) | 303.22 | 303.79 |
| RSI | 48.31 | 34.87 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 278.12
**Exit:** 
**Exit Price:** 305.05
**Position Size:** 
**PnL:** 25.77
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.11 | 4.57 |
| ATR | 8.15 | 7.38 |
| Volume | 20450.00 | 23126.00 |
| SMA (Short) | 276.02 | 308.63 |
| SMA (Long) | 275.86 | 308.73 |
| RSI | 79.46 | 36.17 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 322.05
**Exit:** 
**Exit Price:** 427.34
**Position Size:** 
**PnL:** 103.79
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-07-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.23 | 14.63 |
| ATR | 7.23 | 25.49 |
| Volume | 68212.00 | 78998.00 |
| SMA (Short) | 311.19 | 452.52 |
| SMA (Long) | 309.78 | 455.01 |
| RSI | 57.32 | 36.57 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 558.95
**Exit:** 
**Exit Price:** 736.53
**Position Size:** 
**PnL:** 174.98
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-12-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 57.58 | 8.80 |
| ATR | 27.55 | 22.08 |
| Volume | 434790.00 | 170312.00 |
| SMA (Short) | 470.43 | 746.52 |
| SMA (Long) | 467.91 | 748.48 |
| RSI | 77.96 | 32.98 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 783.84
**Exit:** 
**Exit Price:** 1041.15
**Position Size:** 
**PnL:** 253.66
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-09-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 22.17 | 12.79 |
| ATR | 21.73 | 34.79 |
| Volume | 266264.00 | 184000.00 |
| SMA (Short) | 754.24 | 1061.78 |
| SMA (Long) | 747.83 | 1063.53 |
| RSI | 74.87 | 20.58 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 1070.83
**Exit:** 
**Exit Price:** 1050.14
**Position Size:** 
**PnL:** -24.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.27 | 35.82 |
| ATR | 38.66 | 38.07 |
| Volume | 443617.00 | 1017914.00 |
| SMA (Short) | 1020.13 | 1097.09 |
| SMA (Long) | 1019.00 | 1104.66 |
| RSI | 66.79 | 23.58 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 1137.97
**Exit:** 
**Exit Price:** 1083.86
**Position Size:** 
**PnL:** -58.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-09-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 75.59 | 101.15 |
| ATR | 38.03 | 48.80 |
| Volume | 824105.00 | 802802.00 |
| SMA (Short) | 1078.16 | 1138.68 |
| SMA (Long) | 1060.02 | 1153.84 |
| RSI | 69.44 | 29.62 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 856.1
**Exit:** 
**Exit Price:** 804.49
**Position Size:** 
**PnL:** -54.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 32.22 | 35.10 |
| ATR | 22.63 | 23.69 |
| Volume | 646430.00 | 691072.00 |
| SMA (Short) | 815.06 | 860.81 |
| SMA (Long) | 805.78 | 867.96 |
| RSI | 81.57 | 20.62 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 696.11
**Exit:** 
**Exit Price:** 939.08
**Position Size:** 
**PnL:** 239.7
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-08-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.38 | 55.78 |
| ATR | 22.27 | 38.93 |
| Volume | 340002.00 | 1260983.00 |
| SMA (Short) | 697.18 | 1042.00 |
| SMA (Long) | 695.90 | 1046.73 |
| RSI | 59.08 | 13.33 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 927.88
**Exit:** 
**Exit Price:** 1212.28
**Position Size:** 
**PnL:** 280.12
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-05-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 28.73 | 43.41 |
| ATR | 65.62 | 38.18 |
| Volume | 896734.00 | 391575.00 |
| SMA (Short) | 878.57 | 1253.54 |
| SMA (Long) | 876.56 | 1257.88 |
| RSI | 64.23 | 23.24 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 1330.58
**Exit:** 
**Exit Price:** 1292.72
**Position Size:** 
**PnL:** -43.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 49.57 | 17.20 |
| ATR | 39.42 | 48.79 |
| Volume | 375948.00 | 935521.00 |
| SMA (Short) | 1265.49 | 1317.46 |
| SMA (Long) | 1264.74 | 1317.61 |
| RSI | 50.24 | 27.00 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 1435.3
**Exit:** 
**Exit Price:** 1501.93
**Position Size:** 
**PnL:** 60.76
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 50.31 | 82.13 |
| ATR | 50.50 | 56.62 |
| Volume | 1742646.00 | 1212950.00 |
| SMA (Short) | 1328.70 | 1592.52 |
| SMA (Long) | 1319.31 | 1597.16 |
| RSI | 68.93 | 42.44 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 1599.35
**Exit:** 
**Exit Price:** 2217.47
**Position Size:** 
**PnL:** 610.49
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-04-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.01 | 51.51 |
| ATR | 55.47 | 55.38 |
| Volume | 430886.00 | 468896.00 |
| SMA (Short) | 1591.21 | 2228.45 |
| SMA (Long) | 1588.72 | 2244.03 |
| RSI | 54.45 | 23.62 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2387.0
**Exit:** 
**Exit Price:** 2453.19
**Position Size:** 
**PnL:** 56.51
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-09-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 62.84 | 40.33 |
| ATR | 56.40 | 68.40 |
| Volume | 483625.00 | 420628.00 |
| SMA (Short) | 2264.03 | 2415.95 |
| SMA (Long) | 2260.01 | 2417.38 |
| RSI | 73.08 | 41.02 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2322.57
**Exit:** 
**Exit Price:** 2123.03
**Position Size:** 
**PnL:** -208.43
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 63.53 | 56.44 |
| ATR | 65.33 | 65.00 |
| Volume | 221924.00 | 230260.00 |
| SMA (Short) | 2241.79 | 2232.18 |
| SMA (Long) | 2229.93 | 2238.80 |
| RSI | 86.89 | 30.27 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2087.87
**Exit:** 
**Exit Price:** 1850.75
**Position Size:** 
**PnL:** -245.0
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 32.56 | 90.87 |
| ATR | 75.41 | 67.52 |
| Volume | 173629.00 | 259808.00 |
| SMA (Short) | 2045.45 | 1968.12 |
| SMA (Long) | 2040.62 | 1993.45 |
| RSI | 68.57 | 29.95 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2156.39
**Exit:** 
**Exit Price:** 2036.41
**Position Size:** 
**PnL:** -128.37
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 94.77 | 57.04 |
| ATR | 70.05 | 71.80 |
| Volume | 524240.00 | 123407.00 |
| SMA (Short) | 2050.51 | 2080.24 |
| SMA (Long) | 2037.76 | 2081.86 |
| RSI | 68.32 | 14.77 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2133.14
**Exit:** 
**Exit Price:** 2133.94
**Position Size:** 
**PnL:** -7.73
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-08-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 43.92 | 73.01 |
| ATR | 72.37 | 61.06 |
| Volume | 142057.00 | 232484.00 |
| SMA (Short) | 2092.12 | 2158.55 |
| SMA (Long) | 2089.98 | 2178.92 |
| RSI | 59.31 | 40.68 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 1941.0
**Exit:** 
**Exit Price:** 2004.26
**Position Size:** 
**PnL:** 55.37
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-11-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 38.87 | 145.87 |
| ATR | 48.34 | 56.47 |
| Volume | 199730.00 | 265356.00 |
| SMA (Short) | 1902.09 | 2131.10 |
| SMA (Long) | 1898.32 | 2138.01 |
| RSI | 53.62 | 38.77 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2026.59
**Exit:** 
**Exit Price:** 2332.75
**Position Size:** 
**PnL:** 297.45
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 44.73 | 52.30 |
| ATR | 52.03 | 59.45 |
| Volume | 132571.00 | 200039.00 |
| SMA (Short) | 2021.31 | 2363.16 |
| SMA (Long) | 2010.32 | 2365.31 |
| RSI | 62.50 | 33.66 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2480.8
**Exit:** 
**Exit Price:** 2541.35
**Position Size:** 
**PnL:** 50.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-09-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 43.82 | 59.90 |
| ATR | 57.52 | 53.66 |
| Volume | 510275.00 | 265697.00 |
| SMA (Short) | 2389.14 | 2538.58 |
| SMA (Long) | 2379.97 | 2545.60 |
| RSI | 67.78 | 47.59 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2564.13
**Exit:** 
**Exit Price:** 2418.19
**Position Size:** 
**PnL:** -155.91
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-12-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 42.59 | 54.45 |
| ATR | 54.21 | 57.13 |
| Volume | 246881.00 | 260386.00 |
| SMA (Short) | 2551.28 | 2544.62 |
| SMA (Long) | 2548.37 | 2551.39 |
| RSI | 44.34 | 31.98 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2646.39
**Exit:** 
**Exit Price:** 2419.03
**Position Size:** 
**PnL:** -237.49
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-02-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 56.75 | 87.63 |
| ATR | 59.08 | 73.37 |
| Volume | 646356.00 | 234190.00 |
| SMA (Short) | 2555.02 | 2529.27 |
| SMA (Long) | 2544.78 | 2541.13 |
| RSI | 71.29 | 34.78 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2420.03
**Exit:** 
**Exit Price:** 2832.5
**Position Size:** 
**PnL:** 401.97
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-04-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 62.26 | 99.54 |
| ATR | 63.22 | 95.23 |
| Volume | 374663.00 | 1703248.00 |
| SMA (Short) | 2330.27 | 3108.32 |
| SMA (Long) | 2313.91 | 3129.42 |
| RSI | 72.90 | 13.95 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 3067.24
**Exit:** 
**Exit Price:** 3030.0
**Position Size:** 
**PnL:** -49.44
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 68.97 | 89.64 |
| ATR | 76.97 | 81.60 |
| Volume | 79109.00 | 375908.00 |
| SMA (Short) | 3027.88 | 2979.62 |
| SMA (Long) | 3019.82 | 2980.83 |
| RSI | 81.15 | 50.21 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 3051.14
**Exit:** 
**Exit Price:** 2919.46
**Position Size:** 
**PnL:** -143.62
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 83.21 | 38.53 |
| ATR | 81.01 | 73.99 |
| Volume | 237013.00 | 210522.00 |
| SMA (Short) | 2982.45 | 2958.69 |
| SMA (Long) | 2978.61 | 2964.45 |
| RSI | 47.91 | 40.01 |

---

**Ticker:** BALKRISIND.NS  
**Entry:** 
**Entry Price:** 2905.85
**Exit:** 
**Exit Price:** 2591.96
**Position Size:** 
**PnL:** -324.89
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 34.09 | 91.97 |
| ATR | 70.82 | 73.16 |
| Volume | 243400.00 | 85981.00 |
| SMA (Short) | 2828.32 | 2779.64 |
| SMA (Long) | 2824.41 | 2795.20 |
| RSI | 63.45 | 31.46 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 119.19
**Exit:** 
**Exit Price:** 155.04
**Position Size:** 
**PnL:** 35.3
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-06-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 8.31 | 7.79 |
| ATR | 4.03 | 7.28 |
| Volume | 1105447.00 | 473049.00 |
| SMA (Short) | 109.35 | 157.22 |
| SMA (Long) | 109.04 | 158.43 |
| RSI | 83.58 | 26.75 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 168.71
**Exit:** 
**Exit Price:** 151.37
**Position Size:** 
**PnL:** -17.97
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-12-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.40 | 6.05 |
| ATR | 6.43 | 6.32 |
| Volume | 1820630.00 | 342467.00 |
| SMA (Short) | 159.16 | 158.88 |
| SMA (Long) | 158.78 | 159.64 |
| RSI | 67.61 | 45.10 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 164.36
**Exit:** 
**Exit Price:** 143.74
**Position Size:** 
**PnL:** -21.23
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 4.83 | 7.05 |
| ATR | 6.16 | 6.24 |
| Volume | 335512.00 | 646742.00 |
| SMA (Short) | 161.37 | 157.44 |
| SMA (Long) | 160.54 | 157.58 |
| RSI | 74.00 | 32.06 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 127.81
**Exit:** 
**Exit Price:** 322.43
**Position Size:** 
**PnL:** 193.72
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.21 | 19.95 |
| ATR | 6.23 | 16.17 |
| Volume | 357749.00 | 1717022.00 |
| SMA (Short) | 129.10 | 355.48 |
| SMA (Long) | 128.39 | 356.21 |
| RSI | 61.29 | 25.16 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 348.7
**Exit:** 
**Exit Price:** 653.16
**Position Size:** 
**PnL:** 302.45
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 20.08 | 10.58 |
| ATR | 14.88 | 22.00 |
| Volume | 3587195.00 | 117811.00 |
| SMA (Short) | 313.69 | 643.33 |
| SMA (Long) | 307.43 | 645.03 |
| RSI | 81.31 | 40.44 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 657.87
**Exit:** 
**Exit Price:** 668.17
**Position Size:** 
**PnL:** 7.64
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-09-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.26 | 7.86 |
| ATR | 21.72 | 20.52 |
| Volume | 1625254.00 | 788153.00 |
| SMA (Short) | 631.73 | 673.90 |
| SMA (Long) | 630.33 | 675.12 |
| RSI | 80.64 | 34.79 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 733.59
**Exit:** 
**Exit Price:** 802.95
**Position Size:** 
**PnL:** 66.28
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-12-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 32.51 | 12.19 |
| ATR | 21.38 | 27.85 |
| Volume | 668742.00 | 545053.00 |
| SMA (Short) | 690.23 | 819.14 |
| SMA (Long) | 686.33 | 820.48 |
| RSI | 79.54 | 34.46 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 861.23
**Exit:** 
**Exit Price:** 897.95
**Position Size:** 
**PnL:** 33.2
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-04-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 40.43 | 30.43 |
| ATR | 27.46 | 26.56 |
| Volume | 753807.00 | 1056721.00 |
| SMA (Short) | 843.29 | 884.44 |
| SMA (Long) | 836.29 | 886.47 |
| RSI | 64.40 | 37.76 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 873.52
**Exit:** 
**Exit Price:** 831.8
**Position Size:** 
**PnL:** -45.13
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-08-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 24.73 | 21.10 |
| ATR | 26.42 | 25.48 |
| Volume | 820739.00 | 668530.00 |
| SMA (Short) | 871.32 | 861.44 |
| SMA (Long) | 868.57 | 862.35 |
| RSI | 55.63 | 45.61 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 871.67
**Exit:** 
**Exit Price:** 783.85
**Position Size:** 
**PnL:** -91.12
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-09-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.32 | 29.02 |
| ATR | 25.60 | 26.33 |
| Volume | 1660001.00 | 1611881.00 |
| SMA (Short) | 857.90 | 850.93 |
| SMA (Long) | 857.49 | 853.43 |
| RSI | 57.45 | 35.70 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 647.31
**Exit:** 
**Exit Price:** 660.02
**Position Size:** 
**PnL:** 10.09
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 14.69 | 32.21 |
| ATR | 32.58 | 21.04 |
| Volume | 1630689.00 | 5112096.00 |
| SMA (Short) | 650.28 | 673.45 |
| SMA (Long) | 648.98 | 675.20 |
| RSI | 79.35 | 28.74 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 721.01
**Exit:** 
**Exit Price:** 647.65
**Position Size:** 
**PnL:** -76.09
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 36.71 | 37.89 |
| ATR | 20.44 | 23.12 |
| Volume | 1421911.00 | 1942083.00 |
| SMA (Short) | 678.25 | 718.89 |
| SMA (Long) | 676.17 | 720.29 |
| RSI | 87.59 | 20.08 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 511.69
**Exit:** 
**Exit Price:** 590.09
**Position Size:** 
**PnL:** 76.19
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.37 | 19.36 |
| ATR | 22.41 | 22.13 |
| Volume | 4121858.00 | 1691015.00 |
| SMA (Short) | 487.61 | 621.77 |
| SMA (Long) | 486.04 | 622.14 |
| RSI | 65.02 | 32.98 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 663.2
**Exit:** 
**Exit Price:** 619.82
**Position Size:** 
**PnL:** -45.94
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.62 | 71.72 |
| ATR | 17.40 | 33.46 |
| Volume | 2003755.00 | 2010918.00 |
| SMA (Short) | 622.67 | 754.31 |
| SMA (Long) | 620.13 | 754.38 |
| RSI | 72.05 | 24.01 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 738.61
**Exit:** 
**Exit Price:** 1168.21
**Position Size:** 
**PnL:** 425.79
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-05-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.87 | 26.40 |
| ATR | 56.69 | 51.10 |
| Volume | 3585712.00 | 1292640.00 |
| SMA (Short) | 702.57 | 1174.89 |
| SMA (Long) | 696.64 | 1175.37 |
| RSI | 52.05 | 34.88 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1229.48
**Exit:** 
**Exit Price:** 1234.92
**Position Size:** 
**PnL:** 0.51
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-11-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 22.63 | 48.59 |
| ATR | 52.42 | 45.86 |
| Volume | 1947383.00 | 1372662.00 |
| SMA (Short) | 1190.43 | 1278.14 |
| SMA (Long) | 1188.19 | 1288.18 |
| RSI | 74.11 | 18.82 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1399.21
**Exit:** 
**Exit Price:** 1315.01
**Position Size:** 
**PnL:** -89.64
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 88.23 | 32.16 |
| ATR | 48.03 | 47.64 |
| Volume | 2179561.00 | 1602126.00 |
| SMA (Short) | 1306.02 | 1290.81 |
| SMA (Long) | 1299.57 | 1294.71 |
| RSI | 67.96 | 33.43 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1353.43
**Exit:** 
**Exit Price:** 1245.11
**Position Size:** 
**PnL:** -113.52
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 27.82 | 37.01 |
| ATR | 45.68 | 46.96 |
| Volume | 864530.00 | 667881.00 |
| SMA (Short) | 1309.65 | 1303.01 |
| SMA (Long) | 1306.00 | 1307.20 |
| RSI | 58.93 | 41.06 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1175.37
**Exit:** 
**Exit Price:** 1124.94
**Position Size:** 
**PnL:** -55.03
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-07-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 26.09 | 19.62 |
| ATR | 35.33 | 25.64 |
| Volume | 1264792.00 | 594744.00 |
| SMA (Short) | 1167.32 | 1158.15 |
| SMA (Long) | 1163.45 | 1161.50 |
| RSI | 62.21 | 18.44 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1175.68
**Exit:** 
**Exit Price:** 1821.51
**Position Size:** 
**PnL:** 639.83
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-08-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 34.94 | 10.26 |
| ATR | 26.23 | 27.04 |
| Volume | 1004794.00 | 350403.00 |
| SMA (Short) | 1168.33 | 1827.62 |
| SMA (Long) | 1168.05 | 1827.92 |
| RSI | 50.42 | 43.61 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1641.01
**Exit:** 
**Exit Price:** 1974.56
**Position Size:** 
**PnL:** 326.31
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 53.35 | 15.31 |
| ATR | 47.56 | 68.96 |
| Volume | 453075.00 | 148600.00 |
| SMA (Short) | 1560.50 | 1966.49 |
| SMA (Long) | 1546.80 | 1968.45 |
| RSI | 65.33 | 30.10 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 2016.25
**Exit:** 
**Exit Price:** 1985.14
**Position Size:** 
**PnL:** -39.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-11-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 21.15 | 17.36 |
| ATR | 69.01 | 69.54 |
| Volume | 324319.00 | 195221.00 |
| SMA (Short) | 1973.75 | 1980.66 |
| SMA (Long) | 1972.79 | 1981.43 |
| RSI | 41.47 | 36.55 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 2188.31
**Exit:** 
**Exit Price:** 2116.95
**Position Size:** 
**PnL:** -79.98
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 83.65 | 54.47 |
| ATR | 67.94 | 59.88 |
| Volume | 1490549.00 | 293296.00 |
| SMA (Short) | 2024.45 | 2099.19 |
| SMA (Long) | 2011.53 | 2105.15 |
| RSI | 75.96 | 36.60 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 2153.64
**Exit:** 
**Exit Price:** 2086.68
**Position Size:** 
**PnL:** -75.45
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-01-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 32.54 | 26.50 |
| ATR | 61.12 | 61.59 |
| Volume | 144965.00 | 213180.00 |
| SMA (Short) | 2133.21 | 2132.05 |
| SMA (Long) | 2128.01 | 2132.48 |
| RSI | 53.04 | 62.85 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 1947.11
**Exit:** 
**Exit Price:** 3031.34
**Position Size:** 
**PnL:** 1074.28
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 28.57 | 86.28 |
| ATR | 54.89 | 97.17 |
| Volume | 386583.00 | 201674.00 |
| SMA (Short) | 1944.37 | 3124.15 |
| SMA (Long) | 1944.24 | 3145.48 |
| RSI | 69.31 | 14.76 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 3204.65
**Exit:** 
**Exit Price:** 3200.24
**Position Size:** 
**PnL:** -17.23
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-12-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 51.21 | 29.05 |
| ATR | 87.35 | 87.03 |
| Volume | 177694.00 | 406476.00 |
| SMA (Short) | 3176.40 | 3177.88 |
| SMA (Long) | 3170.48 | 3179.66 |
| RSI | 66.43 | 60.40 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 3229.66
**Exit:** 
**Exit Price:** 3121.15
**Position Size:** 
**PnL:** -121.21
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-12-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 27.83 | 33.44 |
| ATR | 86.47 | 86.50 |
| Volume | 209690.00 | 413007.00 |
| SMA (Short) | 3182.62 | 3174.98 |
| SMA (Long) | 3182.20 | 3180.42 |
| RSI | 58.58 | 39.62 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 3048.66
**Exit:** 
**Exit Price:** 3686.01
**Position Size:** 
**PnL:** 623.88
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-04-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 122.02 | 162.10 |
| ATR | 80.00 | 128.55 |
| Volume | 404732.00 | 414341.00 |
| SMA (Short) | 2868.62 | 4006.54 |
| SMA (Long) | 2850.31 | 4012.83 |
| RSI | 88.22 | 31.51 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 4115.44
**Exit:** 
**Exit Price:** 3688.95
**Position Size:** 
**PnL:** -442.09
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 147.74 | 122.59 |
| ATR | 103.16 | 100.19 |
| Volume | 930475.00 | 202600.00 |
| SMA (Short) | 3892.34 | 3828.17 |
| SMA (Long) | 3860.47 | 3857.84 |
| RSI | 74.54 | 28.32 |

---

**Ticker:** ESCORTS.NS  
**Entry:** 
**Entry Price:** 3563.57
**Exit:** 
**Exit Price:** 3292.17
**Position Size:** 
**PnL:** -285.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-02-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 105.97 | 132.02 |
| ATR | 95.20 | 97.78 |
| Volume | 105561.00 | 291371.00 |
| SMA (Short) | 3430.63 | 3388.97 |
| SMA (Long) | 3425.06 | 3390.46 |
| RSI | 68.76 | 35.65 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 238.05
**Exit:** 
**Exit Price:** 237.75
**Position Size:** 
**PnL:** -1.25
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-05-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.58 | 3.99 |
| ATR | 10.54 | 8.76 |
| Volume | 66199.00 | 40018.00 |
| SMA (Short) | 242.78 | 239.92 |
| SMA (Long) | 241.96 | 240.87 |
| RSI |  | 55.04 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 258.95
**Exit:** 
**Exit Price:** 244.65
**Position Size:** 
**PnL:** -15.3
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.21 | 5.90 |
| ATR | 9.53 | 9.25 |
| Volume | 194657.00 | 90274.00 |
| SMA (Short) | 242.68 | 247.94 |
| SMA (Long) | 242.65 | 247.96 |
| RSI | 66.02 | 29.58 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 252.2
**Exit:** 
**Exit Price:** 310.7
**Position Size:** 
**PnL:** 57.38
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-07-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.03 | 12.95 |
| ATR | 9.12 | 13.72 |
| Volume | 58826.00 | 83574.00 |
| SMA (Short) | 249.08 | 322.93 |
| SMA (Long) | 248.51 | 325.16 |
| RSI | 55.75 | 16.12 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 330.7
**Exit:** 
**Exit Price:** 328.05
**Position Size:** 
**PnL:** -3.97
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-12-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.70 | 4.04 |
| ATR | 13.17 | 13.11 |
| Volume | 66482.00 | 87106.00 |
| SMA (Short) | 333.72 | 333.35 |
| SMA (Long) | 333.36 | 333.53 |
| RSI | 61.41 | 56.50 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 336.25
**Exit:** 
**Exit Price:** 319.75
**Position Size:** 
**PnL:** -17.81
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.19 | 7.37 |
| ATR | 11.86 | 11.08 |
| Volume | 111106.00 | 145178.00 |
| SMA (Short) | 335.17 | 329.92 |
| SMA (Long) | 334.54 | 330.31 |
| RSI | 56.39 | 39.22 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 295.85
**Exit:** 
**Exit Price:** 355.2
**Position Size:** 
**PnL:** 58.05
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-03-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 9.67 | 4.46 |
| ATR | 9.67 | 10.35 |
| Volume | 177461.00 | 67822.00 |
| SMA (Short) | 288.64 | 361.15 |
| SMA (Long) | 288.44 | 361.83 |
| RSI | 70.96 | 47.75 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 354.5
**Exit:** 
**Exit Price:** 305.7
**Position Size:** 
**PnL:** -50.12
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.00 | 18.93 |
| ATR | 9.01 | 10.95 |
| Volume | 101877.00 | 373435.00 |
| SMA (Short) | 352.33 | 348.40 |
| SMA (Long) | 352.16 | 348.93 |
| RSI | 73.15 | 15.00 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 321.7
**Exit:** 
**Exit Price:** 518.35
**Position Size:** 
**PnL:** 194.97
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.47 | 6.64 |
| ATR | 11.62 | 19.87 |
| Volume | 41288.00 | 15558.00 |
| SMA (Short) | 315.46 | 516.00 |
| SMA (Long) | 313.38 | 518.51 |
| RSI | 72.69 | 31.48 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 540.6
**Exit:** 
**Exit Price:** 710.75
**Position Size:** 
**PnL:** 167.65
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-08-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 13.14 | 5.60 |
| ATR | 14.52 | 21.90 |
| Volume | 139327.00 | 91452.00 |
| SMA (Short) | 517.70 | 702.77 |
| SMA (Long) | 517.04 | 703.08 |
| RSI | 81.31 | 54.16 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 725.25
**Exit:** 
**Exit Price:** 779.05
**Position Size:** 
**PnL:** 50.79
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-01-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.96 | 10.64 |
| ATR | 21.59 | 30.62 |
| Volume | 158709.00 | 361417.00 |
| SMA (Short) | 705.23 | 778.95 |
| SMA (Long) | 704.85 | 779.05 |
| RSI | 60.61 | 31.55 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 815.1
**Exit:** 
**Exit Price:** 735.65
**Position Size:** 
**PnL:** -82.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 38.48 | 31.34 |
| ATR | 22.45 | 26.27 |
| Volume | 273930.00 | 196766.00 |
| SMA (Short) | 764.66 | 762.26 |
| SMA (Long) | 760.01 | 768.00 |
| RSI | 82.20 | 11.96 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 609.15
**Exit:** 
**Exit Price:** 703.25
**Position Size:** 
**PnL:** 91.48
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.40 | 10.32 |
| ATR | 28.30 | 25.12 |
| Volume | 37568.00 | 358686.00 |
| SMA (Short) | 606.96 | 714.93 |
| SMA (Long) | 598.28 | 716.80 |
| RSI | 75.88 | 41.17 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 846.35
**Exit:** 
**Exit Price:** 757.2
**Position Size:** 
**PnL:** -92.36
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 52.17 | 35.87 |
| ATR | 25.47 | 35.74 |
| Volume | 1314819.00 | 223964.00 |
| SMA (Short) | 733.64 | 801.90 |
| SMA (Long) | 730.68 | 811.71 |
| RSI | 84.02 | 11.12 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 919.55
**Exit:** 
**Exit Price:** 908.65
**Position Size:** 
**PnL:** -14.56
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-08-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 41.46 | 14.93 |
| ATR | 39.30 | 37.66 |
| Volume | 544289.00 | 493564.00 |
| SMA (Short) | 846.36 | 932.88 |
| SMA (Long) | 839.08 | 935.79 |
| RSI | 78.25 | 37.05 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 906.65
**Exit:** 
**Exit Price:** 919.7
**Position Size:** 
**PnL:** 9.4
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.71 | 27.85 |
| ATR | 29.59 | 38.66 |
| Volume | 88715.00 | 200113.00 |
| SMA (Short) | 924.58 | 967.55 |
| SMA (Long) | 923.02 | 969.07 |
| RSI | 54.05 | 33.43 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 957.6
**Exit:** 
**Exit Price:** 915.4
**Position Size:** 
**PnL:** -45.95
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 12.65 | 65.30 |
| ATR | 28.29 | 40.61 |
| Volume | 169428.00 | 271254.00 |
| SMA (Short) | 937.58 | 1019.55 |
| SMA (Long) | 934.89 | 1037.74 |
| RSI | 75.44 | 13.45 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 832.25
**Exit:** 
**Exit Price:** 858.7
**Position Size:** 
**PnL:** 23.07
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 80.77 | 13.14 |
| ATR | 49.29 | 32.17 |
| Volume | 2808411.00 | 687001.00 |
| SMA (Short) | 669.68 | 877.25 |
| SMA (Long) | 650.37 | 879.47 |
| RSI | 76.62 | 29.46 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 922.25
**Exit:** 
**Exit Price:** 859.6
**Position Size:** 
**PnL:** -66.21
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-09-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 29.64 | 18.29 |
| ATR | 32.15 | 33.20 |
| Volume | 473284.00 | 453179.00 |
| SMA (Short) | 886.53 | 888.13 |
| SMA (Long) | 885.00 | 890.01 |
| RSI | 63.14 | 34.96 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 903.4
**Exit:** 
**Exit Price:** 1397.15
**Position Size:** 
**PnL:** 489.15
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-10-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.74 | 53.88 |
| ATR | 32.99 | 58.66 |
| Volume | 538729.00 | 2880187.00 |
| SMA (Short) | 890.88 | 1332.24 |
| SMA (Long) | 888.32 | 1335.03 |
| RSI | 60.46 | 51.37 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1424.6
**Exit:** 
**Exit Price:** 1317.75
**Position Size:** 
**PnL:** -112.33
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 64.41 | 63.42 |
| ATR | 58.64 | 60.19 |
| Volume | 1055930.00 | 1874370.00 |
| SMA (Short) | 1349.37 | 1426.19 |
| SMA (Long) | 1348.20 | 1434.31 |
| RSI | 51.84 | 6.77 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1361.1
**Exit:** 
**Exit Price:** 1473.7
**Position Size:** 
**PnL:** 106.93
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-06-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 40.12 | 40.07 |
| ATR | 52.97 | 46.18 |
| Volume | 475091.00 | 586448.00 |
| SMA (Short) | 1337.12 | 1492.25 |
| SMA (Long) | 1330.22 | 1500.38 |
| RSI | 73.49 | 22.49 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1577.3
**Exit:** 
**Exit Price:** 2095.75
**Position Size:** 
**PnL:** 511.1
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-09-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 61.87 | 81.41 |
| ATR | 47.63 | 122.70 |
| Volume | 456386.00 | 1163577.00 |
| SMA (Short) | 1528.17 | 2216.25 |
| SMA (Long) | 1522.62 | 2241.89 |
| RSI | 58.60 | 26.33 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1665.6
**Exit:** 
**Exit Price:** 1460.25
**Position Size:** 
**PnL:** -211.6
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 54.89 | 43.35 |
| ATR | 73.10 | 59.31 |
| Volume | 715374.00 | 1653579.00 |
| SMA (Short) | 1598.74 | 1561.77 |
| SMA (Long) | 1595.58 | 1568.65 |
| RSI | 79.11 | 34.15 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1343.55
**Exit:** 
**Exit Price:** 1282.2
**Position Size:** 
**PnL:** -66.6
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-09-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 39.27 | 62.35 |
| ATR | 51.32 | 45.31 |
| Volume | 399829.00 | 688949.00 |
| SMA (Short) | 1294.54 | 1377.05 |
| SMA (Long) | 1293.70 | 1387.88 |
| RSI | 79.12 | 25.97 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1289.7
**Exit:** 
**Exit Price:** 1233.05
**Position Size:** 
**PnL:** -61.7
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 41.57 | 51.06 |
| ATR | 41.92 | 35.89 |
| Volume | 318576.00 | 388379.00 |
| SMA (Short) | 1267.37 | 1262.08 |
| SMA (Long) | 1261.85 | 1266.78 |
| RSI | 57.39 | 38.73 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1279.3
**Exit:** 
**Exit Price:** 1547.5
**Position Size:** 
**PnL:** 262.55
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 112.26 | 55.92 |
| ATR | 34.20 | 44.14 |
| Volume | 855422.00 | 727732.00 |
| SMA (Short) | 1155.24 | 1556.33 |
| SMA (Long) | 1135.90 | 1570.58 |
| RSI | 78.28 | 34.51 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1645.8
**Exit:** 
**Exit Price:** 1572.1
**Position Size:** 
**PnL:** -80.14
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-09-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 44.95 | 48.98 |
| ATR | 42.22 | 42.96 |
| Volume | 593403.00 | 587832.00 |
| SMA (Short) | 1602.94 | 1607.15 |
| SMA (Long) | 1596.26 | 1615.97 |
| RSI | 74.10 | 39.03 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 1727.45
**Exit:** 
**Exit Price:** 2135.55
**Position Size:** 
**PnL:** 400.37
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-10-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 68.50 | 146.01 |
| ATR | 44.91 | 77.47 |
| Volume | 750008.00 | 758302.00 |
| SMA (Short) | 1614.82 | 2304.30 |
| SMA (Long) | 1608.53 | 2320.54 |
| RSI | 65.08 | 25.95 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 2500.35
**Exit:** 
**Exit Price:** 2925.7
**Position Size:** 
**PnL:** 414.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-04-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 115.58 | 122.31 |
| ATR | 79.72 | 127.26 |
| Volume | 1029534.00 | 773740.00 |
| SMA (Short) | 2351.88 | 3012.28 |
| SMA (Long) | 2334.24 | 3034.50 |
| RSI | 74.05 | 34.15 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 3161.17
**Exit:** 
**Exit Price:** 2875.7
**Position Size:** 
**PnL:** -297.55
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 133.44 | 83.90 |
| ATR | 95.53 | 101.81 |
| Volume | 1663667.00 | 406464.00 |
| SMA (Short) | 2979.28 | 2956.44 |
| SMA (Long) | 2976.26 | 2970.81 |
| RSI | 72.30 | 40.77 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 2972.85
**Exit:** 
**Exit Price:** 2734.1
**Position Size:** 
**PnL:** -250.16
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 39.26 | 65.73 |
| ATR | 107.52 | 94.47 |
| Volume | 1359384.00 | 529625.00 |
| SMA (Short) | 2889.93 | 2822.88 |
| SMA (Long) | 2882.11 | 2840.69 |
| RSI | 56.07 | 29.68 |

---

**Ticker:** GODREJPROP.NS  
**Entry:** 
**Entry Price:** 2146.8
**Exit:** 
**Exit Price:** 1974.55
**Position Size:** 
**PnL:** -180.49
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-04-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 58.26 | 81.42 |
| ATR | 91.82 | 92.47 |
| Volume | 1248005.00 | 1474704.00 |
| SMA (Short) | 2125.97 | 2083.42 |
| SMA (Long) | 2106.51 | 2089.19 |
| RSI | 59.04 | 50.07 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 623.95
**Exit:** 
**Exit Price:** 579.17
**Position Size:** 
**PnL:** -47.2
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-05-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.07 | 15.77 |
| ATR | 17.75 | 20.72 |
| Volume | 301291.00 | 918393.00 |
| SMA (Short) | 621.07 | 617.35 |
| SMA (Long) | 620.36 | 618.01 |
| RSI |  | 28.82 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 628.61
**Exit:** 
**Exit Price:** 571.4
**Position Size:** 
**PnL:** -59.61
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 21.23 | 14.77 |
| ATR | 14.28 | 12.85 |
| Volume | 95235.00 | 24998.00 |
| SMA (Short) | 602.98 | 589.49 |
| SMA (Long) | 598.35 | 590.15 |
| RSI | 79.88 | 42.33 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 602.53
**Exit:** 
**Exit Price:** 856.07
**Position Size:** 
**PnL:** 250.62
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.21 | 70.83 |
| ATR | 17.57 | 46.61 |
| Volume | 83021.00 | 435592.00 |
| SMA (Short) | 578.66 | 1006.32 |
| SMA (Long) | 575.93 | 1008.04 |
| RSI | 65.75 | 29.45 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 784.77
**Exit:** 
**Exit Price:** 810.34
**Position Size:** 
**PnL:** 22.39
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-08 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 62.71 | 31.63 |
| ATR | 37.22 | 27.30 |
| Volume | 850557.00 | 104828.00 |
| SMA (Short) | 700.76 | 837.95 |
| SMA (Long) | 689.18 | 838.13 |
| RSI | 83.14 | 45.09 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 916.86
**Exit:** 
**Exit Price:** 1784.39
**Position Size:** 
**PnL:** 862.13
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 61.62 | 56.43 |
| ATR | 27.25 | 48.84 |
| Volume | 281454.00 | 324668.00 |
| SMA (Short) | 840.76 | 1816.14 |
| SMA (Long) | 837.18 | 1828.53 |
| RSI | 80.87 | 39.82 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2032.63
**Exit:** 
**Exit Price:** 2292.97
**Position Size:** 
**PnL:** 251.68
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-08-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 75.79 | 70.66 |
| ATR | 56.81 | 100.03 |
| Volume | 1444108.00 | 348745.00 |
| SMA (Short) | 1876.12 | 2254.80 |
| SMA (Long) | 1870.98 | 2269.24 |
| RSI | 76.47 | 34.92 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2475.0
**Exit:** 
**Exit Price:** 2177.06
**Position Size:** 
**PnL:** -307.24
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 89.62 | 111.13 |
| ATR | 98.13 | 95.46 |
| Volume | 252131.00 | 496336.00 |
| SMA (Short) | 2358.02 | 2355.02 |
| SMA (Long) | 2350.52 | 2360.39 |
| RSI | 77.07 | 33.13 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2510.73
**Exit:** 
**Exit Price:** 2355.94
**Position Size:** 
**PnL:** -164.53
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-12-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 85.68 | 76.06 |
| ATR | 92.13 | 87.97 |
| Volume | 296437.00 | 202744.00 |
| SMA (Short) | 2364.34 | 2325.42 |
| SMA (Long) | 2356.87 | 2335.42 |
| RSI | 68.72 | 51.23 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2418.22
**Exit:** 
**Exit Price:** 2326.84
**Position Size:** 
**PnL:** -100.87
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 56.40 | 62.37 |
| ATR | 79.62 | 81.85 |
| Volume | 187072.00 | 243601.00 |
| SMA (Short) | 2349.30 | 2413.52 |
| SMA (Long) | 2342.59 | 2421.51 |
| RSI | 41.68 | 33.81 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2427.56
**Exit:** 
**Exit Price:** 2390.69
**Position Size:** 
**PnL:** -46.5
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 41.28 | 38.38 |
| ATR | 81.25 | 89.37 |
| Volume | 164413.00 | 377134.00 |
| SMA (Short) | 2362.17 | 2404.81 |
| SMA (Long) | 2358.89 | 2411.60 |
| RSI | 66.68 | 22.11 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2559.2
**Exit:** 
**Exit Price:** 2393.1
**Position Size:** 
**PnL:** -176.01
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-05-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 68.22 | 70.40 |
| ATR | 88.42 | 87.50 |
| Volume | 289065.00 | 317334.00 |
| SMA (Short) | 2428.62 | 2457.40 |
| SMA (Long) | 2424.74 | 2458.94 |
| RSI | 59.58 | 53.86 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2352.95
**Exit:** 
**Exit Price:** 2493.94
**Position Size:** 
**PnL:** 131.3
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-08-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 59.90 | 83.62 |
| ATR | 72.12 | 69.85 |
| Volume | 384807.00 | 210038.00 |
| SMA (Short) | 2237.09 | 2591.76 |
| SMA (Long) | 2233.71 | 2608.75 |
| RSI | 67.33 | 19.35 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2705.91
**Exit:** 
**Exit Price:** 2575.11
**Position Size:** 
**PnL:** -141.36
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 79.23 | 156.37 |
| ATR | 65.80 | 74.16 |
| Volume | 325548.00 | 181789.00 |
| SMA (Short) | 2620.54 | 2648.74 |
| SMA (Long) | 2618.35 | 2655.89 |
| RSI | 87.45 | 42.23 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 2689.63
**Exit:** 
**Exit Price:** 2849.13
**Position Size:** 
**PnL:** 148.43
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-01-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 37.65 | 82.71 |
| ATR | 66.60 | 73.18 |
| Volume | 163033.00 | 264831.00 |
| SMA (Short) | 2633.12 | 2880.91 |
| SMA (Long) | 2626.72 | 2890.75 |
| RSI | 70.38 | 22.36 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 3066.2
**Exit:** 
**Exit Price:** 4899.54
**Position Size:** 
**PnL:** 1817.42
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 96.71 | 213.04 |
| ATR | 72.51 | 134.14 |
| Volume | 383771.00 | 347116.00 |
| SMA (Short) | 2950.33 | 5098.16 |
| SMA (Long) | 2942.33 | 5137.43 |
| RSI | 71.94 | 36.09 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 5290.05
**Exit:** 
**Exit Price:** 4889.34
**Position Size:** 
**PnL:** -421.06
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-01-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 84.11 | 216.57 |
| ATR | 127.05 | 130.23 |
| Volume | 379315.00 | 2695792.00 |
| SMA (Short) | 5172.19 | 5283.55 |
| SMA (Long) | 5157.28 | 5285.64 |
| RSI | 87.56 | 27.43 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 4728.08
**Exit:** 
**Exit Price:** 6619.0
**Position Size:** 
**PnL:** 1868.22
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-02-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 65.46 | 154.94 |
| ATR | 180.99 | 218.15 |
| Volume | 629330.00 | 973579.00 |
| SMA (Short) | 4720.35 | 6587.50 |
| SMA (Long) | 4718.95 | 6593.61 |
| RSI | 79.10 | 34.98 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 6769.55
**Exit:** 
**Exit Price:** 6369.25
**Position Size:** 
**PnL:** -426.58
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 148.77 | 376.03 |
| ATR | 184.36 | 184.97 |
| Volume | 200927.00 | 318609.00 |
| SMA (Short) | 6681.43 | 6830.37 |
| SMA (Long) | 6679.32 | 6855.47 |
| RSI | 64.24 | 11.85 |

---

**Ticker:** POLYCAB.NS  
**Entry:** 
**Entry Price:** 7351.95
**Exit:** 
**Exit Price:** 6251.8
**Position Size:** 
**PnL:** -1127.36
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 371.54 | 366.10 |
| ATR | 210.64 | 189.81 |
| Volume | 229302.00 | 282470.00 |
| SMA (Short) | 6847.24 | 6976.82 |
| SMA (Long) | 6829.36 | 6989.70 |
| RSI | 68.51 | 27.38 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 112.01
**Exit:** 
**Exit Price:** 114.54
**Position Size:** 
**PnL:** 2.07
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-05-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.35 | 1.92 |
| ATR | 4.04 | 4.06 |
| Volume | 28215.00 | 109700.00 |
| SMA (Short) | 113.29 | 112.97 |
| SMA (Long) | 113.19 | 113.25 |
| RSI | 53.14 | 57.58 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 115.74
**Exit:** 
**Exit Price:** 125.71
**Position Size:** 
**PnL:** 9.49
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 1.68 | 3.37 |
| ATR | 4.09 | 5.15 |
| Volume | 60150.00 | 67240.00 |
| SMA (Short) | 113.54 | 126.00 |
| SMA (Long) | 113.31 | 126.30 |
| RSI | 47.09 | 39.27 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 123.48
**Exit:** 
**Exit Price:** 116.12
**Position Size:** 
**PnL:** -7.83
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-10-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.16 | 2.90 |
| ATR | 5.54 | 5.31 |
| Volume | 78500.00 | 4327785.00 |
| SMA (Short) | 122.73 | 120.33 |
| SMA (Long) | 122.22 | 120.45 |
| RSI | 64.15 | 35.67 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 123.76
**Exit:** 
**Exit Price:** 116.93
**Position Size:** 
**PnL:** -7.31
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 3.37 | 2.61 |
| ATR | 4.86 | 4.51 |
| Volume | 221950.00 | 47960.00 |
| SMA (Short) | 118.94 | 118.25 |
| SMA (Long) | 118.79 | 118.89 |
| RSI | 60.15 | 46.00 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 124.75
**Exit:** 
**Exit Price:** 115.34
**Position Size:** 
**PnL:** -9.89
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.47 | 3.10 |
| ATR | 4.32 | 3.74 |
| Volume | 46665.00 | 411395.00 |
| SMA (Short) | 120.22 | 121.82 |
| SMA (Long) | 119.73 | 121.86 |
| RSI | 52.08 | 24.70 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 132.68
**Exit:** 
**Exit Price:** 203.32
**Position Size:** 
**PnL:** 69.97
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-02-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 5.02 | 7.44 |
| ATR | 4.10 | 8.96 |
| Volume | 1054555.00 | 879605.00 |
| SMA (Short) | 123.26 | 219.48 |
| SMA (Long) | 122.49 | 221.61 |
| RSI | 73.85 | 25.12 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 182.0
**Exit:** 
**Exit Price:** 181.44
**Position Size:** 
**PnL:** -1.29
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-03-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 1.57 | 6.24 |
| ATR | 10.09 | 6.20 |
| Volume | 121170.00 | 1080995.00 |
| SMA (Short) | 183.69 | 189.96 |
| SMA (Long) | 183.24 | 191.54 |
| RSI | 52.41 | 26.66 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 207.78
**Exit:** 
**Exit Price:** 192.77
**Position Size:** 
**PnL:** -15.81
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-05-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.45 | 5.42 |
| ATR | 6.04 | 6.93 |
| Volume | 1141125.00 | 1321340.00 |
| SMA (Short) | 195.10 | 200.60 |
| SMA (Long) | 193.51 | 200.87 |
| RSI | 72.41 | 23.11 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 216.44
**Exit:** 
**Exit Price:** 209.13
**Position Size:** 
**PnL:** -8.16
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-09-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.74 | 6.97 |
| ATR | 6.86 | 6.24 |
| Volume | 1756425.00 | 1706645.00 |
| SMA (Short) | 205.43 | 223.73 |
| SMA (Long) | 204.80 | 225.34 |
| RSI | 72.56 | 24.74 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 238.36
**Exit:** 
**Exit Price:** 250.05
**Position Size:** 
**PnL:** 10.71
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-11-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.90 | 3.64 |
| ATR | 6.79 | 6.99 |
| Volume | 10591875.00 | 1138185.00 |
| SMA (Short) | 222.08 | 252.50 |
| SMA (Long) | 221.82 | 252.85 |
| RSI | 65.64 | 39.10 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 266.55
**Exit:** 
**Exit Price:** 291.75
**Position Size:** 
**PnL:** 24.08
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-02-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.72 | 7.34 |
| ATR | 7.43 | 10.23 |
| Volume | 2641315.00 | 787555.00 |
| SMA (Short) | 253.75 | 302.68 |
| SMA (Long) | 253.56 | 303.59 |
| RSI | 62.63 | 30.31 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 316.59
**Exit:** 
**Exit Price:** 286.69
**Position Size:** 
**PnL:** -31.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-06-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 5.27 | 8.74 |
| ATR | 10.43 | 10.81 |
| Volume | 1136100.00 | 3254765.00 |
| SMA (Short) | 311.33 | 311.45 |
| SMA (Long) | 310.98 | 311.49 |
| RSI | 65.77 | 33.47 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 256.13
**Exit:** 
**Exit Price:** 240.91
**Position Size:** 
**PnL:** -16.22
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-12-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.70 | 7.63 |
| ATR | 13.96 | 12.06 |
| Volume | 932105.00 | 1263340.00 |
| SMA (Short) | 251.41 | 241.60 |
| SMA (Long) | 248.50 | 241.71 |
| RSI | 73.41 | 35.26 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 234.53
**Exit:** 
**Exit Price:** 229.57
**Position Size:** 
**PnL:** -5.88
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-02-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.16 | 6.21 |
| ATR | 7.98 | 7.58 |
| Volume | 1772410.00 | 1557705.00 |
| SMA (Short) | 237.02 | 234.13 |
| SMA (Long) | 236.44 | 235.11 |
| RSI | 60.52 | 50.42 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 249.04
**Exit:** 
**Exit Price:** 251.58
**Position Size:** 
**PnL:** 1.54
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-03-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 6.54 | 11.50 |
| ATR | 7.42 | 8.18 |
| Volume | 2563530.00 | 853005.00 |
| SMA (Short) | 234.86 | 266.81 |
| SMA (Long) | 234.67 | 267.58 |
| RSI | 59.11 | 9.92 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 293.54
**Exit:** 
**Exit Price:** 280.26
**Position Size:** 
**PnL:** -14.43
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-06-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 16.58 | 5.62 |
| ATR | 9.66 | 10.31 |
| Volume | 1859275.00 | 765883.00 |
| SMA (Short) | 276.98 | 277.56 |
| SMA (Long) | 275.03 | 277.75 |
| RSI | 75.86 | 42.09 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 286.0
**Exit:** 
**Exit Price:** 271.82
**Position Size:** 
**PnL:** -15.29
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.83 | 5.68 |
| ATR | 10.49 | 10.17 |
| Volume | 476383.00 | 844086.00 |
| SMA (Short) | 277.22 | 277.32 |
| SMA (Long) | 277.16 | 278.10 |
| RSI | 46.70 | 44.26 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 268.05
**Exit:** 
**Exit Price:** 301.31
**Position Size:** 
**PnL:** 32.12
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-09 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.28 | 4.00 |
| ATR | 10.75 | 9.80 |
| Volume | 807999.00 | 1219062.00 |
| SMA (Short) | 264.66 | 300.87 |
| SMA (Long) | 263.48 | 301.07 |
| RSI | 57.62 | 50.52 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 326.95
**Exit:** 
**Exit Price:** 301.86
**Position Size:** 
**PnL:** -26.35
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 12.38 | 10.76 |
| ATR | 9.01 | 9.39 |
| Volume | 1587871.00 | 1957857.00 |
| SMA (Short) | 304.19 | 314.00 |
| SMA (Long) | 303.60 | 314.94 |
| RSI | 71.26 | 27.03 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 153.84
**Exit:** 
**Exit Price:** 539.13
**Position Size:** 
**PnL:** 383.9
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.90 | 18.57 |
| ATR | 15.25 | 24.45 |
| Volume | 16033901.00 | 3560232.00 |
| SMA (Short) | 146.57 | 545.91 |
| SMA (Long) | 145.45 | 546.54 |
| RSI | 63.23 | 45.97 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 532.89
**Exit:** 
**Exit Price:** 531.31
**Position Size:** 
**PnL:** -3.71
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-06-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.98 | 12.57 |
| ATR | 24.42 | 22.08 |
| Volume | 18314642.60 | 1729953.00 |
| SMA (Short) | 547.27 | 549.00 |
| SMA (Long) | 546.51 | 549.21 |
| RSI | 37.10 | 33.18 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 549.78
**Exit:** 
**Exit Price:** 546.26
**Position Size:** 
**PnL:** -5.71
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 22.51 | 37.47 |
| ATR | 16.32 | 25.77 |
| Volume | 5252586.00 | 3525992.00 |
| SMA (Short) | 512.44 | 585.60 |
| SMA (Long) | 509.21 | 590.31 |
| RSI | 64.99 | 26.30 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 596.07
**Exit:** 
**Exit Price:** 620.92
**Position Size:** 
**PnL:** 22.41
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-01-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 20.18 | 53.94 |
| ATR | 21.29 | 27.72 |
| Volume | 1705243.00 | 2465676.00 |
| SMA (Short) | 572.45 | 689.18 |
| SMA (Long) | 566.00 | 695.69 |
| RSI | 73.63 | 31.82 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 682.72
**Exit:** 
**Exit Price:** 724.17
**Position Size:** 
**PnL:** 38.64
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.76 | 31.19 |
| ATR | 24.32 | 21.33 |
| Volume | 1993115.00 | 1228777.00 |
| SMA (Short) | 644.21 | 748.22 |
| SMA (Long) | 641.93 | 755.81 |
| RSI | 63.55 | 30.95 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 732.28
**Exit:** 
**Exit Price:** 722.33
**Position Size:** 
**PnL:** -12.86
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-12-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.49 | 18.20 |
| ATR | 19.17 | 18.01 |
| Volume | 722408.00 | 1359579.00 |
| SMA (Short) | 722.68 | 721.72 |
| SMA (Long) | 722.30 | 724.17 |
| RSI | 79.64 | 43.45 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 771.29
**Exit:** 
**Exit Price:** 725.35
**Position Size:** 
**PnL:** -48.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-03-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 23.68 | 8.95 |
| ATR | 19.48 | 18.47 |
| Volume | 3157794.00 | 1218088.00 |
| SMA (Short) | 718.21 | 743.88 |
| SMA (Long) | 714.79 | 745.37 |
| RSI | 73.68 | 41.05 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 838.75
**Exit:** 
**Exit Price:** 1065.23
**Position Size:** 
**PnL:** 222.68
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 34.13 | 29.14 |
| ATR | 19.23 | 27.94 |
| Volume | 12172829.00 | 1332355.00 |
| SMA (Short) | 755.73 | 1109.98 |
| SMA (Long) | 755.30 | 1111.73 |
| RSI | 72.89 | 31.46 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 1172.96
**Exit:** 
**Exit Price:** 1146.08
**Position Size:** 
**PnL:** -31.52
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-11-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 25.46 | 35.06 |
| ATR | 30.04 | 33.32 |
| Volume | 4004318.00 | 1196729.00 |
| SMA (Short) | 1114.11 | 1163.20 |
| SMA (Long) | 1110.17 | 1167.71 |
| RSI | 82.16 | 25.68 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 1240.63
**Exit:** 
**Exit Price:** 1133.46
**Position Size:** 
**PnL:** -111.92
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-02-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 36.72 | 50.31 |
| ATR | 30.32 | 35.24 |
| Volume | 2123755.00 | 1564033.00 |
| SMA (Short) | 1172.23 | 1201.69 |
| SMA (Long) | 1166.11 | 1204.08 |
| RSI | 87.05 | 31.99 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 1194.65
**Exit:** 
**Exit Price:** 1347.38
**Position Size:** 
**PnL:** 147.65
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-04-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 59.97 | 34.01 |
| ATR | 37.47 | 45.81 |
| Volume | 1568022.00 | 656951.00 |
| SMA (Short) | 1136.79 | 1378.94 |
| SMA (Long) | 1123.89 | 1385.88 |
| RSI | 86.08 | 40.19 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 1454.23
**Exit:** 
**Exit Price:** 1405.38
**Position Size:** 
**PnL:** -54.57
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 42.48 | 43.55 |
| ATR | 43.50 | 49.48 |
| Volume | 1764924.00 | 1310995.00 |
| SMA (Short) | 1403.99 | 1467.89 |
| SMA (Long) | 1399.15 | 1476.73 |
| RSI | 66.88 | 28.44 |

---

**Ticker:** CHOLAFIN.NS  
**Entry:** 
**Entry Price:** 1253.87
**Exit:** 
**Exit Price:** 1221.9
**Position Size:** 
**PnL:** -36.92
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 48.04 | 17.86 |
| ATR | 38.49 | 39.11 |
| Volume | 2116766.00 | 1118698.00 |
| SMA (Short) | 1255.13 | 1248.84 |
| SMA (Long) | 1254.09 | 1249.79 |
| RSI | 60.40 | 37.43 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 161.56
**Exit:** 
**Exit Price:** 142.4
**Position Size:** 
**PnL:** -19.76
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 7.46 | 7.38 |
| ATR | 6.04 | 6.09 |
| Volume | 2651828.00 | 4733962.00 |
| SMA (Short) | 149.98 | 150.96 |
| SMA (Long) | 149.67 | 151.50 |
| RSI | 62.64 | 32.31 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 157.6
**Exit:** 
**Exit Price:** 156.48
**Position Size:** 
**PnL:** -1.74
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-31 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.89 | 9.11 |
| ATR | 5.75 | 7.14 |
| Volume | 2190201.00 | 2207090.00 |
| SMA (Short) | 150.06 | 161.00 |
| SMA (Long) | 149.29 | 162.05 |
| RSI | 64.48 | 47.68 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 165.65
**Exit:** 
**Exit Price:** 141.01
**Position Size:** 
**PnL:** -25.26
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-11-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 4.78 | 11.06 |
| ATR | 7.88 | 6.76 |
| Volume | 1575122.00 | 3101330.00 |
| SMA (Short) | 163.88 | 157.26 |
| SMA (Long) | 163.50 | 159.43 |
| RSI | 46.88 | 22.76 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 139.31
**Exit:** 
**Exit Price:** 142.96
**Position Size:** 
**PnL:** 3.09
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-02-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.78 | 3.12 |
| ATR | 5.32 | 5.18 |
| Volume | 5320936.00 | 1590539.00 |
| SMA (Short) | 129.07 | 144.46 |
| SMA (Long) | 128.78 | 144.47 |
| RSI | 61.47 | 48.53 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 133.7
**Exit:** 
**Exit Price:** 173.82
**Position Size:** 
**PnL:** 39.5
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-07-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.51 | 5.22 |
| ATR | 3.71 | 6.89 |
| Volume | 1490048.00 | 2484882.00 |
| SMA (Short) | 133.29 | 181.26 |
| SMA (Long) | 132.71 | 181.54 |
| RSI | 58.84 | 30.37 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 165.24
**Exit:** 
**Exit Price:** 162.86
**Position Size:** 
**PnL:** -3.03
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-01-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.77 | 4.03 |
| ATR | 5.72 | 4.90 |
| Volume | 5589804.00 | 2431531.00 |
| SMA (Short) | 166.81 | 165.67 |
| SMA (Long) | 166.67 | 165.76 |
| RSI | 53.13 | 49.65 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 175.01
**Exit:** 
**Exit Price:** 228.39
**Position Size:** 
**PnL:** 52.57
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-03-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.36 | 7.02 |
| ATR | 4.46 | 7.81 |
| Volume | 4872998.00 | 3278369.00 |
| SMA (Short) | 163.81 | 229.45 |
| SMA (Long) | 162.77 | 230.26 |
| RSI | 70.28 | 44.38 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 228.79
**Exit:** 
**Exit Price:** 222.29
**Position Size:** 
**PnL:** -7.41
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-02-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 9.23 | 4.49 |
| ATR | 6.25 | 7.25 |
| Volume | 1413873.00 | 5641354.00 |
| SMA (Short) | 218.41 | 231.67 |
| SMA (Long) | 216.87 | 232.38 |
| RSI | 85.66 | 29.45 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 243.0
**Exit:** 
**Exit Price:** 235.78
**Position Size:** 
**PnL:** -8.17
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-02-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 9.15 | 5.51 |
| ATR | 8.19 | 8.66 |
| Volume | 4238095.00 | 2640754.00 |
| SMA (Short) | 234.80 | 236.48 |
| SMA (Long) | 234.27 | 237.14 |
| RSI | 53.96 | 61.61 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 244.83
**Exit:** 
**Exit Price:** 242.87
**Position Size:** 
**PnL:** -2.94
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.29 | 6.29 |
| ATR | 8.56 | 7.57 |
| Volume | 3310412.00 | 2318445.00 |
| SMA (Short) | 235.68 | 251.29 |
| SMA (Long) | 235.23 | 251.59 |
| RSI | 71.69 | 38.09 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 252.46
**Exit:** 
**Exit Price:** 235.84
**Position Size:** 
**PnL:** -17.59
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-08-20 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 6.96 | 6.99 |
| ATR | 7.45 | 7.31 |
| Volume | 5049006.00 | 4447592.00 |
| SMA (Short) | 241.89 | 241.48 |
| SMA (Long) | 241.87 | 242.48 |
| RSI | 84.55 | 24.54 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 206.39
**Exit:** 
**Exit Price:** 201.21
**Position Size:** 
**PnL:** -5.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-01-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.13 | 3.79 |
| ATR | 9.17 | 6.50 |
| Volume | 2500442.00 | 1067341.00 |
| SMA (Short) | 199.52 | 205.85 |
| SMA (Long) | 198.85 | 205.99 |
| RSI | 63.84 | 43.41 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 196.03
**Exit:** 
**Exit Price:** 188.29
**Position Size:** 
**PnL:** -8.51
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-04-25 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.99 | 3.25 |
| ATR | 5.32 | 5.40 |
| Volume | 4214398.00 | 3218763.00 |
| SMA (Short) | 194.65 | 192.54 |
| SMA (Long) | 193.76 | 193.26 |
| RSI | 68.39 | 36.01 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 182.75
**Exit:** 
**Exit Price:** 166.58
**Position Size:** 
**PnL:** -16.87
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 5.37 | 6.01 |
| ATR | 5.84 | 5.69 |
| Volume | 2785295.00 | 1468874.00 |
| SMA (Short) | 176.90 | 172.64 |
| SMA (Long) | 176.74 | 172.97 |
| RSI | 60.00 | 19.53 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 164.01
**Exit:** 
**Exit Price:** 166.07
**Position Size:** 
**PnL:** 1.4
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-09-06 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 3.75 | 4.83 |
| ATR | 5.20 | 5.83 |
| Volume | 2010523.00 | 1914748.00 |
| SMA (Short) | 159.90 | 158.44 |
| SMA (Long) | 159.54 | 158.97 |
| RSI | 67.80 | 39.27 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 169.39
**Exit:** 
**Exit Price:** 153.11
**Position Size:** 
**PnL:** -16.93
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-11-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 4.70 | 10.37 |
| ATR | 5.78 | 5.74 |
| Volume | 1323156.00 | 1891558.00 |
| SMA (Short) | 159.56 | 165.01 |
| SMA (Long) | 159.41 | 165.62 |
| RSI | 45.43 | 25.52 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 164.71
**Exit:** 
**Exit Price:** 151.71
**Position Size:** 
**PnL:** -13.64
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-02-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.84 | 4.95 |
| ATR | 4.36 | 4.33 |
| Volume | 1980997.00 | 3784007.00 |
| SMA (Short) | 156.65 | 156.13 |
| SMA (Long) | 156.29 | 157.15 |
| RSI | 69.58 | 31.55 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 86.38
**Exit:** 
**Exit Price:** 209.44
**Position Size:** 
**PnL:** 122.46
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-05-22 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 1.24 | 7.24 |
| ATR | 6.42 | 11.76 |
| Volume | 6964251.00 | 7068613.00 |
| SMA (Short) | 87.84 | 216.78 |
| SMA (Long) | 87.51 | 217.00 |
| RSI | 53.42 | 25.00 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 213.79
**Exit:** 
**Exit Price:** 209.86
**Position Size:** 
**PnL:** -4.77
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-07-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 4.84 | 5.65 |
| ATR | 8.70 | 5.92 |
| Volume | 5526121.00 | 5460444.00 |
| SMA (Short) | 208.34 | 217.67 |
| SMA (Long) | 208.03 | 218.08 |
| RSI | 60.31 | 41.75 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 229.9
**Exit:** 
**Exit Price:** 214.08
**Position Size:** 
**PnL:** -16.7
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.94 | 8.39 |
| ATR | 6.03 | 7.04 |
| Volume | 8364323.00 | 5546106.00 |
| SMA (Short) | 215.97 | 214.17 |
| SMA (Long) | 214.54 | 215.96 |
| RSI | 67.39 | 27.02 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 225.58
**Exit:** 
**Exit Price:** 205.06
**Position Size:** 
**PnL:** -21.38
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 7.31 | 7.00 |
| ATR | 6.94 | 7.41 |
| Volume | 1696917.00 | 3342382.00 |
| SMA (Short) | 219.13 | 218.10 |
| SMA (Long) | 218.84 | 219.73 |
| RSI | 66.01 | 37.85 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 221.7
**Exit:** 
**Exit Price:** 217.43
**Position Size:** 
**PnL:** -5.15
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 7.16 | 5.23 |
| ATR | 5.97 | 6.63 |
| Volume | 1876933.00 | 5218368.00 |
| SMA (Short) | 212.19 | 212.20 |
| SMA (Long) | 211.50 | 212.32 |
| RSI | 66.56 | 28.94 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 218.25
**Exit:** 
**Exit Price:** 207.34
**Position Size:** 
**PnL:** -11.77
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-02-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 5.33 | 6.19 |
| ATR | 6.55 | 6.71 |
| Volume | 2405339.00 | 2396158.00 |
| SMA (Short) | 213.42 | 213.32 |
| SMA (Long) | 212.69 | 213.92 |
| RSI | 36.61 | 48.23 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 184.44
**Exit:** 
**Exit Price:** 173.99
**Position Size:** 
**PnL:** -11.16
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-06-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 3.80 | 14.44 |
| ATR | 7.01 | 7.03 |
| Volume | 2303227.00 | 3807016.00 |
| SMA (Short) | 191.43 | 194.84 |
| SMA (Long) | 191.21 | 198.03 |
| RSI | 53.44 | 17.33 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 204.06
**Exit:** 
**Exit Price:** 317.18
**Position Size:** 
**PnL:** 112.07
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-07-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 9.12 | 4.79 |
| ATR | 6.78 | 8.56 |
| Volume | 1200408.00 | 3528721.00 |
| SMA (Short) | 196.53 | 313.35 |
| SMA (Long) | 195.89 | 313.37 |
| RSI | 79.93 | 46.66 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 325.33
**Exit:** 
**Exit Price:** 327.3
**Position Size:** 
**PnL:** 0.67
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-02-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.00 | 7.15 |
| ATR | 8.73 | 8.85 |
| Volume | 8286501.00 | 3482811.00 |
| SMA (Short) | 314.36 | 315.16 |
| SMA (Long) | 314.26 | 315.20 |
| RSI | 57.13 | 60.08 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 326.07
**Exit:** 
**Exit Price:** 310.02
**Position Size:** 
**PnL:** -17.32
**Rationale:** Sell: short SMA crossed below long SMA at index 2023-03-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 7.77 | 7.96 |
| ATR | 9.20 | 8.76 |
| Volume | 8825502.00 | 857188.00 |
| SMA (Short) | 316.34 | 318.32 |
| SMA (Long) | 316.15 | 319.54 |
| RSI | 56.80 | 27.99 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 321.28
**Exit:** 
**Exit Price:** 394.27
**Position Size:** 
**PnL:** 71.56
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 6.13 | 21.08 |
| ATR | 7.90 | 10.29 |
| Volume | 1107718.00 | 1265957.00 |
| SMA (Short) | 317.94 | 407.02 |
| SMA (Long) | 316.72 | 410.26 |
| RSI | 60.87 | 30.70 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 379.74
**Exit:** 
**Exit Price:** 452.9
**Position Size:** 
**PnL:** 71.49
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-11-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 6.66 | 26.49 |
| ATR | 8.39 | 15.20 |
| Volume | 3175840.00 | 5046215.00 |
| SMA (Short) | 376.28 | 501.50 |
| SMA (Long) | 375.71 | 503.15 |
| RSI | 45.54 | 28.44 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 496.84
**Exit:** 
**Exit Price:** 468.72
**Position Size:** 
**PnL:** -30.06
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-05-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 13.48 | 14.49 |
| ATR | 14.47 | 15.12 |
| Volume | 2947783.00 | 11896368.00 |
| SMA (Short) | 488.27 | 478.66 |
| SMA (Long) | 487.64 | 480.52 |
| RSI | 57.77 | 42.76 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 476.18
**Exit:** 
**Exit Price:** 471.24
**Position Size:** 
**PnL:** -6.84
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-06-03 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 5.64 | 8.74 |
| ATR | 15.53 | 14.25 |
| Volume | 1703680.00 | 2122390.00 |
| SMA (Short) | 476.80 | 471.22 |
| SMA (Long) | 475.53 | 472.09 |
| RSI | 35.82 | 49.19 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 488.44
**Exit:** 
**Exit Price:** 486.4
**Position Size:** 
**PnL:** -3.99
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-08-14 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 7.12 | 21.11 |
| ATR | 14.74 | 15.33 |
| Volume | 4238014.00 | 1512958.00 |
| SMA (Short) | 476.44 | 510.43 |
| SMA (Long) | 475.58 | 510.86 |
| RSI | 63.48 | 14.38 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 518.25
**Exit:** 
**Exit Price:** 518.8
**Position Size:** 
**PnL:** -1.52
**Rationale:** Sell: short SMA crossed below long SMA at index 2024-10-16 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.87 | 11.32 |
| ATR | 13.52 | 12.32 |
| Volume | 1558438.00 | 1468467.00 |
| SMA (Short) | 517.25 | 510.44 |
| SMA (Long) | 516.29 | 511.10 |
| RSI | 65.34 | 33.86 |

---

**Ticker:** APOLLOTYRE.NS  
**Entry:** 
**Entry Price:** 521.45
**Exit:** 
**Exit Price:** 462.0
**Position Size:** 
**PnL:** -61.42
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-01-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 16.48 | 26.40 |
| ATR | 14.00 | 12.99 |
| Volume | 725837.00 | 3414061.00 |
| SMA (Short) | 505.47 | 505.15 |
| SMA (Long) | 503.94 | 510.82 |
| RSI | 64.86 | 9.09 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 154.65
**Exit:** 
**Exit Price:** 151.41
**Position Size:** 
**PnL:** -3.85
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-15 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.82 | 1.33 |
| ATR | 5.60 | 5.11 |
| Volume | 160351.00 | 28985.00 |
| SMA (Short) | 149.42 | 151.59 |
| SMA (Long) | 149.32 | 151.61 |
| RSI |  | 51.65 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 151.45
**Exit:** 
**Exit Price:** 150.44
**Position Size:** 
**PnL:** -1.62
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-06-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 1.18 | 1.19 |
| ATR | 5.07 | 5.12 |
| Volume | 31161.00 | 460714.00 |
| SMA (Short) | 151.68 | 151.50 |
| SMA (Long) | 151.60 | 151.57 |
| RSI | 48.24 | 47.06 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 163.64
**Exit:** 
**Exit Price:** 156.84
**Position Size:** 
**PnL:** -7.44
**Rationale:** Sell: short SMA crossed below long SMA at index 2015-08-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 4.10 | 2.82 |
| ATR | 5.21 | 6.63 |
| Volume | 398427.00 | 319769.00 |
| SMA (Short) | 152.25 | 157.81 |
| SMA (Long) | 151.75 | 158.05 |
| RSI | 68.94 | 31.00 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 148.21
**Exit:** 
**Exit Price:** 150.9
**Position Size:** 
**PnL:** 2.09
**Rationale:** Buy: short SMA crossed above long SMA at index 2015-10-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 8.46 | 1.37 |
| ATR | 6.52 | 4.89 |
| Volume | 272152.00 | 246208.00 |
| SMA (Short) | 140.88 | 151.83 |
| SMA (Long) | 139.38 | 152.01 |
| RSI | 74.82 | 13.11 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 153.37
**Exit:** 
**Exit Price:** 144.53
**Position Size:** 
**PnL:** -9.44
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-01-21 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 3.63 | 4.44 |
| ATR | 4.93 | 5.17 |
| Volume | 178390.00 | 63542.00 |
| SMA (Short) | 152.65 | 151.98 |
| SMA (Long) | 152.47 | 152.18 |
| RSI | 55.74 | 42.64 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 163.43
**Exit:** 
**Exit Price:** 146.62
**Position Size:** 
**PnL:** -17.43
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-03-01 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.40 | 4.44 |
| ATR | 5.45 | 5.77 |
| Volume | 47852.00 | 64364.00 |
| SMA (Short) | 154.23 | 152.19 |
| SMA (Long) | 153.09 | 152.80 |
| RSI | 54.31 | 32.81 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 157.99
**Exit:** 
**Exit Price:** 287.28
**Position Size:** 
**PnL:** 128.4
**Rationale:** Buy: short SMA crossed above long SMA at index 2016-04-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 2.59 | 11.32 |
| ATR | 4.51 | 15.75 |
| Volume | 509229.00 | 192175.00 |
| SMA (Short) | 152.34 | 298.68 |
| SMA (Long) | 151.76 | 300.76 |
| RSI | 63.73 | 45.21 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 302.42
**Exit:** 
**Exit Price:** 289.49
**Position Size:** 
**PnL:** -14.11
**Rationale:** Sell: short SMA crossed below long SMA at index 2016-11-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.76 | 5.69 |
| ATR | 11.52 | 13.44 |
| Volume | 210513.00 | 1636968.00 |
| SMA (Short) | 300.50 | 299.95 |
| SMA (Long) | 299.97 | 301.01 |
| RSI | 57.04 | 47.65 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 263.16
**Exit:** 
**Exit Price:** 390.9
**Position Size:** 
**PnL:** 126.43
**Rationale:** Buy: short SMA crossed above long SMA at index 2017-01-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 7.15 | 11.44 |
| ATR | 12.10 | 14.02 |
| Volume | 279067.00 | 400475.00 |
| SMA (Short) | 251.70 | 394.27 |
| SMA (Long) | 249.48 | 394.56 |
| RSI | 83.37 | 40.90 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 435.14
**Exit:** 
**Exit Price:** 402.36
**Position Size:** 
**PnL:** -34.45
**Rationale:** Sell: short SMA crossed below long SMA at index 2017-11-13 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.99 | 12.53 |
| ATR | 14.26 | 15.51 |
| Volume | 2614664.00 | 426861.00 |
| SMA (Short) | 400.06 | 420.84 |
| SMA (Long) | 396.37 | 422.56 |
| RSI | 70.95 | 38.88 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 405.16
**Exit:** 
**Exit Price:** 374.1
**Position Size:** 
**PnL:** -32.61
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-01-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 14.26 | 13.42 |
| ATR | 13.63 | 12.41 |
| Volume | 155817.00 | 390996.00 |
| SMA (Short) | 398.32 | 386.76 |
| SMA (Long) | 397.90 | 388.52 |
| RSI | 64.38 | 26.70 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 366.49
**Exit:** 
**Exit Price:** 352.46
**Position Size:** 
**PnL:** -15.47
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-05-23 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 11.60 | 13.63 |
| ATR | 14.15 | 12.53 |
| Volume | 593492.00 | 804520.00 |
| SMA (Short) | 352.58 | 367.88 |
| SMA (Long) | 351.65 | 371.08 |
| RSI | 63.28 | 9.81 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 346.81
**Exit:** 
**Exit Price:** 338.61
**Position Size:** 
**PnL:** -9.58
**Rationale:** Sell: short SMA crossed below long SMA at index 2018-10-05 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 10.48 | 21.01 |
| ATR | 11.05 | 16.75 |
| Volume | 191545.00 | 896852.00 |
| SMA (Short) | 354.55 | 369.04 |
| SMA (Long) | 352.58 | 369.85 |
| RSI | 55.49 | 29.35 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 394.82
**Exit:** 
**Exit Price:** 445.74
**Position Size:** 
**PnL:** 49.24
**Rationale:** Buy: short SMA crossed above long SMA at index 2018-11-07 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 19.77 | 8.68 |
| ATR | 18.63 | 17.42 |
| Volume | 73291.00 | 910606.00 |
| SMA (Short) | 370.04 | 442.42 |
| SMA (Long) | 368.47 | 442.59 |
| RSI | 67.60 | 35.98 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 452.58
**Exit:** 
**Exit Price:** 513.33
**Position Size:** 
**PnL:** 58.82
**Rationale:** Buy: short SMA crossed above long SMA at index 2019-02-12 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 8.98 | 15.90 |
| ATR | 17.34 | 15.53 |
| Volume | 647541.00 | 3557860.00 |
| SMA (Short) | 443.95 | 519.39 |
| SMA (Long) | 443.73 | 521.87 |
| RSI | 39.70 | 42.75 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 577.69
**Exit:** 
**Exit Price:** 570.26
**Position Size:** 
**PnL:** -9.72
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-07-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 26.99 | 10.14 |
| ATR | 15.75 | 16.83 |
| Volume | 1449066.00 | 1554712.00 |
| SMA (Short) | 536.89 | 556.87 |
| SMA (Long) | 532.39 | 557.65 |
| RSI | 64.63 | 47.28 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 571.66
**Exit:** 
**Exit Price:** 572.06
**Position Size:** 
**PnL:** -1.88
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-08-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.85 | 14.05 |
| ATR | 17.75 | 17.51 |
| Volume | 1166807.00 | 816840.00 |
| SMA (Short) | 560.68 | 556.32 |
| SMA (Long) | 559.60 | 557.48 |
| RSI | 62.10 | 55.90 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 560.77
**Exit:** 
**Exit Price:** 546.68
**Position Size:** 
**PnL:** -16.3
**Rationale:** Sell: short SMA crossed below long SMA at index 2019-08-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 11.48 | 10.61 |
| ATR | 17.49 | 17.59 |
| Volume | 643394.00 | 704359.00 |
| SMA (Short) | 558.40 | 556.06 |
| SMA (Long) | 557.52 | 557.37 |
| RSI | 49.51 | 42.96 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 621.08
**Exit:** 
**Exit Price:** 541.01
**Position Size:** 
**PnL:** -82.4
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-03-18 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 27.78 | 87.94 |
| ATR | 19.08 | 32.20 |
| Volume | 2401596.00 | 3319559.00 |
| SMA (Short) | 552.58 | 702.27 |
| SMA (Long) | 552.19 | 714.31 |
| RSI | 73.67 | 14.43 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 750.75
**Exit:** 
**Exit Price:** 1058.3
**Position Size:** 
**PnL:** 303.94
**Rationale:** Buy: short SMA crossed above long SMA at index 2020-04-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 41.87 | 29.46 |
| ATR | 50.49 | 48.93 |
| Volume | 3538348.00 | 1377334.00 |
| SMA (Short) | 684.37 | 1092.62 |
| SMA (Long) | 680.66 | 1097.83 |
| RSI | 77.73 | 45.05 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1066.28
**Exit:** 
**Exit Price:** 1044.1
**Position Size:** 
**PnL:** -26.4
**Rationale:** Sell: short SMA crossed below long SMA at index 2020-11-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.21 | 21.83 |
| ATR | 42.84 | 44.09 |
| Volume | 1301057.00 | 2860035.00 |
| SMA (Short) | 1065.15 | 1071.53 |
| SMA (Long) | 1060.47 | 1073.09 |
| RSI | 69.79 | 28.27 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1123.01
**Exit:** 
**Exit Price:** 1044.01
**Position Size:** 
**PnL:** -83.33
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-01-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 15.47 | 38.60 |
| ATR | 40.76 | 33.78 |
| Volume | 2674862.00 | 1457778.00 |
| SMA (Short) | 1095.89 | 1101.14 |
| SMA (Long) | 1092.22 | 1104.25 |
| RSI | 81.41 | 24.19 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1212.89
**Exit:** 
**Exit Price:** 1139.84
**Position Size:** 
**PnL:** -77.76
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-03-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 57.35 | 25.76 |
| ATR | 35.40 | 39.14 |
| Volume | 4290890.00 | 1195770.00 |
| SMA (Short) | 1112.63 | 1144.18 |
| SMA (Long) | 1111.53 | 1145.21 |
| RSI | 72.93 | 40.70 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1187.06
**Exit:** 
**Exit Price:** 1383.78
**Position Size:** 
**PnL:** 191.58
**Rationale:** Buy: short SMA crossed above long SMA at index 2021-05-19 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 39.64 | 58.43 |
| ATR | 36.14 | 38.08 |
| Volume | 624657.00 | 1364617.00 |
| SMA (Short) | 1130.76 | 1417.59 |
| SMA (Long) | 1125.69 | 1426.31 |
| RSI | 66.27 | 33.16 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1450.01
**Exit:** 
**Exit Price:** 1412.93
**Position Size:** 
**PnL:** -42.81
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-09-24 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 16.22 | 25.58 |
| ATR | 36.24 | 36.64 |
| Volume | 669489.00 | 346181.00 |
| SMA (Short) | 1432.50 | 1428.78 |
| SMA (Long) | 1432.05 | 1429.92 |
| RSI | 74.13 | 49.61 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1446.68
**Exit:** 
**Exit Price:** 1400.02
**Position Size:** 
**PnL:** -52.35
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-02 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 31.21 | 28.47 |
| ATR | 37.85 | 39.12 |
| Volume | 478933.00 | 632883.00 |
| SMA (Short) | 1420.90 | 1420.84 |
| SMA (Long) | 1418.35 | 1423.42 |
| RSI | 49.60 | 40.12 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1529.34
**Exit:** 
**Exit Price:** 1338.91
**Position Size:** 
**PnL:** -196.17
**Rationale:** Sell: short SMA crossed below long SMA at index 2021-11-30 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | trending |
| Volatility | 56.25 | 93.69 |
| ATR | 42.01 | 48.05 |
| Volume | 1287977.00 | 1529711.00 |
| SMA (Short) | 1438.34 | 1431.62 |
| SMA (Long) | 1431.12 | 1442.82 |
| RSI | 59.68 | 22.61 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1425.51
**Exit:** 
**Exit Price:** 1404.67
**Position Size:** 
**PnL:** -26.5
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-01-17 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 19.55 | 17.97 |
| ATR | 40.69 | 39.45 |
| Volume | 707506.00 | 242945.00 |
| SMA (Short) | 1429.27 | 1425.85 |
| SMA (Long) | 1427.60 | 1426.45 |
| RSI | 57.31 | 51.19 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1061.48
**Exit:** 
**Exit Price:** 989.36
**Position Size:** 
**PnL:** -76.22
**Rationale:** Sell: short SMA crossed below long SMA at index 2022-08-29 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 24.93 | 42.55 |
| ATR | 30.83 | 33.05 |
| Volume | 1900084.00 | 608206.00 |
| SMA (Short) | 999.90 | 995.84 |
| SMA (Long) | 999.54 | 997.96 |
| RSI | 67.42 | 34.47 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 998.7
**Exit:** 
**Exit Price:** 1027.82
**Position Size:** 
**PnL:** 25.07
**Rationale:** Buy: short SMA crossed above long SMA at index 2022-10-28 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 12.31 | 17.61 |
| ATR | 26.01 | 26.91 |
| Volume | 345063.00 | 707302.00 |
| SMA (Short) | 990.09 | 1028.56 |
| SMA (Long) | 988.43 | 1029.79 |
| RSI | 45.94 | 36.97 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 979.97
**Exit:** 
**Exit Price:** 1226.38
**Position Size:** 
**PnL:** 242.01
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-04-10 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 20.55 | 39.60 |
| ATR | 21.67 | 26.42 |
| Volume | 779901.00 | 861055.00 |
| SMA (Short) | 939.04 | 1235.86 |
| SMA (Long) | 936.63 | 1245.05 |
| RSI | 84.86 | 25.89 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1256.77
**Exit:** 
**Exit Price:** 1351.71
**Position Size:** 
**PnL:** 89.72
**Rationale:** Buy: short SMA crossed above long SMA at index 2023-10-27 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | ranging |
| Volatility | 18.53 | 40.76 |
| ATR | 27.05 | 36.38 |
| Volume | 303443.00 | 151135.00 |
| SMA (Short) | 1228.74 | 1386.38 |
| SMA (Long) | 1228.42 | 1392.20 |
| RSI | 77.94 | 30.87 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1444.21
**Exit:** 
**Exit Price:** 1926.37
**Position Size:** 
**PnL:** 475.42
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-03-26 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 48.97 | 52.42 |
| ATR | 43.11 | 52.72 |
| Volume | 1560486.00 | 172629.00 |
| SMA (Short) | 1344.16 | 1918.59 |
| SMA (Long) | 1338.34 | 1920.01 |
| RSI | 68.99 | 39.61 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 1924.25
**Exit:** 
**Exit Price:** 2150.53
**Position Size:** 
**PnL:** 218.13
**Rationale:** Buy: short SMA crossed above long SMA at index 2024-12-04 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | ranging | ranging |
| Volatility | 18.14 | 41.03 |
| ATR | 49.88 | 65.52 |
| Volume | 349574.00 | 810783.00 |
| SMA (Short) | 1906.33 | 2150.75 |
| SMA (Long) | 1903.60 | 2159.06 |
| RSI | 77.20 | 36.96 |

---

**Ticker:** MUTHOOTFIN.NS  
**Entry:** 
**Entry Price:** 2217.38
**Exit:** 
**Exit Price:** 1992.61
**Position Size:** 
**PnL:** -233.19
**Rationale:** Sell: short SMA crossed below long SMA at index 2025-04-11 00:00:00+05:30

| Field | Entry Value | Exit Value |
|-------|-------------|------------|
| Regime | trending | trending |
| Volatility | 38.24 | 71.70 |
| ATR | 63.79 | 73.95 |
| Volume | 1242059.00 | 3912506.00 |
| SMA (Short) | 2172.44 | 2184.57 |
| SMA (Long) | 2164.76 | 2184.66 |
| RSI | 60.56 | 0.00 |

---

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

Unknown: 100%


| Start Date | End Date | Regime | Days |
|---|---|---|---|
| 2015-05-06 00:00:00+05:30 | 2015-07-20 00:00:00+05:30 | ranging | 53 |
| 2015-07-20 00:00:00+05:30 | 2015-07-28 00:00:00+05:30 | trending | 6 |
| 2015-07-28 00:00:00+05:30 | 2015-09-14 00:00:00+05:30 | ranging | 34 |
| 2015-09-14 00:00:00+05:30 | 2015-09-30 00:00:00+05:30 | trending | 10 |
| 2015-09-30 00:00:00+05:30 | 2016-11-30 00:00:00+05:30 | ranging | 284 |
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
| 2023-06-08 00:00:00+05:30 | 2023-10-16 00:00:00+05:30 | ranging | 88 |
| 2023-10-16 00:00:00+05:30 | 2023-11-02 00:00:00+05:30 | trending | 12 |
| 2023-11-02 00:00:00+05:30 | 2023-12-27 00:00:00+05:30 | ranging | 36 |
| 2023-12-27 00:00:00+05:30 | 2024-03-13 00:00:00+05:30 | trending | 52 |
| 2024-03-13 00:00:00+05:30 | 2024-10-31 00:00:00+05:30 | ranging | 156 |
| 2024-10-31 00:00:00+05:30 | 2024-12-03 00:00:00+05:30 | trending | 21 |
| 2024-12-03 00:00:00+05:30 | 2025-04-29 00:00:00+05:30 | ranging | 100 |
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

No rationale provided.


## Parameter Sensitivity Analysis

The plot below compares equity curves for different parameter values, illustrating the impact of parameter changes on strategy performance.

![Parameter Sensitivity](plots/parameter_sensitivity.png)

## Trade Statistics Breakdown

| Metric | Value |
|---|---|
| Average Win | 153.79 |
| Average Loss | -65.55 |
| Largest Win | 1868.22 |
| Largest Loss | -1127.36 |
| Profit Factor | 1.57 |
| Expectancy | 22.33 |

### Regime Breakdown

| Regime | Trades | Win Rate | Avg Win | Avg Loss | Largest Win | Largest Loss | Profit Factor | Expectancy | Mean PnL |
|---|---|---|---|---|---|---|---|---|---|
| None | 644 | 0.40 | 153.79 | -65.55 | 1868.22 | -1127.36 | 1.57 | 22.33 | 22.33 |