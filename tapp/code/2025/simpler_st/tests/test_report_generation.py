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
