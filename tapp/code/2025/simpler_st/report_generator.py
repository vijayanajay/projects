import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np

def generate_markdown_report(stats, bt):
    """
    Generates a portfolio report in Markdown format, including all key sections.
    Output file: reports/portfolio_report.md
    """
    os.makedirs("plots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    chart_path = f"plots/portfolio_equity.png"
    equity_curve = stats.get('equity_curve')
    rsi_curve = stats.get('rsi_curve')
    sma_curve = stats.get('sma_curve')
    # Generate chart as in PDF (reuse plotting logic)
    def plot_with_standard_style():
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
        if equity_curve is not None:
            plt.plot(equity_curve, label='Equity Curve', color='#1f77b4')
        if rsi_curve is not None:
            plt.plot(rsi_curve, label='RSI', color='purple')
        if sma_curve is not None:
            plt.plot(range(len(sma_curve)), sma_curve, label='SMA', color='orange')
        if equity_curve is not None:
            plt.legend(loc='best', frameon=True)
            plt.tight_layout()
            plt.savefig(chart_path)
            plt.close()
        else:
            plt.close()
            return
    plot_with_standard_style()
    md_lines = []
    # Cover Page
    md_lines.append("# Technical Analysis Report\n")
    md_lines.append("## Portfolio-Level Report\n")
    md_lines.append("---\n")
    # Table of Contents
    md_lines.append("## Table of Contents\n")
    md_lines.append("1. [Cover Page](#technical-analysis-report)")
    md_lines.append("2. [Table of Contents](#table-of-contents)")
    md_lines.append("3. [Performance Metrics](#performance-metrics)")
    md_lines.append("4. [Trade Log](#trade-log)")
    md_lines.append("5. [Regime Summary](#regime-summary)")
    md_lines.append("6. [Strategy Parameters](#strategy-parameters)")
    md_lines.append("7. [Analyst Notes and Suggestions](#analyst-notes-and-suggestions)")
    md_lines.append("8. [Rationale Summary](#rationale-summary)\n")
    # Section: Performance Metrics
    md_lines.append("## Performance Metrics\n")
    metrics = [
        f"- **Return:** {100 * stats.get('total_return', 0.0):.2f}%",
        f"- **Sharpe Ratio:** {stats.get('sharpe_ratio', 0.0):.2f}",
        f"- **Max Drawdown:** {100 * stats.get('max_drawdown', 0.0):.2f}%",
        f"- **Win Rate:** {100 * stats.get('win_rate', 0.0):.2f}%"
    ]
    md_lines.extend(metrics)
    # Embed equity curve chart
    if os.path.exists(chart_path):
        md_lines.append(f"\n![Equity Curve]({chart_path})\n")
    # Metric Distribution
    returns_dist = stats.get('returns_distribution')
    if returns_dist is not None:
        metric_chart_path = f"plots/portfolio_metric_dist.png"
        plt.figure(facecolor='white')
        mean = np.mean(returns_dist)
        std = np.std(returns_dist)
        outliers = (np.abs(returns_dist - mean) > 2 * std)
        plt.hist(returns_dist[~outliers], bins=20, color='#1f77b4', alpha=0.7, label='Normal')
        if np.any(outliers):
            plt.hist(returns_dist[outliers], bins=5, color='red', alpha=0.8, label='Outlier')
        plt.title('Metric Distribution (Returns)')
        plt.xlabel('Return')
        plt.ylabel('Frequency')
        plt.legend()
        plt.tight_layout()
        plt.savefig(metric_chart_path)
        plt.close()
        md_lines.append(f"\n![Metric Distribution (Returns)]({metric_chart_path})\n")
        if np.any(outliers):
            md_lines.append("Note: Outlier(s) highlighted in red.\n")
    # Section: Regime Summary
    md_lines.append("## Regime Summary\n")
    regime_summary = stats.get('regime_summary')
    if regime_summary:
        md_lines.append(f"{regime_summary}\n")
    # Section: Strategy Parameters
    md_lines.append("## Strategy Parameters\n")
    params = stats.get('strategy_params', {})
    if params:
        for k, v in params.items():
            md_lines.append(f"- **{k}:** {v}")
    else:
        md_lines.append("No strategy parameters available.\n")
    # Section: Trade Log
    md_lines.append("## Trade Log\n")
    trades = stats.get('_trades')
    if trades is None or not hasattr(trades, 'iterrows'):
        trades = stats.get('trades')
    if trades is not None and hasattr(trades, 'iterrows') and hasattr(trades, 'empty') and not trades.empty:
        for idx, trade in trades.iterrows():
            ticker = trade.get('ticker', 'N/A')
            summary = f"- **Ticker:** {ticker} | **Entry:** {trade.get('EntryTime', '')} @ {trade.get('EntryPrice', '')} | **Exit:** {trade.get('ExitTime', '')} @ {trade.get('ExitPrice', '')} | **PnL:** {trade.get('PnL', 0.0):.2f}"
            md_lines.append(summary)
    elif isinstance(trades, list) and len(trades) > 0:
        for trade in trades:
            ticker = trade.get('ticker', 'N/A')
            summary = f"- **Ticker:** {ticker} | **Entry:** {trade.get('EntryTime', '')} @ {trade.get('EntryPrice', '')} | **Exit:** {trade.get('ExitTime', '')} @ {trade.get('ExitPrice', '')} | **PnL:** {trade.get('PnL', 0.0):.2f}"
            md_lines.append(summary)
    else:
        md_lines.append("No trades.\n")
    # Section: Analyst Notes and Suggestions (placeholder)
    md_lines.append("## Analyst Notes and Suggestions\n")
    md_lines.append("(Add your notes here.)\n")
    # Section: Rationale Summary
    md_lines.append("## Rationale Summary\n")
    trades = stats.get('_trades')
    if trades is None or not hasattr(trades, 'iterrows'):
        trades = stats.get('trades')
    rationales = []
    if trades is not None and hasattr(trades, 'iterrows') and hasattr(trades, 'empty') and not trades.empty:
        for idx, trade in trades.iterrows():
            rationale = trade.get('rationale')
            if rationale:
                rationales.append(rationale)
    elif isinstance(trades, list) and len(trades) > 0:
        for trade in trades:
            rationale = trade.get('rationale')
            if rationale:
                rationales.append(rationale)
    if rationales:
        md_lines.append("\n".join([f"- {r}" for r in rationales]))
    else:
        md_lines.append("No rationale provided.\n")
    # Write to Markdown file
    md_path = "reports/portfolio_report.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"[INFO] Markdown report generated at {md_path}")
