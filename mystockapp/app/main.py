"""
Main script to download Reliance stock data, generate technical indicators, and run backtests.
"""

import os
import logging
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from data_fetcher import get_reliance_data
from feature_factory import FeatureFactory
from backtester import (
    add_sma_crossover_signals,
    run_backtest,
    generate_backtest_report,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Download Reliance stock data, generate technical indicators, and run backtests."
    )
    parser.add_argument(
        "--period",
        type=str,
        default="max",
        help="Data period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)",
    )
    parser.add_argument(
        "--interval",
        type=str,
        default="1d",
        help="Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/reliance_features.csv",
        help="Output CSV file for features",
    )
    parser.add_argument(
        "--plot", action="store_true", help="Generate plots of key indicators"
    )
    parser.add_argument(
        "--features",
        type=str,
        default="all",
        help="Comma-separated list of feature families to generate (e.g., sma,ema,rsi)",
    )
    parser.add_argument(
        "--no-cache", action="store_true", help="Disable data caching"
    )
    # New arguments for backtesting
    parser.add_argument(
        "--split-date",
        type=str,
        help="Date to split data into in-sample and out-of-sample periods (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--initial-capital",
        type=float,
        default=100000.0,
        help="Initial capital for backtesting (default: 100000.0)",
    )
    parser.add_argument(
        "--strategy",
        type=str,
        default="sma_crossover",
        help="Trading strategy to backtest (default: sma_crossover)",
    )
    parser.add_argument(
        "--fast-sma",
        type=int,
        default=50,
        help="Fast SMA window size for crossover strategy (default: 50)",
    )
    parser.add_argument(
        "--slow-sma",
        type=int,
        default=200,
        help="Slow SMA window size for crossover strategy (default: 200)",
    )
    return parser.parse_args()


def generate_plots(data, output_dir="plots"):
    """Generate plots for key indicators."""
    logger.info("Generating plots for key indicators")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Plot 1: Price with SMA 50 and 200
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close Price")
    plt.plot(data.index, data["sma_50"], label="SMA 50")
    plt.plot(data.index, data["sma_200"], label="SMA 200")
    plt.title("Reliance Stock Price with SMA 50 and 200")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "price_sma.png"))
    plt.close()

    # Plot 2: RSI
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["rsi_14"], label="RSI 14")
    plt.axhline(y=70, color="r", linestyle="--", alpha=0.5)
    plt.axhline(y=30, color="g", linestyle="--", alpha=0.5)
    plt.title("RSI (14)")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "rsi.png"))
    plt.close()

    # Plot 3: MACD
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["macd_12_26_9_line"], label="MACD Line")
    plt.plot(data.index, data["macd_12_26_9_signal"], label="Signal Line")
    plt.bar(
        data.index,
        data["macd_12_26_9_histogram"],
        label="Histogram",
        alpha=0.3,
    )
    plt.title("MACD (12,26,9)")
    plt.xlabel("Date")
    plt.ylabel("MACD")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "macd.png"))
    plt.close()

    # Plot 4: Bollinger Bands
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close Price")
    plt.plot(data.index, data["bb_20_2.0_upper"], label="Upper Band")
    plt.plot(data.index, data["bb_20_2.0_middle"], label="Middle Band")
    plt.plot(data.index, data["bb_20_2.0_lower"], label="Lower Band")
    plt.title("Bollinger Bands (20,2)")
    plt.xlabel("Date")
    plt.ylabel("Price (₹)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "bollinger_bands.png"))
    plt.close()

    # Plot 5: Volume
    plt.figure(figsize=(12, 6))
    plt.bar(data.index, data["Volume"], label="Volume", alpha=0.5)
    plt.plot(
        data.index, data["volume_sma_20"], label="Volume SMA 20", color="r"
    )
    plt.title("Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, "volume.png"))
    plt.close()

    # New plot for SMA crossover strategy signals
    if "buy_signal" in data.columns and "sell_signal" in data.columns:
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data["Close"], label="Close Price", alpha=0.5)

        # Mark buy signals
        buy_signals = data[data["buy_signal"]]
        plt.scatter(
            buy_signals.index,
            buy_signals["Close"],
            color="green",
            marker="^",
            s=100,
            label="Buy Signal",
        )

        # Mark sell signals
        sell_signals = data[data["sell_signal"]]
        plt.scatter(
            sell_signals.index,
            sell_signals["Close"],
            color="red",
            marker="v",
            s=100,
            label="Sell Signal",
        )

        plt.title("SMA Crossover Strategy Signals")
        plt.xlabel("Date")
        plt.ylabel("Price (₹)")
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, "strategy_signals.png"))
        plt.close()

    logger.info(f"Plots saved to {output_dir} directory")


def plot_backtest_results(is_results, oos_results, output_dir="plots"):
    """
    Generate plots comparing backtest results for in-sample and out-of-sample periods.

    Args:
        is_results (dict): In-sample backtest results
        oos_results (dict): Out-of-sample backtest results
        output_dir (str): Output directory for plots
    """
    if not is_results or not oos_results:
        logger.warning("Missing results for backtest comparison plot")
        return

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Plot performance comparison
    metrics = [
        "total_return_pct",
        "buy_hold_return_pct",
        "win_rate",
        "max_drawdown",
    ]
    labels = [
        "Total Return (%)",
        "Buy & Hold Return (%)",
        "Win Rate (%)",
        "Max Drawdown (%)",
    ]

    plt.figure(figsize=(12, 8))

    x = range(len(metrics))
    is_values = [is_results[m] for m in metrics]
    oos_values = [oos_results[m] for m in metrics]

    bar_width = 0.35
    plt.bar(
        [i - bar_width / 2 for i in x], is_values, bar_width, label="In-Sample"
    )
    plt.bar(
        [i + bar_width / 2 for i in x],
        oos_values,
        bar_width,
        label="Out-of-Sample",
    )

    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.title("Backtest Performance Comparison")
    plt.xticks(x, labels, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "backtest_comparison.png"))
    plt.close()

    logger.info(f"Backtest comparison plot saved to {output_dir}")


def main():
    """Main function to download data, generate features, and run backtests."""
    # Parse command line arguments
    args = parse_args()

    # Download Reliance stock data
    logger.info(
        f"Downloading Reliance stock data (period={args.period}, interval={args.interval})"
    )
    data = get_reliance_data(
        period=args.period,
        interval=args.interval,
        save_to_csv=not args.no_cache,
    )

    if data is None:
        logger.error("Failed to download data. Exiting.")
        return

    logger.info(f"Downloaded {len(data)} rows of data")

    # Determine which feature families to generate
    if args.features.lower() == "all":
        feature_families = None  # All features
    else:
        feature_families = [f.strip() for f in args.features.split(",")]

    # Create feature factory
    logger.info(
        f"Creating FeatureFactory with feature families: {feature_families}"
    )
    factory = FeatureFactory(data, feature_families=feature_families)

    # Generate features
    logger.info("Generating features")
    features_df = factory.generate_features()

    # Save features to CSV
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    features_df.to_csv(args.output)
    logger.info(f"Saved features to {args.output}")

    # Show feature statistics
    logger.info(f"Feature DataFrame shape: {features_df.shape}")
    logger.info(
        f"Number of features generated: {len(features_df.columns) - 5}"
    )  # Subtract the 5 OHLCV columns

    # Generate plots if requested
    if args.plot:
        generate_plots(features_df)

    # Run backtests if split date is provided
    if args.split_date:
        # Parse split date
        try:
            # Convert the split date to a timezone-naive timestamp
            split_date = pd.Timestamp(args.split_date).tz_localize(None)
            logger.info(f"Using split date: {split_date.date()}")

            # Make sure DataFrame index is timezone-naive for comparison
            # Copy the features_df to avoid modifying the original
            backtest_df = features_df.copy()
            if backtest_df.index.tz is not None:
                backtest_df.index = backtest_df.index.tz_localize(None)

            # Verify split date is within the data range
            if (
                split_date < backtest_df.index[0]
                or split_date > backtest_df.index[-1]
            ):
                logger.error(
                    f"Split date {split_date.date()} is outside data range: "
                    + f"{backtest_df.index[0].date()} - {backtest_df.index[-1].date()}"
                )
                return

            # Split data into in-sample and out-of-sample
            in_sample_df = backtest_df[backtest_df.index < split_date].copy()
            out_of_sample_df = backtest_df[
                backtest_df.index >= split_date
            ].copy()

            logger.info(
                f"In-sample period: {in_sample_df.index[0].date()} - {in_sample_df.index[-1].date()}, "
                + f"{len(in_sample_df)} rows"
            )
            logger.info(
                f"Out-of-sample period: {out_of_sample_df.index[0].date()} - {out_of_sample_df.index[-1].date()}, "
                + f"{len(out_of_sample_df)} rows"
            )

            # Check if datasets have enough data
            max_window = max(args.fast_sma, args.slow_sma)
            if (
                len(in_sample_df) <= max_window
                or len(out_of_sample_df) <= max_window
            ):
                logger.warning(
                    f"One or both periods have less data points than the largest SMA window ({max_window})"
                )

            # Apply the specified strategy
            if args.strategy.lower() == "sma_crossover":
                # Apply SMA crossover strategy to both periods
                in_sample_df = add_sma_crossover_signals(
                    in_sample_df,
                    fast_window=args.fast_sma,
                    slow_window=args.slow_sma,
                )

                out_of_sample_df = add_sma_crossover_signals(
                    out_of_sample_df,
                    fast_window=args.fast_sma,
                    slow_window=args.slow_sma,
                )

                # Run backtests
                is_results = run_backtest(
                    in_sample_df, initial_capital=args.initial_capital
                )
                oos_results = run_backtest(
                    out_of_sample_df, initial_capital=args.initial_capital
                )

                # Generate reports
                generate_backtest_report(is_results, "In-Sample")
                generate_backtest_report(oos_results, "Out-of-Sample")

                # Generate comparison plot if requested
                if args.plot:
                    plot_backtest_results(is_results, oos_results)

                # Save dataframes with signals
                signal_output = args.output.replace(
                    ".csv", "_with_signals.csv"
                )
                combined_df = pd.concat([in_sample_df, out_of_sample_df])
                combined_df.to_csv(signal_output)
                logger.info(f"Saved signals to {signal_output}")
            else:
                logger.error(
                    f"Strategy '{args.strategy}' not implemented. Only 'sma_crossover' is available."
                )

        except ValueError as e:
            logger.error(
                f"Invalid split date format: {args.split_date}. Use YYYY-MM-DD format. Error: {str(e)}"
            )

    logger.info("Done!")

    return features_df


if __name__ == "__main__":
    main()
