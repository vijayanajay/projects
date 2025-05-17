"""
Test scenario: App DataFrame Consistency

This test verifies that the app.py file consistently uses
features_with_signals for portfolio data series and buy/sell points,
which resolves the "Critical Data Integrity / UI Bug" identified in the audit.
"""

import os
import logging

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_app_uses_consistent_dataframe():
    """
    Test that app.py uses features_with_signals consistently for indexing
    portfolio_series and finding buy/sell points.
    """
    # Get the path to the app.py file
    app_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app.py")
    )
    assert os.path.exists(app_path), f"app.py not found at {app_path}"

    # Read the file content
    with open(app_path, "r") as f:
        content = f.read()

    # Check for the key fixes

    # 1. portfolio_series should use features_with_signals.index
    portfolio_series_line = (
        'results["portfolio_values"], index=features_with_signals.index'
    )
    assert (
        portfolio_series_line in content
    ), "portfolio_series should use features_with_signals.index"

    # 2. portfolio equity curve should use features_with_signals.index
    equity_curve_line = "x=features_with_signals.index,"
    assert (
        equity_curve_line in content
    ), "Equity curve should use features_with_signals.index"

    # 3. buy_points should use features_with_signals
    buy_points_line = 'buy_points = features_with_signals[features_with_signals["buy_signal"] == True]'
    assert (
        buy_points_line in content
    ), "buy_points should use features_with_signals"

    # 4. sell_points should use features_with_signals
    sell_points_line = 'sell_points = features_with_signals[features_with_signals["sell_signal"] == True]'
    assert (
        sell_points_line in content
    ), "sell_points should use features_with_signals"

    # 5. The problematic code should not be present
    assert (
        'portfolio_series = pd.Series(results["portfolio_values"], index=features_df.index)'
        not in content
    ), "portfolio_series should not use features_df.index"
    assert (
        'buy_points = features_df[features_df["buy_signal"] == True]'
        not in content
    ), "buy_points should not use features_df"

    logger.info(
        "Verified app.py uses features_with_signals consistently for UI elements"
    )
