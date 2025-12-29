"""Utility functions for data profiling and analysis."""
import pandas as pd 


def get_basic_info(df: pd.DataFrame) -> dict:
    """Returns basic information about the DataFrame."""

    info = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.apply(lambda x: x.name).to_dict()
    }
    return info


def get_missing_values(df: pd.DataFrame) -> dict:
    """Returns counts and percentages"""

    missing_info = {}
    total_rows = len(df)
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        missing_percentage = (missing_count / total_rows) * 100 if total_rows > 0 else 0
        missing_info[col] = {
            "count": missing_count,
            "percentage": missing_percentage
        }
    return missing_info


def get_numeric_summary(df: pd.DataFrame) -> dict:
    """Returns mean, median, min, max, std"""

    summary = {}
    for col in df.select_dtypes(include='number').columns:
        if df[col].empty:
            summary[col] = {
                "mean": None,
                "median": None,
                "min": None,
                "max": None,
                "std": None
            }
        else:
            summary[col] = {
                "mean": df[col].mean(),
                "median": df[col].median(),
                "min": df[col].min(),
                "max": df[col].max(),
                "std": df[col].std()
            }
    return summary


def get_categorical_summary(df: pd.DataFrame) -> dict:
    """Returns unique counts, top values"""
    summary = {}
    for col in df.select_dtypes(include='object').columns:
        unique_counts = df[col].nunique()
        top_value = df[col].mode()[0] if not df[col].mode().empty else None
        summary[col] = {
            "unique_counts": unique_counts,
            "top_value": top_value
        }
    return summary


def find_outliers(df: pd.DataFrame) -> dict:
    """Returns outliers using the IQR method"""
    outliers = {}
    for col in df.select_dtypes(include='number').columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outlier_count = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
        outliers[col] = {
            "outlier_count": outlier_count
        }
    return outliers