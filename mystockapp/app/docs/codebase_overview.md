# Codebase Overview

This codebase implements a simple application for fetching historical stock data and generating technical indicators. The primary goal is to provide a tool that can download OHLCV (Open, High, Low, Close, Volume) data for a specified stock (specifically Reliance Industries in the current configuration) and enrich it with various technical analysis features.

The project consists of three main components:

1.  **Data Fetching:** Responsible for retrieving historical stock data from a financial data source (using `yfinance`). It includes basic caching functionality to avoid repeated downloads of recent data.
2.  **Feature Generation:** A dedicated module designed to calculate a wide range of technical indicators (like Moving Averages, RSI, MACD, Bollinger Bands, ATR, and Volume-based indicators) from the fetched OHLCV data. It is built to be configurable regarding which indicators to generate and their parameters, and uses vectorized operations for efficiency.
3.  **Main Application:** Provides a command-line interface to orchestrate the process. It handles parsing user arguments (like data period, interval, output file, features to generate), initiates the data fetching, calls the feature generation module, saves the resulting data with features to a CSV file, and can optionally generate basic plots of key indicators.

In essence, the application serves as a pipeline: Fetch Data -> Generate Features -> Save/Visualize Results. It's designed for users who want to quickly obtain stock data augmented with common technical analysis metrics for further analysis or use in other applications.
