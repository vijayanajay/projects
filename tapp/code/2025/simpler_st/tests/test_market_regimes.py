import pandas as pd
from tech_analysis.market_regimes import classify_market_regime

def test_trending():
    prices = pd.Series([1, 2, 3, 4, 5])
    assert classify_market_regime(prices) == 'trending'

def test_ranging():
    prices = pd.Series([1, 2, 1, 2, 1])
    assert classify_market_regime(prices) == 'ranging'

def test_volatile():
    prices = pd.Series([1, 5, 1, 5, 1])
    assert classify_market_regime(prices) == 'volatile'

def test_calm():
    prices = pd.Series([1, 1.01, 1.02, 1.01, 1])
    assert classify_market_regime(prices) == 'calm'

def test_noisy_trending():
    prices = pd.Series([1, 2, 1.9, 3, 4.1, 5])
    assert classify_market_regime(prices) == 'trending'

def test_noisy_ranging():
    prices = pd.Series([1, 2, 1.1, 2, 1.2, 2])
    assert classify_market_regime(prices) == 'ranging'

def test_calm_with_outlier():
    prices = pd.Series([1, 1.01, 1, 5, 1])
    # For now, expect 'volatile' due to the outlier
    assert classify_market_regime(prices) == 'volatile'

def test_long_trending():
    prices = pd.Series(range(100))
    assert classify_market_regime(prices) == 'trending'
