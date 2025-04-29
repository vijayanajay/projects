import pandas as pd
import numpy as np
from collections import defaultdict

# --- ATR Calculation Utility ---
def calculate_atr(data: pd.DataFrame, window: int = 14):
    """
    Calculate the Average True Range (ATR) for a DataFrame with columns 'high', 'low', 'close'.
    If 'high' and 'low' are missing, fallback to use 'close' only (ATR=rolling std).
    """
    if all(col in data.columns for col in ['high', 'low', 'close']):
        high = data['high']
        low = data['low']
        close = data['close']
        prev_close = close.shift(1)
        tr = pd.concat([
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs()
        ], axis=1).max(axis=1)
        atr = tr.rolling(window=window, min_periods=1).mean()
    else:
        # Fallback: rolling std as proxy
        atr = data['close'].rolling(window=window, min_periods=1).std()
    return atr

def apply_transaction_costs(entry_price, exit_price, commission=0.0, slippage=0.0):
    # Apply slippage: entry worse by +slippage, exit worse by -slippage
    adj_entry = entry_price + slippage if entry_price is not None else None
    adj_exit = exit_price - slippage if exit_price is not None else None
    gross_pnl = (adj_exit - adj_entry) if adj_entry is not None and adj_exit is not None else 0
    commission_cost = commission * (adj_entry + adj_exit) if commission and adj_entry is not None and adj_exit is not None else 0
    net_pnl = gross_pnl - commission_cost
    return adj_entry, adj_exit, net_pnl, commission_cost

def calculate_performance_metrics(equity_curve, trade_log, benchmark_equity_curve=None):
    """
    Compute return, Sharpe ratio, max drawdown, and other metrics for the given equity curve and trade log.
    Optionally compare to a benchmark equity curve.
    Returns a dict of metrics for report generation.
    """
    eq = np.array(equity_curve)
    ret = (eq[-1] - eq[0]) / eq[0] * 100 if len(eq) > 1 else 0
    returns = np.diff(eq) / eq[:-1] if len(eq) > 1 else np.array([0])
    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252) if np.std(returns) > 0 else 0
    # Max drawdown
    running_max = np.maximum.accumulate(eq)
    drawdowns = (eq - running_max) / running_max
    max_drawdown = drawdowns.min() * 100 if len(drawdowns) > 0 else 0
    metrics = {
        'Return [%]': ret,
        'Sharpe Ratio': sharpe,
        'Max. Drawdown [%]': max_drawdown,
    }
    if trade_log:
        pnls = [t['pnl'] for t in trade_log if 'pnl' in t]
        metrics['Avg Trade PnL'] = np.mean(pnls) if pnls else 0
        metrics['Win Rate [%]'] = 100 * sum(p > 0 for p in pnls) / len(pnls) if pnls else 0
    if benchmark_equity_curve is not None:
        bench = np.array(benchmark_equity_curve)
        bench_ret = (bench[-1] - bench[0]) / bench[0] * 100 if len(bench) > 1 else 0
        metrics['Benchmark Return [%]'] = bench_ret
    return metrics

def correlate_performance_with_regimes(trade_log):
    """
    Groups trades by regime and summarizes mean PnL, count, avg win/loss, largest win/loss, profit factor, expectancy per regime.
    Returns a dict keyed by regime.
    """
    regime_stats = defaultdict(list)
    for trade in trade_log:
        if 'regime' in trade and 'pnl' in trade:
            regime_stats[trade['regime']].append(trade['pnl'])
    summary = {}
    for regime, pnls in regime_stats.items():
        arr = np.array(pnls)
        summary[regime] = {
            'mean_pnl': arr.mean() if len(arr) > 0 else 0,
            'count': len(arr),
            'avg_win': arr[arr > 0].mean() if np.any(arr > 0) else 0,
            'avg_loss': arr[arr < 0].mean() if np.any(arr < 0) else 0,
            'largest_win': arr.max() if len(arr) > 0 else 0,
            'largest_loss': arr.min() if len(arr) > 0 else 0,
            'profit_factor': arr[arr > 0].sum() / abs(arr[arr < 0].sum()) if np.any(arr < 0) else float('inf') if np.any(arr > 0) else 0,
            'win_rate': 100 * np.sum(arr > 0) / len(arr) if len(arr) > 0 else 0,
        }
    return summary

def calculate_indicator_summary_stats(df, indicators):
    """
    For each indicator column, compute mean, std, min, max.
    Returns dict: {indicator: {mean, std, min, max}}
    """
    summary = {}
    for ind in indicators:
        if ind in df.columns:
            vals = df[ind].dropna()
            summary[ind] = {
                'mean': vals.mean(),
                'std': vals.std(),
                'min': vals.min(),
                'max': vals.max(),
            }
    return summary

def extract_drawdown_periods(equity_curve):
    """
    Given an equity curve (list or np.array), return a list of dicts:
    [{'start': i, 'end': j, 'drawdown': float, 'recovery': bool}, ...]
    Each dict represents a drawdown period, with start/end indices, max drawdown, and whether it recovered.
    """
    import numpy as np
    eq = np.array(equity_curve)
    running_max = np.maximum.accumulate(eq)
    drawdowns = (eq - running_max) / running_max
    periods = []
    in_drawdown = False
    start = end = None
    for i, d in enumerate(drawdowns):
        if d < 0 and not in_drawdown:
            in_drawdown = True
            start = i
        elif d == 0 and in_drawdown:
            in_drawdown = False
            end = i - 1
            dd = drawdowns[start:end+1].min()
            periods.append({'start': start, 'end': end, 'drawdown': dd, 'recovery': True})
    # If drawdown never recovered
    if in_drawdown and start is not None:
        end = len(drawdowns) - 1
        dd = drawdowns[start:end+1].min()
        periods.append({'start': start, 'end': end, 'drawdown': dd, 'recovery': False})
    return periods
