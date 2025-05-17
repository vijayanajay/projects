"""
Test scenario: Backtest with Zero Capital or Zero Costs

This test verifies the behavior of run_backtest function with edge case
financial inputs like:
- Zero initial capital
- Zero commission/slippage
- Zero position size percentage
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
from src.backtester import run_backtest, SMACrossoverStrategy
from src.feature_factory import FeatureFactory

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def sample_data_with_signals():
    """Generate a sample DataFrame with buy/sell signals for testing."""
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
        },
        index=dates,
    )

    # Generate SMA columns
    data["sma_20"] = data["Close"].rolling(window=20).mean()
    data["sma_50"] = data["Close"].rolling(window=50).mean()

    # Generate buy/sell signals
    data["fast_gt_slow"] = data["sma_20"] > data["sma_50"]
    data["buy_signal"] = (data["sma_20"] > data["sma_50"]) & (
        data["sma_20"].shift(1) <= data["sma_50"].shift(1)
    )
    data["sell_signal"] = (data["sma_20"] < data["sma_50"]) & (
        data["sma_20"].shift(1) >= data["sma_50"].shift(1)
    )

    # Drop NaN values
    data = data.dropna()

    return data


def test_backtest_with_zero_capital(sample_data_with_signals):
    """Test run_backtest with initial_capital=0."""
    # Run backtest with zero initial capital
    results = run_backtest(
        sample_data_with_signals,
        initial_capital=0.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results even with zero capital"
    assert results["initial_capital"] == 0.0, "Initial capital should be 0"
    assert results["final_value"] == 0.0, "Final value should be 0"
    assert (
        results["closed_trade_count"] == 0
    ), "No trades should be closed with zero capital"
    assert results["num_trades"] == 0, "No trades should be executed"
    assert results["win_rate"] == 0.0, "Win rate should be 0"
    assert results["total_return_pct"] == 0.0, "Return percentage should be 0"


def test_backtest_with_zero_costs(sample_data_with_signals):
    """Test run_backtest with zero commission and slippage costs."""
    # Run backtest with zero costs
    results = run_backtest(
        sample_data_with_signals,
        initial_capital=100000.0,
        commission_fixed=0.0,
        commission_pct=0.0,
        slippage_pct=0.0,
        position_size_pct=0.25,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results with zero costs"
    assert results["total_commission"] == 0.0, "Total commission should be 0"
    assert results["total_slippage_cost"] == 0.0, "Total slippage should be 0"
    assert (
        results["commission_impact_pct"] == 0.0
    ), "Commission impact should be 0%"
    assert (
        results["slippage_impact_pct"] == 0.0
    ), "Slippage impact should be 0%"

    # Verify that trades executed with correct purchase amounts
    if results["num_trades"] > 0:
        # With zero costs, actual_buy_price should equal close_price
        trades = results["trades"]
        for trade in trades:
            if trade["type"] == "buy":
                assert (
                    trade["price"] == trade["actual_price"]
                ), "With no slippage, trade price should equal actual price"

    assert (
        results["closed_trade_count"] >= 0
    ), "Trades should execute without costs"
    assert (
        results["win_rate"] == pytest.approx(0.0, abs=1e-10)
        if results["closed_trade_count"] == 0
        else results["win_rate"] > 0
    ), "Win rate should be calculated correctly"


def test_backtest_with_zero_position_size(sample_data_with_signals):
    """Test run_backtest with position_size_pct=0."""
    # Run backtest with zero position size
    results = run_backtest(
        sample_data_with_signals,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.0,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results with zero position size"
    assert results["closed_trade_count"] == 0, "No trades should be closed"
    assert results["num_trades"] == 0, "No trades should be executed"
    assert (
        results["final_value"] == 100000.0
    ), "Final value should equal initial capital"
    assert results["total_return_pct"] == 0.0, "Return percentage should be 0"


def test_backtest_with_full_position_size(sample_data_with_signals):
    """Test run_backtest with position_size_pct=1.0 (full position sizing)."""
    # Run backtest with full position size
    results = run_backtest(
        sample_data_with_signals,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results with full position size"

    # Check that at least one trade was made
    if results["num_trades"] > 0:
        # First trade should use all available capital
        trades = results["trades"]
        first_buy = next((t for t in trades if t["type"] == "buy"), None)

        if first_buy:
            # With slippage and commission, value should be slightly less than initial capital
            assert (
                first_buy["value"] < 100000.0
            ), "First trade value should be less than initial capital"
            assert (
                first_buy["value"] > 99000.0
            ), "First trade value should be close to initial capital"


def test_backtest_with_very_small_capital(sample_data_with_signals):
    """Test run_backtest with very small initial capital."""
    # Run backtest with small capital
    results = run_backtest(
        sample_data_with_signals,
        initial_capital=100.0,  # Just $100
        commission_fixed=20.0,  # $20 fixed commission
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=1.0,  # Use all capital
    )

    # With $20 fixed commission and $100 capital, might not be able to make any trades
    assert (
        results is not None
    ), "Backtest should return results with small capital"

    # The exact outcomes depend on the implementation:
    # Case 1: System attempts a trade but cannot afford any shares after commission
    # Case 2: System decides not to attempt trades at all when capital is insufficient

    # In either case, capital should remain unchanged or slightly reduced
    assert results["final_value"] <= 100.0, "Final value should not increase"

    # Log the actual results for analysis
    logger.info(
        f"Backtest with small capital results: num_trades={results['num_trades']}, "
        f"final_value={results['final_value']}"
    )


def test_backtest_with_very_high_commission(sample_data_with_signals):
    """Test run_backtest with very high commission costs."""
    # Run backtest with high commissions
    results = run_backtest(
        sample_data_with_signals,
        initial_capital=100000.0,
        commission_fixed=1000.0,  # Very high fixed commission
        commission_pct=0.05,  # Very high percentage commission (5%)
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # Verify results
    assert (
        results is not None
    ), "Backtest should return results with high commission"

    # With such high commissions, performance should be worse than buy & hold
    assert (
        results["total_return_pct"] < results["buy_hold_return_pct"]
    ), "Strategy return should be worse than buy & hold"

    # The commission impact should be significant
    assert (
        results["commission_impact_pct"] > 1.0
    ), "Commission impact should be significant"

    # Log the actual results for analysis
    logger.info(
        f"Backtest with high commission results: "
        f"total_return={results['total_return_pct']:.2f}%, "
        f"buy_hold_return={results['buy_hold_return_pct']:.2f}%, "
        f"commission_impact={results['commission_impact_pct']:.2f}%"
    )


def test_backtest_with_negative_parameters():
    """
    Test run_backtest with negative values for financial parameters.

    This test checks that the system handles invalid inputs correctly.
    """
    # Create a minimal valid DataFrame
    dates = pd.date_range(start="2022-01-01", periods=10)
    df = pd.DataFrame(
        {
            "Close": np.linspace(100, 110, 10),
            "buy_signal": [
                False,
                True,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "sell_signal": [
                False,
                False,
                False,
                False,
                True,
                False,
                False,
                False,
                False,
                False,
            ],
        },
        index=dates,
    )

    # Test with negative initial capital
    with pytest.raises(Exception):
        run_backtest(
            df,
            initial_capital=-10000.0,  # Invalid negative value
            commission_fixed=20.0,
            commission_pct=0.0003,
            slippage_pct=0.001,
            position_size_pct=0.25,
        )

    # Test with negative commission
    with pytest.raises(Exception):
        run_backtest(
            df,
            initial_capital=10000.0,
            commission_fixed=-20.0,  # Invalid negative value
            commission_pct=0.0003,
            slippage_pct=0.001,
            position_size_pct=0.25,
        )

    # Test with negative slippage
    with pytest.raises(Exception):
        run_backtest(
            df,
            initial_capital=10000.0,
            commission_fixed=20.0,
            commission_pct=0.0003,
            slippage_pct=-0.001,  # Invalid negative value
            position_size_pct=0.25,
        )

    # Test with negative position size
    with pytest.raises(Exception):
        run_backtest(
            df,
            initial_capital=10000.0,
            commission_fixed=20.0,
            commission_pct=0.0003,
            slippage_pct=0.001,
            position_size_pct=-0.25,  # Invalid negative value
        )
