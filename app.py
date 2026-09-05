import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Sales Dashboard", layout="centered")

# Title and header
st.title("Simple Sales Dashboard")
st.write("Analyze regional performance interactively.")

# Sidebar controls
st.sidebar.header("Filter Options")
num_points = st.sidebar.slider("Number of data points", min_value=10, max_value=100, value=30)
region = st.sidebar.selectbox("Select Region", ["North", "South", "East", "West"])

# Generate sample data based on inputs
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=num_points)
sales = np.random.randint(100, 500, size=num_points)
revenue = sales * np.random.uniform(1.2, 1.8, size=num_points)

df = pd.DataFrame({"Date": dates, "Sales": sales, "Revenue ($)": revenue}).set_index("Date")

# Metric cards
col1, col2 = st.columns(2)
col1.metric(label="Total Units Sold", value=int(df["Sales"].sum()))
col2.metric(label="Total Revenue", value=f"${df['Revenue ($)'].sum():,.2f}")

# Visualizations
st.subheader(f"Sales Trend: {region}")
st.line_chart(df["Sales"])

# Collapsible data preview
with st.expander("View Raw Data"):
    st.dataframe(df)

# Simple action button
if st.button("Export Confirmation"):
    st.success(f"Report for {region} region saved to cache!")