# File: D:/Code/projects/mystockapp/app/main.py

This script serves as the main entry point for the stock analysis application. It provides a command-line interface for users to specify data fetching parameters and feature generation options, orchestrates the data download and feature calculation processes, and handles saving the results and optionally generating plots.

## Main Components:

1.  **`parse_args()` Function:**
    *   **Purpose:** Parses command-line arguments provided by the user.
    *   **Logic:**
        *   Uses the `argparse` module to define expected arguments.
        *   Defines arguments for:
            *   `--period`: Data period (e.g., '1y', 'max'). Defaults to 'max'.
            *   `--interval`: Data interval (e.g., '1d', '1h'). Defaults to '1d'.
            *   `--output`: Path to save the output CSV file. Defaults to 'data/reliance_features.csv'.
            *   `--plot`: A flag (`action='store_true'`) to indicate whether to generate plots.
            *   `--features`: A comma-separated string of feature families to generate (e.g., 'sma,rsi'). Defaults to 'all'.
            *   `--no-cache`: A flag (`action='store_true'`) to disable data caching.
        *   Parses the arguments provided when the script is run.
    *   **Output:** Returns an `argparse.Namespace` object containing the parsed arguments.

2.  **`generate_plots(data, output_dir='plots')` Function:**
    *   **Purpose:** Generates and saves standard plots for key technical indicators from the processed data.
    *   **Inputs:**
        *   `data` (pd.DataFrame): The DataFrame containing OHLCV data and generated features.
        *   `output_dir` (str): The directory where plots should be saved. Defaults to 'plots'.
    *   **Logic:**
        *   Ensures the output directory exists, creating it if necessary.
        *   Generates several plots using `matplotlib.pyplot`:
            *   Close Price with SMA 50 and 200.
            *   RSI (14) with overbought/oversold lines (70/30).
            *   MACD (12, 26, 9) including the MACD line, Signal line, and Histogram.
            *   Bollinger Bands (20, 2.0) with the Close Price.
            *   Volume with Volume SMA 20.
        *   Each plot is configured with titles, labels, legends, and a grid.
        *   Each plot is saved as a PNG file in the specified `output_dir`.
        *   Plots are closed after saving to free up memory.
    *   **Output:** Saves image files to the filesystem.

3.  **`main()` Function:**
    *   **Purpose:** The main execution logic of the script. It ties together argument parsing, data fetching, feature generation, saving, and plotting.
    *   **Logic:**
        *   Calls `parse_args()` to get user inputs.
        *   Calls `data_fetcher.get_reliance_data()` using the specified `period`, `interval`, and `save_to_csv` (derived from `--no-cache`).
        *   Checks if data fetching was successful, logging an error and exiting if not.
        *   Determines the list of feature families to generate based on the `--features` argument ('all' or a comma-separated list).
        *   Instantiates the `FeatureFactory` class with the downloaded data and the determined feature families.
        *   Calls `factory.generate_features()` to perform the technical indicator calculations.
        *   Extracts the directory path from the `--output` file path and creates it if it doesn't exist.
        *   Saves the resulting `features_df` DataFrame to the specified output CSV file using `to_csv`.
        *   Logs information about the shape of the resulting DataFrame and the number of features generated.
        *   If the `--plot` flag was set, it calls `generate_plots()` with the `features_df`.
        *   Logs a "Done!" message upon completion.
    *   **Output:** Executes the full workflow, potentially saving a CSV file and plot images. Returns the final features DataFrame.

The script includes logging setup for tracking execution progress and messages. The `if __name__ == "__main__":` block ensures that the `main()` function is called when the script is executed directly.
