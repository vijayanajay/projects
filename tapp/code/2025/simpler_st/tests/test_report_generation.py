import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Import the generate_markdown_report function from the new report_generator.py
from report_generator import generate_markdown_report
from tech_analysis.utils import (
    calculate_performance_metrics,
    correlate_performance_with_regimes,
    extract_drawdown_periods,
    calculate_indicator_summary_stats
)

def dummy_bt():
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    return DummyBT()

def test_markdown_contains_regime_summary(tmp_path):
    stats = {
        'Return [%]': 12.5,
        'Sharpe Ratio': 1.2,
        'Max. Drawdown [%]': -5.7,
        '_trades': None,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Trending: 60%" in text, "Regime summary not found in Markdown report."

def test_markdown_includes_equity_curve_chart(tmp_path):
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': None,
        'regime_summary': 'Trending: 50%, Ranging: 30%, Volatile: 20%',
        'equity_curve': [10000, 10100, 10200, 10300, 10400],
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    chart_path = tmp_path / "plots/portfolio_equity.png"
    assert chart_path.exists(), "Equity curve chart not generated."
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Equity Curve" in text, "Equity curve section missing in Markdown report."

def test_markdown_includes_trade_log(tmp_path):
    import pandas as pd
    stats = {
        'Return [%]': 12.0,
        'Sharpe Ratio': 1.3,
        'Max. Drawdown [%]': -4.0,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        '_trades': pd.DataFrame([
            {'EntryTime': '2025-04-01', 'EntryPrice': 100, 'ExitTime': '2025-04-10', 'ExitPrice': 110, 'PnL': 10.0, 'PositionSize': 50, 'Rationale': 'Buy: SMA cross'},
            {'EntryTime': '2025-04-15', 'EntryPrice': 105, 'ExitTime': '2025-04-20', 'ExitPrice': 108, 'PnL': 3.0, 'PositionSize': 40, 'Rationale': 'Sell: target hit'}
        ]),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "**Entry:** 2025-04-01" in text, "Trade entry data missing in Markdown report."
    assert "**Entry Price:** 100" in text, "Trade entry price missing in Markdown report."
    assert "**Exit:** 2025-04-10" in text, "Trade exit data missing in Markdown report."
    assert "**Exit Price:** 110" in text, "Trade exit price missing in Markdown report."
    assert "**Position Size:** 50" in text, "Trade position size missing in Markdown report."
    assert "**PnL:** 10.00" in text, "Trade PnL missing in Markdown report."
    assert "**Rationale:** Buy: SMA cross" in text, "Trade rationale missing in Markdown report."

def test_markdown_includes_analyst_notes_placeholder(tmp_path):
    stats = {
        'Return [%]': 7.5,
        'Sharpe Ratio': 0.7,
        'Max. Drawdown [%]': -2.5,
        '_trades': None,
        'regime_summary': 'Trending: 30%, Ranging: 50%, Volatile: 20%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Analyst Notes and Suggestions" in text, "Analyst Notes placeholder not found in Markdown report."

def test_markdown_includes_analyst_notes_substantive(tmp_path):
    stats = {
        'Return [%]': 7.5,
        'Sharpe Ratio': 0.7,
        'Max. Drawdown [%]': -2.5,
        '_trades': None,
        'regime_summary': 'Trending: 30%, Ranging: 50%, Volatile: 20%',
        'analyst_notes': 'The strategy underperformed due to regime filtering.',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Analyst Notes and Suggestions" in text, "Analyst Notes section missing in Markdown report."
    # Ensure there is a substantive note, not just a placeholder
    assert "(Add your notes here.)" not in text, "Placeholder note found; substantive note required."
    assert "strategy underperformed" in text or "consider parameter tuning" in text or "regime filtering" in text, "No substantive analyst note found."

def test_markdown_includes_rationale_summary(tmp_path):
    import pandas as pd
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': pd.DataFrame([
            {'EntryTime': '2025-04-01', 'EntryPrice': 100, 'ExitTime': '2025-04-10', 'ExitPrice': 110, 'PnL': 10.0, 'rationale': 'Buy: SMA cross'},
            {'EntryTime': '2025-04-15', 'EntryPrice': 105, 'ExitTime': '2025-04-20', 'ExitPrice': 108, 'PnL': 3.0, 'rationale': 'Sell: SMA cross'},
            {'EntryTime': '2025-04-25', 'EntryPrice': 108, 'ExitTime': '2025-04-30', 'ExitPrice': 112, 'PnL': 4.0, 'rationale': 'Buy: SMA cross'},
        ]),
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Rationale Summary" in text, "Rationale Summary section missing in Markdown report."
    assert "Buy: SMA cross" in text, "Rationale count summary incorrect."
    assert "Sell: SMA cross" in text, "Rationale count summary incorrect."

def test_regime_table_filters_short_runs(tmp_path):
    import pandas as pd
    # Create a regime series: 2 days trending, 4 days ranging, 3 days volatile, 5 days calm
    dates = pd.date_range("2025-04-01", periods=14)
    regimes = [
        'trending', 'trending', # 2 days (should be skipped)
        'ranging', 'ranging', 'ranging', 'ranging', # 4 days (should be included)
        'volatile', 'volatile', 'volatile', # 3 days (should be skipped)
        'calm', 'calm', 'calm', 'calm', 'calm' # 5 days (should be included)
    ]
    regime_series = pd.Series(regimes, index=dates)
    stats = {
        'regime_summary': 'Trending: 15%, Ranging: 30%, Volatile: 20%, Calm: 35%',
        'regime_series': regime_series,
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Look for the regime summary table
    summary_start = text.find("## Regime Summary")
    assert summary_start != -1, "Regime Summary section not found in report."
    summary_text = text[summary_start:summary_start+1000]  # Extend window for robustness
    # Look for Markdown table rows for the expected regimes and durations
    found_ranging = False
    found_calm = False
    table_lines = []
    for line in summary_text.splitlines():
        if "|" in line:
            table_lines.append(line)
            if "ranging" in line and "4" in line:
                found_ranging = True
            if "calm" in line and "5" in line:
                found_calm = True
    if not (found_ranging and found_calm):
        print("\n--- Regime Summary Table Lines ---")
        for l in table_lines:
            print(l)
        print("--- End Regime Summary Table Lines ---\n")
        print("\n--- Full Regime Summary Section ---")
        print(summary_text)
        print("--- End Full Regime Summary Section ---\n")
    assert found_ranging, "Regime of exactly min_duration days (ranging, 4) not included as a table row in summary."
    assert found_calm, "Regime of exactly min_duration days (calm, 5) not included as a table row in summary."
    # Table should include only ranging (4 days) and calm (5 days), not trending (2) or volatile (3)
    assert "ranging" in text and "calm" in text, "Expected regimes not found in table."
    assert "trending" not in text, "Short trending regime should not be in table."
    assert "volatile" not in text, "Short volatile regime should not be in table."
    # Table format check
    assert "| Start Date | End Date | Regime | Days |" in text, "Regime table header missing."
    # Check correct days count
    assert "4" in text and "5" in text, "Regime days count missing or incorrect."

def test_regime_definitions_are_parameterized(tmp_path):
    """
    Test that regime definitions and criteria in the report are generated using actual strategy parameters, not hardcoded values.
    """
    stats = {
        'regime_summary': 'Trending: 40%, Ranging: 60%',
        'strategy_params': {
            'position_size': 1, 
            'initial_cash': 1, 
            'short_window': 13,
            'long_window': 55,
            'min_regime_days': 7,
            'rsi_period': 10,
            'overbought': 80,
            'oversold': 20
        }
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Check that all parameter values appear in the regime summary section
    assert "short-term SMA (window: 13)" in text, "Short SMA window not reflected in regime definition."
    assert "long-term SMA (window: 55)" in text, "Long SMA window not reflected in regime definition."
    assert "for more than 6 days" in text, "Min regime days not reflected in regime definition."
    assert "**Short SMA window:** 13 days" in text, "Short SMA window not reflected in quantitative parameters."
    assert "**Long SMA window:** 55 days" in text, "Long SMA window not reflected in quantitative parameters."
    assert "**Minimum regime duration:** 7 days" in text, "Min regime days not reflected in quantitative parameters."
    assert "**RSI period:** 10" in text, "RSI period not reflected in quantitative parameters."
    assert "**RSI thresholds:** Overbought (80), Oversold (20)" in text, "RSI thresholds not reflected in quantitative parameters."
    # Should not contain any default/hardcoded values if custom provided
    assert "window: 20" not in text, "Hardcoded default short_window found in regime definition."
    assert "window: 50" not in text, "Hardcoded default long_window found in regime definition."
    assert "for more than 3 days" not in text, "Hardcoded min regime days found in regime definition."
    assert "Overbought (70), Oversold (30)" not in text, "Hardcoded RSI thresholds found in regime definition."

def test_markdown_includes_trade_level_chart(tmp_path):
    import pandas as pd
    stats = {
        'equity_curve': [100, 102, 101, 105, 107, 106],
        'sma_curve': [100, 101, 101.5, 103, 104, 105],
        'rsi_curve': [50, 55, 60, 65, 70, 68],
        '_trades': pd.DataFrame([
            {'EntryTime': 1, 'EntryPrice': 102, 'ExitTime': 4, 'ExitPrice': 107, 'PnL': 5.0, 'PositionSize': 10, 'Rationale': 'Buy: SMA cross'},
        ]),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    chart_path = tmp_path / "plots/trade_chart.png"
    md_path = tmp_path / "reports/portfolio_report.md"
    assert chart_path.exists(), "Trade-level chart not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "trade_chart.png" in text, "Trade-level chart not embedded in Markdown report."

def test_markdown_includes_drawdown_curve(tmp_path):
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'equity_curve': [10000, 10100, 9800, 10400],
        'drawdown_curve': [0, 0, -300, 0],
        'regime_summary': 'Trending: 50%, Ranging: 30%, Volatile: 20%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    chart_path = tmp_path / "plots/drawdown_curve.png"
    assert chart_path.exists(), "Drawdown curve chart not generated."
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Drawdown Curve" in text, "Drawdown curve section missing in Markdown report."

def test_markdown_includes_return_distribution(tmp_path):
    import numpy as np
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'returns_distribution': np.array([0.01, -0.02, 0.03, 0.01, -0.01, 0.02]),
        'regime_summary': 'Trending: 50%, Ranging: 30%, Volatile: 20%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    chart_path = tmp_path / "plots/return_distribution.png"
    # The file may be named differently, so just check for the section in the report
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Return Distribution" in text, "Return distribution section missing in Markdown report."

def test_markdown_includes_trade_heatmap(tmp_path):
    import pandas as pd
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': pd.DataFrame({
            'ticker': ['A', 'B', 'A', 'B'],
            'pnl': [1, -1, 2, -2],
            'regime': ['Trending', 'Ranging', 'Trending', 'Ranging']
        }),
        'regime_summary': 'Trending: 50%, Ranging: 50%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    chart_path = tmp_path / "plots/trade_heatmap.png"
    assert chart_path.exists(), "Trade heatmap not generated."
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Trade Outcome Heatmap" in text, "Trade outcome heatmap section missing in Markdown report."

def test_report_risk_section_uses_params(tmp_path):
    """
    The report's risk/position sizing section should use the exact values from parameters.
    """
    stats = {
        'Return [%]': 7.0,
        'Sharpe Ratio': 0.9,
        'Max. Drawdown [%]': -2.0,
        '_trades': None,
        'strategy_params': {'position_size': 42, 'initial_cash': 3141}
    }
    from report_generator import generate_markdown_report
    class DummyBT:
        def plot(self, filename=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.0
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 1}
            return DummyStrategy()
    os.chdir(tmp_path)
    generate_markdown_report(stats, DummyBT(), output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Check for new risk section wording and config values
    assert "% Risked Per Trade" in text
    assert "position_size=42" in text and "initial_cash=3141" in text
    assert "Allocation Rule" in text
    assert "Max Simultaneous Positions" in text

def test_report_risk_section_missing_keys(tmp_path):
    """
    The report should raise if position_size or initial_cash is missing in parameters.
    """
    stats = {
        'Return [%]': 7.0,
        'Sharpe Ratio': 0.9,
        'Max. Drawdown [%]': -2.0,
        '_trades': None,
        'strategy_params': {'initial_cash': 3141}  # missing position_size
    }
    from report_generator import generate_markdown_report
    class DummyBT:
        def plot(self, filename=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.0
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 1}
            return DummyStrategy()
    import os
    os.chdir(tmp_path)
    try:
        generate_markdown_report(stats, DummyBT(), output_dir=tmp_path)
        assert False, "Should raise KeyError if sizing keys are missing."
    except KeyError as e:
        assert "position_size" in str(e) or "initial_cash" in str(e)

def test_markdown_includes_assumptions_section(tmp_path):
    import pandas as pd
    stats = {
        'strategy_params': {
            'commission': 0.01,
            'slippage': 0.5,
            'position_size': 1,
            'initial_cash': 10000
        },
        '_trades': pd.DataFrame([])
    }
    class DummyBT:
        _commission = 0.002
        _slippage = 0.0
        def plot(self, filename=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
    bt = DummyBT()
    import os
    os.chdir(tmp_path)
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Assumptions: Slippage and Commission" in text, "Assumptions section missing."
    assert "commission=0.01" in text, "Commission value missing or incorrect."
    assert ("slippage=0.5" in text or "slippage: 0.5" in text), "Slippage value missing or incorrect."

def test_markdown_includes_parameter_sensitivity(tmp_path):
    """
    Test that the Markdown report includes the parameter sensitivity plot if generated.
    """
    import shutil
    from report_generator import generate_markdown_report
    # Create dummy stats and bt
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': None,
        'regime_summary': 'Trending: 50%, Ranging: 30%, Volatile: 20%',
        'equity_curve': [10000, 10100, 10200, 10300, 10400],
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        _commission = 0.001
        def plot(self, filename=None):
            pass
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    # Simulate parameter sensitivity plot
    plots_dir = tmp_path / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)
    sens_path = plots_dir / "parameter_sensitivity.png"
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot([1, 2, 3], [1, 2, 3], label='A')
    plt.plot([1, 2, 3], [1, 1.5, 2], label='B')
    plt.legend()
    plt.savefig(sens_path)
    plt.close()
    # Generate report
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = reports_dir / "portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Parameter Sensitivity Analysis" in text, "Parameter sensitivity section not found in report."
    assert "parameter_sensitivity.png" in text, "Parameter sensitivity plot not referenced in report."

def test_markdown_includes_trade_statistics_breakdown(tmp_path):
    """
    Test that the Markdown report includes a trade statistics breakdown with average win, average loss, largest win/loss, profit factor, expectancy, and regime breakdown.
    """
    # Construct dummy trade log with regimes and PnL
    trades = [
        {'PnL': 100, 'regime': 'trending'},
        {'PnL': -50, 'regime': 'trending'},
        {'PnL': 200, 'regime': 'ranging'},
        {'PnL': -30, 'regime': 'ranging'},
        {'PnL': 300, 'regime': 'trending'},
        {'PnL': -150, 'regime': 'volatile'},
    ]
    equity_curve = [1000, 1100, 1050, 1250, 1220, 1520, 1370]
    from tech_analysis.utils import calculate_performance_metrics
    stats = {
        'equity_curve': equity_curve,
        'trades': trades,
        'strategy_params': {'position_size': 1, 'initial_cash': 1},
    }
    # Compute and insert strategy metrics
    stats.update(calculate_performance_metrics(equity_curve, trades))
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Check for key metrics
    assert "Average Win" in text, "Average Win not found in report."
    assert "Average Loss" in text, "Average Loss not found in report."
    assert "Largest Win" in text, "Largest Win not found in report."
    assert "Largest Loss" in text, "Largest Loss not found in report."
    assert "Profit Factor" in text, "Profit Factor not found in report."
    assert "Expectancy" in text, "Expectancy not found in report."
    # Check regime breakdown section
    assert "Regime Breakdown" in text, "Regime breakdown section not found."
    assert "trending" in text and "ranging" in text and "volatile" in text, "Not all regimes present in breakdown."

def test_markdown_includes_risk_and_position_sizing_details(tmp_path):
    """
    Test that the Markdown report includes % risked per trade, allocation rule, and max simultaneous positions in the Risk and Position Sizing Logic section.
    """
    stats = {
        'Return [%]': 12.5,
        'Sharpe Ratio': 1.2,
        'Max. Drawdown [%]': -5.7,
        '_trades': None,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        'strategy_params': {'position_size': 100, 'initial_cash': 10000}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "% Risked Per Trade" in text, "% risked per trade missing in risk section."
    assert "Allocation Rule" in text, "Allocation rule missing in risk section."
    assert "Max Simultaneous Positions" in text, "Max simultaneous positions missing in risk section."
    assert "1.00% of initial capital" in text, "Percent risked per trade value incorrect in risk section."
    assert "Fixed allocation per trade" in text, "Allocation rule description incorrect in risk section."
    assert "No explicit maximum; limited by available cash" in text, "Max simultaneous positions description incorrect in risk section."

def test_markdown_includes_benchmark_comparison(tmp_path):
    """
    Test that the Markdown report contains a section comparing portfolio returns to benchmark returns
    and that the benchmark comparison chart is generated and embedded as a static image.
    """
    stats = {
        'Return [%]': 15.0,
        'Sharpe Ratio': 1.4,
        'Max. Drawdown [%]': -6.0,
        'regime_summary': 'Trending: 70%, Ranging: 20%, Volatile: 10%',
        'equity_curve': [10000, 10100, 10200, 10400, 10700],
        'benchmark_curve': [10000, 10050, 10150, 10200, 10300],
        'benchmark_name': 'NIFTY',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    # Generate the report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    # Check for chart
    chart_path = tmp_path / "plots/benchmark_comparison.png"
    assert chart_path.exists(), "Benchmark comparison chart not generated."
    # Check for section in Markdown
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Benchmark Comparison" in text, "Benchmark Comparison section missing in Markdown report."
    assert "![](../plots/benchmark_comparison.png)" in text or "![](plots/benchmark_comparison.png)" in text, "Benchmark comparison image not embedded in Markdown report."

def test_markdown_commission_and_slippage_affect_pnl_and_report(tmp_path):
    import pandas as pd
    # Simulate trades with known PnL
    trades = [
        {'EntryTime': '2025-04-01', 'EntryPrice': 100, 'ExitTime': '2025-04-10', 'ExitPrice': 110, 'PnL': 10.0, 'PositionSize': 1, 'Rationale': 'Buy: SMA cross'},
        {'EntryTime': '2025-04-15', 'EntryPrice': 105, 'ExitTime': '2025-04-20', 'ExitPrice': 108, 'PnL': 3.0, 'PositionSize': 1, 'Rationale': 'Sell: target hit'}
    ]
    stats = {
        'Return [%]': 13.0,
        'Sharpe Ratio': 1.3,
        'Max. Drawdown [%]': -4.0,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        '_trades': pd.DataFrame(trades),
        'strategy_params': {'position_size': 1, 'initial_cash': 1, 'commission': 0.02, 'slippage': 0.7}
    }
    class DummyBT:
        _commission = 0.01  # Should be ignored
        _slippage = 0.5     # Should be ignored
        def plot(self, filename=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
    bt = DummyBT()
    import os
    os.chdir(tmp_path)
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Assumptions section must state commission and slippage from stats['strategy_params'], not bt
    assert "Assumptions: Slippage and Commission" in text
    assert "commission=0.02" in text, "Commission should be sourced from stats['strategy_params'] only."
    assert ("slippage=0.7" in text or "slippage: 0.7" in text), "Slippage should be sourced from stats['strategy_params'] only."
    # Should not mention bt._commission or bt._slippage values
    assert "commission=0.01" not in text, "Should not use bt._commission."
    assert ("slippage=0.5" not in text and "slippage: 0.5" not in text), "Should not use bt._slippage."
    # Check that net PnL is reduced by both costs (using stats['strategy_params'] values)
    expected_net = 10+3 - 2*0.02*100 - 2*0.7  # commission as percent of price, slippage per trade
    assert str(int(expected_net)) in text or str(round(expected_net, 2)) in text, "Net PnL after costs not shown or incorrect."

def test_markdown_includes_trade_level_chart_per_ticker(tmp_path):
    import pandas as pd
    stats = {
        'equity_curve': {
            'AAPL': [100, 102, 101, 105, 107, 106],
            'MSFT': [200, 202, 201, 205, 207, 206],
        },
        'sma_curve': {
            'AAPL': [100, 101, 101.5, 103, 104, 105],
            'MSFT': [200, 201, 201.5, 203, 204, 205],
        },
        'regime_series': {
            'AAPL': ['uptrend', 'uptrend', 'downtrend', 'downtrend', 'uptrend', 'uptrend'],
            'MSFT': ['downtrend', 'downtrend', 'uptrend', 'uptrend', 'downtrend', 'downtrend'],
        },
        '_trades': pd.DataFrame([
            {'ticker': 'AAPL', 'entry_time': 1, 'entry_price': 102, 'exit_time': 4, 'exit_price': 107, 'pnl': 5.0, 'position_size': 10, 'rationale': 'Buy: SMA cross'},
            {'ticker': 'MSFT', 'entry_time': 2, 'exit_time': 5, 'entry_price': 202, 'exit_price': 206, 'pnl': 4.0, 'position_size': 8, 'rationale': 'Sell: SMA cross'}
        ]),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        def plot(self, filename=None, ticker=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.title(f"{ticker}")
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    for ticker in ['AAPL', 'MSFT']:
        chart_path = tmp_path / f"plots/trade_chart_{ticker}.png"
        assert chart_path.exists(), f"Trade-level chart for {ticker} not generated."
        assert f"plots/trade_chart_{ticker}.png" in text, f"Chart for {ticker} not embedded in report."
        assert f"Chart shows all trade entries" in text or f"{ticker}" in text, "Caption for trade markup chart missing or incomplete."

def test_markdown_includes_drawdown_table(tmp_path):
    """
    Test that the Markdown report includes a drawdown table as a static image and the section is present.
    """
    # Construct a dummy equity curve with two drawdown periods
    equity_curve = [1000, 950, 900, 950, 1000, 900, 850, 900, 1000]
    from tech_analysis.utils import calculate_performance_metrics
    stats = {
        'equity_curve': equity_curve,
        'strategy_params': {'position_size': 1, 'initial_cash': 1},
    }
    # Compute and insert strategy metrics
    stats.update(calculate_performance_metrics(equity_curve, []))
    bt = dummy_bt()
    os.chdir(tmp_path)
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Check for Drawdown Table section and image
    assert "Drawdown Table" in text, "Drawdown Table section not found in report."
    assert "drawdown_table.png" in text, "Drawdown table image not embedded in report."

def test_markdown_includes_holding_duration_distribution(tmp_path):
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    # Create dummy trades with varying holding durations
    base_date = datetime(2025, 4, 1)
    trades = []
    for i in range(5):
        entry = base_date + timedelta(days=i*5)
        exit = entry + timedelta(days=i+1)  # holding: 1,2,3,4,5 days
        trades.append({
            'EntryTime': entry.strftime('%Y-%m-%d'),
            'ExitTime': exit.strftime('%Y-%m-%d'),
            'EntryPrice': 100 + i*2,
            'ExitPrice': 105 + i*2,
            'PnL': 5.0 + i,
            'PositionSize': 10,
            'Rationale': 'Test trade'
        })
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': pd.DataFrame(trades),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    from report_generator import generate_markdown_report
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    chart_path = tmp_path / "plots/holding_duration.png"
    md_path = tmp_path / "reports/portfolio_report.md"
    assert chart_path.exists(), "Holding duration histogram not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Trade Holding Duration Distribution" in text, "Holding duration section missing in Markdown report."
    assert "holding_duration.png" in text, "Holding duration histogram not embedded in Markdown report."

def test_markdown_includes_regime_plots(tmp_path):
    """
    Test that the Markdown report includes both a barplot (mean PnL per regime)
    and a boxplot (PnL distribution per regime) as static images in the regime breakdown section.
    """
    import pandas as pd
    from report_generator import generate_markdown_report
    trades = [
        {'PnL': 100, 'regime': 'trending'},
        {'PnL': -50, 'regime': 'trending'},
        {'PnL': 200, 'regime': 'ranging'},
        {'PnL': -30, 'regime': 'ranging'},
        {'PnL': 300, 'regime': 'trending'},
        {'PnL': -150, 'regime': 'volatile'},
    ]
    stats = {
        'equity_curve': [1000, 1100, 1050, 1250, 1220, 1520, 1370],
        'trades': trades,
        'strategy_params': {'position_size': 1, 'initial_cash': 1},
    }
    os.chdir(tmp_path)
    generate_markdown_report(stats, None, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Check for plot image references
    assert "regime_barplot.png" in text, "Regime barplot not embedded in Markdown report."
    assert "regime_boxplot.png" in text, "Regime boxplot not embedded in Markdown report."
    # Check that files are created
    barplot_path = tmp_path / "plots/regime_barplot.png"
    boxplot_path = tmp_path / "plots/regime_boxplot.png"
    assert barplot_path.exists(), "Regime barplot image not generated."
    assert boxplot_path.exists(), "Regime boxplot image not generated."

def test_markdown_includes_out_of_sample_section(tmp_path):
    """
    Test that the Markdown report includes an Out-of-Sample/Walk-Forward Validation section with metrics if provided.
    """
    stats = {
        'out_of_sample': {
            'period': '2022-2023',
            'return': 2.7,
            'sharpe': 0.18,
            'max_drawdown': 1.1,
            'note': 'Performance is consistent with in-sample results, suggesting robustness.'
        },
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Out-of-Sample Walk-Forward Results" in text, "Out-of-sample section missing in report."
    assert "2022-2023" in text, "Out-of-sample period missing in report."
    assert "2.7%" in text, "Out-of-sample return missing in report."
    assert "Sharpe: 0.18" in text, "Out-of-sample Sharpe missing in report."
    assert "Max Drawdown: 1.1%" in text, "Out-of-sample drawdown missing in report."
    assert "robustness" in text, "Out-of-sample note missing in report."

def test_markdown_includes_strategy_rule_summary(tmp_path):
    """
    Test that the Markdown report includes a plain-English summary of all strategy rules and exceptions.
    """
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1},
        'strategy_rules': [
            'Enter long when 10-period SMA crosses above 50-period SMA.',
            'Exit when 10-period SMA crosses below 50-period SMA.',
            'Skip trade if ATR(14) < 2.0.',
            'No trades on earnings announcement days.',
            'Position size is 2% of available capital, rounded down to nearest share.'
        ]
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Strategy Rules (Plain English)" in text, "Strategy rule summary section missing."
    for rule in stats['strategy_rules']:
        assert rule in text, f"Rule not found in report: {rule}"

def test_markdown_includes_trade_markup_visuals_per_ticker(tmp_path):
    """
    Test that the Markdown report embeds an annotated trade markup chart for each ticker with a descriptive caption.
    """
    import pandas as pd
    tickers = ['APOLLOTYRE.NS', 'HCLTECH.NS']
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1},
        'tickers': tickers,
        '_trades': pd.DataFrame([])
    }
    class DummyBT:
        def plot(self, filename=None, ticker=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.title(f"{ticker}")
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 10, 'n2': 50}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    for ticker in tickers:
        chart_path = tmp_path / f"plots/trade_chart_{ticker}.png"
        assert chart_path.exists(), f"Trade markup chart not generated for {ticker}."
        assert f"plots/trade_chart_{ticker}.png" in text, f"Chart for {ticker} not embedded in report."
        assert f"Chart shows all trade entries" in text or f"{ticker}" in text, "Caption for trade markup chart missing or incomplete."

def test_trade_log_includes_context_and_indicators(tmp_path):
    import pandas as pd
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': pd.DataFrame([
            {
                'EntryTime': '2025-04-01',
                'EntryPrice': 100,
                'ExitTime': '2025-04-10',
                'ExitPrice': 110,
                'PnL': 10.0,
                'PositionSize': 50,
                'Rationale': 'Buy: SMA cross',
                'EntryRegime': 'trending',
                'ExitRegime': 'ranging',
                'EntryVolatility': 1.2,
                'ExitVolatility': 1.5,
                'EntryVolume': 100000,
                'ExitVolume': 120000,
                'EntrySMA': 101.5,
                'ExitSMA': 108.2,
                'EntryRSI': 65.0,
                'ExitRSI': 72.0,
            }
        ]),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Entry Regime: trending" in text, "Trade log missing entry regime."
    assert "Exit Regime: ranging" in text, "Trade log missing exit regime."
    assert "Entry Volatility: 1.2" in text, "Trade log missing entry volatility."
    assert "Exit Volatility: 1.5" in text, "Trade log missing exit volatility."
    assert "Entry Volume: 100000" in text, "Trade log missing entry volume."
    assert "Exit Volume: 120000" in text, "Trade log missing exit volume."
    assert "Entry SMA: 101.5" in text, "Trade log missing entry SMA."
    assert "Exit SMA: 108.2" in text, "Trade log missing exit SMA."
    assert "Entry RSI: 65.0" in text, "Trade log missing entry RSI."
    assert "Exit RSI: 72.0" in text, "Trade log missing exit RSI."

def test_markdown_includes_trade_duration_and_exposure(tmp_path):
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'trade_duration_stats': {
            'avg_duration': 5.2,
            'median_duration': 4.0,
            'max_duration': 12.0,
            'avg_exposure': 0.83
        },
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Trade Duration and Exposure Statistics" in text, "Trade duration/exposure section missing."
    assert "Average Duration: 5.2 days" in text, "Average duration missing."
    assert "Median Duration: 4.0 days" in text, "Median duration missing."
    assert "Max Duration: 12.0 days" in text, "Max duration missing."
    assert "Average Portfolio Exposure: 83.0%" in text, "Portfolio exposure missing."

def test_markdown_includes_slippage_commission_sensitivity(tmp_path):
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'slippage_commission_sensitivity': [
            {'slippage': 0.0, 'commission': 0.002, 'sharpe': 1.0, 'return': 10.0, 'drawdown': 4.0},
            {'slippage': 0.001, 'commission': 0.004, 'sharpe': 0.8, 'return': 7.5, 'drawdown': 6.0}
        ],
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Slippage/Commission Sensitivity Analysis" in text, "Slippage/commission sensitivity section missing."
    assert "0.0" in text and "0.002" in text, "Slippage/commission values missing."
    assert "Sharpe" in text and "Return" in text and "Drawdown" in text, "Metric headers missing."

def test_markdown_includes_per_period_benchmark_comparison(tmp_path):
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'per_period_benchmark': [
            {'period': '2024', 'strategy_return': 12.0, 'benchmark_return': 10.0},
            {'period': '2025', 'strategy_return': 8.0, 'benchmark_return': 11.0}
        ],
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Per-Period Benchmark Comparison" in text, "Per-period benchmark section missing."
    assert "2024" in text and "2025" in text, "Period labels missing."
    assert "Strategy Return" in text and "Benchmark Return" in text, "Return headers missing."

def test_regime_barplot_handles_series_and_array(tmp_path):
    import pandas as pd
    import numpy as np
    from report_generator import generate_markdown_report

    # Provide regime_series as a pandas Series
    stats_series = {
        'regime_series': pd.Series(['trending', 'ranging', 'trending', 'volatile', 'trending']),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats_series, bt, output_dir=tmp_path)
    barplot_path = tmp_path / "plots/regime_barplot.png"
    assert barplot_path.exists(), "Regime barplot not generated for pandas Series."

    # Provide regime_series as a numpy array
    stats_array = {
        'regime_series': np.array(['trending', 'ranging', 'trending', 'volatile', 'trending']),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    generate_markdown_report(stats_array, bt, output_dir=tmp_path)
    assert barplot_path.exists(), "Regime barplot not generated for numpy array."

def test_regime_breakdown_with_series(tmp_path):
    """
    Test that generate_markdown_report correctly handles a Pandas Series for regime_series and produces a regime breakdown.
    Should not fail due to incorrect use of .values() and should use value_counts().
    """
    import pandas as pd
    from report_generator import generate_markdown_report
    from datetime import datetime, timedelta
    # Create a regime_series as a Pandas Series
    dates = pd.date_range(start="2025-04-01", periods=10)
    regimes = ["trending", "trending", "ranging", "ranging", "volatile", "volatile", "calm", "calm", "calm", "calm"]
    regime_series = pd.Series(regimes, index=dates)
    # Add a minimal trade log (required for regime breakdown)
    trades = [
        {"EntryTime": dates[0], "ExitTime": dates[1], "EntryPrice": 100, "ExitPrice": 105, "PnL": 5.0, "PositionSize": 10, "Rationale": "Test trade", "regime": regimes[0]},
        {"EntryTime": dates[2], "ExitTime": dates[3], "EntryPrice": 102, "ExitPrice": 107, "PnL": 5.0, "PositionSize": 10, "Rationale": "Test trade", "regime": regimes[2]},
        {"EntryTime": dates[4], "ExitTime": dates[5], "EntryPrice": 104, "ExitPrice": 109, "PnL": 5.0, "PositionSize": 10, "Rationale": "Test trade", "regime": regimes[4]},
        {"EntryTime": dates[6], "ExitTime": dates[7], "EntryPrice": 106, "ExitPrice": 111, "PnL": 5.0, "PositionSize": 10, "Rationale": "Test trade", "regime": regimes[6]},
    ]
    stats = {
        "regime_series": regime_series,
        "trades": trades,
        "strategy_params": {"position_size": 1, "initial_cash": 1}
    }
    class DummyBT:
        pass
    # Run report generation
    generate_markdown_report(stats, DummyBT(), output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    # The report should include the regime breakdown
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Regime Breakdown" in text, "Regime breakdown section not found."
    assert "trending" in text and "ranging" in text and "volatile" in text and "calm" in text, "Not all regimes present in breakdown."

def test_report_does_not_show_zero_or_unknown_for_nontrivial_stats(tmp_path):
    """
    The report should not display 'Strategy Return: 0.00%', 'Sharpe: 0.00', 'Max Drawdown: 0.00%',
    'Regime Summary: Unknown: 100%', or 'Rationale Summary: No rationale provided' if the stats dict
    contains valid, nonzero values and summaries. This test exposes the bug described in Task #3.
    """
    stats = {
        'Return [%]': 15.7,
        'Sharpe Ratio': 1.45,
        'Max. Drawdown [%]': -8.2,
        'regime_summary': 'Trending: 70%, Ranging: 20%, Volatile: 10%',
        'rationale_summary': 'Buy on crossover; Sell on crossunder',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    from report_generator import generate_markdown_report
    bt = dummy_bt()  # Provided earlier in this file
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Strategy Return: 0.00%" not in text, "Incorrect zero return shown."
    assert "Sharpe: 0.00" not in text, "Incorrect zero Sharpe shown."
    assert "Max Drawdown: 0.00%" not in text, "Incorrect zero drawdown shown."
    assert "Regime Summary: Unknown: 100%" not in text, "Incorrect regime summary shown."
    assert "Rationale Summary: No rationale provided" not in text, "Incorrect rationale summary shown."

def test_trade_log_no_duplicate_fields(tmp_path):
    import pandas as pd
    stats = {
        'Return [%]': 8.0,
        'Sharpe Ratio': 1.1,
        'Max. Drawdown [%]': -3.0,
        'regime_summary': 'Trending: 70%, Ranging: 20%, Volatile: 10%',
        '_trades': pd.DataFrame([
            {'EntryTime': '2025-04-01', 'EntryPrice': 100, 'ExitTime': '2025-04-10', 'ExitPrice': 110, 'PnL': 10.0, 'PositionSize': 50, 'Rationale': 'Buy: SMA cross'},
            {'EntryTime': '2025-04-15', 'EntryPrice': 105, 'ExitTime': '2025-04-20', 'ExitPrice': 108, 'PnL': 3.0, 'PositionSize': 40, 'Rationale': 'Sell: target hit'}
        ]),
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    
    # Find the Trade Log section
    trade_log_start = text.find("Trade Log")
    assert trade_log_start != -1, "Trade Log section not found in report."
    trade_log_text = text[trade_log_start:]
    # Only consider the first N lines after Trade Log (for the two trades)
    trade_lines = trade_log_text.splitlines()[1:20]  # Read enough lines for two trades
    
    # For each field, ensure only one output per trade (no duplicate key lines)
    fields = ['EntryTime', 'EntryPrice', 'ExitTime', 'ExitPrice', 'PnL', 'PositionSize', 'Rationale']
    for field in fields:
        # Count lines with either bolded or plain key for this field
        bolded = sum(1 for line in trade_lines if f"**{field}:" in line)
        plain = sum(1 for line in trade_lines if f"{field}:" in line and not line.strip().startswith("**"))
        # There should not be both a bolded and a plain line for the same field in the same trade
        assert not (bolded > 0 and plain > 0), f"Duplicate output for field '{field}' in trade log."
        # There should not be more than one output per field per trade
        assert bolded <= 2, f"Field '{field}' appears more than once in bold in trade log."
        assert plain <= 2, f"Field '{field}' appears more than once in plain in trade log."

def test_regime_filter_includes_exact_min_duration(tmp_path):
    import pandas as pd
    # Simulate a regime series with a regime of exactly min_duration days
    min_duration = 5
    # 5 days of 'Trending', then 3 days of 'Ranging'
    dates = pd.date_range('2025-04-01', periods=8)
    regimes = ['Trending'] * 5 + ['Ranging'] * 3
    regime_series = pd.Series(regimes, index=dates)
    # Patch stats to include this regime_series and a dummy trade log
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        'regime_series': regime_series,
        '_trades': pd.DataFrame(),
        'strategy_params': {'position_size': 1, 'initial_cash': 1, 'min_regime_days': 5}
    }
    class DummyBT:
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt, output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # Look for the regime summary table
    summary_start = text.find("## Regime Summary")
    assert summary_start != -1, "Regime Summary section not found in report."
    summary_text = text[summary_start:summary_start+1000]  # Extend window for robustness
    # Look for a Markdown table row with 'Trending' and the expected duration
    found_row = False
    table_lines = []
    for line in summary_text.splitlines():
        if "|" in line:
            table_lines.append(line)
            if "Trending" in line and "5" in line:
                found_row = True
                break
    if not found_row:
        print("\n--- Regime Summary Table Lines ---")
        for l in table_lines:
            print(l)
        print("--- End Regime Summary Table Lines ---\n")
        print("\n--- Full Regime Summary Section ---")
        print(summary_text)
        print("--- End Full Regime Summary Section ---\n")
    assert found_row, "Regime of exactly min_duration days not included as a table row in summary."
