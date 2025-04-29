import pandas as pd
import numpy as np
from collections import defaultdict

# --- ATR Calculation Utility ---
def calculate_atr(data: pd.DataFrame, window: int = 14):
    """
    Calculate the Average True Range (ATR) for a DataFrame with columns 'high', 'low', 'close'.
    If 'high' and 'low' are missing, raise ValueError (no fallback to std).
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
        raise ValueError("ATR calculation requires 'high' and 'low' columns in data.")
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
    Returns a dict of metrics for report generation with 'strategy' and 'benchmark' keys.
    """
    def _metrics(eq_curve, tlog):
        eq = np.array(eq_curve)
        ret = (eq[-1] - eq[0]) / eq[0] if len(eq) > 1 else 0
        returns = np.diff(eq) / eq[:-1] if len(eq) > 1 else np.array([0])
        sharpe = float(np.mean(returns) / np.std(returns) * np.sqrt(252)) if np.std(returns) > 0 else 0.0
        running_max = np.maximum.accumulate(eq)
        drawdowns = (eq - running_max) / running_max
        max_drawdown = float(drawdowns.min()) if len(drawdowns) > 0 else 0.0
        pnls = [t['pnl'] for t in tlog if 'pnl' in t] if tlog else []
        avg_win = float(np.mean([p for p in pnls if p > 0])) if any(p > 0 for p in pnls) else 0.0
        avg_loss = float(np.mean([p for p in pnls if p < 0])) if any(p < 0 for p in pnls) else 0.0
        largest_win = float(np.max(pnls)) if pnls else 0.0
        largest_loss = float(np.min(pnls)) if pnls else 0.0
        profit_factor = float(sum(p for p in pnls if p > 0) / abs(sum(p for p in pnls if p < 0))) if any(p < 0 for p in pnls) else (float('inf') if any(p > 0 for p in pnls) else 0.0)
        win_rate = float(sum(p > 0 for p in pnls) / len(pnls)) if pnls else 0.0
        expectancy = float(np.mean(pnls)) if pnls else 0.0
        return {
            'total_return': ret,
            'sharpe_ratio': sharpe,
            'max_drawdown': max_drawdown,
            'win_rate': win_rate,
            'average_win': avg_win,
            'average_loss': avg_loss,
            'largest_win': largest_win,
            'largest_loss': largest_loss,
            'profit_factor': profit_factor,
            'expectancy': expectancy,
        }
    metrics = {}
    metrics['strategy'] = _metrics(equity_curve, trade_log)
    if benchmark_equity_curve is not None:
        metrics['benchmark'] = _metrics(benchmark_equity_curve, trade_log)
    return metrics

def correlate_performance_with_regimes(trade_log):
    # Group trades by regime and calculate stats, always include all keys
    from collections import defaultdict
    import numpy as np
    regime_stats = defaultdict(list)
    for t in trade_log:
        regime = t.get('regime', 'Unknown')
        regime_stats[regime].append(t)
    output = {}
    for regime, trades in regime_stats.items():
        pnls = [t.get('pnl', 0.0) for t in trades]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p < 0]
        output[regime] = {
            'count': len(trades),
            'win_rate': float(len(wins)) / len(trades) if trades else 0.0,
            'average_win': float(np.mean(wins)) if wins else 0.0,
            'average_loss': float(np.mean(losses)) if losses else 0.0,
            'largest_win': float(np.max(wins)) if wins else 0.0,
            'largest_loss': float(np.min(losses)) if losses else 0.0,
            'profit_factor': float(sum(wins) / abs(sum(losses))) if losses else (float('inf') if wins else 0.0),
            'expectancy': float(np.mean(pnls)) if pnls else 0.0,
            'mean_pnl': float(np.mean(pnls)) if pnls else 0.0,
        }
    # Ensure all regimes in output have all keys, even if empty
    all_keys = ['count', 'win_rate', 'average_win', 'average_loss', 'largest_win', 'largest_loss', 'profit_factor', 'expectancy', 'mean_pnl']
    for regime in output:
        for k in all_keys:
            if k not in output[regime]:
                output[regime][k] = 0.0
    return output

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

calculate_indicator_summary_stats = calculate_indicator_summary_stats

def extract_drawdown_periods(equity_curve):
    """
    Given an equity curve (list or np.array), return a list of dicts:
    [{'start': i, 'end': j, 'drawdown': float, 'depth': float, 'recovery': bool}, ...]
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
            periods.append({'start': start, 'end': end, 'drawdown': dd, 'depth': dd, 'recovery': True})
    # If drawdown never recovered
    if in_drawdown and start is not None:
        end = len(drawdowns) - 1
        dd = drawdowns[start:end+1].min()
        periods.append({'start': start, 'end': end, 'drawdown': dd, 'depth': dd, 'recovery': False})
    return periods
