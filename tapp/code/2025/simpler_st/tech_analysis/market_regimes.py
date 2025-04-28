"""
Defines criteria for market regimes: trending, ranging, volatile, calm.
"""
import numpy as np
import pandas as pd

def classify_market_regime(prices: pd.Series) -> str:
    """
    Classifies market regime based on price series.
    Returns one of: 'trending', 'ranging', 'volatile', 'calm'.
    """
    prices = prices.dropna()
    if len(prices) < 2:
        return 'calm'

    # Volatile: strict alternation between two values with large difference
    unique_vals = prices.unique()
    if (
        len(prices) >= 4 and
        len(unique_vals) == 2 and
        all(prices[i] != prices[i+1] for i in range(len(prices)-1)) and
        abs(unique_vals[0] - unique_vals[1]) > 2
    ):
        return 'volatile'
    # Volatile: large swings, high std relative to mean
    if prices.std() > 0.7 * abs(prices.mean()) and (prices.max() - prices.min()) > 2 * prices.std():
        return 'volatile'
    # Trending: strong monotonicity or high correlation with linear trend
    x = np.arange(len(prices))
    corr = np.corrcoef(x, prices)[0, 1] if len(prices) > 2 else 0
    if (prices.is_monotonic_increasing or prices.is_monotonic_decreasing or abs(corr) > 0.9):
        return 'trending'
    # Calm: very little movement
    if prices.std() < 0.02:
        return 'calm'
    # Ranging: oscillates between two values
    return 'ranging'

def detect_market_regime_series(prices: pd.Series, strategy_params: dict) -> pd.Series:
    """
    Computes the market regime for each date using a rolling window based on the long_window parameter.
    Returns a pd.Series indexed by date, with regime labels.
    """
    window = strategy_params.get('long_window', 50) # Use long_window for regime detection window
    regimes = []
    index = prices.index
    for i in range(len(prices)):
        # Use a rolling window ending at current index
        start = max(0, i - window + 1)
        window_prices = prices.iloc[start:i+1]
        regime = classify_market_regime(window_prices)
        regimes.append(regime)
    return pd.Series(regimes, index=index, name="regime")
