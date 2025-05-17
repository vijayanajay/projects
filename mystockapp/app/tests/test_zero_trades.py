"""
Test scenario: Backtest with Zero Trades (No Signals)

This test verifies that the backtester correctly handles the case where there are no
buy or sell signals in the input data, which is a fundamental baseline.
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
def sample_data_no_signals():
    """Generate a sample DataFrame with no buy/sell signals for testing."""
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
            # All signals are False
            "buy_signal": False,
            "sell_signal": False,
        },
        index=dates,
    )

    return data


def test_backtest_with_zero_trades():
    """Test that run_backtest handles datasets with no trading signals correctly."""
    # Get test data with no signals
    df = sample_data_no_signals()

    # Run backtest with standard parameters
    results = run_backtest(
        df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results even with no signals"
    assert results["closed_trade_count"] == 0, "No trades should be closed"
    assert results["num_trades"] == 0, "No trades should be executed"
    assert results["win_rate"] == 0.0, "Win rate should be 0"
    assert results["total_return_pct"] == 0.0, "Total return should be 0"
    assert (
        results["final_value"] == 100000.0
    ), "Final value should equal initial capital"
    assert (
        results["total_commission"] == 0.0
    ), "No commission should be charged with no trades"
    assert (
        results["total_slippage_cost"] == 0.0
    ), "No slippage should be incurred with no trades"

    # Check that portfolio values match the input length
    assert len(results["portfolio_values"]) == len(
        df
    ), "Portfolio values should match input DataFrame length"

    # All portfolio values should be equal to initial capital
    assert all(
        v == 100000.0 for v in results["portfolio_values"]
    ), "All portfolio values should equal initial capital"


def test_backtest_with_nan_values(sample_data_no_signals):
    """Test that run_backtest handles datasets with NaN values appropriately."""
    df = sample_data_no_signals
    # Add NaN values to some rows in critical columns
    df.loc[df.index[10:20], "Close"] = np.nan
    df.loc[df.index[30:40], "buy_signal"] = np.nan

    # Run backtest, should return None or raise error due to NaN values
    results = run_backtest(
        df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    assert (
        results is None
    ), "Backtest should fail with NaN values in critical columns"


@pytest.fixture
def sample_ohlcv_data():
    """
    Create a sample OHLCV DataFrame for testing.

    Returns:
        pd.DataFrame: Sample OHLCV DataFrame with 60 days of data
    """
    # Create date range for 60 business days
    dates = pd.date_range(start="2023-01-01", periods=60, freq="B")

    # Generate random price data that somewhat resembles a stock
    rng = np.random.RandomState(42)  # Fixed seed for reproducibility
    close_series = pd.Series(100 + rng.randn(60).cumsum(), index=dates)

    # Create realistic Open, High, Low values based on Close
    daily_volatility = 2.0
    open_prices = (
        close_series.shift(1).fillna(close_series.iloc[0])
        + rng.randn(60) * daily_volatility
    )
    high_prices = (
        np.maximum(close_series.values, open_prices)
        + rng.rand(60) * daily_volatility * 1.5
    )
    low_prices = (
        np.minimum(close_series.values, open_prices)
        - rng.rand(60) * daily_volatility * 1.5
    )
    volume = (1000000 + rng.randn(60) * 200000).astype(int)
    volume = np.abs(volume)

    data = pd.DataFrame(
        {
            "Open": open_prices,
            "High": high_prices,
            "Low": low_prices,
            "Close": close_series,
            "Volume": volume,
            "buy_signal": False,
            "sell_signal": False,
        },
        index=dates,
    )
    return data


def test_backtest_with_zero_trades(sample_ohlcv_data):
    """
    Test that backtest works correctly when no trades are executed.

    This test creates a DataFrame with OHLCV data but all buy/sell signals
    are set to False, meaning no trades should occur.
    """
    # Ensure all signals are False
    sample_ohlcv_data["buy_signal"] = False
    sample_ohlcv_data["sell_signal"] = False

    # Set backtest parameters
    initial_capital = 100000.0

    # Run backtest
    results = run_backtest(
        sample_ohlcv_data,
        initial_capital=initial_capital,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # Verify that we have results
    assert results is not None

    # Check final value equals initial capital (no change)
    assert results["final_value"] == pytest.approx(initial_capital, rel=1e-10)

    # Verify no trades were executed
    assert results["num_trades"] == 0
    assert len(results["trades"]) == 0
    assert results["closed_trade_count"] == 0

    # Check all performance metrics are at baseline (zero)
    assert results["total_return_pct"] == pytest.approx(0.0, abs=1e-10)
    assert results["win_rate"] == pytest.approx(0.0, abs=1e-10)
    assert results["max_drawdown"] == pytest.approx(0.0, abs=1e-10)
    assert results["total_commission"] == pytest.approx(0.0, abs=1e-10)
    assert results["total_slippage_cost"] == pytest.approx(0.0, abs=1e-10)

    # Verify all portfolio values match initial capital
    assert all(
        value == pytest.approx(initial_capital, rel=1e-10)
        for value in results["portfolio_values"]
    )


def test_backtest_with_only_buy_signal_executed(sample_ohlcv_data):
    """
    Test backtest behavior when only buy signals occur, and position remains open at the end.
    """
    # Set a buy signal in the middle of the data
    buy_index = 30
    sample_ohlcv_data["buy_signal"] = False
    sample_ohlcv_data["sell_signal"] = False
    sample_ohlcv_data.loc[sample_ohlcv_data.index[buy_index], "buy_signal"] = (
        True
    )

    # Set backtest parameters
    initial_capital = 100000.0

    # Run backtest
    results = run_backtest(
        sample_ohlcv_data,
        initial_capital=initial_capital,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # Verify that we have results
    assert results is not None

    # Should be exactly one trade (the buy)
    assert results["num_trades"] == 1
    assert len(results["trades"]) == 1
    assert results["trades"][0]["type"] == "buy"

    # No trades should be completed (no sells)
    assert results["closed_trade_count"] == 0
    assert results["win_rate"] == pytest.approx(0.0, abs=1e-10)

    # Final value should include mark-to-market value of the open position
    trade_value_at_entry = (
        results["trades"][0]["shares"] * results["trades"][0]["actual_price"]
    )
    cash_after_buy = (
        initial_capital
        - trade_value_at_entry
        - results["trades"][0]["commission"]
    )
    final_position_value_at_exit_price = (
        results["trades"][0]["shares"] * sample_ohlcv_data["Close"].iloc[-1]
    )
    assert results["final_value"] == pytest.approx(
        cash_after_buy + final_position_value_at_exit_price, rel=1e-4
    )


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
