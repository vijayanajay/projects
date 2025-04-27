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

def sma_crossover_backtest_with_log(data: pd.DataFrame, short_window: int, long_window: int):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    trades = []
    trade_log = []
    position = None
    entry_index = None
    entry_price = None
    entry_volatility = None
    entry_volume = None
    entry_regime = None
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
            price_window = data['close'].iloc[max(0, data.index.get_loc(idx)-10):data.index.get_loc(idx)+1]
            entry_regime = classify_market_regime(price_window)
            entry_volatility = price_window.std()
            entry_volume = row['volume'] if 'volume' in data.columns else 0
        # Sell
        elif prev_short.loc[idx] >= prev_long.loc[idx] and row['sma_short'] < row['sma_long'] and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            exit_index = idx
            exit_price = row['close']
            pnl = exit_price - entry_price if entry_price is not None else 0
            # Market context at exit
            price_window = data['close'].iloc[max(0, data.index.get_loc(idx)-10):data.index.get_loc(idx)+1]
            regime = classify_market_regime(price_window)
            volatility = price_window.std()
            volume = row['volume'] if 'volume' in data.columns else 0
            trade_log.append({
                'entry_index': entry_index,
                'exit_index': exit_index,
                'entry_price': entry_price,
                'exit_price': exit_price,
                'pnl': pnl,
                'regime': regime,
                'volatility': volatility,
                'volume': volume,
                'entry_sma_short': data.loc[entry_index, 'sma_short'] if entry_index is not None else None,
                'entry_sma_long': data.loc[entry_index, 'sma_long'] if entry_index is not None else None,
                'exit_sma_short': data.loc[exit_index, 'sma_short'] if exit_index is not None else None,
                'exit_sma_long': data.loc[exit_index, 'sma_long'] if exit_index is not None else None,
                'rationale': f"{'Buy' if pnl > 0 else 'Sell'}: short SMA {'crossed above' if pnl > 0 else 'crossed below'} long SMA at index {entry_index if pnl > 0 else exit_index}"
            })
            position = None
            entry_index = None
            entry_price = None
            entry_volatility = None
            entry_volume = None
            entry_regime = None
    return trades, trade_log

def rsi_strategy_backtest(data: pd.DataFrame, period: int, overbought: float, oversold: float):
    data = data.copy()
    # Calculate RSI
    delta = data['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / (avg_loss + 1e-10)  # avoid div by zero
    data['rsi'] = 100 - (100 / (1 + rs))

    trades = []
    position = None
    for idx in range(1, len(data)):
        prev_rsi = data['rsi'].iloc[idx-1]
        curr_rsi = data['rsi'].iloc[idx]
        # Buy: prev RSI <= oversold, now RSI > oversold
        if prev_rsi <= oversold and curr_rsi > oversold and position != 'long':
            trades.append({'action': 'buy', 'index': idx})
            position = 'long'
        # Sell: prev RSI >= overbought, now RSI < overbought
        elif prev_rsi >= overbought and curr_rsi < overbought and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            position = None
    return trades

def calculate_performance_metrics(equity_curve, trade_log):
    import numpy as np
    equity_curve = np.array(equity_curve)
    # Total return
    total_return = (equity_curve[-1] / equity_curve[0]) - 1 if len(equity_curve) > 1 else 0.0
    # Win rate
    wins = sum(1 for trade in trade_log if (trade.get('PnL', trade.get('pnl', 0)) > 0))
    win_rate = wins / len(trade_log) if trade_log else 0.0
    # Daily returns (assume 1 step per day for simplicity)
    returns = np.diff(equity_curve) / equity_curve[:-1]
    mean_ret = returns.mean() if len(returns) > 0 else 0.0
    std_ret = returns.std(ddof=1) if len(returns) > 1 else 1e-10
    sharpe_ratio = (mean_ret / std_ret) * np.sqrt(252) if std_ret > 0 else 0.0
    # Max drawdown
    running_max = np.maximum.accumulate(equity_curve)
    drawdowns = (equity_curve - running_max) / running_max
    max_drawdown = drawdowns.min() if len(drawdowns) > 0 else 0.0
    return {
        'total_return': total_return,
        'win_rate': win_rate,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': abs(max_drawdown),
    }

def export_backtest_results(trade_log, metrics, output_path):
    """
    Export trade log and metrics to a JSON file for report generation.
    """
    import json
    with open(output_path, 'w') as f:
        json.dump({'trade_log': trade_log, 'metrics': metrics}, f)

def correlate_performance_with_regimes(trade_log):
    """
    Groups trades by regime and summarizes mean PnL and count per regime.
    Returns dict: {regime: {'mean_pnl': float, 'count': int}}
    """
    from collections import defaultdict
    regime_pnls = defaultdict(list)
    for trade in trade_log:
        regime = trade.get('regime')
        pnl = trade.get('pnl', 0)
        regime_pnls[regime].append(pnl)
    result = {}
    for regime, pnls in regime_pnls.items():
        result[regime] = {'mean_pnl': sum(pnls)/len(pnls) if pnls else 0, 'count': len(pnls)}
    return result

def portfolio_backtest(data_dict, initial_cash=10000, position_size=100, strategy_params=None):
    """
    Unified portfolio-level backtest for multiple tickers, time-based iteration, buy preference, no short selling, rationale logging.
    data_dict: dict of ticker -> pd.DataFrame with 'close' column
    Returns: {'portfolio_state': PortfolioState, 'trade_log': list, 'strategy_params': dict}
    """
    if strategy_params is None:
        strategy_params = {
            'strategy': 'naive_momentum',
            'rule': 'buy if price increases',
            'position_size': position_size,
            'initial_cash': initial_cash,
        }
    from tech_analysis.portfolio import PortfolioState
    pf = PortfolioState(initial_cash, strategy_params=strategy_params)
    trade_log = []
    max_len = max(len(df) for df in data_dict.values())
    tickers = list(data_dict.keys())
    open_positions = {ticker: None for ticker in tickers}  # Track open positions per ticker
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
                    price_window = df['close'].iloc[max(0, i-10):i+1]
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
                pnl = (price - entry['EntryPrice']) * qty
                trade_log.append({
                    'action': 'buy',
                    'ticker': ticker,
                    'qty': qty,
                    'EntryTime': entry['EntryTime'],
                    'EntryPrice': entry['EntryPrice'],
                    'ExitTime': str(df.index[i]),
                    'ExitPrice': price,
                    'PositionSize': qty,
                    'PnL': pnl,
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
            pnl = (price - entry['EntryPrice']) * qty
            trade_log.append({
                'action': 'buy',
                'ticker': ticker,
                'qty': qty,
                'EntryTime': entry['EntryTime'],
                'EntryPrice': entry['EntryPrice'],
                'ExitTime': str(df.index[last_idx]),
                'ExitPrice': price,
                'PositionSize': qty,
                'PnL': pnl,
                'rationale': f"{entry['Rationale']} | Sell (forced exit at end): {ticker} close {price} at idx {last_idx}",
                'regime': entry['regime']
            })
            open_positions[ticker] = None
    return {'portfolio_state': pf, 'trade_log': trade_log, 'strategy_params': strategy_params}
