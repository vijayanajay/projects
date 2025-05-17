"""
Test scenario: Backtest with Only Buy Signals (No Corresponding Sells)

This test verifies that the backtester correctly handles the case where buy signals are
generated, but no sell signals occur before the end of the data period, leaving the
position open at the end of backtesting.
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os
import logging

# Add the src directory to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.backtester import run_backtest

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def sample_data_only_buy_signals():
    """Generate a sample DataFrame with only buy signals (no sell signals) for testing."""
    # Generate dates for a year of data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(
        start=start_date, end=end_date, freq="B"
    )  # Business days

    # Generate random price data
    np.random.seed(42)  # For reproducibility
    close_price = 100 + np.random.normal(0, 1, len(dates)).cumsum()
    high_price = close_price * (1 + np.random.uniform(0, 0.05, len(dates)))
    low_price = close_price * (1 - np.random.uniform(0, 0.05, len(dates)))
    open_price = close_price * (1 + np.random.uniform(-0.02, 0.02, len(dates)))
    volume = np.random.randint(1000, 100000, len(dates))

    # Create DataFrame
    data = pd.DataFrame(
        {
            "Open": open_price,
            "High": high_price,
            "Low": low_price,
            "Close": close_price,
            "Volume": volume,
            # Initialize signals as False
            "buy_signal": False,
            "sell_signal": False,
        },
        index=dates,
    )

    # Set a single buy signal at 20% into the dataset
    buy_index = len(data) // 5
    data.iloc[buy_index, data.columns.get_loc("buy_signal")] = True

    return data


def test_backtest_with_only_buy_signals(sample_data_only_buy_signals):
    """Test that run_backtest properly handles a dataset with buy signals but no sell signals."""
    df = sample_data_only_buy_signals

    # Run backtest with standard parameters
    results = run_backtest(
        df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,  # Use full position size for simplicity
    )

    # Verify results
    assert results is not None, "Backtest should return results"
    assert results["closed_trade_count"] == 0, "No trades should be closed"
    assert results["num_trades"] == 1, "Only one buy trade should be executed"
    assert (
        results["win_rate"] == 0.0
    ), "Win rate should be 0 with no closed trades"
    assert (
        results["final_value"] > results["initial_capital"]
    ), "Final value should include open position value"

    # The unrealized P&L should be reflected in the total return
    assert (
        results["total_return_pct"] != 0.0
    ), "Total return should reflect unrealized P&L"

    # Check that the last portfolio value includes the marked-to-market position
    final_portfolio_value = results["portfolio_values"][-1]
    final_close_price = df["Close"].iloc[-1]

    # Verify that we have an open position by checking if there's cash difference
    assert (
        abs(final_portfolio_value - results["initial_capital"]) > 0.01
    ), "Final portfolio value should differ from initial capital"


def test_multiple_buys_no_sells(sample_data_only_buy_signals):
    """Test backtest with multiple buy signals but no sell signals."""
    df = sample_data_only_buy_signals.copy()

    # Add two more buy signals
    buy_indices = [
        len(df) // 2,
        len(df) * 3 // 4,
    ]  # Add buys at 50% and 75% of the dataset
    for idx in buy_indices:
        df.iloc[idx, df.columns.get_loc("buy_signal")] = True

    # Run backtest
    results = run_backtest(
        df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,  # Use 25% position sizing to allow multiple entries
    )

    # Verify results
    assert results is not None, "Backtest should return results"
    assert results["closed_trade_count"] == 0, "No trades should be closed"
    assert results["num_trades"] > 1, "Multiple buy trades should be executed"
    assert results["win_rate"] == 0.0, "Win rate should be 0"

    # The final value should include the value of the open position
    assert (
        results["final_value"] > results["initial_capital"]
    ), "Final value should include open position value"

    # The unrealized P&L should be reflected in the total return
    assert (
        results["total_return_pct"] != 0.0
    ), "Total return should reflect unrealized P&L"

    # Check that the last portfolio value includes the marked-to-market position
    final_portfolio_value = results["portfolio_values"][-1]
    final_close_price = df["Close"].iloc[-1]

    # Verify that we have an open position by checking if there's cash difference
    assert (
        abs(final_portfolio_value - results["initial_capital"]) > 0.01
    ), "Final portfolio value should differ from initial capital"


def test_buy_signals_with_insufficient_capital(sample_data_only_buy_signals):
    """Test backtest with buy signals after capital is depleted."""
    df = sample_data_only_buy_signals.copy()

    # Add more buy signals throughout the dataset
    for i in range(1, 10):
        idx = (
            len(df) * i // 10
        )  # Add buys at 10%, 20%, ..., 90% of the dataset
        df.iloc[idx, df.columns.get_loc("buy_signal")] = True

    # Run backtest with full position sizing to deplete capital quickly
    results = run_backtest(
        df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,  # Use 100% position sizing to deplete capital with first trade
    )

    # Verify results
    assert results is not None, "Backtest should return results"
    assert (
        results["num_trades"] == 1
    ), "Only first buy trade should be executed due to insufficient capital"
    assert (
        results["closed_trade_count"] == 0
    ), "No trades should be closed (no sells)"
