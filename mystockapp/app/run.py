#!/usr/bin/env python
"""
Stock Trading App Launcher

This script serves as the entry point for the Stock Trading App. It allows users to:
1. Launch the interactive dashboard (Streamlit app)
2. Run the stock scanner
3. Run the command-line backtester directly
"""

import os
import sys
import subprocess
import argparse
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Get the absolute path to the root directory
ROOT_DIR = Path(__file__).resolve().parent


def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        import pandas
        import numpy
        import plotly
        import yf
        import matplotlib

        logger.info("All required dependencies are installed.")
        return True
    except ImportError as e:
        logger.error(f"Missing dependency: {str(e)}")
        logger.error(
            "Please install all required dependencies: pip install -r requirements.txt"
        )
        return False


def run_streamlit_dashboard(app_path):
    """Run the Streamlit dashboard."""
    logger.info(f"Launching Streamlit dashboard: {app_path}")

    cmd = [sys.executable, "-m", "streamlit", "run", app_path]

    try:
        process = subprocess.Popen(cmd)
        logger.info("Streamlit server started. Press Ctrl+C to stop.")
        process.wait()
    except KeyboardInterrupt:
        logger.info("Stopping Streamlit server...")
        process.terminate()
        process.wait()
    except Exception as e:
        logger.error(f"Error running Streamlit dashboard: {str(e)}")
        return False

    return True


def run_stock_scanner(scanner_path):
    """Run the stock scanner."""
    logger.info(f"Launching Stock Scanner: {scanner_path}")

    cmd = [sys.executable, "-m", "streamlit", "run", scanner_path]

    try:
        process = subprocess.Popen(cmd)
        logger.info("Scanner server started. Press Ctrl+C to stop.")
        process.wait()
    except KeyboardInterrupt:
        logger.info("Stopping Scanner server...")
        process.terminate()
        process.wait()
    except Exception as e:
        logger.error(f"Error running Stock Scanner: {str(e)}")
        return False

    return True


def run_command_line_backtest(args_list=None):
    """
    Run the command-line backtester with provided arguments.

    Args:
        args_list (list): List of command-line arguments to pass to main.py
    """
    if args_list is None:
        args_list = []

    main_path = os.path.join(ROOT_DIR, "main.py")
    logger.info(f"Running command-line backtester: {main_path}")

    cmd = [sys.executable, main_path] + args_list

    try:
        subprocess.run(cmd)
    except Exception as e:
        logger.error(f"Error running backtester: {str(e)}")
        return False

    return True


def parse_args():
    """Parse command line arguments for the launcher."""
    parser = argparse.ArgumentParser(
        description="Stock Trading App Launcher - Run interactive dashboard, scanner, or backtester"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["dashboard", "scanner", "backtest"],
        default="dashboard",
        help="Mode to run: dashboard, scanner, or backtest",
    )

    # Pass through arguments for backtester
    parser.add_argument(
        "--backtest-args",
        type=str,
        help="Arguments to pass to the backtester (in quotes, e.g. '--ticker AAPL --period 1y')",
    )

    return parser.parse_args()


def main():
    """Main function."""
    # Parse command line arguments
    args = parse_args()

    # Check dependencies
    if not check_dependencies():
        return 1

    # Run the selected mode
    if args.mode == "dashboard":
        app_path = os.path.join(ROOT_DIR, "app.py")
        success = run_streamlit_dashboard(app_path)
    elif args.mode == "scanner":
        scanner_path = os.path.join(ROOT_DIR, "scanner.py")
        success = run_stock_scanner(scanner_path)
    elif args.mode == "backtest":
        backtest_args = []
        if args.backtest_args:
            backtest_args = args.backtest_args.split()
        success = run_command_line_backtest(backtest_args)
    else:
        logger.error(f"Unknown mode: {args.mode}")
        return 1

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
