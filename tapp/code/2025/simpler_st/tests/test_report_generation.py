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
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%'
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
        'equity_curve': [10000, 10100, 10200, 10300, 10400]
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
        ])
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
        'regime_summary': 'Trending: 30%, Ranging: 50%, Volatile: 20%'
    }
    bt = dummy_bt()
    os.chdir(tmp_path)
    generate_markdown_report(stats, bt)
    md_path = tmp_path / "reports/portfolio_report.md"
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Analyst Notes and Suggestions" in text, "Analyst Notes placeholder not found in Markdown report."

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
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%'
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
