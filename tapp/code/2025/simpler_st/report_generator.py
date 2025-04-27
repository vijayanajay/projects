import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def generate_report(stats, bt, ticker: str):
    # Ensure plots and reports directories exist
    os.makedirs("plots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    # Create plots
    bt.plot(filename=f"plots/{ticker}_equity.png")
    pdf = FPDF()
    # Cover Page
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.cell(200, 20, txt="Technical Analysis Report", ln=1, align='C')
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 15, txt=f"Ticker: {ticker}", ln=1, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cover", ln=1, align='C')
    # Table of Contents
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 15, txt="Table of Contents", ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="1. Cover Page", ln=1)
    pdf.cell(200, 10, txt="2. Table of Contents", ln=1)
    pdf.cell(200, 10, txt="3. Performance Metrics", ln=1)
    pdf.cell(200, 10, txt="4. Trade Log", ln=1)
    pdf.cell(200, 10, txt="5. Regime Summary", ln=1)
    pdf.cell(200, 10, txt="6. Strategy Parameters", ln=1)
    # Section: Performance Metrics
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 12, txt="Performance Metrics", ln=1)
    pdf.set_font("Arial", size=12)
    metrics = [
        f"Return: {stats['Return [%]']:.2f}%",
        f"Sharpe Ratio: {stats['Sharpe Ratio']:.2f}",
        f"Max Drawdown: {stats['Max. Drawdown [%]']:.2f}%",
        f"Commission: {bt._commission}"
    ]
    for metric in metrics:
        pdf.cell(200, 10, txt=metric, ln=1)
    # Section: Regime Summary
    pdf.ln(5)
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 12, txt="Regime Summary", ln=1)
    pdf.set_font("Arial", size=12)
    regime_summary = stats.get('regime_summary')
    if regime_summary:
        pdf.cell(200, 10, txt=f"Regime Summary: {regime_summary}", ln=1)
    # Section: Strategy Parameters
    pdf.ln(5)
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 12, txt="Strategy Parameters", ln=1)
    pdf.set_font("Arial", size=12)
    params = getattr(bt.strategy, 'parameters', None)
    if params:
        for k, v in params.items():
            pdf.cell(200, 10, txt=f"{k}: {v}", ln=1)
    # Section: Trade Log
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 12, txt="Trade Log", ln=1)
    pdf.set_font("Arial", size=12)
    trades = stats.get('_trades') or stats.get('trades')
    if trades is not None and hasattr(trades, 'iterrows'):
        for idx, trade in trades.iterrows():
            summary = f"Entry: {trade['EntryTime']} @ {trade['EntryPrice']} | Exit: {trade['ExitTime']} @ {trade['ExitPrice']} | PnL: {trade['PnL']:.2f}"
            pdf.cell(200, 10, txt=summary, ln=1)
    else:
        pdf.cell(200, 10, txt="No trades.", ln=1)
    try:
        pdf.output(f"reports/{ticker}_report.pdf")
    except Exception as e:
        print(f"PDF generation failed: {e}")
