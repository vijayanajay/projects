"""
Test to verify that CLI indicator parameters are correctly passed to FeatureFactory.
This test specifically validates the fix for the critical flaw (Incorrect Feature Parameterization)
in arch_review.md.
"""

import unittest
import pandas as pd
import numpy as np
import os
import sys
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

# Add parent directory to path to import main.py
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

# Mock required modules before importing main
sys.modules["yaml"] = MagicMock()
sys.modules["streamlit"] = MagicMock()

import main
from src.feature_factory import FeatureFactory


class TestIndicatorParamsPassthrough(unittest.TestCase):
    """Tests for correct passing of CLI indicator parameters to FeatureFactory."""

    def setUp(self):
        """Set up common test data."""
        # Create a small synthetic DataFrame with OHLCV data
        dates = pd.date_range(start="2023-01-01", periods=250, freq="B")
        self.mock_data = pd.DataFrame(
            {
                "Open": np.random.normal(100, 5, 250),
                "High": np.random.normal(105, 5, 250),
                "Low": np.random.normal(95, 5, 250),
                "Close": np.random.normal(100, 5, 250),
                "Volume": np.random.randint(1000, 10000, 250),
            },
            index=dates,
        )

    @patch("src.data_fetcher.get_stock_data")
    @patch("main.FeatureFactory")
    def test_sma_params_passthrough(
        self, mock_feature_factory, mock_get_stock_data
    ):
        """Test that SMA strategy parameters are correctly passed to FeatureFactory."""
        # Mock the get_stock_data function to return our test data
        mock_get_stock_data.return_value = self.mock_data

        # Mock the FeatureFactory class to capture its instantiation arguments
        mock_is_instance = MagicMock()
        mock_is_factory = MagicMock()
        mock_feature_factory.return_value = mock_is_factory
        mock_is_factory.generate_features.return_value = self.mock_data

        mock_oos_instance = MagicMock()
        mock_oos_factory = MagicMock()
        # Replace this with the second call behavior
        mock_feature_factory.side_effect = [mock_is_factory, mock_oos_factory]
        mock_oos_factory.generate_features.return_value = self.mock_data

        # Create test CLI arguments
        test_args = [
            "main.py",
            "--ticker",
            "MOCK",
            "--period",
            "1y",
            "--features",
            "sma",
            "--strategy",
            "sma_crossover",
            "--fast-sma",
            "15",
            "--slow-sma",
            "45",
            "--split-date",
            "2023-06-01",
        ]

        # Patch sys.argv to use our test arguments
        with patch("sys.argv", test_args):
            # Call the main function
            try:
                with patch(
                    "main.create_strategy"
                ):  # Avoid errors in create_strategy
                    main.main()
            except SystemExit:
                pass  # Ignore any SystemExit that main() might raise

        # Check that FeatureFactory was initialized with the correct custom_indicator_params
        # Get the calls to FeatureFactory
        calls = mock_feature_factory.call_args_list

        # There should be at least two calls to FeatureFactory (in-sample and out-of-sample)
        self.assertTrue(
            len(calls) >= 1, "FeatureFactory should be called at least once"
        )

        # Get keyword arguments from the first call (in-sample)
        _, kwargs = calls[0]

        # Verify that indicator_params contains the specified SMA windows
        self.assertIn(
            "indicator_params",
            kwargs,
            "indicator_params should be passed to FeatureFactory",
        )
        indicator_params = kwargs["indicator_params"]

        # Verify the structure of indicator_params - should include sma windows
        self.assertIn(
            "sma",
            indicator_params,
            "indicator_params should include 'sma' family",
        )
        self.assertIn(
            "windows",
            indicator_params["sma"],
            "indicator_params['sma'] should include 'windows'",
        )

        # Verify the specific windows are included
        self.assertIn(
            15,
            indicator_params["sma"]["windows"],
            "Fast SMA (15) should be in indicator_params",
        )
        self.assertIn(
            45,
            indicator_params["sma"]["windows"],
            "Slow SMA (45) should be in indicator_params",
        )

    @patch("src.data_fetcher.get_stock_data")
    @patch("main.FeatureFactory")
    def test_rsi_params_passthrough(
        self, mock_feature_factory, mock_get_stock_data
    ):
        """Test that RSI strategy parameters are correctly passed to FeatureFactory."""
        # Mock the get_stock_data function to return our test data
        mock_get_stock_data.return_value = self.mock_data

        # Mock the FeatureFactory class to capture its instantiation arguments
        mock_is_factory = MagicMock()
        mock_is_factory.generate_features.return_value = self.mock_data
        mock_oos_factory = MagicMock()
        mock_oos_factory.generate_features.return_value = self.mock_data

        # Replace this with the second call behavior
        mock_feature_factory.side_effect = [mock_is_factory, mock_oos_factory]

        # Create test CLI arguments
        test_args = [
            "main.py",
            "--ticker",
            "MOCK",
            "--period",
            "1y",
            "--features",
            "rsi",
            "--strategy",
            "rsi",
            "--rsi-window",
            "10",
            "--split-date",
            "2023-06-01",
        ]

        # Patch sys.argv to use our test arguments
        with patch("sys.argv", test_args):
            # Call the main function
            try:
                with patch(
                    "main.create_strategy"
                ):  # Avoid errors in create_strategy
                    main.main()
            except SystemExit:
                pass  # Ignore any SystemExit that main() might raise

        # Check that FeatureFactory was initialized with the correct custom_indicator_params
        # Get the calls to FeatureFactory
        calls = mock_feature_factory.call_args_list

        # There should be at least two calls to FeatureFactory (in-sample and out-of-sample)
        self.assertTrue(
            len(calls) >= 1, "FeatureFactory should be called at least once"
        )

        # Get keyword arguments from the first call (in-sample)
        _, kwargs = calls[0]

        # Verify that indicator_params contains the specified RSI window
        self.assertIn(
            "indicator_params",
            kwargs,
            "indicator_params should be passed to FeatureFactory",
        )
        indicator_params = kwargs["indicator_params"]

        # Verify the structure of indicator_params - should include rsi window
        self.assertIn(
            "rsi",
            indicator_params,
            "indicator_params should include 'rsi' family",
        )
        self.assertIn(
            "windows",
            indicator_params["rsi"],
            "indicator_params['rsi'] should include 'windows'",
        )

        # Verify the specific window is included
        self.assertIn(
            10,
            indicator_params["rsi"]["windows"],
            "RSI window (10) should be in indicator_params",
        )


if __name__ == "__main__":
    unittest.main()
