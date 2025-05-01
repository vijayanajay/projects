import pandas as pd
import re
import numpy as np
from itertools import product
import copy  # Added for deep copying configurations

def calculate_ema(data, period=2):
    """
    Calculate the Exponential Moving Average (EMA) for a given data series.
    
    Args:
        data (pd.Series): Input data series
        period (int): Period for EMA calculation (default: 2)
        
    Returns:
        pd.Series: EMA values with the same index as input data
    """
    if not isinstance(data, pd.Series):
        raise ValueError("Input data must be a pandas Series")
    
    if period <= 0:
        raise ValueError("Period must be a positive integer")
    
    if len(data) < 1:
        return pd.Series([], dtype="float64")
    
    # If all values are NaN, return a series of NaN
    if data.isnull().all():
        return pd.Series([np.nan] * len(data), index=data.index)
    
    # Calculate EMA using pandas' ewm with alpha=1/period
    ema = data.ewm(alpha=1/period, adjust=False).mean()
    
    # Ensure output is NaN where input is NaN
    ema[data.isnull()] = np.nan
    
    return ema

def calculate_sma(data, period=2):
    """
    Calculate the Simple Moving Average (SMA) for a given data series.
    
    Args:
        data (pd.Series): Input data series
        period (int): Period for SMA calculation (default: 2)
        
    Returns:
        pd.Series: SMA values with the same index as input data
    """
    if not isinstance(data, pd.Series):
        raise ValueError("Input data must be a pandas Series")
    
    if period <= 0:
        raise ValueError("Period must be a positive integer")
    
    if len(data) < 1:
        return pd.Series([], dtype="float64")
    
    # Calculate SMA using pandas' rolling window
    sma = data.rolling(window=period, min_periods=1).mean()
    
    return sma

def generate_crossover_signals(short_sma, long_sma):
    """
    Generate crossover signals based on short and long SMAs.
    
    Args:
        short_sma (pd.Series): Short period SMA values
        long_sma (pd.Series): Long period SMA values
        
    Returns:
        pd.Series: Trading signals (1 for buy, 0 for hold)
    """
    if not (isinstance(short_sma, pd.Series) and isinstance(long_sma, pd.Series)):
        raise ValueError("Both inputs must be pandas Series")
    
    if not short_sma.index.equals(long_sma.index):
        raise ValueError("Input series must have the same index")
    
    signals = pd.Series(0, index=short_sma.index)
    prev_short = short_sma.shift(1, fill_value=short_sma.iloc[0])
    prev_long = long_sma.shift(1, fill_value=long_sma.iloc[0])
    crossover = (short_sma > long_sma) & (prev_short <= prev_long)
    crossover_indices = crossover[crossover].index
    if len(crossover_indices) == 1:
        signals.loc[crossover_indices[0]:] = 1
    else:
        signals[crossover] = 1
    return signals

def validate_configuration(config):
    """
    Validate strategy configuration against required schema.
    
    Args:
        config (dict): Configuration dictionary to validate
        
    Raises:
        ValueError: If configuration doesn't match required schema
    """
    # Check required top-level sections
    if 'data' not in config:
        raise ValueError("Missing required section: data")
    if 'strategy' not in config:
        raise ValueError("Missing required section: strategy")
    
    # Validate data section
    data = config['data']
    for key in ['symbol', 'timeframe', 'lookback_period']:
        if key not in data:
            raise ValueError(f"Missing required data field: {key}")
    
    # Validate symbol (basic string check)
    if not isinstance(data['symbol'], str) or not data['symbol']:
        raise ValueError("Symbol must be a non-empty string")
    
    # Validate timeframe format (e.g., '1d', '1w', '1m', '1y')
    timeframe_pattern = r'^[1-9][0-9]*[dhwmy]$'
    if not re.match(timeframe_pattern, data['timeframe']):
        raise ValueError(f"Invalid timeframe format: {data['timeframe']}. Expected format: {timeframe_pattern}")
    
    # Validate lookback_period (positive integer)
    if not isinstance(data['lookback_period'], (int, float)) or data['lookback_period'] <= 0:
        raise ValueError("Lookback period must be a positive number")
    
    # Validate strategy section
    strategy = config['strategy']
    for key in ['short_sma', 'long_sma', 'risk_ratio']:
        if key not in strategy:
            raise ValueError(f"Missing required strategy field: {key}")
    
    # Validate SMA periods (positive integers)
    for key in ['short_sma', 'long_sma']:
        if not isinstance(strategy[key], (int, float)) or strategy[key] <= 0:
            raise ValueError(f"{key} must be a positive number")
    
    # Validate risk ratio (between 0 and 1)
    risk_ratio = strategy['risk_ratio']
    if not isinstance(risk_ratio, (int, float)) or risk_ratio < 0 or risk_ratio > 1:
        raise ValueError("Risk ratio must be between 0 and 1")

class Backtester:
    """
    Backtest trading strategies against historical data.
    
    Attributes:
        prices (pd.Series): Historical prices
        signals (pd.Series): Trading signals (1 for buy, 0 for hold)
        config (dict): Strategy configuration
    """
    
    def __init__(self, prices, signals, config):
        """
        Initialize the Backtester with strategy parameters.
        
        Args:
            prices (pd.Series): Historical price data
            signals (pd.Series): Trading signals
            config (dict): Strategy configuration
        """
        if not isinstance(prices, pd.Series):
            raise ValueError("Prices must be a pandas Series")
        
        if not isinstance(signals, pd.Series):
            raise ValueError("Signals must be a pandas Series")
        
        if prices.index.size != signals.index.size:
            raise ValueError("Prices and signals must have the same length")
        
        if not prices.index.equals(signals.index):
            raise ValueError("Prices and signals must have the same index")
        
        validate_configuration(config)
        
        self.prices = prices
        self.signals = signals
        self.config = config
        self.trades = []
    
    def run(self):
        """
        Run the backtest and generate performance metrics.
        
        Returns:
            dict: Backtest results including trades and metrics
        """
        self.trades = self._generate_trades()
        
        results = {
            'trades': self.trades,
            'cumulative_returns': self._calculate_cumulative_returns(),
            'sharpe_ratio': self._calculate_sharpe_ratio(),
            'max_drawdown': self._calculate_max_drawdown(),
            'avg_return_per_trade': self._calculate_avg_return_per_trade(),
            'win_rate': self._calculate_win_rate(),
            'avg_holding_period': self._calculate_avg_holding_period(),
            'profit_factor': self._calculate_profit_factor(),
        }
        
        return results
    
    def _generate_trades(self):
        """
        Generate trade history based on signals, applying slippage, commissions, and position sizing.
        Returns:
            list: List of trade dictionaries
        """
        trades = []
        in_position = False
        entry_price = 0
        entry_date = None
        position_size = 0
        # Get config values or defaults
        slippage_pct = self.config.get('slippage_pct', 0.0)
        commission_pct = self.config.get('commission_pct', 0.0)
        risk_ratio = self.config['strategy'].get('risk_ratio', 1.0)
        for date, price in self.prices.items():
            signal = self.signals.loc[date]
            if signal == 1 and not in_position:
                # Buy signal: apply slippage and commission to entry
                entry_price = price * (1 + slippage_pct) * (1 + commission_pct)
                entry_date = date
                position_size = risk_ratio
                in_position = True
            elif signal == 0 and in_position:
                # Sell signal: apply slippage and commission to exit
                exit_price = price * (1 - slippage_pct) * (1 - commission_pct)
                exit_date = date
                abs_profit = (exit_price - entry_price) * position_size
                pct_profit = (exit_price - entry_price) / entry_price
                trade = {
                    'symbol': self.config['data']['symbol'],
                    'entry_date': entry_date,
                    'exit_date': exit_date,
                    'entry_price': entry_price,
                    'exit_price': exit_price,
                    'position_size': position_size,
                    'profit': abs_profit,
                    'return_pct': pct_profit
                }
                trades.append(trade)
                in_position = False
        # Close any open position at the end of the data period
        if in_position:
            exit_price = self.prices.iloc[-1] * (1 - slippage_pct) * (1 - commission_pct)
            exit_date = self.prices.index[-1]
            abs_profit = (exit_price - entry_price) * position_size
            pct_profit = (exit_price - entry_price) / entry_price
            trade = {
                'symbol': self.config['data']['symbol'],
                'entry_date': entry_date,
                'exit_date': exit_date,
                'entry_price': entry_price,
                'exit_price': exit_price,
                'position_size': position_size,
                'profit': abs_profit,
                'return_pct': pct_profit
            }
            trades.append(trade)
        return trades
    
    def _calculate_cumulative_returns(self):
        """
        Calculate cumulative returns from trades.
        
        Returns:
            float: Total cumulative returns
        """
        if not self.trades:
            return 0.0
        
        total_return = sum(trade['return_pct'] for trade in self.trades)
        return total_return
    
    def _calculate_sharpe_ratio(self):
        """
        Calculate the Sharpe ratio of the strategy.
        
        Returns:
            float: Sharpe ratio
        """
        if not self.trades:
            return 0.0
        
        # Calculate daily returns
        daily_returns = pd.Series(index=self.prices.index, dtype='float64')
        
        for trade in self.trades:
            mask = (daily_returns.index >= trade['entry_date']) & (daily_returns.index <= trade['exit_date'])
            daily_returns[mask] = trade['return_pct'] / len(daily_returns[mask])
        
        # Fill NaN values with 0 for days without trades
        daily_returns = daily_returns.fillna(0)
        
        # Calculate Sharpe ratio (assuming risk-free rate of 0)
        if daily_returns.std() == 0:
            return 0.0
        
        sharpe_ratio = daily_returns.mean() / daily_returns.std()
        
        # Annualize the Sharpe ratio (assuming 252 trading days)
        return sharpe_ratio * np.sqrt(252)
    
    def _calculate_max_drawdown(self):
        """
        Calculate the maximum drawdown of the strategy.
        
        Returns:
            float: Maximum drawdown
        """
        if len(self.prices) < 2:
            return 0.0
        
        # Calculate running maximum
        running_max = self.prices.cummax()
        
        # Calculate drawdowns
        drawdowns = (self.prices - running_max) / running_max
        
        # Return the worst (most negative) drawdown
        max_drawdown = drawdowns.min()
        
        return max_drawdown

    def _calculate_avg_return_per_trade(self):
        if not self.trades:
            return 0.0
        return float(np.mean([t['return_pct'] for t in self.trades]))

    def _calculate_win_rate(self):
        if not self.trades:
            return 0.0
        wins = [t for t in self.trades if t['profit'] > 0]
        return float(len(wins)) / len(self.trades) if self.trades else 0.0

    def _calculate_avg_holding_period(self):
        if not self.trades:
            return 0.0
        periods = [(t['exit_date'] - t['entry_date']).days for t in self.trades]
        return float(np.mean(periods)) if periods else 0.0

    def _calculate_profit_factor(self):
        if not self.trades:
            return 0.0
        gross_profit = sum(t['profit'] for t in self.trades if t['profit'] > 0)
        gross_loss = -sum(t['profit'] for t in self.trades if t['profit'] < 0)
        if gross_loss == 0:
            return float('inf') if gross_profit > 0 else 0.0
        return float(gross_profit) / gross_loss

class StrategyOptimizer:
    """
    Optimize strategy parameters based on backtesting results.
    
    Attributes:
        prices (pd.Series): Historical price data
        config_template (dict): Base configuration template
        param_ranges (dict): Parameter ranges for optimization
    """
    
    def __init__(self, prices, config_template, param_ranges):
        """
        Initialize the StrategyOptimizer.
        
        Args:
            prices (pd.Series): Historical price data
            config_template (dict): Base configuration template
            param_ranges (dict): Parameter ranges for optimization
        """
        if not isinstance(prices, pd.Series):
            raise ValueError("Prices must be a pandas Series")
        
        # Moved empty price check to optimize method
        
        if not isinstance(config_template, dict):
            raise ValueError("Config template must be a dictionary")
        
        if not isinstance(param_ranges, dict):
            raise ValueError("Parameter ranges must be a dictionary")
        
        # Validate parameter ranges
        for param_path, values in param_ranges.items():
            if not values:
                raise ValueError(f"Parameter range for {param_path} cannot be empty")
            
            # Check if the parameter path exists in the config template
            keys = param_path.split('.')
            current = config_template
            for key in keys:
                if key not in current:
                    raise ValueError(f"Parameter path {param_path} does not exist in config template")
                current = current[key]
            
            # Ensure values are valid
            if any(v <= 0 for v in values if isinstance(v, (int, float))):
                raise ValueError(f"All parameter values for {param_path} must be positive")
        
        self.prices = prices
        self.config_template = config_template
        self.param_ranges = param_ranges
    
    def _set_nested_value(self, config, param_path, value):
        """
        Set a nested value in a dictionary.
        
        Args:
            config (dict): Configuration dictionary
            param_path (str): Dot-separated path to parameter
            value: Value to set
            
        Returns:
            dict: Updated configuration
        """
        keys = param_path.split('.')
        current = config
        for key in keys[:-1]:
            current = current[key]
        current[keys[-1]] = value
        return config
    
    def _generate_param_combinations(self):
        """
        Generate all possible parameter combinations.
        
        Returns:
            list: List of parameter combination dictionaries
        """
        # Create a list of (param_path, value) pairs for each parameter
        param_options = []
        for param_path, values in self.param_ranges.items():
            param_options.append([(param_path, value) for value in values])
        
        # Generate all combinations using Cartesian product
        combinations = []
        for combination in product(*param_options):
            # Convert combination from tuple of tuples to dictionary
            combination_dict = dict(combination)
            combinations.append(combination_dict)
        
        return combinations
    
    def _run_backtest(self, config):
        """
        Run a backtest with the given configuration.
        
        Args:
            config (dict): Configuration for backtesting
            
        Returns:
            float: Cumulative returns from the backtest
        """
        # Generate signals using the current configuration
        short_sma = config['strategy']['short_sma']
        long_sma = config['strategy']['long_sma']
        
        # Calculate SMAs
        short_sma_series = calculate_sma(self.prices, short_sma)
        long_sma_series = calculate_sma(self.prices, long_sma)
        
        # Generate signals
        signals = generate_crossover_signals(short_sma_series, long_sma_series)
        
        # Run backtest
        backtester = Backtester(self.prices, signals, config)
        results = backtester.run()
        
        return results['cumulative_returns']
    
    def optimize(self):
        """
        Optimize strategy parameters.
        
        Returns:
            dict: Optimization results including best parameters and scores
        """
        if self.prices.empty:
            raise ValueError("Cannot optimize with empty price data")
        
        # Generate all parameter combinations
        combinations = self._generate_param_combinations()
        
        # Initialize best parameters and score
        best_score = float('-inf')
        best_config = None
        all_results = []
        
        # Test each parameter combination
        for combination in combinations:
            # Create a deep copy of the config template to avoid modifying original
            config = copy.deepcopy(self.config_template)
            
            # Update config with current parameter combination
            for param_path, value in combination.items():
                self._set_nested_value(config, param_path, value)
            
            try:
                # Run backtest with current parameters
                score = self._run_backtest(config)
                
                # Store results
                all_results.append({
                    'params': combination,
                    'score': score
                })
                
                # Update best parameters if current score is better
                if score > best_score:
                    best_score = score
                    best_config = config
            
            except Exception as e:
                # Skip invalid parameter combinations
                print(f"Error with parameters {combination}: {str(e)}")
                continue
        
        # Return optimization results
        return {
            'best_params': best_config,
            'best_score': best_score,
            'all_results': all_results,
            'param_ranges': self.param_ranges
        }

def calculate_consistency_score(trade_period_metrics, target_return, max_drawdown):
    if not trade_period_metrics:
        return 0
    count = 0
    for period in trade_period_metrics:
        # drawdown >= max_drawdown means drawdown is less severe (e.g., -0.02 >= -0.05)
        if period['return'] >= target_return and period['drawdown'] >= max_drawdown:
            count += 1
    return int(100 * count / len(trade_period_metrics))