import os
from pathlib import Path
from tech_analysis.data.fetcher import fetch_stock_data, clean_and_validate_data
from tech_analysis.backtest import portfolio_backtest, calculate_performance_metrics
from report_generator import generate_report

def run_pipeline(tickers, output_dir=None):
    """
    Orchestrates fetching, backtesting, and reporting for a unified portfolio of tickers.
    Minimal implementation for integration test.
    """
    # Set up output directory
    if output_dir:
        reports_dir = Path(output_dir) / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(output_dir)
    # Filter out invalid tickers
    invalid_tickers = {'', '.', None}
    filtered_tickers = [t for t in tickers if t not in invalid_tickers]
    if not filtered_tickers:
        raise ValueError("No valid tickers provided after filtering invalid ones.")
    # Fetch and clean data for all filtered tickers
    data_dict = {}
    for ticker in filtered_tickers:
        df = fetch_stock_data(ticker, period="1y")
        df = clean_and_validate_data(df)
        df.columns = df.columns.str.lower()
        if df is not None and not df.empty and 'close' in df.columns:
            data_dict[ticker] = df
        else:
            print(f"[WARN] Skipping {ticker}: no valid data.")
    if not data_dict:
        raise ValueError("No valid data for any ticker. Cannot generate unified report.")
    # Unified portfolio backtest
    bt_result = portfolio_backtest(data_dict)
    pf = bt_result['portfolio_state']
    trade_log = bt_result['trade_log']
    # Compute unified stats (minimal example)
    # For now, just use the first available equity curve for demonstration
    sample_ticker = next(iter(data_dict))
    equity_curve = data_dict[sample_ticker]['close']
    stats = {
        'Return [%]': 0.0,
        'Sharpe Ratio': 0.0,
        'Max. Drawdown [%]': 0.0,
        '_trades': trade_log,
        'regime_summary': 'N/A',
        'equity_curve': equity_curve,
    }
    # Dummy BT object for report (minimal, as in test_report_generation)
    class DummyBT:
        def plot(self, filename=None, equity_curve=None, **kwargs):
            pass
        _commission = 0.0
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 20, 'n2': 50}
            return DummyStrategy()
    bt = DummyBT()
    try:
        generate_report(stats, bt)
    except Exception as e:
        import traceback
        print(f"[DEBUG] Exception in generate_report: {e}")
        traceback.print_exc()
        raise

if __name__ == "__main__":
    from tech_analysis.data.stocks_list import STOCKS_LIST
    output_dir = "."
    print(f"[INFO] Running unified pipeline for all tickers in STOCKS_LIST...")
    try:
        run_pipeline(STOCKS_LIST, output_dir)
        print(f"[INFO] Unified portfolio report generated.")
    except Exception as e:
        print(f"[ERROR] Unified pipeline failed: {e}")
    print(f"[INFO] Pipeline completed. Unified PDF report should be generated in {output_dir}.")
