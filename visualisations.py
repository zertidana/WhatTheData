"""Visualisation utilities for the data profiling app."""

import streamlit as st
import pandas as pd
import plotly.express as px


def generate_histogram(df: pd.DataFrame, column: str):
    """Generates and displays a histogram for a numeric column."""

    st.subheader(f"Histogram for {column}")
    fig = px.histogram(df, x=column, nbins=30, title=f'Histogram of {column}')
    st.plotly_chart(fig)
    return fig


def generate_bar_chart(df: pd.DataFrame, column: str):
    """Bar chart for categorical columns with < 20 unique values"""

    st.subheader(f"Bar Chart for {column}")
    value_counts = df[column].value_counts().nlargest(20)
    fig = px.bar(x=value_counts.index,
                 y=value_counts.values,
                 labels={'x': column, 'y': 'Count'},
                 title=f'Bar Chart of {column}')
    st.plotly_chart(fig)
    return fig


def generate_scatter_plot(df: pd.DataFrame, x_col: str, y_col: str):
    """Generates and displays a scatter plot for two numeric columns."""

    st.subheader(f"Scatter Plot: {x_col} vs {y_col}")
    fig = px.scatter(df, x=x_col, y=y_col, title=f'Scatter Plot of {x_col} vs {y_col}')
    st.plotly_chart(fig)
    return fig


def generate_heatmap(df: pd.DataFrame):
    """Generates and displays a heatmap of correlations between numeric columns."""

    st.subheader("Correlation Heatmap")
    numeric_df = df.select_dtypes(include=['number'])
    corr = numeric_df.corr()
    fig = px.imshow(corr,
                    text_auto=True,
                    title='Correlation Heatmap')
    st.plotly_chart(fig)
    return fig
