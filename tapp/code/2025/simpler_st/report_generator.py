import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def generate_report(stats, bt, ticker: str):
    # Ensure plots and reports directories exist
    os.makedirs("plots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    # Create plots
    bt.plot(filename=f"plots/{ticker}_equity.png")
    # PDF Report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Technical Analysis Report: {ticker}", ln=1)
    pdf.image(f"plots/{ticker}_equity.png", w=180)
    # Add metrics
    metrics = [
        f"Return: {stats['Return [%]']:.2f}%",
        f"Sharpe Ratio: {stats['Sharpe Ratio']:.2f}",
        f"Max Drawdown: {stats['Max. Drawdown [%]']:.2f}%",
        f"Commission: {bt._commission}"
    ]
    for metric in metrics:
        pdf.cell(200, 10, txt=metric, ln=1)
    # Add regime summary if present
    regime_summary = stats.get('regime_summary')
    if regime_summary:
        pdf.cell(200, 10, txt=f"Regime Summary: {regime_summary}", ln=1)
    # Add strategy parameters
    pdf.cell(200, 10, txt="Strategy Parameters:", ln=1)
    params = getattr(bt.strategy, 'parameters', None)
    if params:
        for k, v in params.items():
            pdf.cell(200, 10, txt=f"{k}: {v}", ln=1)
    # Add trade log
    pdf.cell(200, 10, txt="\nTrade Log:", ln=1)
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
