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
