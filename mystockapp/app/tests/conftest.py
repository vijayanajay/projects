import pytest
from unittest.mock import patch


def passthrough_decorator(func=None, **kwargs):
    """A decorator that does nothing but return the original function."""
    if func is None:
        return lambda f: f
    return func


@pytest.fixture(autouse=True, scope="session")
def mock_streamlit_cache():
    """Mocks streamlit.cache_data to be a pass-through decorator for all tests."""
    try:
        with patch("src.backtester.st.cache_data", passthrough_decorator):
            yield
    except (AttributeError, ImportError):
        try:
            with patch("streamlit.cache_data", passthrough_decorator):
                yield
        except ImportError:
            yield
