"""
Module for backtesting trading strategies.

This module provides functionality for:
1. Generating trading signals based on strategies
2. Running backtests over specified periods
3. Generating performance reports
"""

import logging
import pandas as pd
import numpy as np
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def add_sma_crossover_signals(df, fast_window=50, slow_window=200):
    """
    Add SMA crossover buy/sell signals to the dataframe.

    Args:
        df (pd.DataFrame): DataFrame containing price data and SMA columns
        fast_window (int): Fast SMA window size
        slow_window (int): Slow SMA window size

    Returns:
        pd.DataFrame: DataFrame with added signal columns
    """
    if (
        f"sma_{fast_window}" not in df.columns
        or f"sma_{slow_window}" not in df.columns
    ):
        logger.error(
            f"Missing required SMA columns: sma_{fast_window} or sma_{slow_window}"
        )
        return df

    logger.info(
        f"Generating SMA crossover signals (fast={fast_window}, slow={slow_window})"
    )

    # Get SMA columns
    sma_fast = df[f"sma_{fast_window}"]
    sma_slow = df[f"sma_{slow_window}"]

    # Calculate crossover conditions
    df["fast_gt_slow"] = sma_fast > sma_slow

    # Generate buy signals (fast crosses above slow)
    df["buy_signal"] = (sma_fast > sma_slow) & (
        sma_fast.shift(1) <= sma_slow.shift(1)
    )

    # Generate sell signals (fast crosses below slow)
    df["sell_signal"] = (sma_fast < sma_slow) & (
        sma_fast.shift(1) >= sma_slow.shift(1)
    )

    # Count the number of signals
    buy_count = df["buy_signal"].sum()
    sell_count = df["sell_signal"].sum()
    logger.info(
        f"Generated {buy_count} buy signals and {sell_count} sell signals"
    )

    return df


def run_backtest(df, initial_capital=100000.0):
    """
    Run a backtest simulation using the provided signals.

    Args:
        df (pd.DataFrame): DataFrame with OHLCV data and buy/sell signals
        initial_capital (float): Initial capital for the backtest

    Returns:
        dict: Dictionary containing backtest results and metrics
    """
    if "buy_signal" not in df.columns or "sell_signal" not in df.columns:
        logger.error("Missing required signal columns")
        return None

    logger.info(
        f"Running backtest with initial capital: ${initial_capital:,.2f}"
    )

    # Initialize portfolio state
    cash = initial_capital
    position = 0
    portfolio_values = []
    trades = []

    # Get the initial close price for Buy & Hold calculation
    initial_price = df["Close"].iloc[0]

    # Iterate through each day
    for index, row in df.iterrows():
        close_price = row["Close"]

        # Check for buy signal
        if row["buy_signal"] and position == 0 and cash > 0:
            # Calculate shares to buy (use all available cash)
            shares_to_buy = cash / close_price
            position += shares_to_buy
            cash = 0

            # Record the trade
            trades.append(
                {
                    "date": index,
                    "type": "buy",
                    "price": close_price,
                    "shares": shares_to_buy,
                    "value": shares_to_buy * close_price,
                }
            )
            logger.debug(
                f"BUY: {index}, {shares_to_buy:.2f} shares at ${close_price:.2f}"
            )

        # Check for sell signal
        elif row["sell_signal"] and position > 0:
            # Calculate cash received
            cash_received = position * close_price
            cash += cash_received

            # Record the trade
            trades.append(
                {
                    "date": index,
                    "type": "sell",
                    "price": close_price,
                    "shares": position,
                    "value": position * close_price,
                }
            )
            logger.debug(
                f"SELL: {index}, {position:.2f} shares at ${close_price:.2f}"
            )

            # Reset position
            position = 0

        # Calculate portfolio value for this day
        portfolio_value = cash + (position * close_price)
        portfolio_values.append(portfolio_value)

    # Calculate final portfolio value
    final_price = df["Close"].iloc[-1]
    final_value = cash + (position * final_price)

    # Calculate Buy & Hold final value
    buy_hold_shares = initial_capital / initial_price
    buy_hold_final_value = buy_hold_shares * final_price

    # Calculate max drawdown
    portfolio_series = pd.Series(portfolio_values, index=df.index)
    portfolio_max = portfolio_series.cummax()
    drawdown = ((portfolio_series - portfolio_max) / portfolio_max) * 100
    max_drawdown = drawdown.min()

    # Calculate performance metrics
    total_return_pct = ((final_value / initial_capital) - 1) * 100
    buy_hold_return_pct = ((buy_hold_final_value / initial_capital) - 1) * 100
    num_trades = len(trades)

    # Calculate win rate if there are sell trades
    sell_trades = [t for t in trades if t["type"] == "sell"]
    buy_trades = [t for t in trades if t["type"] == "buy"]

    if sell_trades:
        # Simple win rate: count sells where price > preceding buy price
        # This requires matching each sell with its preceding buy
        win_count = 0
        for i, trade in enumerate(sell_trades):
            # Find the most recent buy before this sell
            if i < len(buy_trades):  # Simple matching for baseline
                buy_price = buy_trades[i]["price"]
                sell_price = trade["price"]
                if sell_price > buy_price:
                    win_count += 1
        win_rate = (win_count / len(sell_trades)) * 100 if sell_trades else 0
    else:
        win_rate = 0

    # Return results
    results = {
        "initial_capital": initial_capital,
        "final_value": final_value,
        "total_return_pct": total_return_pct,
        "buy_hold_return_pct": buy_hold_return_pct,
        "num_trades": num_trades,
        "win_rate": win_rate,
        "max_drawdown": max_drawdown,
        "start_date": df.index[0],
        "end_date": df.index[-1],
        "trades": trades,
        "portfolio_values": portfolio_values,
    }

    logger.info(
        f"Backtest completed. Final value: ${final_value:,.2f}, Return: {total_return_pct:.2f}%"
    )

    return results


def generate_backtest_report(results, period_name):
    """
    Generate a human-readable report from backtest results.

    Args:
        results (dict): Backtest results from run_backtest
        period_name (str): Name of the period (e.g., 'In-Sample', 'Out-of-Sample')
    """
    if not results:
        logger.error(f"No results to generate report for {period_name}")
        return

    print(f"\n{'=' * 50}")
    print(f"--- {period_name} Backtest Report ---")
    print(f"{'=' * 50}")
    print(
        f"Period: {results['start_date'].date()} to {results['end_date'].date()}"
    )
    print(f"Initial Capital: ${results['initial_capital']:,.2f}")
    print(f"Final Portfolio Value: ${results['final_value']:,.2f}")
    print(f"Total Return: {results['total_return_pct']:.2f}%")
    print(f"Buy & Hold Return: {results['buy_hold_return_pct']:.2f}%")
    print(f"Number of Trades: {results['num_trades']}")
    print(f"Win Rate: {results['win_rate']:.2f}%")
    print(f"Max Drawdown: {results['max_drawdown']:.2f}%")
    print(f"{'=' * 50}")
