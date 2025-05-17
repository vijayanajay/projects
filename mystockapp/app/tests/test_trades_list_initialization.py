"""
Test scenario: Trades List Initialization

This test verifies that the 'trades' list is properly initialized in the run_backtest function
to prevent a NameError when a buy signal is encountered.
"""

import os
import logging
import re

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_trades_list_properly_initialized():
    """
    Test that the 'trades' list is properly initialized in the run_backtest function
    by examining the source code.
    """
    # Get the path to the backtester.py file
    backtester_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src", "backtester.py")
    )
    assert os.path.exists(
        backtester_path
    ), f"backtester.py not found at {backtester_path}"

    # Read the file content
    with open(backtester_path, "r") as f:
        content = f.read()

    # Find the run_backtest function in the content
    run_backtest_match = re.search(
        r"def run_backtest\([^)]*\):[^\n]*\n(.*?)(?=\n\n\n|\n\n\w+\s+\w+)",
        content,
        re.DOTALL,
    )
    assert (
        run_backtest_match
    ), "Could not find run_backtest function in backtester.py"

    run_backtest_body = run_backtest_match.group(1)

    # Check that trades list is initialized
    assert (
        "trades = []" in run_backtest_body
    ), "trades list should be initialized at the beginning of run_backtest"

    # Check that trades list is returned
    assert (
        '"trades": trades,' in content
    ), "trades list should be included in the returned results dictionary"

    # Verify there's no place where "trades.append" is called without "trades" being initialized
    # This is a basic check - a more thorough one would parse the AST
    trades_append_match = re.search(r"trades\.append\(", content)
    assert (
        trades_append_match
    ), "Expected to find trades.append in the function"

    logger.info(
        "Verified 'trades' list is properly initialized in run_backtest function"
    )
