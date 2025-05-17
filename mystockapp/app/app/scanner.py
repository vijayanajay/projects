import streamlit as st

# Initialize session state
if "scan_results" not in st.session_state:
    st.session_state.scan_results = []
if "last_scan_inputs" not in st.session_state:
    st.session_state.last_scan_inputs = None

# Capture current inputs to check for changes
current_scan_inputs = (
    tickers,
    period,
    interval,
    selected_strategy,
    strategy_params,
    max_workers,
)

if run_scan or st.session_state.last_scan_inputs != current_scan_inputs:
    st.session_state.last_scan_inputs = current_scan_inputs

    # Run the scanner
    st.session_state.scan_results = scan_stocks(
        tickers,
        period,
        interval,
        selected_strategy,
        strategy_params,
        max_workers=max_workers,
    )

# ... existing code for displaying results ...
