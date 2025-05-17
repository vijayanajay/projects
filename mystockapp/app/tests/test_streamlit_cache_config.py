"""
Test scenario: Streamlit Cache TTL Configuration

This test verifies that the Streamlit cache decorator in data_fetcher.py
is correctly configured with a fixed TTL value instead of using a function parameter.
"""

import os
import logging
from datetime import timedelta

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_streamlit_cache_decorator_configuration():
    """
    Test that the Streamlit cache decorator in data_fetcher.py uses a fixed TTL value
    instead of a function parameter by inspecting the file content directly.
    """
    # Get the path to the data_fetcher.py file
    data_fetcher_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src", "data_fetcher.py")
    )

    # Verify the file exists
    assert os.path.exists(
        data_fetcher_path
    ), f"data_fetcher.py not found at {data_fetcher_path}"

    # Read the file content
    with open(data_fetcher_path, "r") as f:
        content = f.read()

    # Verify the key changes are in place

    # 1. Verify the constant is defined
    assert (
        "STREAMLIT_CACHE_TTL_DAYS = 1" in content
    ), "STREAMLIT_CACHE_TTL_DAYS constant should be defined"

    # 2. Verify the decorator uses the constant
    assert (
        "@st.cache_data(ttl=timedelta(days=STREAMLIT_CACHE_TTL_DAYS))"
        in content
    ), "Decorator should use STREAMLIT_CACHE_TTL_DAYS constant"

    # 3. Verify the problematic code is not present
    assert (
        "@st.cache_data(ttl=timedelta(days=cache_expiry_days))" not in content
    ), "Decorator should not use cache_expiry_days parameter"

    # 4. Verify the function parameter still exists (for file cache)
    assert (
        "cache_expiry_days=1," in content
    ), "cache_expiry_days parameter should still exist for file-based caching"

    # 5. Verify the docstring mentions file-based cache for clarity
    assert (
        "(for file-based cache)" in content
    ), "Docstring should specify cache_expiry_days is for file-based cache"

    logger.info(
        "Verified Streamlit cache decorator is correctly configured with fixed TTL"
    )
