import pandas as pd
from tech_analysis.market_regimes import classify_market_regime

def sma_crossover_backtest(data: pd.DataFrame, short_window: int, long_window: int):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    trades = []
    position = None
    prev_short = data['sma_short'].shift(1)
    prev_long = data['sma_long'].shift(1)
    for idx, row in data.iterrows():
        # Only check crossover if not at the first row
        if pd.isna(prev_short.loc[idx]) or pd.isna(prev_long.loc[idx]):
            continue
        # Buy: previous short <= long and now short > long
        if prev_short.loc[idx] <= prev_long.loc[idx] and row['sma_short'] > row['sma_long'] and position != 'long':
            trades.append({'action': 'buy', 'index': idx})
            position = 'long'
        # Sell: previous short >= long and now short < long
        elif prev_short.loc[idx] >= prev_long.loc[idx] and row['sma_short'] < row['sma_long'] and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            position = None
    return trades

def apply_transaction_costs(entry_price, exit_price, commission=0.0, slippage=0.0):
    # Apply slippage: entry worse by +slippage, exit worse by -slippage
    adj_entry = entry_price + slippage if entry_price is not None else None
    adj_exit = exit_price - slippage if exit_price is not None else None
    gross_pnl = (adj_exit - adj_entry) if adj_entry is not None and adj_exit is not None else 0
    commission_cost = commission * (adj_entry + adj_exit) if commission and adj_entry is not None and adj_exit is not None else 0
    net_pnl = gross_pnl - commission_cost
    return adj_entry, adj_exit, net_pnl, commission_cost

def sma_crossover_backtest_with_log(data: pd.DataFrame, short_window: int, long_window: int, strategy_params: dict):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()
    # ATR window: use long_window or 14 as default
    atr_window = strategy_params.get('atr_window', max(long_window, 14))
    data['atr'] = calculate_atr(data, window=atr_window)

    commission = strategy_params.get('commission', 0.0)
    slippage = strategy_params.get('slippage', 0.0)

    trades = []
    trade_log = []
    position = None
    entry_index = None
    entry_price = None
    entry_volatility = None
    entry_volume = None
    entry_regime = None
    entry_atr = None
    prev_short = data['sma_short'].shift(1)
    prev_long = data['sma_long'].shift(1)
    for idx, row in data.iterrows():
        if pd.isna(prev_short.loc[idx]) or pd.isna(prev_long.loc[idx]):
            continue
        # Buy
        if prev_short.loc[idx] <= prev_long.loc[idx] and row['sma_short'] > row['sma_long'] and position != 'long':
            trades.append({'action': 'buy', 'index': idx})
            position = 'long'
            entry_index = idx
            entry_price = row['close']
            # Market context at entry
            context_window = strategy_params.get('context_window', 10)
            price_window = data['close'].iloc[max(0, data.index.get_loc(idx)-context_window):data.index.get_loc(idx)+1]
            entry_regime = classify_market_regime(price_window)
            entry_volatility = price_window.std()
            entry_volume = row['volume'] if 'volume' in data.columns else 0
            entry_atr = row['atr'] if 'atr' in data.columns else 0
        # Sell
        elif prev_short.loc[idx] >= prev_long.loc[idx] and row['sma_short'] < row['sma_long'] and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            exit_index = idx
            exit_price = row['close']
            adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(entry_price, exit_price, commission, slippage)
            # Market context at exit
            context_window = strategy_params.get('context_window', 10)
            price_window = data['close'].iloc[max(0, data.index.get_loc(idx)-context_window):data.index.get_loc(idx)+1]
            regime = classify_market_regime(price_window)
            volatility = price_window.std()
            volume = row['volume'] if 'volume' in data.columns else 0
            trade_log.append({
                'entry_index': entry_index,
                'exit_index': exit_index,
                'entry_price': adj_entry,
                'exit_price': adj_exit,
                'pnl': net_pnl,
                'commission_cost': commission_cost,
                'regime': regime,
                'volatility': volatility,
                'volume': volume,
                'entry_sma_short': data.loc[entry_index, 'sma_short'] if entry_index is not None else None,
                'entry_sma_long': data.loc[entry_index, 'sma_long'] if entry_index is not None else None,
                'exit_sma_short': data.loc[exit_index, 'sma_short'] if exit_index is not None else None,
                'exit_sma_long': data.loc[exit_index, 'sma_long'] if exit_index is not None else None,
                'rationale': f"{'Buy' if net_pnl > 0 else 'Sell'}: short SMA {'crossed above' if net_pnl > 0 else 'crossed below'} long SMA at index {entry_index if net_pnl > 0 else exit_index}",
                'atr_entry': entry_atr,
                'volume_entry': entry_volume
            })
            position = None
            entry_index = None
            entry_price = None
            entry_volatility = None
            entry_volume = None
            entry_regime = None
            entry_atr = None
    return trades, trade_log

def rsi_strategy_backtest(data: pd.DataFrame, period: int, overbought: float, oversold: float, strategy_params: dict = None):
    data = data.copy()
    delta = data['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    data['rsi'] = 100 - (100 / (1 + rs))
    signals = []
    trade_log = []
    position = None
    entry_index = None
    entry_price = None
    commission = 0.0
    slippage = 0.0
    if strategy_params:
        commission = strategy_params.get('commission', 0.0)
        slippage = strategy_params.get('slippage', 0.0)
    for idx, row in data.iterrows():
        if row['rsi'] < oversold and position != 'long':
            signals.append({'action': 'buy', 'index': idx})
            position = 'long'
            entry_index = idx
            entry_price = row['close']
        elif row['rsi'] > overbought and position == 'long':
            signals.append({'action': 'sell', 'index': idx})
            exit_index = idx
            exit_price = row['close']
            adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(entry_price, exit_price, commission, slippage)
            trade_log.append({
                'entry_index': entry_index,
                'exit_index': exit_index,
                'entry_price': adj_entry,
                'exit_price': adj_exit,
                'pnl': net_pnl,
                'commission_cost': commission_cost,
                'rationale': f"{'Buy' if net_pnl > 0 else 'Sell'}: RSI strategy trade"
            })
            position = None
            entry_index = None
            entry_price = None
    return signals, trade_log

def calculate_performance_metrics(equity_curve, trade_log, benchmark_equity_curve=None):
    import numpy as np
    def _calc_metrics(curve, log):
        curve = np.array(curve)
        total_return = (curve[-1] / curve[0]) - 1 if len(curve) > 1 else 0.0
        wins = [trade.get('PnL', trade.get('pnl', 0)) for trade in log if trade.get('PnL', trade.get('pnl', 0)) > 0]
        losses = [trade.get('PnL', trade.get('pnl', 0)) for trade in log if trade.get('PnL', trade.get('pnl', 0)) < 0]
        win_rate = len(wins) / len(log) if log else 0.0
        avg_win = np.mean(wins) if wins else 0.0
        avg_loss = np.mean(losses) if losses else 0.0
        largest_win = np.max(wins) if wins else 0.0
        largest_loss = np.min(losses) if losses else 0.0
        profit_factor = (np.sum(wins) / abs(np.sum(losses))) if losses else float('inf') if wins else 0.0
        expectancy = (avg_win * win_rate + avg_loss * (1 - win_rate)) if log else 0.0
        returns = np.diff(curve) / curve[:-1]
        mean_ret = returns.mean() if len(returns) > 0 else 0.0
        std_ret = returns.std(ddof=1) if len(returns) > 1 else 1e-10
        sharpe_ratio = (mean_ret / std_ret) * np.sqrt(252) if std_ret > 0 else 0.0
        running_max = np.maximum.accumulate(curve)
        drawdowns = (curve - running_max) / running_max
        max_drawdown = drawdowns.min() if len(drawdowns) > 0 else 0.0
        return {
            'total_return': total_return,
            'win_rate': win_rate,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': abs(max_drawdown),
            'average_win': avg_win,
            'average_loss': avg_loss,
            'largest_win': largest_win,
            'largest_loss': largest_loss,
            'profit_factor': profit_factor,
            'expectancy': expectancy,
        }
    result = {'strategy': _calc_metrics(equity_curve, trade_log)}
    if benchmark_equity_curve is not None:
        result['benchmark'] = _calc_metrics(benchmark_equity_curve, [])
    return result

def correlate_performance_with_regimes(trade_log):
    """
    Groups trades by regime and summarizes mean PnL, count, avg win/loss, largest win/loss, profit factor, expectancy per regime.
    Returns dict: {regime: {...}}
    """
    from collections import defaultdict
    import numpy as np
    regime_trades = defaultdict(list)
    for trade in trade_log:
        regime = trade.get('regime')
        pnl = trade.get('PnL', trade.get('pnl', 0))
        regime_trades[regime].append(pnl)
    result = {}
    for regime, pnls in regime_trades.items():
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p < 0]
        win_rate = len(wins) / len(pnls) if pnls else 0.0
        avg_win = np.mean(wins) if wins else 0.0
        avg_loss = np.mean(losses) if losses else 0.0
        largest_win = np.max(wins) if wins else 0.0
        largest_loss = np.min(losses) if losses else 0.0
        profit_factor = (np.sum(wins) / abs(np.sum(losses))) if losses else float('inf') if wins else 0.0
        expectancy = (avg_win * win_rate + avg_loss * (1 - win_rate)) if pnls else 0.0
        result[regime] = {
            'mean_pnl': np.mean(pnls) if pnls else 0.0,
            'count': len(pnls),
            'win_rate': win_rate,
            'average_win': avg_win,
            'average_loss': avg_loss,
            'largest_win': largest_win,
            'largest_loss': largest_loss,
            'profit_factor': profit_factor,
            'expectancy': expectancy,
        }
    return result

def export_backtest_results(trade_log, metrics, output_path):
    """
    Export trade log and metrics to a JSON file for report generation.
    """
    import json
    with open(output_path, 'w') as f:
        json.dump({'trade_log': trade_log, 'metrics': metrics}, f)

def portfolio_backtest(data_dict, initial_cash, position_size, strategy_params):
    """
    Unified portfolio-level backtest for multiple tickers, time-based iteration, buy preference, no short selling, rationale logging.
    data_dict: dict of ticker -> pd.DataFrame with 'close' column
    Returns: {'portfolio_state': PortfolioState, 'trade_log': list, 'strategy_params': dict}
    """
    if strategy_params is None:
        raise ValueError("strategy_params must be provided (from config.json)")
    from tech_analysis.portfolio import PortfolioState
    pf = PortfolioState(initial_cash, strategy_params=strategy_params)
    trade_log = []
    max_len = max(len(df) for df in data_dict.values())
    tickers = list(data_dict.keys())
    open_positions = {ticker: None for ticker in tickers}  # Track open positions per ticker
    commission = strategy_params.get('commission', 0.0)
    slippage = strategy_params.get('slippage', 0.0)
    for i in range(1, max_len):
        price_dict = {ticker: data_dict[ticker]['close'].iloc[i] if i < len(data_dict[ticker]) else data_dict[ticker]['close'].iloc[-1] for ticker in tickers}
        for ticker in tickers:
            df = data_dict[ticker]
            if i >= len(df):
                continue
            prev_close = df['close'].iloc[i-1]
            curr_close = df['close'].iloc[i]
            # Entry condition: price increases
            if curr_close > prev_close:
                price = curr_close
                qty = int(position_size // price)
                if qty > 0 and pf.cash >= qty * price and open_positions[ticker] is None:
                    pf.buy(
                        ticker,
                        qty,
                        price,
                        rationale=f"Buy: {ticker} close {curr_close} > prev {prev_close} at idx {i}"
                    )
                    context_window = strategy_params.get('context_window', 10) # Get from params, default 10
                    price_window = df['close'].iloc[max(0, i-context_window):i+1]
                    regime = classify_market_regime(price_window)
                    open_positions[ticker] = {
                        'EntryTime': str(df.index[i]),
                        'EntryPrice': price,
                        'PositionSize': qty,
                        'Rationale': f"Buy: {ticker} close {curr_close} > prev {prev_close} at idx {i}",
                        'regime': regime
                    }
            # Exit condition: price decreases and position is open
            elif curr_close < prev_close and open_positions[ticker] is not None:
                price = curr_close
                qty = open_positions[ticker]['PositionSize']
                pf.sell(
                    ticker,
                    qty,
                    price,
                    rationale=f"Sell: {ticker} close {curr_close} < prev {prev_close} at idx {i}"
                )
                entry = open_positions[ticker]
                adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(entry['EntryPrice'], price, commission, slippage)
                trade_log.append({
                    'action': 'buy',
                    'ticker': ticker,
                    'qty': qty,
                    'EntryTime': entry['EntryTime'],
                    'EntryPrice': adj_entry,
                    'ExitTime': str(df.index[i]),
                    'ExitPrice': adj_exit,
                    'PositionSize': qty,
                    'PnL': net_pnl,
                    'commission_cost': commission_cost,
                    'rationale': f"{entry['Rationale']} | Sell: {ticker} close {curr_close} < prev {prev_close} at idx {i}",
                    'regime': entry['regime']
                })
                open_positions[ticker] = None
        pf.update_equity(price_dict)
    # At the end, close any open positions at last price
    for ticker in tickers:
        if open_positions[ticker] is not None:
            df = data_dict[ticker]
            last_idx = len(df) - 1
            price = df['close'].iloc[last_idx]
            entry = open_positions[ticker]
            qty = entry['PositionSize']
            pf.sell(
                ticker,
                qty,
                price,
                rationale=f"Sell (forced exit at end): {ticker} close {price} at idx {last_idx}"
            )
            adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(entry['EntryPrice'], price, commission, slippage)
            trade_log.append({
                'action': 'buy',
                'ticker': ticker,
                'qty': qty,
                'EntryTime': entry['EntryTime'],
                'EntryPrice': adj_entry,
                'ExitTime': str(df.index[last_idx]),
                'ExitPrice': adj_exit,
                'PositionSize': qty,
                'PnL': net_pnl,
                'commission_cost': commission_cost,
                'rationale': f"{entry['Rationale']} | Sell (forced exit at end): {ticker} close {price} at idx {last_idx}",
                'regime': entry['regime']
            })
            open_positions[ticker] = None
    # Explicitly list all assets traded
    return {'portfolio_state': pf, 'trade_log': trade_log, 'strategy_params': strategy_params, 'assets': tickers}

# Utility to load config and fetch data with timeframe/frequency
import json
import os
from tech_analysis.data.fetcher import fetch_all_stocks_data

def load_config():
    # Always resolve config.json relative to project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(project_root, 'config.json')
    with open(config_path, 'r') as f:
        cfg = json.load(f)
    return cfg

# Example utility to get data for backtests using new config fields
def get_data_for_backtest():
    cfg = load_config()
    return fetch_all_stocks_data(
        period=cfg.get('period'),
        start_date=cfg.get('start_date'),
        end_date=cfg.get('end_date'),
        frequency=cfg.get('frequency')
    )

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

# --- Indicator Summary Stats ---
def calculate_indicator_summary_stats(trade_log):
    import numpy as np
    fields = ['atr_entry', 'volume_entry']
    stats = {}
    for field in fields:
        values = [trade.get(field, 0) for trade in trade_log if field in trade]
        stats[field] = {
            'mean': float(np.mean(values)) if values else 0.0,
            'min': float(np.min(values)) if values else 0.0,
            'max': float(np.max(values)) if values else 0.0
        }
    return stats
