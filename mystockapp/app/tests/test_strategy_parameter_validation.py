"""
Test to verify that strategy classes correctly validate their parameters.
This test specifically validates the fix for the critical flaw (Invalid Strategy Parameters from UI)
in arch_review.md.
"""

import unittest
import sys
import os

# from unittest.mock import patch, MagicMock  # Keep if needed for other mocks

# Add parent directory to path to import source files
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

# Mock streamlit before importing backtester
# REMOVE THIS LINE: sys.modules["streamlit"] = MagicMock()

from src.backtester import SMACrossoverStrategy, RSIStrategy


class TestStrategyParameterValidation(unittest.TestCase):
    """Tests for validating strategy parameters during initialization."""

    def test_sma_crossover_strategy_valid_params(self):
        """Test SMACrossoverStrategy with valid parameters."""
        # Valid parameters: fast < slow, both positive integers
        strategy = SMACrossoverStrategy(fast_window=20, slow_window=50)
        self.assertEqual(strategy.fast_window, 20)
        self.assertEqual(strategy.slow_window, 50)
        self.assertEqual(strategy.name, "SMA Crossover (20/50)")

    def test_sma_crossover_strategy_invalid_fast_equals_slow(self):
        """Test SMACrossoverStrategy rejects fast_window == slow_window."""
        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=50, slow_window=50)

        self.assertIn("must be less than", str(context.exception))

    def test_sma_crossover_strategy_invalid_fast_greater_than_slow(self):
        """Test SMACrossoverStrategy rejects fast_window > slow_window."""
        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=100, slow_window=50)

        self.assertIn("must be less than", str(context.exception))

    def test_sma_crossover_strategy_invalid_negative_window(self):
        """Test SMACrossoverStrategy rejects negative window values."""
        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=-10, slow_window=50)

        self.assertIn("must be positive integers", str(context.exception))

        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=10, slow_window=-50)

        self.assertIn("must be positive integers", str(context.exception))

    def test_sma_crossover_strategy_invalid_zero_window(self):
        """Test SMACrossoverStrategy rejects zero window values."""
        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=0, slow_window=50)

        self.assertIn("must be positive integers", str(context.exception))

        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=10, slow_window=0)

        self.assertIn("must be positive integers", str(context.exception))

    def test_sma_crossover_strategy_invalid_non_integer_window(self):
        """Test SMACrossoverStrategy rejects non-integer window values."""
        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window="10", slow_window=50)

        self.assertIn("must be positive integers", str(context.exception))

        with self.assertRaises(ValueError) as context:
            SMACrossoverStrategy(fast_window=10, slow_window="50")

        self.assertIn("must be positive integers", str(context.exception))

    def test_rsi_strategy_valid_params(self):
        """Test RSIStrategy with valid parameters."""
        # Valid parameters: 0 <= oversold < overbought <= 100
        strategy = RSIStrategy(
            rsi_window=14, oversold_threshold=30, overbought_threshold=70
        )
        self.assertEqual(strategy.rsi_window, 14)
        self.assertEqual(strategy.oversold_threshold, 30)
        self.assertEqual(strategy.overbought_threshold, 70)
        self.assertEqual(strategy.name, "RSI (14, 30/70)")

    def test_rsi_strategy_invalid_threshold_relation(self):
        """Test RSIStrategy rejects oversold_threshold >= overbought_threshold."""
        # Equal thresholds
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window=14, oversold_threshold=50, overbought_threshold=50
            )

        self.assertIn("must be less than", str(context.exception))

        # Oversold > Overbought
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window=14, oversold_threshold=70, overbought_threshold=30
            )

        self.assertIn("must be less than", str(context.exception))

    def test_rsi_strategy_invalid_threshold_range(self):
        """Test RSIStrategy rejects thresholds outside [0, 100]."""
        # Below 0
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window=14, oversold_threshold=-10, overbought_threshold=70
            )

        self.assertIn("must be between 0 and 100", str(context.exception))

        # Above 100
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window=14, oversold_threshold=30, overbought_threshold=110
            )

        self.assertIn("must be between 0 and 100", str(context.exception))

    def test_rsi_strategy_invalid_window(self):
        """Test RSIStrategy rejects invalid window values."""
        # Zero window
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window=0, oversold_threshold=30, overbought_threshold=70
            )

        self.assertIn("must be a positive integer", str(context.exception))

        # Negative window
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window=-14, oversold_threshold=30, overbought_threshold=70
            )

        self.assertIn("must be a positive integer", str(context.exception))

        # Non-integer window
        with self.assertRaises(ValueError) as context:
            RSIStrategy(
                rsi_window="14", oversold_threshold=30, overbought_threshold=70
            )

        self.assertIn("must be a positive integer", str(context.exception))


if __name__ == "__main__":
    unittest.main()
