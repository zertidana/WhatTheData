"""Conftest file for pytest configurations and fixtures."""

import pytest
import pandas as pd

@pytest.fixture
def sample_dataframe():
    """Provides a sample DataFrame for testing."""
    data = {
        'A': [1, 2, None, 4],
        'B': ['a', None, 'c', 'd'],
        'C': [10.5, 20.3, 30.1, None]
    }
    return pd.DataFrame(data)

