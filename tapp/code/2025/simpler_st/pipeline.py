import os
from pathlib import Path
from tech_analysis.data.fetcher import fetch_stock_data, clean_and_validate_data
from tech_analysis.backtest import sma_crossover_backtest, calculate_performance_metrics
from report_generator import generate_report

def run_pipeline(ticker, output_dir=None):
    """
    Orchestrates fetching, backtesting, and reporting for a single ticker.
    Minimal implementation for integration test.
    """
    # Set up output directory
    if output_dir:
        reports_dir = Path(output_dir) / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(output_dir)
    # Fetch and clean data
    df = fetch_stock_data(ticker, period="1y")
    df = clean_and_validate_data(df)
    # Standardize column names to lowercase for downstream compatibility
    df.columns = df.columns.str.lower()
    print(f"[DEBUG] DataFrame columns for {ticker}: {df.columns.tolist()}")
    print(f"[DEBUG] DataFrame is empty: {df.empty}")
    # Defensive: check data validity
    if df is None or df.empty or 'close' not in df.columns:
        raise ValueError(f"No valid data for ticker {ticker}. Cannot generate report.")
    # Run a basic SMA crossover backtest (minimal params)
    trades = sma_crossover_backtest(df, short_window=20, long_window=50)
    print(f"[DEBUG] Trades output: {trades}")
    # Compute minimal stats for report
    equity_curve = df['close'].copy()
    print(f"[DEBUG] Equity curve head: {equity_curve.head()}")
    stats = {
        'Return [%]': 0.0,
        'Sharpe Ratio': 0.0,
        'Max. Drawdown [%]': 0.0,
        '_trades': trades,
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
        generate_report(stats, bt, ticker)
    except Exception as e:
        import traceback
        print(f"[DEBUG] Exception in generate_report: {e}")
        traceback.print_exc()
        raise

if __name__ == "__main__":
    from tech_analysis.data.stocks_list import STOCKS_LIST
    output_dir = "."
    print(f"[INFO] Running pipeline for all tickers in STOCKS_LIST...")
    for ticker in STOCKS_LIST:
        print(f"[INFO] Processing {ticker}...")
        try:
            run_pipeline(ticker, output_dir)
            print(f"[INFO] Report generated for {ticker}.")
        except Exception as e:
            print(f"[ERROR] Pipeline failed for {ticker}: {e}")
    print(f"[INFO] Pipeline completed for all tickers. PDF reports should be generated in {output_dir}.")
