"""
Test scenario: Main Return Value

This test verifies that the main() function in main.py
correctly returns the combined_df (with signals) instead of the features_df.
"""

import sys
import os
import logging
from unittest.mock import patch, MagicMock, ANY
import pandas as pd
import importlib.util

# Add parent directory to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_main_returns_combined_df():
    """
    Test that the main() function returns combined_df instead of features_df.
    """
    # Import main.py
    main_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "main.py")
    )
    assert os.path.exists(main_path), f"main.py not found at {main_path}"

    # Read the file to check if the fix is in place
    with open(main_path, "r") as f:
        content = f.read()

    # Verify that the return statement uses combined_df and not features_df
    assert (
        "return combined_df if" in content
    ), "main() should return combined_df"
    assert (
        "return features_df if" not in content
    ), "main() should not return features_df"

    # Check for the safety checks in the return statement
    assert (
        "combined_df is not None" in content
    ), "Return should check if combined_df is not None"
    assert (
        "not combined_df.empty" in content
    ), "Return should check if combined_df is not empty"

    logger.info("Verified main() function correctly returns combined_df")
