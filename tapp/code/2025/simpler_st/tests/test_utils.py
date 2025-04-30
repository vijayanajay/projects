import pandas as pd
import numpy as np
import pytest
from tech_analysis.utils import calculate_atr, apply_transaction_costs, calculate_performance_metrics, correlate_performance_with_regimes, calculate_indicator_summary_stats, extract_drawdown_periods

def test_calculate_atr_basic():
    # Simple price data
    data = pd.DataFrame({
        'high': [10, 12, 13, 15, 14],
        'low': [8, 9, 10, 12, 13],
        'close': [9, 11, 12, 14, 13]
    })
    atr = calculate_atr(data, window=3)
    assert isinstance(atr, pd.Series)
    # ATR should be the same length as input
    assert len(atr) == len(data)
    # ATR should not be all zeros or all NaN
    assert not np.all(atr == 0)
    assert not atr.isnull().all()

def test_apply_transaction_costs_basic():
    # Simple case: entry=100, exit=110, commission=0.01, slippage=1
    adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(100, 110, commission=0.01, slippage=1)
    # Entry should be 101, exit should be 109
    assert adj_entry == 101
    assert adj_exit == 109
    # Gross PnL: 8, Commission: 0.01*(101+109)=2.1, Net PnL: 5.9
    assert abs(net_pnl - 5.9) < 1e-6
    assert abs(commission_cost - 2.1) < 1e-6

def test_calculate_performance_metrics_basic():
    equity_curve = [100, 110, 120, 115, 130]
    trade_log = [
        {'pnl': 10},
        {'pnl': 10},
        {'pnl': -5},
        {'pnl': 15}
    ]
    metrics = calculate_performance_metrics(equity_curve, trade_log)
    assert isinstance(metrics, dict)
    # Should contain 'strategy' key with subfields for return, Sharpe, and drawdown
    assert 'strategy' in metrics
    strat = metrics['strategy']
    assert 'total_return' in strat
    assert 'sharpe_ratio' in strat
    assert 'max_drawdown' in strat

def test_correlate_performance_with_regimes_basic():
    trade_log = [
        {'regime': 'Trending', 'pnl': 10},
        {'regime': 'Trending', 'pnl': -5},
        {'regime': 'Ranging', 'pnl': 7},
        {'regime': 'Ranging', 'pnl': 3},
        {'regime': 'Volatile', 'pnl': -2}
    ]
    result = correlate_performance_with_regimes(trade_log)
    assert isinstance(result, dict)
    assert 'Trending' in result
    assert 'Ranging' in result
    assert 'Volatile' in result
    # Should contain mean_pnl and count for each regime
    for regime in ['Trending', 'Ranging', 'Volatile']:
        assert 'mean_pnl' in result[regime]
        assert 'count' in result[regime]

def test_calculate_indicator_summary_stats_basic():
    df = pd.DataFrame({
        'sma_short': [1, 2, 3, 4, 5],
        'sma_long': [2, 3, 4, 5, 6]
    })
    summary = calculate_indicator_summary_stats(df, ['sma_short', 'sma_long'])
    assert isinstance(summary, dict)
    assert 'sma_short' in summary and 'sma_long' in summary
    for k in ['mean', 'std', 'min', 'max']:
        assert k in summary['sma_short']
        assert k in summary['sma_long']

def test_extract_drawdown_periods_basic():
    eq = [100, 120, 110, 105, 130, 125, 140]
    periods = extract_drawdown_periods(eq)
    assert isinstance(periods, list)
    # At least one drawdown period should be detected
    assert any(p['drawdown'] < 0 for p in periods)
    for p in periods:
        assert 'start' in p and 'end' in p and 'drawdown' in p

# Optionally, more edge cases can be added after minimal extraction
