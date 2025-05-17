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
import os
import json
from datetime import datetime
from abc import ABC, abstractmethod
from collections import deque
import streamlit as st


# Setup enhanced logging
def setup_logging(log_level=logging.INFO):
    """
    Configure logging with a more detailed format and multiple handlers.

    Args:
        log_level: The logging level to use (default: INFO)

    Returns:
        logging.Logger: Configured logger
    """
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Create logger
    logger = logging.getLogger("backtester")
    logger.setLevel(log_level)
    logger.propagate = False  # Prevent double logging

    # Clear any existing handlers
    if logger.handlers:
        logger.handlers.clear()

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create file handler for general logs
    log_file = os.path.join(
        "logs", f'backtester_{datetime.now().strftime("%Y%m%d")}.log'
    )
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # Create file handler specifically for errors
    error_log_file = os.path.join(
        "logs", f'backtester_errors_{datetime.now().strftime("%Y%m%d")}.log'
    )
    error_file_handler = logging.FileHandler(error_log_file)
    error_file_handler.setLevel(logging.ERROR)

    # Create formatters
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    error_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
    )

    # Add formatters to handlers
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)
    error_file_handler.setFormatter(error_formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_file_handler)

    return logger


# Initialize logger
logger = setup_logging()


class Strategy(ABC):
    """Base class for all trading strategies."""

    def __init__(self, name="BaseStrategy"):
        """Initialize strategy with a name."""
        self.name = name

    @abstractmethod
    def required_features(self):
        """
        Return a list of features required by this strategy.

        This method must be implemented by all strategy subclasses to declare
        what features they need to operate properly.

        Returns:
            list: List of column names that must be present in the dataframe
        """
        pass

    def validate_features(self, df):
        """
        Validate that the DataFrame contains all required features.

        Args:
            df (pd.DataFrame): DataFrame to validate

        Returns:
            bool: True if all required features are present, False otherwise

        Raises:
            ValueError: If required features are missing
        """
        required = self.required_features()
        missing = [col for col in required if col not in df.columns]
        if missing:
            raise ValueError(
                f"Missing required features for {self.name} strategy: {missing}"
            )
        return True

    @abstractmethod
    def generate_signals(self, df):
        """
        Generate buy/sell signals for the given DataFrame.

        This method must be implemented by all strategy subclasses.
        It should add at least 'buy_signal' and 'sell_signal' columns to the DataFrame.

        Args:
            df (pd.DataFrame): DataFrame with price data and indicators

        Returns:
            pd.DataFrame: DataFrame with added signal columns
        """
        pass

    def __str__(self):
        """Return string representation of the strategy."""
        return f"{self.name} Strategy"


class SMACrossoverStrategy(Strategy):
    """Strategy based on SMA crossovers."""

    def __init__(self, fast_window=50, slow_window=200):
        """
        Initialize SMA crossover strategy with window parameters.

        Args:
            fast_window (int): Fast SMA window size
            slow_window (int): Slow SMA window size

        Raises:
            ValueError: If parameters are invalid
        """
        super().__init__(name=f"SMA Crossover ({fast_window}/{slow_window})")

        # Validate parameters to ensure logical constraints are met
        if (
            not isinstance(fast_window, int)
            or not isinstance(slow_window, int)
            or fast_window <= 0
            or slow_window <= 0
        ):
            raise ValueError("SMA windows must be positive integers.")
        if fast_window >= slow_window:
            raise ValueError(
                f"Fast SMA window ({fast_window}) must be less than slow SMA window ({slow_window})."
            )

        self.fast_window = fast_window
        self.slow_window = slow_window

    def required_features(self):
        """
        Return features required by the SMA Crossover strategy.

        Returns:
            list: List of required column names
        """
        return [f"sma_{self.fast_window}", f"sma_{self.slow_window}"]

    def generate_signals(self, df):
        """
        Generate SMA crossover buy/sell signals for the given DataFrame.

        Args:
            df (pd.DataFrame): DataFrame with price data and SMA columns

        Returns:
            pd.DataFrame: DataFrame with added signal columns
        """
        # Validate required features are present
        try:
            self.validate_features(df)
        except ValueError as e:
            logger.error(str(e))
            return df

        logger.info(
            f"Generating SMA crossover signals (fast={self.fast_window}, slow={self.slow_window})"
        )

        # Get SMA columns
        sma_fast = df[f"sma_{self.fast_window}"]
        sma_slow = df[f"sma_{self.slow_window}"]

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


class RSIStrategy(Strategy):
    """Strategy based on RSI overbought/oversold conditions."""

    def __init__(
        self, rsi_window=14, oversold_threshold=30, overbought_threshold=70
    ):
        """
        Initialize RSI strategy with parameters.

        Args:
            rsi_window (int): RSI window size
            oversold_threshold (int): RSI level below which we consider the market oversold (buy signal)
            overbought_threshold (int): RSI level above which we consider the market overbought (sell signal)

        Raises:
            ValueError: If parameters are invalid
        """
        super().__init__(
            name=f"RSI ({rsi_window}, {oversold_threshold}/{overbought_threshold})"
        )

        # Validate parameters to ensure logical constraints are met
        if not isinstance(rsi_window, int) or rsi_window <= 0:
            raise ValueError("RSI window must be a positive integer.")
        if not (
            0 <= oversold_threshold <= 100 and 0 <= overbought_threshold <= 100
        ):
            raise ValueError("RSI thresholds must be between 0 and 100.")
        if oversold_threshold >= overbought_threshold:
            raise ValueError(
                f"RSI oversold threshold ({oversold_threshold}) must be less than overbought threshold ({overbought_threshold})."
            )

        self.rsi_window = rsi_window
        self.oversold_threshold = oversold_threshold
        self.overbought_threshold = overbought_threshold

    def required_features(self):
        """
        Return features required by the RSI strategy.

        Returns:
            list: List of required column names
        """
        return [f"rsi_{self.rsi_window}"]

    def generate_signals(self, df):
        """
        Generate RSI-based buy/sell signals for the given DataFrame.

        Args:
            df (pd.DataFrame): DataFrame with price data and RSI column

        Returns:
            pd.DataFrame: DataFrame with added signal columns
        """
        # Validate required features are present
        try:
            self.validate_features(df)
        except ValueError as e:
            logger.error(str(e))
            return df

        logger.info(
            f"Generating RSI signals (period={self.rsi_window}, "
            f"oversold={self.oversold_threshold}, overbought={self.overbought_threshold})"
        )

        # Get RSI column
        rsi = df[f"rsi_{self.rsi_window}"]

        # Generate buy signals (RSI crosses above oversold threshold)
        df["buy_signal"] = (rsi > self.oversold_threshold) & (
            rsi.shift(1) <= self.oversold_threshold
        )

        # Generate sell signals (RSI crosses below overbought threshold)
        df["sell_signal"] = (rsi < self.overbought_threshold) & (
            rsi.shift(1) >= self.overbought_threshold
        )

        # Count the number of signals
        buy_count = df["buy_signal"].sum()
        sell_count = df["sell_signal"].sum()
        logger.info(
            f"Generated {buy_count} buy signals and {sell_count} sell signals"
        )

        return df


# Keep the original function for backward compatibility
def add_sma_crossover_signals(df, fast_window=50, slow_window=200):
    """
    Add SMA crossover buy/sell signals to the dataframe.

    This function is kept for backward compatibility.
    New code should use the SMACrossoverStrategy class instead.

    Args:
        df (pd.DataFrame): DataFrame containing price data and SMA columns
        fast_window (int): Fast SMA window size
        slow_window (int): Slow SMA window size

    Returns:
        pd.DataFrame: DataFrame with added signal columns
    """
    logger.warning(
        "add_sma_crossover_signals is deprecated. Use SMACrossoverStrategy class instead."
    )

    strategy = SMACrossoverStrategy(
        fast_window=fast_window, slow_window=slow_window
    )
    return strategy.generate_signals(df)


@st.cache_data
def run_backtest(
    df,
    initial_capital=100000.0,
    commission_fixed=20.0,
    commission_pct=0.0003,
    slippage_pct=0.001,
    position_size_pct=0.25,
):
    """
    Run a backtest simulation using the provided signals.

    Args:
        df (pd.DataFrame): DataFrame with OHLCV data and buy/sell signals
        initial_capital (float): Initial capital for the backtest
        commission_fixed (float): Fixed commission per trade (e.g., 20 rupees)
        commission_pct (float): Percentage commission per trade (e.g., 0.03% = 0.0003)
        slippage_pct (float): Slippage as percentage of price (e.g., 0.1% = 0.001)
        position_size_pct (float): Percentage of available capital to use per trade (0-1)

    Returns:
        dict: Dictionary containing backtest results and metrics
    """
    # Validate input DataFrame
    required_columns = ["Close", "buy_signal", "sell_signal"]
    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]
    if missing_columns:
        logger.error(
            f"Missing required columns in input DataFrame: {missing_columns}"
        )
        return None

    # Check for NaN values in critical columns
    if df[required_columns].isna().any().any():
        logger.error(
            "Input DataFrame contains NaN values in critical columns. Please handle NaN values before backtesting."
        )
        return None

    # Validate input parameters
    if initial_capital < 0:
        raise ValueError("initial_capital cannot be negative")
    if commission_fixed < 0:
        raise ValueError("commission_fixed cannot be negative")
    if commission_pct < 0:
        raise ValueError("commission_pct cannot be negative")
    if slippage_pct < 0:
        raise ValueError("slippage_pct cannot be negative")
    if position_size_pct < 0 or position_size_pct > 1:
        raise ValueError("position_size_pct must be between 0 and 1")

    logger.info(
        f"Running backtest with initial capital: ${initial_capital:,.2f}, "
        f"Commission: ${commission_fixed} + {commission_pct*100}%, "
        f"Slippage: {slippage_pct*100}%, "
        f"Position Size: {position_size_pct*100}%"
    )

    # Initialize portfolio state with simplified position tracking
    cash = initial_capital
    position = 0  # Current number of shares held
    open_positions = (
        []
    )  # List of dictionaries: [{'date': buy_date, 'actual_price': buy_price, 'shares': shares, 'commission': commission}]
    portfolio_values = []
    completed_trades = []
    total_commission = 0
    total_slippage_cost = 0
    gross_profit = 0  # Track total profit from winning trades
    gross_loss = 0  # Track total loss from losing trades
    win_count = 0  # Track number of winning trades
    loss_count = 0  # Track number of losing trades

    # Pre-calculate prices adjusted for slippage
    actual_buy_prices = df["Close"] * (1 + slippage_pct)
    actual_sell_prices = df["Close"] * (1 - slippage_pct)

    # Get the initial close price for Buy & Hold calculation
    initial_price = df["Close"].iloc[0]

    # Iterate through each day
    for index, row in df.iterrows():
        close_price = row["Close"]

        # Check for buy signal when we have cash
        if row["buy_signal"] and cash > 0:
            # Calculate the amount to invest based on position sizing
            cash_to_invest = min(cash, initial_capital * position_size_pct)

            # Apply slippage to buy price
            actual_buy_price = actual_buy_prices.loc[
                index
            ]  # Use pre-calculated price

            # Calculate commission and shares to buy
            shares_to_buy = max(
                0,
                (cash_to_invest - commission_fixed)
                / (actual_buy_price * (1 + commission_pct)),
            )

            # Ensure shares_to_buy is an integer if trading whole shares, or handle fractional shares
            # For simplicity, let's assume fractional shares are allowed for now.

            # Ensure we have enough for at least one share
            if shares_to_buy <= 0:
                logger.warning(
                    f"Not enough cash to invest after commission at {index}. Skipping trade."
                )
            else:
                # Calculate the actual commission
                commission = commission_fixed + (
                    shares_to_buy * actual_buy_price * commission_pct
                )

                # Calculate total cost (price + commission)
                total_cost = shares_to_buy * actual_buy_price + commission

                # Calculate slippage cost for reporting (difference between actual price and close price)
                slippage_cost = shares_to_buy * close_price * slippage_pct

                # Ensure the total cost doesn't exceed available cash
                if total_cost > cash:
                    # This case should ideally be handled by the shares_to_buy calculation above,
                    # but as a safeguard, log and skip if it somehow happens.
                    logger.error(
                        f"Calculated total cost ${total_cost:.2f} exceeds available cash ${cash:.2f} at {index}. Skipping trade."
                    )
                    continue  # Skip this trade

                # Update portfolio
                position += shares_to_buy
                cash -= total_cost
                total_commission += commission
                total_slippage_cost += slippage_cost

                # Record the buy as an open position (lot)
                open_positions.append(
                    {
                        "date": index,
                        "actual_price": actual_buy_price,
                        "shares": shares_to_buy,
                        "commission": commission,
                    }
                )
                trades.append(
                    {
                        "date": index,
                        "type": "buy",
                        "actual_price": actual_buy_price,
                        "shares": shares_to_buy,
                        "commission": commission,
                        "slippage_cost": slippage_cost,
                        "remaining_position": position,
                    }
                )
                logger.debug(
                    f"BUY: {index}, {shares_to_buy:.2f} shares at ${actual_buy_price:.2f} "
                    f"(commission: ${commission:.2f}, slippage cost: ${slippage_cost:.2f})"
                )

        # Check for sell signal when we have a position
        elif row["sell_signal"] and position > 0:
            # Apply slippage to sell price (selling at lower price)
            actual_sell_price = actual_sell_prices.loc[
                index
            ]  # Use pre-calculated price

            shares_to_sell = position  # Sell the entire current position

            # Calculate total commission for this sell transaction
            # Commission is based on the value of shares being sold at the actual sell price
            sell_value_gross = shares_to_sell * actual_sell_price
            commission = commission_fixed + (sell_value_gross * commission_pct)

            # Calculate slippage cost for reporting
            slippage_cost = shares_to_sell * close_price * slippage_pct

            # Ensure cash received is not negative after commission
            cash_received = sell_value_gross - commission
            if cash_received < 0:
                logger.error(
                    f"Commission ${commission:.2f} exceeds gross sell value ${sell_value_gross:.2f} at {index}. Cannot complete sell trade."
                )
                # Decide how to handle: skip sell, or sell for 0 cash? Skipping for now.
                continue

            # Process open positions (FIFO) to calculate P&L for completed lots
            shares_sold_from_lots = 0
            while shares_sold_from_lots < shares_to_sell and open_positions:
                buy_lot = open_positions[0]  # Get the oldest buy lot
                shares_from_this_lot = min(
                    shares_to_sell - shares_sold_from_lots, buy_lot["shares"]
                )

                # Calculate P&L for this segment
                # Gross P/L based on entry/exit prices
                gross_profit_loss = (
                    actual_sell_price - buy_lot["actual_price"]
                ) * shares_from_this_lot

                # Calculate costs associated with this segment (pro-rated buy commission + pro-rated sell commission)
                buy_commission_per_share = (
                    buy_lot["commission"] / buy_lot["shares"]
                    if buy_lot["shares"] > 0
                    else 0
                )
                sell_commission_per_share = (
                    commission / shares_to_sell if shares_to_sell > 0 else 0
                )
                costs_for_segment = (
                    buy_commission_per_share + sell_commission_per_share
                ) * shares_from_this_lot

                net_profit_loss = gross_profit_loss - costs_for_segment

                # Calculate the cost basis for this segment
                cost_basis = buy_lot["actual_price"] * shares_from_this_lot

                # Calculate the total transaction costs for this segment
                total_transaction_costs = (
                    costs_for_segment + buy_lot["commission"] + commission
                )

                # Calculate the return percentage
                return_pct = (
                    (net_profit_loss / cost_basis) * 100
                    if cost_basis > 0
                    else 0.0
                )

                # Record completed trade
                completed_trades.append(
                    {
                        "entry_date": buy_lot["date"],
                        "exit_date": index,
                        "entry_price": buy_lot["actual_price"],
                        "exit_price": actual_sell_price,
                        "shares": shares_from_this_lot,
                        "cost_basis": cost_basis,
                        "sale_value": cash_received,
                        "holding_period_days": (index - buy_lot["date"]).days,
                        "commission": commission,
                        "slippage": slippage_cost,
                        "net_profit_loss": net_profit_loss,
                        "return_pct": return_pct,
                    }
                )

                # Update the buy lot
                buy_lot["shares"] -= shares_from_this_lot
                if buy_lot["shares"] <= 0:
                    open_positions.pop(0)  # Remove the lot if fully sold

                shares_sold_from_lots += shares_from_this_lot

            # Update portfolio state
            cash += cash_received
            total_commission += commission
            total_slippage_cost += slippage_cost

            # Reset position
            position = 0

        # Calculate portfolio value for this day
        portfolio_value = cash + (position * close_price)
        portfolio_values.append(portfolio_value)

    # Calculate final portfolio value
    final_price = df["Close"].iloc[-1]
    final_value = cash + (position * final_price)

    # If there's still an open position at the end, log it
    if position > 0:
        mark_to_market_value = position * final_price
        logger.info(
            f"Open position at end of backtest: {position:.2f} shares, "
            f"Mark-to-market value: ${mark_to_market_value:.2f}"
        )

    # Calculate Buy & Hold final value with proper transaction costs
    if initial_capital <= 0:
        # Handle zero or negative initial capital
        buy_hold_shares = 0
        initial_buy_commission = 0
        buy_hold_initial_slippage = 0
        final_sell_value = 0
        final_sell_commission = 0
        buy_hold_final_value = 0
        buy_hold_total_commission = 0
        buy_hold_total_slippage = 0
    else:
        # Initial buy transaction with accurate cost calculation
        actual_buy_price = initial_price * (
            1 + slippage_pct
        )  # Account for slippage on buy

        # Calculate shares using the formula that accounts for both fixed and percentage costs
        buy_hold_shares = (initial_capital - commission_fixed) / (
            actual_buy_price * (1 + commission_pct)
        )

        # Handle case where fixed commission exceeds initial capital
        if buy_hold_shares <= 0:
            buy_hold_shares = 0
            initial_buy_commission = 0
            buy_hold_initial_slippage = 0
            final_sell_value = 0
            final_sell_commission = 0
            buy_hold_final_value = 0
            buy_hold_total_commission = 0
            buy_hold_total_slippage = 0
        else:
            initial_buy_commission = commission_fixed + (
                buy_hold_shares * actual_buy_price * commission_pct
            )

            # Calculate Buy & Hold slippage for reporting
            buy_hold_initial_slippage = (
                buy_hold_shares * initial_price * slippage_pct
            )

            # Final sell transaction
            actual_sell_price = final_price * (
                1 - slippage_pct
            )  # Account for slippage on sell
            final_sell_value = (
                buy_hold_shares * actual_sell_price
            )  # Value before commission
            final_sell_commission = commission_fixed + (
                final_sell_value * commission_pct
            )  # Commission on sell
            buy_hold_final_value = (
                final_sell_value - final_sell_commission
            )  # Net value after costs

            # Calculate Buy & Hold final slippage for reporting
            buy_hold_final_slippage = (
                buy_hold_shares * final_price * slippage_pct
            )

            # Total Buy & Hold transaction costs
            buy_hold_total_commission = (
                initial_buy_commission + final_sell_commission
            )
            buy_hold_total_slippage = (
                buy_hold_initial_slippage + buy_hold_final_slippage
            )

    # Ensure we have portfolio values for each date in the DataFrame
    if len(portfolio_values) < len(df):
        padding_needed = len(df) - len(portfolio_values)
        logger.debug(f"Padding portfolio values with {padding_needed} entries")
        padding_value = (
            portfolio_values[-1] if portfolio_values else initial_capital
        )
        portfolio_values.extend([padding_value] * padding_needed)
    elif len(portfolio_values) > len(df):
        logger.warning(
            f"Too many portfolio values ({len(portfolio_values)}) for DataFrame length ({len(df)}). Trimming."
        )
        portfolio_values = portfolio_values[: len(df)]

    # Calculate max drawdown
    portfolio_series = pd.Series(portfolio_values, index=df.index)
    portfolio_max = portfolio_series.cummax()
    drawdown = ((portfolio_series - portfolio_max) / portfolio_max) * 100
    max_drawdown = drawdown.min()

    # Calculate performance metrics
    if initial_capital <= 0:
        total_return_pct = 0.0
        buy_hold_return_pct = 0.0
        commission_impact_pct = 0.0
        slippage_impact_pct = 0.0
    else:
        total_return_pct = ((final_value / initial_capital) - 1) * 100
        buy_hold_return_pct = (
            (buy_hold_final_value / initial_capital) - 1
        ) * 100
        commission_impact_pct = (total_commission / initial_capital) * 100
        slippage_impact_pct = (total_slippage_cost / initial_capital) * 100

    # Trading statistics
    num_buy_transactions = len(
        [t for t in trades if t["type"] == "buy"]
    )  # Count of buy signals acted upon
    num_sell_transactions = len(
        [t for t in completed_trades if t["shares"] > 0]
    )  # Count of sell transactions that closed positions
    closed_trade_count = len(
        completed_trades
    )  # Number of completed buy-sell cycles (or segments)

    # Calculate win rate and profit metrics from correctly tracked completed trades
    if closed_trade_count > 0:
        winning_trades = [
            t for t in completed_trades if t["net_profit_loss"] > 0
        ]
        losing_trades = [
            t for t in completed_trades if t["net_profit_loss"] <= 0
        ]

        win_rate = (len(winning_trades) / closed_trade_count) * 100
        avg_profit = (
            np.mean([t["net_profit_loss"] for t in winning_trades])
            if winning_trades
            else 0
        )
        avg_loss = (
            np.mean([t["net_profit_loss"] for t in losing_trades])
            if losing_trades
            else 0
        )

        gross_profit = (
            sum(t["net_profit_loss"] for t in winning_trades)
            if winning_trades
            else 0
        )
        gross_loss = (
            abs(sum(t["net_profit_loss"] for t in losing_trades))
            if losing_trades
            else 0
        )
        profit_factor = (
            (gross_profit / gross_loss)
            if gross_loss > 0
            else (1.0 if gross_profit > 0 else 0.0)
        )
    else:
        win_rate = 0.0
        avg_profit = 0.0
        avg_loss = 0.0
        profit_factor = 0.0

    # Return results
    results = {
        "initial_capital": initial_capital,
        "final_value": final_value,
        "total_return_pct": total_return_pct,
        "buy_hold_return_pct": buy_hold_return_pct,
        "num_trades": num_buy_transactions,
        "win_rate": win_rate,
        "avg_profit": avg_profit,
        "avg_loss": avg_loss,
        "profit_factor": profit_factor,
        "max_drawdown": max_drawdown,
        "total_commission": total_commission,
        "total_slippage_cost": total_slippage_cost,
        "commission_impact_pct": commission_impact_pct,
        "slippage_impact_pct": slippage_impact_pct,
        "buy_hold_total_commission": buy_hold_total_commission,
        "buy_hold_total_slippage": buy_hold_total_slippage,
        "start_date": df.index[0],
        "end_date": df.index[-1],
        "trades": trades,
        "completed_trades": completed_trades,
        "portfolio_values": portfolio_values,
        "closed_trade_count": closed_trade_count,
    }

    logger.info(
        f"Backtest completed. Final value: ${final_value:,.2f}, Return: {total_return_pct:.2f}%, "
        f"Win Rate: {win_rate:.1f}%, Profit Factor: {profit_factor:.2f}, "
        f"Total Commission: ${total_commission:.2f}"
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
    print(f"Number of Trades (Buy Txns): {results['num_trades']}")
    print(f"Number of Completed Trades: {results['closed_trade_count']}")
    print(f"Win Rate: {results['win_rate']:.2f}%")
    print(f"Profit Factor: {results['profit_factor']:.2f}")
    if results["closed_trade_count"] > 0:
        print(
            f"Average Profit per Winning Trade: ${results['avg_profit']:.2f}"
        )
        print(f"Average Loss per Losing Trade: ${results['avg_loss']:.2f}")
    print(f"Max Drawdown: {results['max_drawdown']:.2f}%")
    print(f"Total Commission: ${results['total_commission']:.2f}")
    print(f"Total Slippage: ${results['total_slippage_cost']:.2f}")
    print(f"Commission Impact: {results['commission_impact_pct']:.2f}%")
    print(f"Slippage Impact: {results['slippage_impact_pct']:.2f}%")
    print(f"{'=' * 50}")
