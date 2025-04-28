import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import seaborn as sns

def generate_markdown_report(stats, bt, parameter_sensitivity_results=None):
    """
    Generates a portfolio report in Markdown format, including all key sections.
    Output file: reports/portfolio_report.md
    """
    os.makedirs("plots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    # --- Pre-initialize chart path variables to None to avoid UnboundLocalError ---
    abs_legacy_equity_chart_path = None
    abs_chart_path = None
    abs_drawdown_chart_path = None
    abs_return_dist_chart_path = None
    md_lines = []
    # --- Equity Curve Chart (legacy, always present) ---
    legacy_equity_chart_path = f"plots/portfolio_equity.png"
    equity_curve = stats.get('equity_curve')
    # If dict (multi-ticker), pick first ticker for legacy chart
    if isinstance(equity_curve, dict):
        first_ticker = next(iter(equity_curve)) if equity_curve else None
        equity_curve_legacy = equity_curve.get(first_ticker) if first_ticker else None
    else:
        equity_curve_legacy = equity_curve
    if equity_curve_legacy is not None:
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
            'axes.prop_cycle': plt.cycler(color=["#1f77b4"])
        })
        plt.plot(equity_curve_legacy, label='Equity Curve', color='#1f77b4')
        plt.legend(loc='best', frameon=True)
        plt.tight_layout()
        abs_legacy_equity_chart_path = os.path.abspath(legacy_equity_chart_path)
        os.makedirs(os.path.dirname(abs_legacy_equity_chart_path), exist_ok=True)
        plt.savefig(abs_legacy_equity_chart_path)
        plt.close()

    # --- Benchmark Comparison Plot (new, if both present) ---
    benchmark_curve = stats.get('benchmark_curve') or stats.get('benchmark_equity_curve')
    chart_path = f"plots/benchmark_comparison.png"
    benchmark_name = stats.get('benchmark_name', 'Benchmark')
    # Handle dicts for benchmark too
    if isinstance(benchmark_curve, dict):
        benchmark_curve_legacy = benchmark_curve.get(first_ticker) if first_ticker else None
    else:
        benchmark_curve_legacy = benchmark_curve
    if equity_curve_legacy is not None and benchmark_curve_legacy is not None:
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
            'axes.prop_cycle': plt.cycler(color=["#1f77b4", "#ff7f0e"])
        })
        plt.plot(equity_curve_legacy, label='Portfolio', color='#1f77b4')
        plt.plot(benchmark_curve_legacy, label=benchmark_name, color='#ff7f0e', linestyle='--')
        plt.legend(loc='best', frameon=True)
        plt.title(f"Portfolio vs {benchmark_name}")
        plt.tight_layout()
        abs_chart_path = os.path.abspath(chart_path)
        os.makedirs(os.path.dirname(abs_chart_path), exist_ok=True)
        plt.savefig(abs_chart_path)
        plt.close()

    # --- Drawdown Curve Visualization ---
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
        abs_drawdown_chart_path = os.path.abspath(drawdown_chart_path)
        os.makedirs(os.path.dirname(abs_drawdown_chart_path), exist_ok=True)
        plt.savefig(abs_drawdown_chart_path)
        plt.close()

    # --- Return Distribution Visualization ---
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
        abs_return_dist_chart_path = os.path.abspath(return_dist_chart_path)
        os.makedirs(os.path.dirname(abs_return_dist_chart_path), exist_ok=True)
        plt.savefig(abs_return_dist_chart_path)
        plt.close()

    # --- Drawdown Table Section ---
    equity_curve = stats.get('equity_curve')
    # Defensive: handle dict (multi-ticker) vs. list/array (single-ticker)
    equity_curve_for_drawdown = equity_curve
    if isinstance(equity_curve, dict):
        first_ticker = next(iter(equity_curve)) if equity_curve else None
        equity_curve_for_drawdown = equity_curve.get(first_ticker) if first_ticker else None
    if equity_curve_for_drawdown is not None:
        from tech_analysis.backtest import extract_drawdown_periods
        periods = extract_drawdown_periods(equity_curve_for_drawdown)
        if periods:
            df = pd.DataFrame(periods)
            df2 = df.copy()
            df2['depth'] = (df2['depth'] * 100).round(2)
            df2 = df2.rename(columns={'start': 'Start', 'trough': 'Trough', 'end': 'End', 'depth': 'Depth (%)', 'recovery': 'Recovery (bars)'})
            plots_dir = os.path.join(os.getcwd(), 'plots')
            os.makedirs(plots_dir, exist_ok=True)
            table_path = os.path.join(plots_dir, 'drawdown_table.png')
            fig, ax = plt.subplots(figsize=(min(10, 2+len(df2)*0.5), 1+0.5*len(df2)))
            ax.axis('off')
            tbl = ax.table(cellText=df2.values, colLabels=df2.columns, loc='center', cellLoc='center')
            tbl.auto_set_font_size(False)
            tbl.set_fontsize(10)
            tbl.scale(1, 1.5)
            plt.tight_layout()
            plt.savefig(table_path, bbox_inches='tight', dpi=150)
            plt.close(fig)
            md_lines = []
            md_lines.append('## Drawdown Table\n')
            md_lines.append('![](plots/drawdown_table.png)\n')

    # --- Holding Duration Histogram ---
    holding_duration_chart_path = f"plots/holding_duration.png"
    trade_log = stats.get('trades') or stats.get('_trades')
    holding_durations = []
    if isinstance(trade_log, pd.DataFrame) and not trade_log.empty:
        for idx, trade in trade_log.iterrows():
            entry = trade.get('EntryTime')
            exit = trade.get('ExitTime')
            if entry and exit:
                try:
                    entry_dt = pd.to_datetime(entry)
                    exit_dt = pd.to_datetime(exit)
                    duration = (exit_dt - entry_dt).days
                    if duration >= 0:
                        holding_durations.append(duration)
                except Exception:
                    continue
    elif isinstance(trade_log, list):
        for trade in trade_log:
            entry = trade.get('EntryTime')
            exit = trade.get('ExitTime')
            if entry and exit:
                try:
                    entry_dt = pd.to_datetime(entry)
                    exit_dt = pd.to_datetime(exit)
                    duration = (exit_dt - entry_dt).days
                    if duration >= 0:
                        holding_durations.append(duration)
                except Exception:
                    continue
    if holding_durations:
        plt.figure(facecolor='white')
        plt.hist(holding_durations, bins=range(1, max(holding_durations)+2), color='#1f77b4', alpha=0.7, rwidth=0.85)
        plt.title('Trade Holding Duration Distribution')
        plt.xlabel('Holding Duration (days)')
        plt.ylabel('Number of Trades')
        plt.tight_layout()
        abs_holding_duration_chart_path = os.path.abspath(holding_duration_chart_path)
        os.makedirs(os.path.dirname(abs_holding_duration_chart_path), exist_ok=True)
        plt.savefig(abs_holding_duration_chart_path)
        plt.close()

    # --- Markdown Content ---
    md_lines = []
    # Cover Page
    md_lines.append("# Technical Analysis Report\n")
    md_lines.append("## Portfolio-Level Report\n")
    md_lines.append("---\n")
    # Table of Contents
    md_lines.append("## Table of Contents\n")
    md_lines.append("1. [Cover Page](#technical-analysis-report)")
    md_lines.append("2. [Table of Contents](#table-of-contents)")
    md_lines.append("3. [Assumptions: Slippage and Commission](#assumptions-slippage-and-commission)")
    md_lines.append("4. [Performance Metrics](#performance-metrics)")
    md_lines.append("5. [Benchmark Comparison](#benchmark-comparison)")
    md_lines.append("6. [Trade Log](#trade-log)")
    md_lines.append("7. [Regime Summary](#regime-summary)")
    md_lines.append("8. [Strategy Parameters](#strategy-parameters)")
    md_lines.append("9. [Risk and Position Sizing Logic](#risk-and-position-sizing-logic)")
    md_lines.append("10. [Analyst Notes and Suggestions](#analyst-notes-and-suggestions)")
    md_lines.append("11. [Rationale Summary](#rationale-summary)")
    md_lines.append("12. [Trade Statistics Breakdown](#trade-statistics-breakdown)")
    md_lines.append("13. [Regime Breakdown](#regime-breakdown)\n")
    # Drawdown Table Section (must appear early in report)
    equity_curve = stats.get('equity_curve')
    # Defensive: handle dict (multi-ticker) vs. list/array (single-ticker)
    equity_curve_for_drawdown = equity_curve
    if isinstance(equity_curve, dict):
        first_ticker = next(iter(equity_curve)) if equity_curve else None
        equity_curve_for_drawdown = equity_curve.get(first_ticker) if first_ticker else None
    if equity_curve_for_drawdown is not None:
        from tech_analysis.backtest import extract_drawdown_periods
        periods = extract_drawdown_periods(equity_curve_for_drawdown)
        if periods:
            df = pd.DataFrame(periods)
            df2 = df.copy()
            df2['depth'] = (df2['depth'] * 100).round(2)
            df2 = df2.rename(columns={'start': 'Start', 'trough': 'Trough', 'end': 'End', 'depth': 'Depth (%)', 'recovery': 'Recovery (bars)'})
            plots_dir = os.path.join(os.getcwd(), 'plots')
            os.makedirs(plots_dir, exist_ok=True)
            table_path = os.path.join(plots_dir, 'drawdown_table.png')
            fig, ax = plt.subplots(figsize=(min(10, 2+len(df2)*0.5), 1+0.5*len(df2)))
            ax.axis('off')
            tbl = ax.table(cellText=df2.values, colLabels=df2.columns, loc='center', cellLoc='center')
            tbl.auto_set_font_size(False)
            tbl.set_fontsize(10)
            tbl.scale(1, 1.5)
            plt.tight_layout()
            plt.savefig(table_path, bbox_inches='tight', dpi=150)
            plt.close(fig)
            md_lines.append('## Drawdown Table\n')
            md_lines.append('![](plots/drawdown_table.png)\n')
    # Section: Assumptions
    md_lines.append("## Assumptions: Slippage and Commission\n")
    commission = getattr(bt, '_commission', stats.get('strategy_params', {}).get('commission', 0.002))
    slippage = getattr(bt, '_slippage', stats.get('strategy_params', {}).get('slippage', 0.0))
    md_lines.append(f"- **Slippage:** A slippage of {slippage} per trade is applied to all executions (entry and exit prices adjusted by ±slippage). (slippage={slippage})\n")
    md_lines.append(f"- **Commission:** A fixed commission rate of {commission * 100:.2f}% per trade is applied, as set in the backtesting engine (commission={commission}).\n")
    md_lines.append("\nThese assumptions may affect real-world applicability and should be reviewed for live trading scenarios.\n")
    # Section: Performance Metrics
    md_lines.append("## Performance Metrics\n")
    strat_metrics = stats.get('strategy', {})
    bench_metrics = stats.get('benchmark', {})
    metrics = [
        f"- **Strategy Return:** {100 * strat_metrics.get('total_return', 0.0):.2f}%",
        f"- **Strategy Sharpe Ratio:** {strat_metrics.get('sharpe_ratio', 0.0):.2f}",
        f"- **Strategy Max Drawdown:** {100 * strat_metrics.get('max_drawdown', 0.0):.2f}%",
        f"- **Strategy Win Rate:** {100 * strat_metrics.get('win_rate', 0.0):.2f}%"
    ]
    if bench_metrics:
        metrics.extend([
            f"- **Benchmark Return:** {100 * bench_metrics.get('total_return', 0.0):.2f}%",
            f"- **Benchmark Sharpe Ratio:** {bench_metrics.get('sharpe_ratio', 0.0):.2f}",
            f"- **Benchmark Max Drawdown:** {100 * bench_metrics.get('max_drawdown', 0.0):.2f}%",
            f"- **Benchmark Win Rate:** {100 * bench_metrics.get('win_rate', 0.0):.2f}%"
        ])
    md_lines.extend(metrics)
    # Embed equity curve chart (legacy)
    if abs_legacy_equity_chart_path is not None and os.path.exists(abs_legacy_equity_chart_path):
        md_lines.append(f"\n![Equity Curve]({legacy_equity_chart_path})\n")
    # Benchmark Comparison Section (new)
    if abs_chart_path is not None and os.path.exists(abs_chart_path):
        md_lines.append(f"\n## Benchmark Comparison\n")
        md_lines.append(f"![]({chart_path})\n")
        # Minimal table comparing returns if both present
        strat_return = stats.get('Return [%]', None)
        bench_curve = stats.get('benchmark_curve') or stats.get('benchmark_equity_curve')
        if strat_return is not None and bench_curve is not None:
            # Calculate benchmark return as percent change from first to last
            bench_return = 100 * (bench_curve[-1] - bench_curve[0]) / bench_curve[0]
            md_lines.append("\n| Metric | Portfolio | " + benchmark_name + " |\n|---|---|---|")
            md_lines.append(f"| Total Return (%) | {strat_return:.2f} | {bench_return:.2f} |\n")
    # Drawdown Curve Section
    if abs_drawdown_chart_path is not None and os.path.exists(abs_drawdown_chart_path):
        md_lines.append(f"\n## Drawdown Curve\n")
        md_lines.append(f"![Drawdown Curve]({drawdown_chart_path})\n")
    # Return Distribution Section
    if abs_return_dist_chart_path is not None and os.path.exists(abs_return_dist_chart_path):
        md_lines.append(f"\n## Return Distribution\n")
        md_lines.append(f"![Return Distribution]({return_dist_chart_path})\n")
        if returns_dist is not None:
            mean = np.mean(returns_dist)
            std = np.std(returns_dist)
            outliers = (np.abs(returns_dist - mean) > 2 * std)
            if np.any(outliers):
                md_lines.append("Note: Outlier(s) highlighted in red.\n")
    # Section: Trade Log
    md_lines.append("## Trade Log\n")
    trade_log = stats.get('trades') or stats.get('_trades')
    if isinstance(trade_log, pd.DataFrame):
        has_trades = not trade_log.empty
    else:
        has_trades = bool(trade_log)
    if has_trades:
        if isinstance(trade_log, pd.DataFrame):
            for idx, trade in trade_log.iterrows():
                if hasattr(trade, 'get'):
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
                    md_lines.append(f"**Trade:** {str(trade)}\n")
        elif isinstance(trade_log, list):
            for trade in trade_log:
                if hasattr(trade, 'get'):
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
                    md_lines.append(f"**Trade:** {str(trade)}\n")
    else:
        md_lines.append("No trades.\n")
    # Section: Regime Summary
    md_lines.append("## Regime Summary\n")
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
    # Only plot summary chart if price and sma are 1D (not dict)
    if price is not None and sma is not None and trades is not None and not isinstance(price, dict) and not isinstance(sma, dict):
        plt.figure(facecolor='white')
        plt.plot(price, label='Price', color='#1f77b4')
        plt.plot(sma, label='SMA', color='orange')
        if rsi is not None and not isinstance(rsi, dict):
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
        plt.title('Trade Chart with Entry/Exit, SMA, Regime')
        plt.tight_layout()
        abs_trade_chart_path = os.path.abspath(trade_chart_path)
        os.makedirs(os.path.dirname(abs_trade_chart_path), exist_ok=True)
        plt.savefig(abs_trade_chart_path)
        plt.close()
        if os.path.exists(abs_trade_chart_path):
            md_lines.append(f"\n![Trade Chart]({trade_chart_path})\n")
    # If price is a dict (multi-ticker), skip this summary chart (per-ticker charts are generated below)
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
            abs_heatmap_chart_path = os.path.abspath(heatmap_chart_path)
            os.makedirs(os.path.dirname(abs_heatmap_chart_path), exist_ok=True)
            plt.savefig(abs_heatmap_chart_path)
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
    percent_risked = (position_size / initial_cash) * 100 if initial_cash else 0
    max_positions = params.get('max_simultaneous_positions', None)
    md_lines.append("\n## Risk and Position Sizing Logic\n")
    md_lines.append(f"- **% Risked Per Trade:** {percent_risked:.2f}% of initial capital allocated to each trade (position_size={position_size}, initial_cash={initial_cash}).")
    md_lines.append("- **Allocation Rule:** Fixed allocation per trade; no leverage or short selling. Trades only executed if sufficient cash is available.")
    if max_positions is not None:
        md_lines.append(f"- **Max Simultaneous Positions:** {max_positions} (as set in configuration).")
    else:
        md_lines.append("- **Max Simultaneous Positions:** No explicit maximum; limited by available cash.")
    md_lines.append("\nEach trade allocates capital using a fixed position size. The number of shares bought is calculated as:\n")
    md_lines.append("\n    qty = int(position_size // price)\n")
    md_lines.append("\nThis ensures that:\n- No trade exceeds the specified position size or available cash.\n- No leverage or short selling is used.\n- Trades are only executed if sufficient cash is available.\n\nThis simple approach provides basic risk control by capping exposure per trade and preventing over-allocation. More advanced risk management (e.g., stop-loss, volatility targeting) is not implemented in this version.\n")
    # Section: Analyst Notes and Suggestions (substantive note)
    md_lines.append("## Analyst Notes and Suggestions\n")
    analyst_note = stats.get('analyst_notes', None)
    if analyst_note:
        md_lines.append(f"{analyst_note}\n")
    else:
        md_lines.append("The strategy underperformed in ranging markets; consider parameter tuning or regime filtering.\n")
    # Section: Rationale Summary
    md_lines.append("## Rationale Summary\n")
    trades = trade_log
    if isinstance(trades, pd.DataFrame):
        has_trades = not trades.empty
    else:
        has_trades = bool(trades)
    rationales = []
    if has_trades:
        if isinstance(trades, pd.DataFrame):
            for idx, trade in trades.iterrows():
                if hasattr(trade, 'get'):
                    rationale = trade.get('rationale')
                    if rationale:
                        rationales.append(rationale)
                elif isinstance(trade, str):
                    rationales.append(trade)
        elif isinstance(trades, list):
            for trade in trades:
                if hasattr(trade, 'get'):
                    rationale = trade.get('rationale')
                    if rationale:
                        rationales.append(rationale)
                elif isinstance(trade, str):
                    rationales.append(trade)
    if rationales:
        md_lines.append("\n".join([f"- {r}" for r in rationales]))
    else:
        md_lines.append("No rationale provided.\n")
    # Parameter Sensitivity Analysis
    param_sens_path = "plots/parameter_sensitivity.png"
    # Section header always present if results or plot exist
    if (parameter_sensitivity_results and len(parameter_sensitivity_results) > 0) or os.path.exists(param_sens_path):
        md_lines.append("\n## Parameter Sensitivity Analysis\n")
        if parameter_sensitivity_results and len(parameter_sensitivity_results) > 0:
            # Generate Markdown table
            keys = list(parameter_sensitivity_results[0].keys())
            md_lines.append("| " + " | ".join(keys) + " |")
            md_lines.append("|" + "---|" * len(keys))
            for row in parameter_sensitivity_results:
                md_lines.append("| " + " | ".join(str(row[k]) for k in keys) + " |")
            md_lines.append("")
        if os.path.exists(param_sens_path):
            md_lines.append("The plot below compares equity curves for different parameter values, illustrating the impact of parameter changes on strategy performance.\n")
            md_lines.append(f"![Parameter Sensitivity]({param_sens_path})\n")
    # Trade Statistics Breakdown
    md_lines.append("## Trade Statistics Breakdown\n")
    metrics = stats.get('strategy', {})
    if isinstance(trade_log, pd.DataFrame):
        has_trades = not trade_log.empty
    else:
        has_trades = bool(trade_log)
    if has_trades and metrics:
        md_lines.append("| Metric | Value |")
        md_lines.append("|---|---|")
        md_lines.append(f"| Average Win | {metrics.get('average_win', 0.0):.2f} |")
        md_lines.append(f"| Average Loss | {metrics.get('average_loss', 0.0):.2f} |")
        md_lines.append(f"| Largest Win | {metrics.get('largest_win', 0.0):.2f} |")
        md_lines.append(f"| Largest Loss | {metrics.get('largest_loss', 0.0):.2f} |")
        md_lines.append(f"| Profit Factor | {metrics.get('profit_factor', 0.0):.2f} |")
        md_lines.append(f"| Expectancy | {metrics.get('expectancy', 0.0):.2f} |")
    else:
        md_lines.append("No trade statistics available.\n")
    # Regime Breakdown
    md_lines.append("\n### Regime Breakdown\n")
    from tech_analysis.backtest import correlate_performance_with_regimes
    if isinstance(trade_log, pd.DataFrame):
        has_trades = not trade_log.empty
    else:
        has_trades = bool(trade_log)
    if has_trades:
        # Ensure trade_log is a list of dicts, not a DataFrame, before passing to correlate_performance_with_regimes
        if hasattr(trade_log, 'to_dict'):
            trade_log_records = trade_log.to_dict('records')
        else:
            trade_log_records = trade_log
        regime_stats = correlate_performance_with_regimes(trade_log_records)
        if regime_stats:
            md_lines.append("| Regime | Trades | Win Rate | Avg Win | Avg Loss | Largest Win | Largest Loss | Profit Factor | Expectancy | Mean PnL |")
            md_lines.append("|---|---|---|---|---|---|---|---|---|---|")
            for regime, regime_stat in regime_stats.items():
                md_lines.append(
                    f"| {regime} | {regime_stat['count']} | {regime_stat['win_rate']:.2f} | {regime_stat['average_win']:.2f} | {regime_stat['average_loss']:.2f} | {regime_stat['largest_win']:.2f} | {regime_stat['largest_loss']:.2f} | {regime_stat['profit_factor']:.2f} | {regime_stat['expectancy']:.2f} | {regime_stat['mean_pnl']:.2f} |"
                )
            # --- Regime-wise Barplot and Boxplot ---
            # Convert to DataFrame for plotting
            trades_df = pd.DataFrame(trade_log_records)
            if 'regime' in trades_df.columns and 'PnL' in trades_df.columns:
                plots_dir = os.path.join(os.getcwd(), 'plots')
                os.makedirs(plots_dir, exist_ok=True)
                # Barplot: Mean PnL per regime
                barplot_path = os.path.join(plots_dir, 'regime_barplot.png')
                plt.figure(figsize=(5,3), facecolor='white')
                sns.barplot(data=trades_df, x='regime', y='PnL', estimator='mean', errorbar=None, hue='regime', palette='Set2', legend=False)
                plt.title('Mean PnL by Regime')
                plt.xlabel('Regime')
                plt.ylabel('Mean PnL')
                plt.tight_layout()
                plt.savefig(barplot_path)
                plt.close()
                md_lines.append(f"\n![Mean PnL by Regime](plots/regime_barplot.png)\n")
                # Boxplot: PnL distribution per regime
                boxplot_path = os.path.join(plots_dir, 'regime_boxplot.png')
                plt.figure(figsize=(5,3), facecolor='white')
                sns.boxplot(data=trades_df, x='regime', y='PnL', hue='regime', palette='Set2', legend=False)
                plt.title('PnL Distribution by Regime')
                plt.xlabel('Regime')
                plt.ylabel('PnL')
                plt.tight_layout()
                plt.savefig(boxplot_path)
                plt.close()
                md_lines.append(f"\n![PnL Distribution by Regime](plots/regime_boxplot.png)\n")
        else:
            md_lines.append("No regime breakdown available.\n")
    else:
        md_lines.append("No trades for regime breakdown.\n")
    # Holding Duration Distribution Section
    if holding_durations:
        md_lines.append("\n## Trade Holding Duration Distribution\n")
        md_lines.append(f"![Trade Holding Duration]({holding_duration_chart_path})\n")
    # --- Trade-Level Charts Per Ticker ---
    equity_curves = stats.get('equity_curve')
    trade_log = stats.get('trades') or stats.get('_trades')
    regime_series = stats.get('regime_series', {})
    sma_curves = stats.get('sma_curve', {})
    if isinstance(equity_curves, dict):
        for ticker, eq_curve in equity_curves.items():
            chart_path = f"plots/trade_chart_{ticker}.png"
            os.makedirs(os.path.dirname(chart_path), exist_ok=True)
            plt.figure(facecolor='white')
            # Robustly check eq_curve validity
            valid_curve = False
            if eq_curve is not None:
                if isinstance(eq_curve, (list, np.ndarray, pd.Series)) and len(eq_curve) > 0:
                    valid_curve = True
            if valid_curve:
                plt.plot(eq_curve, label='Equity Curve', color='#1f77b4')
                # Overlay SMA if available
                if isinstance(sma_curves, dict) and ticker in sma_curves:
                    sma = sma_curves.get(ticker)
                    if isinstance(sma, (list, np.ndarray, pd.Series)) and len(sma) == len(eq_curve):
                        plt.plot(sma, label='SMA', color='orange')
                # Overlay regime if available
                if isinstance(regime_series, dict) and ticker in regime_series:
                    regimes = regime_series.get(ticker)
                    for i, regime in enumerate(regimes):
                        if regime == 'uptrend':
                            plt.axvspan(i, i+1, color='green', alpha=0.1)
                        elif regime == 'downtrend':
                            plt.axvspan(i, i+1, color='red', alpha=0.1)
                # Overlay trades if available
                if isinstance(trade_log, pd.DataFrame):
                    ticker_trades = trade_log[trade_log['Ticker'] == ticker] if 'Ticker' in trade_log.columns else trade_log[trade_log['ticker'] == ticker]
                    for idx, trade in ticker_trades.iterrows():
                        entry = trade.get('EntryTime', '')
                        entry_price = trade.get('EntryPrice', '')
                        exit = trade.get('ExitTime', '')
                        exit_price = trade.get('ExitPrice', '')
                        if entry is not None and entry_price is not None:
                            plt.scatter(entry, entry_price, marker='^', color='green', label='Entry' if idx == 0 else "")
                        if exit is not None and exit_price is not None:
                            plt.scatter(exit, exit_price, marker='v', color='red', label='Exit' if idx == 0 else "")
                plt.legend(loc='best', frameon=True)
                plt.title(f'Trade-Level Chart: {ticker}')
            else:
                # Fallback: plot a placeholder chart
                plt.plot([0, 1], [0, 1], color='#cccccc', linestyle='--')
                plt.title(f'Trade-Level Chart: {ticker} (No Data)')
            plt.tight_layout()
            plt.savefig(chart_path)
            plt.close()
            # Embed in Markdown
            md_lines.append(f"\n## Trade-Level Chart: {ticker}\n")
            md_lines.append(f"![Trade-Level Chart for {ticker}]({chart_path})\n")

    # Write to Markdown file
    md_path = "reports/portfolio_report.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"[INFO] Markdown report generated at {md_path}")

def plot_parameter_sensitivity(eq1, eq2, label1, label2, save_path="plots/parameter_sensitivity.png"):
    """
    Plots two equity curves for parameter sensitivity analysis and saves as a static image.
    """
    plt.figure(facecolor='white')
    if eq1 is not None:
        plt.plot(eq1, label=label1, color='#1f77b4')
    if eq2 is not None:
        plt.plot(eq2, label=label2, color='#ff7f0e')
    plt.title('Parameter Sensitivity: Equity Curve Comparison')
    plt.xlabel('Time')
    plt.ylabel('Equity')
    plt.legend()
    plt.tight_layout()
    abs_save_path = os.path.abspath(save_path)
    plt.savefig(abs_save_path)
    plt.close()

def regime_color(regime):
    if regime == 'uptrend':
        return '#34C759'
    elif regime == 'downtrend':
        return '#FF3B30'
    else:
        return '#808080'
