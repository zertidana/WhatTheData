"""
This Script deals with the CSV upload 
and displays the profiling report using Streamlit 
and ydata-profiling.
"""

import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from utils.profiler import (
    get_basic_info,
    get_missing_values,
    get_numeric_summary,
    get_categorical_summary
)


def generate_profiling_report(df: pd.DataFrame) -> ProfileReport:
    """Generates a profiling report using ydata-profiling."""

    profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
    return profile


def st_profile_report(profile: ProfileReport):
    """Displays the ydata-profiling report in Streamlit."""

    with st.expander("Show Profiling Report"):
        profile_html = profile.to_html()
        st.components.v1.html(profile_html, height=800, scrolling=True)


def display_basic_info(info: dict):
    """Displays basic information about the DataFrame."""

    st.subheader("Basic Information")
    st.write(f"Shape: {info['shape']}")
    st.write("Columns and Data Types:")
    for col, dtype in info['dtypes'].items():
        st.write(f"- {col}: {dtype}")


def display_missing_values(missing_info: dict):
    """Displays missing values information."""

    st.subheader("Missing Values")
    for col, stats in missing_info.items():
        st.write(f"- {col}: {stats['count']} missing ({stats['percentage']:.2f}%)")

def display_numeric_summary(summary: dict):
    """Displays numeric summary statistics."""

    st.subheader("Numeric Summary")
    for col, stats in summary.items():
        st.write(f"""- {col}: Mean={stats['mean']},
                Median={stats['median']},
                Min={stats['min']},
                Max={stats['max']},
                Std={stats['std']}
         """)


def display_categorical_summary(summary: dict):
    """Displays categorical summary statistics."""

    st.subheader("Categorical Summary")
    if not summary:
        st.write("No categorical columns found.")
        return

    for col, stats in summary.items():
        unique = stats.get('unique_count', stats.get('unique', 'N/A'))
        top = stats.get('top_values', stats.get('top', 'N/A'))
        st.write(f"- {col}: Unique={unique}, Top={top}")


def main():
    """
    Main function to run the Streamlit app.
    Handles file upload and displays profiling report and summaries.
    """
    st.title("Data Profiling Application")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.header("DataFrame Overview")
        st.write(df.head())

        # Generate and display profiling report
        profile = generate_profiling_report(df)
        st_profile_report(profile)

        # Display custom summaries
        basic_info = get_basic_info(df)
        display_basic_info(basic_info)

        missing_info = get_missing_values(df)
        display_missing_values(missing_info)

        numeric_summary = get_numeric_summary(df)
        display_numeric_summary(numeric_summary)

        categorical_summary = get_categorical_summary(df)
        display_categorical_summary(categorical_summary)


if __name__ == "__main__":
    main()