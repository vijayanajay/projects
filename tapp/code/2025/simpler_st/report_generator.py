import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
import numpy as np

def reusable_chart_component(pdf, image_path, x=10, y=None, w=190):
    """
    Embeds a reusable chart image into the PDF.
    Args:
        pdf: FPDF instance
        image_path: Path to the chart image file
        x, y, w: Image placement and width
    """
    pdf.image(image_path, x=x, y=y, w=w)
    # Add a caption below the chart to reinforce legend presence
    pdf.ln(2)
    pdf.set_font("Arial", style="I", size=10)
    pdf.cell(0, 8, txt="Legend: Equity Curve, SMA, RSI", ln=1)
    pdf.set_font("Arial", size=12)


def generate_report(stats, bt, ticker: str):
    # Ensure plots and reports directories exist
    os.makedirs("plots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    chart_path = f"plots/{ticker}_equity.png"
    equity_curve = stats.get('equity_curve')
    rsi_curve = stats.get('rsi_curve')
    sma_curve = stats.get('sma_curve')
    # Standardize chart style
    def plot_with_standard_style():
        import matplotlib.pyplot as plt
        plt.figure(facecolor='white')
        plt.rcParams.update({
            'font.size': 12,
            'axes.labelsize': 12,
            'axes.titlesize': 14,
            'legend.fontsize': 12,
            'axes.edgecolor': 'gray',
            'axes.linewidth': 1,
            'axes.grid': True,
            'grid.color': '#e0e0e0',
            'axes.prop_cycle': plt.cycler(color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
        })
        if equity_curve is not None and rsi_curve is not None:
            plt.plot(equity_curve, label='Equity Curve')
            plt.plot(rsi_curve, label='RSI', color='purple')
            plt.annotate('RSI Start', xy=(0, rsi_curve[0]), xytext=(0, rsi_curve[0]+5),
                         arrowprops=dict(arrowstyle='->', color='purple'))
        elif equity_curve is not None and sma_curve is not None:
            plt.plot(equity_curve, label='Equity Curve')
            plt.plot(range(len(sma_curve)), sma_curve, label='SMA', color='orange')
            plt.annotate('SMA Start', xy=(10, sma_curve[0]), xytext=(10, sma_curve[0]+5),
                         arrowprops=dict(arrowstyle='->', color='orange'))
        else:
            bt.plot(filename=chart_path)
            return
        plt.legend(loc='best', frameon=True)
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()
    # Always use standardized plot style
    plot_with_standard_style()
    pdf = FPDF()
    # Cover Page
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=20)
    pdf.cell(200, 20, txt="Technical Analysis Report", ln=1, align='C')
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 15, txt=f"Ticker: {ticker}", ln=1, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cover", ln=1, align='C')
    # Table of Contents
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 15, txt="Table of Contents", ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="1. Cover Page", ln=1)
    pdf.cell(200, 10, txt="2. Table of Contents", ln=1)
    pdf.cell(200, 10, txt="3. Performance Metrics", ln=1)
    pdf.cell(200, 10, txt="4. Trade Log", ln=1)
    pdf.cell(200, 10, txt="5. Regime Summary", ln=1)
    pdf.cell(200, 10, txt="6. Strategy Parameters", ln=1)
    pdf.cell(200, 10, txt="7. Analyst Notes and Suggestions", ln=1)
    pdf.cell(200, 10, txt="8. Rationale Summary", ln=1)
    # Section: Performance Metrics
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=14)
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
    # Embed equity curve chart as reusable component
    if os.path.exists(chart_path):
        reusable_chart_component(pdf, chart_path)
    # Minimal implementation for metric distribution visualization with outlier highlighting
    returns_dist = stats.get('returns_distribution')
    if returns_dist is not None:
        metric_chart_path = f"plots/{ticker}_metric_dist.png"
        plt.figure(facecolor='white')
        # Identify outliers (e.g., >2 std from mean)
        mean = np.mean(returns_dist)
        std = np.std(returns_dist)
        outliers = (np.abs(returns_dist - mean) > 2 * std)
        # Plot histogram
        plt.hist(returns_dist[~outliers], bins=20, color='#1f77b4', alpha=0.7, label='Normal')
        if np.any(outliers):
            plt.hist(returns_dist[outliers], bins=5, color='red', alpha=0.8, label='Outlier')
        plt.title('Metric Distribution (Returns)')
        plt.xlabel('Return')
        plt.ylabel('Frequency')
        plt.legend()
        # Annotate if outliers present
        if np.any(outliers):
            plt.annotate('Outlier', xy=(returns_dist[outliers][0], 1), xytext=(returns_dist[outliers][0], 2),
                arrowprops=dict(arrowstyle='->', color='red'))
        plt.tight_layout()
        plt.savefig(metric_chart_path)
        plt.close()
        # Embed in PDF
        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(0, 10, txt="Metric Distribution (Returns)", ln=1)
        reusable_chart_component(pdf, metric_chart_path)
        pdf.set_font("Arial", size=12)
        if np.any(outliers):
            pdf.cell(0, 10, txt="Note: Outlier(s) highlighted in red.", ln=1)
    # Section: Regime Summary
    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 12, txt="Regime Summary", ln=1)
    pdf.set_font("Arial", size=12)
    regime_summary = stats.get('regime_summary')
    if regime_summary:
        pdf.cell(200, 10, txt=f"Regime Summary: {regime_summary}", ln=1)
    # Section: Strategy Parameters
    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 12, txt="Strategy Parameters", ln=1)
    pdf.set_font("Arial", size=12)
    params = getattr(bt.strategy, 'parameters', None)
    if params:
        for k, v in params.items():
            pdf.cell(200, 10, txt=f"{k}: {v}", ln=1)
    # Section: Trade Log
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 12, txt="Trade Log", ln=1)
    pdf.set_font("Arial", size=12)
    trades = stats.get('_trades')
    if trades is None or not hasattr(trades, 'iterrows'):
        trades = stats.get('trades')
    if trades is not None and hasattr(trades, 'iterrows') and hasattr(trades, 'empty') and not trades.empty:
        for idx, trade in trades.iterrows():
            summary = f"Entry: {trade['EntryTime']} @ {trade['EntryPrice']} | Exit: {trade['ExitTime']} @ {trade['ExitPrice']} | PnL: {trade['PnL']:.2f}"
            pdf.cell(200, 10, txt=summary, ln=1)
    else:
        pdf.cell(200, 10, txt="No trades.", ln=1)
    # Section: Rationale Summary
    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 12, txt="Rationale Summary", ln=1)
    pdf.set_font("Arial", size=12)
    rationale_summary = None
    trades = stats.get('_trades')
    if trades is None or not hasattr(trades, 'iterrows'):
        trades = stats.get('trades')
    rationales = []
    if trades is not None and hasattr(trades, 'iterrows') and hasattr(trades, 'empty') and not trades.empty:
        for idx, trade in trades.iterrows():
            rationale = trade.get('rationale')
            if rationale:
                rationales.append(rationale)
    if rationales:
        from collections import Counter
        rationale_counts = Counter(rationales)
        summary_lines = [f"{k}: {v} occurrence(s)" for k, v in rationale_counts.items()]
        rationale_summary = "Rationale summary for trades:\n" + "; ".join(summary_lines)
        pdf.multi_cell(0, 10, txt=rationale_summary)
    else:
        pdf.cell(200, 10, txt="No rationale data available.", ln=1)
    # Section: Analyst Notes & Suggestions
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 12, txt="Analyst Notes and Suggestions", ln=1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="[Placeholder for analyst notes, observations, and improvement suggestions.]")
    try:
        pdf.output(f"reports/{ticker}_report.pdf")
    except Exception as e:
        print(f"PDF generation failed: {e}")
