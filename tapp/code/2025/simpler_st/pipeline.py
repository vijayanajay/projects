import os
from pathlib import Path
from tech_analysis.data.fetcher import fetch_stock_data, clean_and_validate_data
from tech_analysis.backtest import portfolio_backtest
from tech_analysis.utils import calculate_performance_metrics, correlate_performance_with_regimes
from report_generator import generate_markdown_report
import json
from tech_analysis.market_regimes import detect_market_regime_series
import numpy as np
import pandas as pd

def run_pipeline(tickers, output_dir=None, config_path=None):
    """
    Orchestrates fetching, backtesting, and reporting for a unified portfolio of tickers.
    Minimal implementation for integration test.
    """
    # Set up output directory
    if output_dir:
        reports_dir = Path(output_dir) / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(output_dir)
    # Load config
    if config_path is None:
        config_path = Path(__file__).parent / "config.json"
    else:
        config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"config.json not found at {config_path}. Please provide a config.json with required parameters.")
    with open(config_path, "r") as f:
        config = json.load(f)
    # Ensure required config keys are present and error messages are explicit
    required_keys = ["initial_cash", "position_size", "period"]
    missing_keys = [k for k in required_keys if k not in config]
    if missing_keys:
        raise KeyError(f"Missing required config key(s): {', '.join(missing_keys)}. Please specify all required keys in config.json.")
    period = config["period"]
    initial_cash = config["initial_cash"]
    position_size = config["position_size"]
    strategy = config.get("strategy", "naive_momentum")
    strategy_params = dict(config.get("strategy_params", {}))  # Make a copy to avoid mutation issues
    # Always inject sizing params into strategy_params for downstream use
    strategy_params["position_size"] = position_size
    strategy_params["initial_cash"] = initial_cash
    # Filter out invalid tickers
    invalid_tickers = {'', '.', None}
    filtered_tickers = [t for t in tickers if t not in invalid_tickers]
    if not filtered_tickers:
        # Always return 4-tuple on early exit for test compatibility
        return None, None, None, None
    # Fetch and clean data for all filtered tickers
    data_dict = {}
    for ticker in filtered_tickers:
        df = fetch_stock_data(ticker, period=period)
        df = clean_and_validate_data(df)
        df.columns = df.columns.str.lower()
        # DEBUG: Data quality
        # print(f"[DEBUG] {ticker} data length: {len(df)}; head: {df.head(2)}; tail: {df.tail(2)}")
        if df is not None and not df.empty and 'close' in df.columns:
            data_dict[ticker] = df
        else:
            print(f"[WARN] Skipping {ticker}: no valid data.")
    if not data_dict:
        # Always return 4-tuple on early exit for test compatibility
        return None, None, None, None
    # After fetching and cleaning data for all tickers, aggregate close prices for regime detection
    # For simplicity, use the first ticker's close prices (or aggregate as needed for your use case)
    sample_ticker = next(iter(data_dict))
    close_prices = data_dict[sample_ticker]['close']
    # Compute full-date-range regime series, passing strategy_params
    regime_series = detect_market_regime_series(close_prices, strategy_params)
    # Unified portfolio backtest
    bt_result = portfolio_backtest(data_dict, initial_cash=initial_cash, position_size=position_size, strategy_params=strategy_params)
    # DEBUG: Backtest result
    print("[DEBUG] portfolio_backtest result:", bt_result)
    strategy_params = bt_result.get('strategy_params', {})
    pf = bt_result['portfolio_state']
    trade_log = bt_result['trade_log']
    # DEBUG: Trade log with rationale
    print("[DEBUG] Trade log:", trade_log)
    # Extract the real equity curve from the portfolio state
    equity_curve = pf.equity_curve if hasattr(pf, 'equity_curve') else None
    if equity_curve is None or len(equity_curve) == 0:
        # Always return 4-tuple on early exit for test compatibility
        return None, None, None, None
    # Compute real stats using actual equity curve and trade log
    stats = calculate_performance_metrics(equity_curve, trade_log)
    stats['_trades'] = trade_log
    stats['trades'] = trade_log  # Ensure compatibility with report generator
    stats['equity_curve'] = equity_curve
    stats['regime_series'] = regime_series
    # Compute regime summary string from trade log
    regime_stats = correlate_performance_with_regimes(trade_log)
    if regime_stats and any(regime_stats.values()):
        total = sum(v['count'] for v in regime_stats.values())
        summary_parts = []
        for regime, v in regime_stats.items():
            regime_str = regime.capitalize() if isinstance(regime, str) and regime else "Unknown"
            percent = 100 * v['count'] / total if total else 0
            summary_parts.append(f"{regime_str}: {percent:.0f}%")
        regime_summary = ', '.join(summary_parts)
    else:
        regime_summary = 'No trades or regimes detected.'
    stats['regime_summary'] = regime_summary

    # Compute drawdown curve
    def compute_drawdown_curve(equity_curve):
        equity_curve = np.array(equity_curve)
        peak = np.maximum.accumulate(equity_curve)
        drawdown = equity_curve - peak
        return drawdown
    stats['drawdown_curve'] = compute_drawdown_curve(equity_curve)

    # Compute returns distribution (simple daily returns)
    def compute_returns_distribution(equity_curve):
        equity_curve = np.array(equity_curve)
        returns = np.diff(equity_curve) / equity_curve[:-1]
        return returns
    stats['returns_distribution'] = compute_returns_distribution(equity_curve)

    # Always ensure stats['strategy_params'] contains correct sizing values for the report
    stats['strategy_params'] = dict(stats.get('strategy_params', {}))
    stats['strategy_params']['position_size'] = position_size
    stats['strategy_params']['initial_cash'] = initial_cash

    # Ensure _trades is a DataFrame with correct columns for heatmap
    if isinstance(stats['_trades'], list):
        stats['_trades'] = pd.DataFrame(stats['_trades'])
    if isinstance(stats['_trades'], pd.DataFrame):
        # Map 'ticker' to 'Ticker', 'regime' to 'Regime', preserve correct values
        rename_map = {}
        if 'ticker' in stats['_trades'].columns:
            rename_map['ticker'] = 'Ticker'
        if 'regime' in stats['_trades'].columns:
            rename_map['regime'] = 'Regime'
        stats['_trades'] = stats['_trades'].rename(columns=rename_map)
        # Ensure 'PnL' column exists (upper-case), mapping from 'pnl' if needed
        if 'PnL' not in stats['_trades'].columns and 'pnl' in stats['_trades'].columns:
            stats['_trades']['PnL'] = stats['_trades']['pnl']
        # Only fill missing values, do not overwrite correct data
        if 'Regime' in stats['_trades'].columns:
            stats['_trades']['Regime'] = stats['_trades']['Regime'].fillna('Unknown')
        if 'Ticker' in stats['_trades'].columns:
            stats['_trades']['Ticker'] = stats['_trades']['Ticker'].fillna(sample_ticker)
    # DEBUG: Metrics/stats for report
    print("[DEBUG] Stats for report:", stats)
    # Pass real stats to report generator
    try:
        generate_markdown_report(stats, pf)
    except Exception as e:
        import traceback
        print(f"[DEBUG] Exception in generate_markdown_report: {e}")
        traceback.print_exc()
        raise

    # Return all required outputs for tests: stats, pf, trade_log, regime_series
    return stats, pf, trade_log, regime_series

# --- Parameter Sensitivity/Robustness Analysis ---
def run_parameter_sensitivity_analysis(tickers, output_dir=None, config_path=None):
    """
    Runs the pipeline twice with different strategy parameters to show sensitivity.
    Plots both equity curves for comparison and saves the plot for the report.
    """
    import copy
    from report_generator import plot_parameter_sensitivity
    # 1. Run with default config
    result1 = run_pipeline(tickers, output_dir=output_dir, config_path=config_path)
    # 2. Load config and modify one parameter (e.g., short_window)
    if config_path is None:
        config_path = Path(__file__).parent / "config.json"
    else:
        config_path = Path(config_path)
    with open(config_path, "r") as f:
        config = json.load(f)
    alt_config = copy.deepcopy(config)
    alt_config["strategy_params"]["short_window"] = max(5, config["strategy_params"].get("short_window", 20) // 2)
    alt_config_path = Path("alt_config.json")
    with open(alt_config_path, "w") as f:
        json.dump(alt_config, f)
    # 3. Run with alternative config
    result2 = run_pipeline(tickers, output_dir=output_dir, config_path=alt_config_path)
    # 4. Plot both equity curves
    eq1 = result1[0]["equity_curve"] if isinstance(result1, tuple) else None
    eq2 = result2[0]["equity_curve"] if isinstance(result2, tuple) else None
    label1 = f"short_window={config['strategy_params']['short_window']}"
    label2 = f"short_window={alt_config['strategy_params']['short_window']}"
    plot_parameter_sensitivity(eq1, eq2, label1, label2, save_path="plots/parameter_sensitivity.png")
    # 5. Clean up alt_config.json
    try:
        os.remove(alt_config_path)
    except Exception:
        pass
    return True

if __name__ == "__main__":
    import traceback
    from tech_analysis.data.stocks_list import STOCKS_LIST
    output_dir = "."
    print(f"[INFO] Running unified pipeline for all tickers in STOCKS_LIST...")
    try:
        run_pipeline(STOCKS_LIST, output_dir)
        print(f"[INFO] Unified portfolio report generated.")
    except Exception as e:
        print(f"[ERROR] Exception in main pipeline: {e}")
        traceback.print_exc()
    print(f"[INFO] Pipeline completed. Unified PDF report should be generated in {output_dir}.")
    # --- Parameter Sensitivity/Robustness Analysis ---
    try:
        print("[INFO] Running parameter sensitivity analysis...")
        run_parameter_sensitivity_analysis(STOCKS_LIST, output_dir=".")
        print("[INFO] Parameter sensitivity plot generated.")
    except Exception as e:
        print(f"[ERROR] Sensitivity analysis failed: {e}")
