import streamlit as st
import plotly.express as px

from data_loader import load_data
from filters import apply_filters

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="👥",
    layout="wide"
)

df = load_data()
df = apply_filters(df)

st.title("👥 Customer Intelligence")

# --------------------------------------------------
# Customer Search
# --------------------------------------------------

customers = sorted(df["Customer Name"].unique())

selected_customer = st.selectbox(
    "🔍 Search Customer",
    ["All Customers"] + customers
)

if selected_customer != "All Customers":
    filtered = df[df["Customer Name"] == selected_customer]
else:
    filtered = df.copy()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

sales = filtered["Sales"].sum()
profit = filtered["Profit"].sum()
orders = filtered["Order ID"].nunique()

states = filtered["State"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Sales", f"${sales:,.2f}")
c2.metric("📈 Profit", f"${profit:,.2f}")
c3.metric("🛒 Orders", orders)
c4.metric("🌍 States", states)

st.divider()

# --------------------------------------------------
# Top Customers by Sales
# --------------------------------------------------

top_sales = (
    df.groupby("Customer Name", as_index=False)["Sales"]
    .sum()
    .sort_values(by="Sales", ascending=False)
    .head(10)
)

fig1 = px.bar(
    top_sales,
    x="Sales",
    y="Customer Name",
    orientation="h",
    color="Sales",
    title="Top 10 Customers by Sales",
    text_auto=".2s"
)

st.plotly_chart(fig1, use_container_width=True)

# --------------------------------------------------
# Top Customers by Profit
# --------------------------------------------------

top_profit = (
    df.groupby("Customer Name", as_index=False)["Profit"]
    .sum()
    .sort_values(by="Profit", ascending=False)
    .head(10)
)

fig2 = px.bar(
    top_profit,
    x="Profit",
    y="Customer Name",
    orientation="h",
    color="Profit",
    title="Top 10 Customers by Profit",
    text_auto=".2s"
)

st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# Customer Segment Distribution
# --------------------------------------------------

segment = (
    df.groupby("Segment", as_index=False)["Sales"]
    .sum()
)

fig3 = px.pie(
    segment,
    names="Segment",
    values="Sales",
    hole=0.5,
    title="Customer Segment Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# Customer Details
# --------------------------------------------------

st.subheader("📋 Customer Details")

st.dataframe(filtered, use_container_width=True)