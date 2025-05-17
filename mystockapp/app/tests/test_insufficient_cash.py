"""
Test scenario: Backtest with Insufficient Cash for a Trade

This test verifies that the backtester correctly handles the case where a buy signal occurs
but there is insufficient cash to execute the trade (e.g., the available cash is less than
the cost of one share plus commission and slippage).
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
def sample_data_with_buy_signals():
    """Generate a sample DataFrame with buy signals for testing."""
    # Generate dates for a month of data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)  # One month of data
    dates = pd.date_range(
        start=start_date, end=end_date, freq="B"
    )  # Business days

    # Generate price data (around $1000 per share to test low capital scenarios)
    close_price = np.ones(len(dates)) * 1000  # Set price at $1000 per share
    high_price = close_price * 1.01  # 1% higher
    low_price = close_price * 0.99  # 1% lower
    open_price = close_price
    volume = np.ones(len(dates)) * 10000

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

    # Set buy signals at specific points
    data.iloc[5, data.columns.get_loc("buy_signal")] = (
        True  # Buy signal at day 5
    )
    data.iloc[15, data.columns.get_loc("buy_signal")] = (
        True  # Buy signal at day 15
    )

    return data


def test_insufficient_cash_for_single_share():
    """Test that run_backtest handles the case where there's not enough cash for a single share."""
    # Get test data with buy signals
    df = sample_data_with_buy_signals()

    # Set price to $1000 and initial capital to just below what's needed
    # Assume the share price is $1000, and with commission ($20) and slippage (0.1% = $1),
    # we would need about $1021 for one share
    initial_capital = 1020.0  # Just below what's needed for one share

    # Run backtest with low initial capital
    results = run_backtest(
        df,
        initial_capital=initial_capital,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,  # Try to use all capital
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results even with insufficient cash"
    assert (
        results["num_trades"] == 0
    ), "No trades should be executed due to insufficient cash"
    assert results["closed_trade_count"] == 0, "No trades should be closed"
    assert (
        results["final_value"] == initial_capital
    ), "Final value should equal initial capital"
    assert (
        results["total_commission"] == 0.0
    ), "No commission should be charged"

    # Check that portfolio values remain unchanged
    assert all(
        v == initial_capital for v in results["portfolio_values"]
    ), "All portfolio values should equal initial capital"


def test_just_enough_cash_for_single_share():
    """Test that run_backtest executes a trade when there's just enough cash for a single share."""
    # Get test data with buy signals
    df = sample_data_with_buy_signals()

    # Set initial capital to just above what's needed for one share
    # For $1000 share price with commission ($20) and slippage (0.1% = $1),
    # we need about $1021 for one share
    initial_capital = 1022.0  # Just above what's needed for one share

    # Run backtest
    results = run_backtest(
        df,
        initial_capital=initial_capital,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,  # Try to use all capital
    )

    # Verify results
    assert results is not None, "Backtest should return results"
    assert results["num_trades"] > 0, "At least one trade should be executed"

    # Ensure portfolio value now includes a position
    assert (
        results["final_value"] != initial_capital
    ), "Final value should differ from initial capital"


def test_insufficient_cash_after_first_trade():
    """Test that run_backtest handles multiple buy signals when cash becomes insufficient after first trade."""
    # Get test data with buy signals
    df = sample_data_with_buy_signals()

    # Set initial capital to just enough for one share, but not two
    initial_capital = 1500.0  # Enough for one $1000 share but not two

    # Run backtest
    results = run_backtest(
        df,
        initial_capital=initial_capital,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.75,  # Use 75% of capital per trade
    )

    # Verify results
    assert results is not None, "Backtest should return results"
    assert (
        results["num_trades"] == 1
    ), "Only one trade should be executed due to insufficient cash for second trade"


def test_high_commission_prevents_trade():
    """Test that run_backtest handles the case where high commission prevents trading."""
    # Get test data with buy signals
    df = sample_data_with_buy_signals()

    # Set very high fixed commission that exceeds initial capital
    initial_capital = 5000.0
    commission_fixed = 6000.0  # Higher than initial capital

    # Run backtest
    results = run_backtest(
        df,
        initial_capital=initial_capital,
        commission_fixed=commission_fixed,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results even with high commission"
    assert (
        results["num_trades"] == 0
    ), "No trades should be executed due to commission exceeding capital"
    assert (
        results["final_value"] == initial_capital
    ), "Final value should equal initial capital"


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
    close = 100 + rng.randn(60).cumsum()

    # Create realistic Open, High, Low values based on Close
    daily_volatility = 2.0
    open_prices = (
        close.shift(1).fillna(close[0]) + rng.randn(60) * daily_volatility
    )
    high_prices = (
        np.maximum(close, open_prices) + rng.rand(60) * daily_volatility * 1.5
    )
    low_prices = (
        np.minimum(close, open_prices) - rng.rand(60) * daily_volatility * 1.5
    )

    # Generate volume data
    volume = (1000000 + rng.randn(60) * 200000).astype(int)
    volume = np.abs(volume)  # Ensure positive volume

    # Create DataFrame
    data = pd.DataFrame(
        {
            "Open": open_prices,
            "High": high_prices,
            "Low": low_prices,
            "Close": close,
            "Volume": volume,
            # Add empty signal columns
            "buy_signal": False,
            "sell_signal": False,
        },
        index=dates,
    )

    return data


def test_insufficient_cash_for_trade(sample_ohlcv_data):
    """
    Test that backtest handles insufficient cash for a trade correctly.

    The test sets initial capital to a very low value, just slightly
    above the price of one share, but below what's needed when including
    commission and slippage.
    """
    # Get price of first row to set up the test
    first_price = sample_ohlcv_data["Close"].iloc[0]

    # Set initial capital to just above share price but below share price + costs
    # This should result in insufficient funds after accounting for costs
    initial_capital = first_price * 1.05  # Just 5% above share price

    # Set a buy signal in the first row
    sample_ohlcv_data.loc[sample_ohlcv_data.index[0], "buy_signal"] = True

    # Run backtest with fixed commission that will make the trade impossible
    commission_fixed = (
        first_price * 0.10
    )  # 10% of share price as fixed commission

    results = run_backtest(
        sample_ohlcv_data,
        initial_capital=initial_capital,
        commission_fixed=commission_fixed,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,  # Try to use 100% of capital
    )

    # Verify that we have results
    assert results is not None

    # Check final value equals initial capital (no change since no trades executed)
    assert results["final_value"] == pytest.approx(initial_capital, rel=1e-10)

    # Verify no trades were executed
    assert results["num_trades"] == 0
    assert len(results["trades"]) == 0
    assert results["closed_trade_count"] == 0

    # No commissions should have been charged
    assert results["total_commission"] == pytest.approx(0.0, abs=1e-10)
    assert results["total_slippage_cost"] == pytest.approx(0.0, abs=1e-10)


def test_insufficient_cash_after_cost_calculation(sample_ohlcv_data):
    """
    Test where there's enough cash for the share but not when all costs are calculated.

    This test checks if the backtester correctly abandons a trade when the calculated
    total cost (share price + commission + slippage) exceeds the available cash.
    """
    # Get price of first row to set up the test
    first_price = sample_ohlcv_data["Close"].iloc[0]

    # Set initial capital to be more than share price but not enough for costs
    initial_capital = first_price * 1.2  # 20% above share price

    # Set a buy signal in the first row
    sample_ohlcv_data.loc[sample_ohlcv_data.index[0], "buy_signal"] = True

    # Run backtest with parameters that will make the total cost exceed available capital
    results = run_backtest(
        sample_ohlcv_data,
        initial_capital=initial_capital,
        commission_fixed=first_price
        * 0.15,  # 15% of share price as fixed cost
        commission_pct=0.05,  # 5% commission
        slippage_pct=0.02,  # 2% slippage
        position_size_pct=1.0,  # Try to use 100% of capital
    )

    # Verify that we have results
    assert results is not None

    # Check if no trades were executed or if shares were adjusted to a smaller amount
    # Depending on implementation, the backtester might skip the trade or adjust it

    # If no trades executed:
    if len(results["trades"]) == 0:
        assert results["final_value"] == pytest.approx(
            initial_capital, rel=1e-10
        )
        assert results["num_trades"] == 0
        assert results["total_commission"] == pytest.approx(0.0, abs=1e-10)

    # If shares adjusted:
    else:
        # Verify we bought less than 1 share
        assert results["trades"][0]["shares"] < 1.0
        # Verify the final cost was less than or equal to initial capital
        total_cost = (
            results["trades"][0]["value"] + results["trades"][0]["commission"]
        )
        assert total_cost <= initial_capital


def test_multiple_trades_with_limited_capital(sample_ohlcv_data):
    """
    Test that the backtester correctly handles multiple trades when capital becomes limited.
    """
    # Set price to a known value for predictable test
    first_price = 100.0
    sample_ohlcv_data["Close"] = first_price

    # Set initial capital to enough for exactly two shares after costs
    commission_fixed = 10.0
    commission_pct = 0.01  # 1%
    slippage_pct = 0.005  # 0.5%

    # Calculate cost of one share with all fees
    share_price_with_slippage = first_price * (1 + slippage_pct)
    commission_per_share = commission_fixed + (
        share_price_with_slippage * commission_pct
    )
    total_cost_per_share = share_price_with_slippage + commission_per_share

    # Set initial capital to be enough for exactly 2 shares
    initial_capital = total_cost_per_share * 2

    # Set buy signals at the first three days
    sample_ohlcv_data.loc[sample_ohlcv_data.index[0], "buy_signal"] = True
    sample_ohlcv_data.loc[sample_ohlcv_data.index[2], "buy_signal"] = True
    sample_ohlcv_data.loc[sample_ohlcv_data.index[4], "buy_signal"] = True

    # Run backtest with position size 50% - this should allow exactly 2 trades
    results = run_backtest(
        sample_ohlcv_data,
        initial_capital=initial_capital,
        commission_fixed=commission_fixed,
        commission_pct=commission_pct,
        slippage_pct=slippage_pct,
        position_size_pct=0.5,  # Use 50% of capital per trade
    )

    # Verify that we have results
    assert results is not None

    # Should have executed exactly 2 trades (since the third would exceed capital)
    assert results["num_trades"] == 2

    # Verify total commission is for exactly 2 trades
    expected_commission = 2 * commission_per_share
    assert results["total_commission"] == pytest.approx(
        expected_commission, rel=1e-6
    )


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
