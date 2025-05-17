# Backtester Documentation

This file provides specific documentation for the `backtester.py` module, which implements a backtesting framework for trading strategies.

## Overview

The `backtester.py` module provides functionality for:

1. Generating trading signals based on strategies
2. Running backtests over specified periods with realistic conditions:
   - Transaction costs (fixed + percentage)
   - Slippage modeling
   - Position sizing
3. Generating performance reports and visualizations

## Key Components

### `Strategy` Abstract Base Class

The `Strategy` class serves as the base class for all trading strategies and defines the interface for signal generation.

### `SMACrossoverStrategy` Class

Implementation of the Simple Moving Average (SMA) crossover strategy which generates buy signals when a fast SMA crosses above a slow SMA and sells when it crosses below.

### `run_backtest` Function

Executes a backtest simulation with the following features:
- Initial capital allocation
- Fixed and percentage-based commissions
- Slippage modeling
- Position sizing
- FIFO position tracking
- Buy & Hold comparison
- Portfolio value tracking
- Trade metrics (win/loss, P&L)

### `generate_backtest_report` Function

Produces a formatted report of backtest results with performance metrics.

## Buy & Hold Benchmark Calculation

The Buy & Hold benchmark is calculated with the following realistic assumptions:

1. **Initial Buy Transaction:**
   - Apply slippage to the initial price (buy at a slightly higher price)
   - Calculate shares bought accounting for both fixed and percentage commissions using the formula:
     `shares = (initial_capital - fixed_commission) / (buy_price * (1 + percentage_commission))`
   - This ensures proper calculation of the maximum affordable shares given the capital constraints and all costs

2. **Final Sell Transaction:**
   - Apply slippage to the final price (sell at a slightly lower price)
   - Calculate gross proceeds from selling all shares
   - Deduct fixed commission + percentage commission from the proceeds
   - Final value is the net proceeds after all costs

This approach ensures a fair comparison between the strategy and the Buy & Hold benchmark by applying the same transaction costs to both.

## Usage Notes

- The proper handling of commissions and slippage is critical for accurate backtest results
- Slippage is applied directly to the execution prices (higher for buys, lower for sells)
- Commission calculation accounts for both fixed and percentage components
- Position sizing respects the cash availability constraint and considers transaction costs
- The FIFO position tracking logic is used for calculating trade returns and win rate

## Implementation Details

In the implementation, slippage is handled by adjusting transaction prices directly:
- Buy transactions use a price of `close_price * (1 + slippage_pct)`
- Sell transactions use a price of `close_price * (1 - slippage_pct)`

Commission is calculated from this adjusted price using both fixed and percentage components.

The backtester then calculates the maximum number of shares that can be purchased given:
1. The available cash (including position sizing)
2. The fixed commission component
3. The percentage commission component

A key formula used is:
`shares = (cash_to_invest - commission_fixed) / (actual_buy_price * (1 + commission_pct))`
