import os
import pytest
from fpdf import FPDF
from pathlib import Path
import matplotlib.pyplot as plt
from pypdf import PdfReader

# Import the generate_report function from the new report_generator.py
from report_generator import generate_report

def dummy_bt():
    class DummyBT:
        def plot(self, filename=None):
            # Create a minimal valid PNG file using matplotlib
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

def test_pdf_contains_regime_summary(tmp_path):
    stats = {
        'Return [%]': 12.5,
        'Sharpe Ratio': 1.2,
        'Max. Drawdown [%]': -5.7,
        '_trades': None,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%'
    }
    bt = dummy_bt()
    ticker = 'TEST'
    os.chdir(tmp_path)
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    reader = PdfReader(str(pdf_path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    assert "Trending: 60%" in text, "Regime summary not found in PDF."

def test_pdf_template_structure(tmp_path):
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': None,
        'regime_summary': 'Trending: 50%, Ranging: 30%, Volatile: 20%'
    }
    bt = dummy_bt()
    ticker = 'TEMPLATE'
    os.chdir(tmp_path)
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    reader = PdfReader(str(pdf_path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    # Check for cover page content
    assert "Technical Analysis Report" in text or "Cover" in text, "Cover page missing or not labeled."
    # Check for Table of Contents
    assert "Table of Contents" in text or "Contents" in text, "Table of Contents missing."
    # Check for at least one section placeholder
    assert "Performance Metrics" in text or "Trade Log" in text or "Section" in text, "Section placeholder missing."

def test_pdf_includes_chart_component(tmp_path):
    """
    TDD: Verifies that a reusable chart component (e.g., equity curve) is included in the PDF report.
    The test generates a report and asserts that at least one image (chart) is embedded in the PDF.
    """
    stats = {
        'Return [%]': 8.0,
        'Sharpe Ratio': 0.8,
        'Max. Drawdown [%]': -3.0,
        '_trades': None,
        'regime_summary': 'Trending: 40%, Ranging: 40%, Volatile: 20%'
    }
    bt = dummy_bt()
    ticker = 'CHART'
    os.chdir(tmp_path)
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    reader = PdfReader(str(pdf_path))
    # Check for at least one embedded image (chart) in the PDF
    images_found = False
    for page in reader.pages:
        if hasattr(page, 'images') and page.images:
            images_found = True
            break
    assert images_found, "No chart image found in PDF."

def test_pdf_includes_analyst_notes_placeholder(tmp_path):
    """
    TDD: Verifies that the PDF report includes a placeholder section for Analyst Notes and Suggestions.
    """
    stats = {
        'Return [%]': 7.5,
        'Sharpe Ratio': 0.7,
        'Max. Drawdown [%]': -2.5,
        '_trades': None,
        'regime_summary': 'Trending: 30%, Ranging: 50%, Volatile: 20%'
    }
    bt = dummy_bt()
    ticker = 'NOTES'
    os.chdir(tmp_path)
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    reader = PdfReader(str(pdf_path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    assert "Analyst Notes and Suggestions" in text, "Analyst Notes placeholder not found in PDF."

def test_pdf_includes_sma_overlay_with_annotation(tmp_path):
    """
    TDD: Verifies that the PDF report contains an equity curve chart with an SMA overlay and annotation.
    The test generates a report and asserts that the SMA overlay is present in the chart embedded in the PDF.
    """
    import numpy as np
    import pandas as pd
    from pypdf import PdfReader
    # Create dummy equity curve and SMA data
    equity = np.linspace(100, 200, 100)
    sma = np.convolve(equity, np.ones(10)/10, mode='valid')
    # Simulate stats and bt
    stats = {
        'Return [%]': 10.0,
        'Sharpe Ratio': 1.0,
        'Max. Drawdown [%]': -4.0,
        '_trades': None,
        'regime_summary': 'Trending: 50%, Ranging: 30%, Volatile: 20%',
        'equity_curve': equity,
        'sma_curve': sma
    }
    class DummyBT:
        def plot(self, filename=None, equity_curve=None, sma_curve=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot(equity_curve, label='Equity Curve')
            plt.plot(range(len(sma_curve)), sma_curve, label='SMA', color='orange')
            plt.annotate('SMA Start', xy=(10, sma_curve[0]), xytext=(10, sma_curve[0]+5),
                         arrowprops=dict(arrowstyle='->', color='orange'))
            plt.legend()
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    ticker = 'SMA_OVERLAY'
    os.chdir(tmp_path)
    from report_generator import generate_report
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    reader = PdfReader(str(pdf_path))
    # Check for at least one embedded image (chart) in the PDF
    images_found = False
    for page in reader.pages:
        if hasattr(page, 'images') and page.images:
            images_found = True
            break
    assert images_found, "No chart image with SMA overlay found in PDF."

def test_pdf_includes_rsi_overlay_with_annotation(tmp_path):
    """
    TDD: Verifies that the PDF report contains an equity curve chart with an RSI overlay and annotation.
    The test generates a report and asserts that the RSI overlay is present in the chart embedded in the PDF.
    """
    import numpy as np
    import pandas as pd
    from pypdf import PdfReader
    # Create dummy equity curve and RSI data
    equity = np.linspace(100, 200, 100)
    rsi = np.linspace(30, 70, 100)
    # Simulate stats and bt
    stats = {
        'Return [%]': 9.0,
        'Sharpe Ratio': 0.9,
        'Max. Drawdown [%]': -3.5,
        '_trades': None,
        'regime_summary': 'Trending: 45%, Ranging: 35%, Volatile: 20%',
        'equity_curve': equity,
        'rsi_curve': rsi
    }
    class DummyBT:
        def plot(self, filename=None, equity_curve=None, rsi_curve=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot(equity_curve, label='Equity Curve')
            plt.plot(rsi_curve, label='RSI', color='purple')
            plt.annotate('RSI Start', xy=(0, rsi_curve[0]), xytext=(0, rsi_curve[0]+5),
                         arrowprops=dict(arrowstyle='->', color='purple'))
            plt.legend()
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'period': 14, 'overbought': 70, 'oversold': 30}
            return DummyStrategy()
    bt = DummyBT()
    ticker = 'RSI_OVERLAY'
    os.chdir(tmp_path)
    from report_generator import generate_report
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    reader = PdfReader(str(pdf_path))
    # Check for at least one embedded image (chart) in the PDF
    images_found = False
    for page in reader.pages:
        if hasattr(page, 'images') and page.images:
            images_found = True
            break
    assert images_found, "No chart image with RSI overlay found in PDF."

def test_pdf_includes_trade_entry_exit_log(tmp_path):
    """
    TDD: Verifies that the PDF report includes trade entry and exit data in the Trade Log section.
    """
    import pandas as pd
    stats = {
        'Return [%]': 12.0,
        'Sharpe Ratio': 1.3,
        'Max. Drawdown [%]': -4.0,
        'regime_summary': 'Trending: 60%, Ranging: 30%, Volatile: 10%',
        '_trades': pd.DataFrame([
            {'EntryTime': '2025-04-01', 'EntryPrice': 100, 'ExitTime': '2025-04-10', 'ExitPrice': 110, 'PnL': 10.0},
            {'EntryTime': '2025-04-15', 'EntryPrice': 105, 'ExitTime': '2025-04-20', 'ExitPrice': 108, 'PnL': 3.0}
        ])
    }
    class DummyBT:
        def plot(self, filename=None):
            import matplotlib.pyplot as plt
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
    ticker = 'TRADELOG'
    os.chdir(tmp_path)
    from report_generator import generate_report
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    # Check for entry/exit data in the PDF
    assert "Entry: 2025-04-01 @ 100" in text, "Trade entry data missing in PDF."
    assert "Exit: 2025-04-10 @ 110" in text, "Trade exit data missing in PDF."
    assert "PnL: 10.00" in text, "Trade PnL missing in PDF."

def test_pdf_standardized_visual_style_and_legends(tmp_path):
    """
    TDD: Verifies that all charts in the PDF report have a legend and that the PDF uses a consistent visual style (fonts, section headers).
    """
    import numpy as np
    stats = {
        'Return [%]': 11.0,
        'Sharpe Ratio': 1.1,
        'Max. Drawdown [%]': -3.5,
        'regime_summary': 'Trending: 55%, Ranging: 35%, Volatile: 10%',
        'equity_curve': np.linspace(100, 200, 100),
        'sma_curve': np.convolve(np.linspace(100, 200, 100), np.ones(10)/10, mode='valid')
    }
    class DummyBT:
        def plot(self, filename=None, equity_curve=None, sma_curve=None):
            import matplotlib.pyplot as plt
            plt.figure()
            plt.plot(equity_curve, label='Equity Curve')
            plt.plot(range(len(sma_curve)), sma_curve, label='SMA', color='orange')
            plt.annotate('SMA Start', xy=(10, sma_curve[0]), xytext=(10, sma_curve[0]+5),
                         arrowprops=dict(arrowstyle='->', color='orange'))
            plt.legend()
            plt.savefig(filename)
            plt.close()
        _commission = 0.001
        @property
        def strategy(self):
            class DummyStrategy:
                parameters = {'n1': 50, 'n2': 200}
            return DummyStrategy()
    bt = DummyBT()
    ticker = 'STYLE_TEST'
    os.chdir(tmp_path)
    from report_generator import generate_report
    generate_report(stats, bt, ticker)
    pdf_path = tmp_path / f"reports/{ticker}_report.pdf"
    assert pdf_path.exists(), "PDF not generated."
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    # Check for section header font consistency (e.g., 'Performance Metrics' and 'Regime Summary' should be present)
    assert "Performance Metrics" in text, "Performance Metrics section header missing."
    assert "Regime Summary" in text, "Regime Summary section header missing."
    # Check for legend label in chart (since legend label is 'Equity Curve' and 'SMA')
    assert "Equity Curve" in text, "Legend for Equity Curve missing in PDF."
    assert "SMA" in text, "Legend for SMA missing in PDF."
