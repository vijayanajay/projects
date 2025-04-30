import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from data_handler import fetch_ohlcv_data
from config_loader import load_config

class StrategyOptimizer:
    def __init__(self, config: Dict):
        self.config = config
        self.ohlcv_data = fetch_ohlcv_data(
            config['ticker'],
            config['start_date'],
            config['end_date']
        )
        
    def calculate_moving_average(self, prices: pd.Series, window: int) -> pd.Series:
        """Calculate simple moving average"""
        return prices.rolling(window=window).mean()
    
    def generate_signals(self, short_ma: pd.Series, long_ma: pd.Series) -> pd.Series:
        """Generate trading signals based on moving average crossover"""
        signals = pd.Series(0, index=short_ma.index)
        signals[short_ma > long_ma] = 1  # Buy signal
        signals[short_ma < long_ma] = -1 # Sell signal
        return signals
    
    def calculate_position_size(self, portfolio_value: float, volatility: float) -> float:
        """Calculate position size based on portfolio value and volatility"""
        if volatility == 0:
            return 0.0
        return portfolio_value * (self.config['transaction_cost_pct'] / volatility)
    
    def backtest_strategy(self, signals: pd.Series) -> Dict:
        """Backtest the trading strategy and calculate performance metrics"""
        # Calculate returns
        returns = self.ohlcv_data['Close'].pct_change()
        
        # Calculate strategy returns with signal lag
        strategy_returns = returns.shift(1) * signals.shift(1)
        
        # Calculate cumulative returns
        cumulative_returns = (1 + strategy_returns).cumprod()
        
        # Calculate performance metrics
        total_return = cumulative_returns.iloc[-1] - 1
        annualized_return = (1 + total_return) ** (252 / len(strategy_returns)) - 1
        volatility = strategy_returns.std() * np.sqrt(252)
        sharpe_ratio = annualized_return / volatility if volatility != 0 else float('inf')
        
        return {
            'total_return': total_return,
            'annualized_return': annualized_return,
            'volatility': volatility,
            'sharpe_ratio': sharpe_ratio,
            'cumulative_returns': cumulative_returns
        }
    
    def optimize_parameters(self) -> Dict:
        """Optimize strategy parameters using walk-forward analysis"""
        # Initialize best parameters and performance
        best_params = {
            'short_ma': self.config['initial_ma_short'],
            'long_ma': self.config['initial_ma_long']
        }
        best_performance = {'sharpe_ratio': float('-inf')}
        
        # Perform walk-forward analysis
        for short_window in range(5, 20):
            for long_window in range(short_window + 5, 50):
                # Calculate moving averages
                short_ma = self.calculate_moving_average(self.ohlcv_data['Close'], short_window)
                long_ma = self.calculate_moving_average(self.ohlcv_data['Close'], long_window)
                
                # Generate signals
                signals = self.generate_signals(short_ma, long_ma)
                
                # Backtest strategy
                performance = self.backtest_strategy(signals)
                
                # Update best parameters if performance improves
                if performance['sharpe_ratio'] > best_performance['sharpe_ratio']:
                    best_performance = performance
                    best_params = {
                        'short_ma': short_window,
                        'long_ma': long_window
                    }
        
        return {
            'best_params': best_params,
            'best_performance': best_performance
        }

if __name__ == "__main__":
    # Load configuration
    config = load_config()
    
    # Initialize optimizer
    optimizer = StrategyOptimizer(config)
    
    # Optimize strategy parameters
    results = optimizer.optimize_parameters()
    
    # Print results
    print(f"Best Parameters: {results['best_params']}")
    print(f"Best Performance: {results['best_performance']}")