import streamlit as st
import plotly.express as px
import pandas as pd

from data_loader import load_data
from filters import apply_filters

st.set_page_config(
    page_title="Sales Trends",
    page_icon="📈",
    layout="wide"
)

df = load_data()
df = apply_filters(df)

st.title("📈 Sales Trends")

# ----------------------------------------
# Prepare Date Columns
# ----------------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.strftime("%b")
df["Quarter"] = df["Order Date"].dt.quarter

# ----------------------------------------
# Monthly Sales
# ----------------------------------------

monthly = (
    df.groupby(["Year", "Month"], as_index=False)["Sales"]
    .sum()
)

fig1 = px.line(
    monthly,
    x="Month",
    y="Sales",
    color="Year",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# ----------------------------------------
# Quarterly Sales
# ----------------------------------------

quarterly = (
    df.groupby(["Year", "Quarter"], as_index=False)["Sales"]
    .sum()
)

fig2 = px.bar(
    quarterly,
    x="Quarter",
    y="Sales",
    color="Year",
    barmode="group",
    title="Quarterly Sales"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------------
# Yearly Sales
# ----------------------------------------

yearly = (
    df.groupby("Year", as_index=False)["Sales"]
    .sum()
)

fig3 = px.bar(
    yearly,
    x="Year",
    y="Sales",
    color="Sales",
    text_auto=".2s",
    title="Yearly Sales"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------------
# Monthly Profit
# ----------------------------------------

profit = (
    df.groupby(["Year", "Month"], as_index=False)["Profit"]
    .sum()
)

fig4 = px.line(
    profit,
    x="Month",
    y="Profit",
    color="Year",
    markers=True,
    title="Monthly Profit Trend"
)

st.plotly_chart(fig4, use_container_width=True)

# ----------------------------------------
# Sales Summary
# ----------------------------------------

st.subheader("📋 Sales Trend Data")

st.dataframe(
    monthly,
    use_container_width=True
)