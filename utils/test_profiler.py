"""Tests for the profiler utility functions."""

# pylint skip-file

import pandas as pd
import pytest
from profiler import get_basic_info, get_missing_values, get_numeric_summary, get_categorical_summary, find_outliers


class TestGetBasicInfo:
    """
    Tests for get_basic_info function.
    """
    def test_basic_info_returns_correct_info_with_valid_dataframe(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        info = get_basic_info(df)
        assert info['shape'] == (3, 2)
        assert info['columns'] == ['A', 'B']
        assert info['dtypes'] == {'A': 'int64', 'B': 'object'}


class TestGetMissingValues:
    """
    Tests for get_missing_values function.
    """

    def test_missing_values_returns_correct_counts_and_percentages(self):
        df = pd.DataFrame({
            'A': [1, None, 3],
            'B': ['a', 'b', None]
        })
        missing = get_missing_values(df)
        assert missing['A']['count'] == 1
        assert missing['A']['percentage'] == pytest.approx(33.33, 0.1)
        assert missing['B']['count'] == 1
        assert missing['B']['percentage'] == pytest.approx(33.33, 0.1)

    def test_missing_values_with_no_missing_data(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        missing = get_missing_values(df)
        assert missing['A']['count'] == 0
        assert missing['A']['percentage'] == 0.0
        assert missing['B']['count'] == 0
        assert missing['B']['percentage'] == 0.0


class TestGetNumericSummary:
    """
    Tests for get_numeric_summary function.
    """

    def test_numeric_summary_returns_correct_statistics(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5]
        })
        summary = get_numeric_summary(df)
        assert summary['A']['mean'] == 3.0
        assert summary['A']['median'] == 3.0
        assert summary['A']['min'] == 1
        assert summary['A']['max'] == 5
        assert summary['A']['std'] == pytest.approx(1.58, 0.01)

    def test_numeric_summary_with_empty_column(self):
        df = pd.DataFrame({
            'A': []
        })
        summary = get_numeric_summary(df)
        assert summary['A']['mean'] is None
        assert summary['A']['median'] is None
        assert summary['A']['min'] is None
        assert summary['A']['max'] is None
        assert summary['A']['std'] is None


class TestGetCategoricalSummary:
    """
    Tests for get_categorical_summary function.
    """

    def test_categorical_summary_returns_correct_unique_counts_and_top_values(self):
        df = pd.DataFrame({
            'B': ['a', 'b', 'a', 'c', 'b', 'a']
        })
        summary = get_categorical_summary(df)
        assert summary['B']['unique_counts'] == 3
        assert summary['B']['top_value'] == 'a'
        assert summary['B']['top_value_count'] == 3
    
    def test_categorical_summary_with_all_unique_values(self):
        df = pd.DataFrame({
            'B': ['a', 'b', 'c', 'd']
        })
        summary = get_categorical_summary(df)
        assert summary['B']['unique_counts'] == 4
        assert summary['B']['top_value'] in ['a', 'b', 'c', 'd']
        assert summary['B']['top_value_count'] == 1


class TestFindOutliers:
    """
    Tests for find_outliers function.
    """

    def test_find_outliers_identifies_outliers_correctly(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 100]
        })
        outliers = find_outliers(df)
        assert outliers['A'] == [100]

    def test_find_outliers_no_outliers(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5]
        })
        outliers = find_outliers(df)
        assert outliers['A'] == []