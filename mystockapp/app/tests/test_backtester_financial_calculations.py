"""
Test scenario: Backtester Core Financial Calculation Verification

This test verifies that the run_backtest function correctly calculates:
- Number of shares purchased
- Actual buy price including slippage
- Commission for a single buy trade
- Total cost of trades

These values should be accurately reflected in the trades list and summary results.
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


def test_backtester_buy_transaction_calculations():
    """
    Verify that run_backtest correctly calculates financial metrics for a buy transaction.

    This test creates a minimal dataframe with a single buy signal and manually calculates
    the expected shares, price with slippage, commission, and slippage costs, then
    verifies that the backtester's calculations match.
    """
    # Create a minimal DataFrame with a single buy signal
    dates = pd.date_range(start="2023-01-01", periods=5, freq="B")
    close_price = 100.0  # Fixed price for easy calculation

    df = pd.DataFrame(
        {
            "Open": close_price,
            "High": close_price * 1.01,
            "Low": close_price * 0.99,
            "Close": close_price,
            "Volume": 10000,
            "buy_signal": False,
            "sell_signal": False,
        },
        index=dates,
    )

    # Set buy signal on the second day
    df.iloc[1, df.columns.get_loc("buy_signal")] = True

    # Define backtest parameters
    initial_capital = 10000.0
    commission_fixed = 10.0
    commission_pct = 0.01  # 1%
    slippage_pct = 0.005  # 0.5%
    position_size_pct = 0.5  # Use 50% of capital

    # Manually calculate expected values
    cash_to_invest = initial_capital * position_size_pct
    price_with_slippage = close_price * (1 + slippage_pct)
    expected_shares = (cash_to_invest - commission_fixed) / (
        price_with_slippage * (1 + commission_pct)
    )
    expected_commission = commission_fixed + (
        expected_shares * price_with_slippage * commission_pct
    )
    expected_slippage_cost = expected_shares * close_price * slippage_pct

    # Run backtest
    results = run_backtest(
        df,
        initial_capital=initial_capital,
        commission_fixed=commission_fixed,
        commission_pct=commission_pct,
        slippage_pct=slippage_pct,
        position_size_pct=position_size_pct,
    )

    # Verify results
    assert results is not None, "Backtest should return results"
    assert results["num_trades"] == 1, "Should have exactly one trade"
    assert len(results["trades"]) == 1, "Trades list should contain one entry"

    # Get the trade entry
    trade = results["trades"][0]

    # Verify trade details
    assert trade["type"] == "buy", "Trade should be a buy"
    assert trade["shares"] == pytest.approx(
        expected_shares, rel=1e-6
    ), f"Shares should be {expected_shares}"
    assert trade["actual_price"] == pytest.approx(
        price_with_slippage, rel=1e-6
    ), f"Actual price should be {price_with_slippage}"
    assert trade["commission"] == pytest.approx(
        expected_commission, rel=1e-6
    ), f"Commission should be {expected_commission}"
    assert trade["slippage_cost"] == pytest.approx(
        expected_slippage_cost, rel=1e-6
    ), f"Slippage cost should be {expected_slippage_cost}"

    # Verify summary results
    assert results["total_commission"] == pytest.approx(
        expected_commission, rel=1e-6
    ), "Total commission should match"
    assert results["total_slippage_cost"] == pytest.approx(
        expected_slippage_cost, rel=1e-6
    ), "Total slippage cost should match"

    # Verify final value includes mark-to-market value of the position
    expected_final_value = (
        initial_capital
        - expected_shares * price_with_slippage
        - expected_commission
    ) + (expected_shares * close_price)
    assert results["final_value"] == pytest.approx(
        expected_final_value, rel=1e-6
    ), f"Final value should be {expected_final_value}"

    # Log calculation details for clarity
    logger.info(
        f"Manual calculation: shares={expected_shares:.6f}, price_with_slippage={price_with_slippage:.6f}"
    )
    logger.info(
        f"Manual calculation: commission={expected_commission:.6f}, slippage_cost={expected_slippage_cost:.6f}"
    )
    logger.info(
        f"Backtester results: shares={trade['shares']:.6f}, actual_price={trade['actual_price']:.6f}"
    )
    logger.info(
        f"Backtester results: commission={trade['commission']:.6f}, slippage_cost={trade['slippage_cost']:.6f}"
    )


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
