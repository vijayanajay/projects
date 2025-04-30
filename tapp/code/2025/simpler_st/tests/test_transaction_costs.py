import pytest
from tech_analysis.utils import apply_transaction_costs
from tech_analysis.backtest import sma_crossover_backtest_with_log, rsi_strategy_backtest
import pandas as pd

def test_apply_transaction_costs_basic():
    # No costs
    adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(100, 110, commission=0.0, slippage=0.0)
    assert adj_entry == 100 and adj_exit == 110
    assert net_pnl == 10
    assert commission_cost == 0
    # With commission only
    adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(100, 110, commission=0.01, slippage=0.0)
    assert adj_entry == 100 and adj_exit == 110
    assert commission_cost == 2.1  # 1% of (100+110)
    assert net_pnl == 10 - 2.1
    # With slippage only
    adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(100, 110, commission=0.0, slippage=0.5)
    assert adj_entry == 100.5 and adj_exit == 109.5
    assert net_pnl == 109.5 - 100.5
    # With both
    adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(100, 110, commission=0.01, slippage=0.5)
    assert adj_entry == 100.5 and adj_exit == 109.5
    assert commission_cost == pytest.approx(2.1, rel=1e-6)
    assert net_pnl == pytest.approx((109.5-100.5) - 2.1, rel=1e-6)

def test_sma_crossover_backtest_with_log_costs():
    # Simple price series with one crossover
    data = pd.DataFrame({
        'close': [100, 102, 104, 106, 104, 102, 100, 98, 96, 94, 96, 98, 100, 102, 104, 106],
        'volume': [1000]*16,
        'high': [101, 103, 105, 107, 105, 103, 101, 99, 97, 95, 97, 99, 101, 103, 105, 107],
        'low': [99, 101, 103, 105, 103, 101, 99, 97, 95, 93, 95, 97, 99, 101, 103, 105]
    })
    short_window = 2
    long_window = 3
    strategy_params = {'commission': 0.01, 'slippage': 0.5, 'context_window': 2}
    trades, trade_log = sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)
    # All trade logs should have commission_cost and net pnl reflecting costs
    for trade in trade_log:
        assert 'commission_cost' in trade
        assert 'pnl' in trade
        assert trade['commission_cost'] >= 0
        # PnL must be less than gross (i.e., costs are deducted)
        gross = (trade['exit_price'] - trade['entry_price']) if trade['entry_price'] is not None and trade['exit_price'] is not None else 0
        assert trade['pnl'] <= gross

def test_rsi_strategy_backtest_costs():
    data = pd.DataFrame({'close': [100, 99, 98, 97, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]})
    period = 2
    overbought = 70
    oversold = 30
    strategy_params = {'commission': 0.02, 'slippage': 1.0}
    signals, trade_log = rsi_strategy_backtest(data, period, overbought, oversold, strategy_params)
    for trade in trade_log:
        assert 'commission_cost' in trade
        assert 'pnl' in trade
        assert trade['commission_cost'] >= 0
        gross = (trade['exit_price'] - trade['entry_price']) if trade['entry_price'] is not None and trade['exit_price'] is not None else 0
        assert trade['pnl'] <= gross
