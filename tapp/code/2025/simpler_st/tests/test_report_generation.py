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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
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
    generate_markdown_report(stats, bt)
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
    from report_generator import generate_markdown_report
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
    chart_path = tmp_path / "plots/return_distribution.png"
    # The file may be named differently, so just check for the section in the report
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Return Distribution" in text, "Return distribution section missing in Markdown report."

def test_markdown_includes_trade_heatmap(tmp_path):
    import numpy as np
    import pandas as pd
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': pd.DataFrame({
            'Ticker': ['A', 'B', 'A', 'B'],
            'PnL': [1, -1, 2, -2],
            'Regime': ['Trending', 'Ranging', 'Trending', 'Ranging']
        }),
        'regime_summary': 'Trending: 50%, Ranging: 50%',
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, DummyBT())
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
        generate_markdown_report(stats, DummyBT())
        assert False, "Should raise KeyError if sizing keys are missing."
    except KeyError as e:
        assert "position_size" in str(e) or "initial_cash" in str(e)

def test_markdown_includes_assumptions_section(tmp_path):
    stats = {
        'total_return': 0.1,
        'sharpe_ratio': 1.0,
        'max_drawdown': 0.05,
        'win_rate': 0.6,
        'strategy_params': {'position_size': 1, 'initial_cash': 1}
    }
    class DummyBT:
        _commission = 0.003
        def plot(self, filename=None):
            plt.figure()
            plt.plot([0, 1], [0, 1])
            plt.savefig(filename)
            plt.close()
    bt = DummyBT()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Markdown report not generated."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Assumptions: Slippage and Commission" in text, "Assumptions section missing."
    assert "No explicit slippage is modeled" in text, "Slippage assumption missing."
    assert "commission=0.003" in text, "Commission value missing or incorrect."

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
    generate_markdown_report(stats, bt)
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
    from tech_analysis.backtest import calculate_performance_metrics
    stats = {
        'equity_curve': equity_curve,
        'trades': trades,
        'strategy_params': {'position_size': 1, 'initial_cash': 1},
    }
    # Compute and insert strategy metrics
    stats.update(calculate_performance_metrics(equity_curve, trades))
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt)
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
    generate_markdown_report(stats, bt)
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
