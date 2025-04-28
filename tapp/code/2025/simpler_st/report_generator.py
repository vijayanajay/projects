import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import seaborn as sns

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
    md_lines.append("7. [Risk and Position Sizing Logic](#risk-and-position-sizing-logic)")
    md_lines.append("8. [Analyst Notes and Suggestions](#analyst-notes-and-suggestions)")
    md_lines.append("9. [Rationale Summary](#rationale-summary)\n")
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
    # Drawdown Curve Visualization
    drawdown_curve = stats.get('drawdown_curve')
    drawdown_chart_path = f"plots/drawdown_curve.png"
    if drawdown_curve is not None:
        plt.figure(facecolor='white')
        plt.plot(drawdown_curve, label='Drawdown', color='red')
        plt.title('Drawdown Curve')
        plt.xlabel('Time')
        plt.ylabel('Drawdown')
        plt.legend()
        plt.tight_layout()
        plt.savefig(drawdown_chart_path)
        plt.close()
        md_lines.append(f"\n## Drawdown Curve\n")
        md_lines.append(f"![Drawdown Curve]({drawdown_chart_path})\n")

    # Return Distribution Visualization (dedicated section)
    returns_dist = stats.get('returns_distribution')
    return_dist_chart_path = f"plots/return_distribution.png"
    if returns_dist is not None:
        plt.figure(facecolor='white')
        mean = np.mean(returns_dist)
        std = np.std(returns_dist)
        outliers = (np.abs(returns_dist - mean) > 2 * std)
        plt.hist(returns_dist[~outliers], bins=20, color='#1f77b4', alpha=0.7, label='Normal')
        if np.any(outliers):
            plt.hist(returns_dist[outliers], bins=5, color='red', alpha=0.8, label='Outlier')
        plt.title('Return Distribution')
        plt.xlabel('Return')
        plt.ylabel('Frequency')
        plt.legend()
        plt.tight_layout()
        plt.savefig(return_dist_chart_path)
        plt.close()
        md_lines.append(f"\n## Return Distribution\n")
        md_lines.append(f"![Return Distribution]({return_dist_chart_path})\n")
        if np.any(outliers):
            md_lines.append("Note: Outlier(s) highlighted in red.\n")

    # Section: Regime Summary
    md_lines.append("## Regime Summary\n")
    # Dynamically add regime definitions and classification criteria using actual parameters
    params = stats.get('strategy_params', {})
    short_sma = params.get('short_window', 20)
    long_sma = params.get('long_window', 50)
    min_days = params.get('min_regime_days', 4)
    rsi_period = params.get('rsi_period', 14)
    overbought = params.get('overbought', 70)
    oversold = params.get('oversold', 30)
    md_lines.append("**Regime Definitions and Classification Criteria:**\n")
    md_lines.append(f"- **Trending:** A period where price exhibits a clear upward or downward movement, typically identified by the short-term SMA (window: {short_sma}) being consistently above (uptrend) or below (downtrend) the long-term SMA (window: {long_sma}) for more than {min_days - 1} days.\n")
    md_lines.append(f"- **Ranging:** A period where price oscillates within a horizontal channel, identified when the short-term SMA crosses above and below the long-term SMA frequently, with no sustained trend for more than {min_days - 1} days.\n")
    md_lines.append("- **Quantitative Parameters:**\n" +
        f"**Short SMA window:** {short_sma} days\n" +
        f"**Long SMA window:** {long_sma} days\n" +
        f"**Minimum regime duration:** {min_days} days (regimes shorter than this are filtered out)\n" +
        f"**RSI period:** {rsi_period}\n" +
        f"**RSI thresholds:** Overbought ({overbought}), Oversold ({oversold})\n"
    )
    regime_summary = stats.get('regime_summary')
    if regime_summary:
        md_lines.append(f"{regime_summary}\n")
    # Render filtered regime series table
    regime_series = stats.get('regime_series')
    if regime_series is not None and len(regime_series) > 0:
        # Pass min_days to the filter function
        def filter_regime_series(series, min_duration):
            filtered = []
            prev_regime = None
            start_date = None
            count = 0
            threshold = min_duration - 1 # Check against min_duration - 1
            for date, regime in series.items():
                if regime != prev_regime:
                    # Use the threshold derived from min_duration
                    if prev_regime is not None and count > threshold:
                        filtered.append((start_date, date, prev_regime, count))
                    start_date = date
                    count = 1
                    prev_regime = regime
                else:
                    count += 1
            # Handle last segment, using the threshold
            if prev_regime is not None and count > threshold:
                filtered.append((start_date, date, prev_regime, count))
            return filtered
        # Call the function with the min_days parameter
        filtered_regimes = filter_regime_series(regime_series, min_days)
        if filtered_regimes:
            md_lines.append("\n| Start Date | End Date | Regime | Days |\n|---|---|---|---|")
            for start, end, regime, days in filtered_regimes:
                md_lines.append(f"| {start} | {end} | {regime} | {days} |")
        else:
            # Update the message to use min_days
            md_lines.append(f"\n_No regime persisted more than {min_days - 1} days in a row._\n")
    # Trade-level chart with entry/exit markers and indicator overlays
    trade_chart_path = f"plots/trade_chart.png"
    price = stats.get('equity_curve')
    sma = stats.get('sma_curve')
    rsi = stats.get('rsi_curve')
    trades = stats.get('_trades')
    if trades is None or not hasattr(trades, 'iterrows'):
        trades = stats.get('trades')
    if price is not None and sma is not None and trades is not None:
        plt.figure(facecolor='white')
        plt.plot(price, label='Price', color='#1f77b4')
        plt.plot(sma, label='SMA', color='orange')
        if rsi is not None:
            ax1 = plt.gca()
            ax2 = ax1.twinx()
            ax2.plot(rsi, label='RSI', color='purple', alpha=0.4)
            ax2.set_ylabel('RSI', color='purple')
        # Plot trade entry/exit markers
        if hasattr(trades, 'iterrows'):
            for idx, trade in trades.iterrows():
                entry = trade.get('EntryTime')
                entry_price = trade.get('EntryPrice')
                exit = trade.get('ExitTime')
                exit_price = trade.get('ExitPrice')
                if entry is not None and entry_price is not None:
                    plt.scatter(entry, entry_price, marker='^', color='green', label='Entry' if idx == 0 else "")
                if exit is not None and exit_price is not None:
                    plt.scatter(exit, exit_price, marker='v', color='red', label='Exit' if idx == 0 else "")
        elif isinstance(trades, list):
            for i, trade in enumerate(trades):
                entry = trade.get('EntryTime')
                entry_price = trade.get('EntryPrice')
                exit = trade.get('ExitTime')
                exit_price = trade.get('ExitPrice')
                if entry is not None and entry_price is not None:
                    plt.scatter(entry, entry_price, marker='^', color='green', label='Entry' if i == 0 else "")
                if exit is not None and exit_price is not None:
                    plt.scatter(exit, exit_price, marker='v', color='red', label='Exit' if i == 0 else "")
        plt.legend(loc='best', frameon=True)
        plt.title('Trade Chart with Entry/Exit and Indicators')
        plt.tight_layout()
        plt.savefig(trade_chart_path)
        plt.close()
    # Embed trade-level chart in Markdown
    if os.path.exists(trade_chart_path):
        md_lines.append(f"\n![Trade Chart]({trade_chart_path})\n")
    # Trade Outcome Heatmap Visualization
    heatmap_chart_path = f"plots/trade_heatmap.png"
    if trades is not None and isinstance(trades, pd.DataFrame):
        # Minimal: Heatmap by Ticker vs Regime, values = mean PnL
        if all(col in trades.columns for col in ['Ticker', 'Regime', 'PnL']):
            pivot = trades.pivot_table(index='Ticker', columns='Regime', values='PnL', aggfunc='mean', fill_value=0)
            plt.figure(figsize=(6,4), facecolor='white')
            sns.heatmap(pivot, annot=True, fmt=".2f", cmap="RdYlGn", cbar=True)
            plt.title('Trade Outcome Heatmap (Mean PnL by Ticker & Regime)')
            plt.tight_layout()
            plt.savefig(heatmap_chart_path)
            plt.close()
            md_lines.append(f"\n## Trade Outcome Heatmap\n")
            md_lines.append(f"![Trade Outcome Heatmap]({heatmap_chart_path})\n")
    # Section: Strategy Parameters
    md_lines.append("## Strategy Parameters\n")
    params = stats.get('strategy_params', {})
    if params:
        for k, v in params.items():
            md_lines.append(f"- **{k}:** {v}")
    else:
        md_lines.append("No strategy parameters available.\n")
    # Section: Risk and Position Sizing Logic
    if 'position_size' not in params or 'initial_cash' not in params:
        raise KeyError("Both 'position_size' and 'initial_cash' must be present in strategy parameters (from config.json).")
    position_size = params['position_size']
    initial_cash = params['initial_cash']
    md_lines.append("\n## Risk and Position Sizing Logic\n")
    md_lines.append(f"Each trade allocates capital using a fixed position size (set to: {position_size} currency units per trade, initial cash: {initial_cash}). The number of shares bought is calculated as:\n")
    md_lines.append("\n    qty = int(position_size // price)\n")
    md_lines.append("\nThis ensures that:\n- No trade exceeds the specified position size or available cash.\n- No leverage or short selling is used.\n- Trades are only executed if sufficient cash is available.\n\nThis simple approach provides basic risk control by capping exposure per trade and preventing over-allocation. More advanced risk management (e.g., stop-loss, volatility targeting) is not implemented in this version.\n")
    # Section: Trade Log
    md_lines.append("## Trade Log\n")
    trades = stats.get('_trades')
    if trades is None or not hasattr(trades, 'iterrows'):
        trades = stats.get('trades')
    if trades is not None and hasattr(trades, 'iterrows') and hasattr(trades, 'empty') and not trades.empty:
        for idx, trade in trades.iterrows():
            ticker = trade.get('ticker', trade.get('Ticker', ''))
            rationale = trade.get('rationale', trade.get('Rationale', ''))
            md_lines.append(f"**Ticker:** {ticker}")
            md_lines.append(f"**Entry:** {trade.get('EntryTime', '')}")
            md_lines.append(f"**Entry Price:** {trade.get('EntryPrice', '')}")
            md_lines.append(f"**Exit:** {trade.get('ExitTime', '')}")
            md_lines.append(f"**Exit Price:** {trade.get('ExitPrice', '')}")
            md_lines.append(f"**Position Size:** {trade.get('PositionSize', '')}")
            md_lines.append(f"**PnL:** {trade.get('PnL', 0.0):.2f}")
            md_lines.append(f"**Rationale:** {rationale}\n")
    elif isinstance(trades, list) and len(trades) > 0:
        for trade in trades:
            ticker = trade.get('ticker', trade.get('Ticker', ''))
            rationale = trade.get('rationale', trade.get('Rationale', ''))
            md_lines.append(f"**Ticker:** {ticker}")
            md_lines.append(f"**Entry:** {trade.get('EntryTime', '')}")
            md_lines.append(f"**Entry Price:** {trade.get('EntryPrice', '')}")
            md_lines.append(f"**Exit:** {trade.get('ExitTime', '')}")
            md_lines.append(f"**Exit Price:** {trade.get('ExitPrice', '')}")
            md_lines.append(f"**Position Size:** {trade.get('PositionSize', '')}")
            md_lines.append(f"**PnL:** {trade.get('PnL', 0.0):.2f}")
            md_lines.append(f"**Rationale:** {rationale}\n")
    else:
        md_lines.append("No trades.\n")
    # Section: Analyst Notes and Suggestions (substantive note)
    md_lines.append("## Analyst Notes and Suggestions\n")
    analyst_note = stats.get('analyst_notes', None)
    if analyst_note:
        md_lines.append(f"{analyst_note}\n")
    else:
        md_lines.append("The strategy underperformed in ranging markets; consider parameter tuning or regime filtering.\n")
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
