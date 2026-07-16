import streamlit as st
import plotly.express as px

from data_loader import load_data
from filters import apply_filters

st.set_page_config(
    page_title="Geographic Intelligence",
    page_icon="🌍",
    layout="wide"
)

df = load_data()
df = apply_filters(df)

st.title("🌍 Geographic Intelligence")

# ---------------------------------------
# State Filter
# ---------------------------------------

states = sorted(df["State"].unique())

selected_state = st.selectbox(
    "📍 Select State",
    ["All States"] + states
)

if selected_state != "All States":
    filtered = df[df["State"] == selected_state]
else:
    filtered = df.copy()

# ---------------------------------------
# KPI Cards
# ---------------------------------------

sales = filtered["Sales"].sum()
profit = filtered["Profit"].sum()
orders = filtered["Order ID"].nunique()
cities = filtered["City"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Sales", f"${sales:,.2f}")
c2.metric("📈 Profit", f"${profit:,.2f}")
c3.metric("📦 Orders", orders)
c4.metric("🏙 Cities", cities)

st.divider()

# ---------------------------------------
# Sales by State
# ---------------------------------------

state_sales = (
    df.groupby("State", as_index=False)["Sales"]
    .sum()
    .sort_values(by="Sales", ascending=False)
    .head(15)
)

fig1 = px.bar(
    state_sales,
    x="Sales",
    y="State",
    orientation="h",
    color="Sales",
    title="Top States by Sales",
    text_auto=".2s"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------
# Profit by State
# ---------------------------------------

state_profit = (
    df.groupby("State", as_index=False)["Profit"]
    .sum()
    .sort_values(by="Profit", ascending=False)
    .head(15)
)

fig2 = px.bar(
    state_profit,
    x="Profit",
    y="State",
    orientation="h",
    color="Profit",
    title="Top States by Profit",
    text_auto=".2s"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------
# Top Cities
# ---------------------------------------

city_sales = (
    df.groupby("City", as_index=False)["Sales"]
    .sum()
    .sort_values(by="Sales", ascending=False)
    .head(10)
)

fig3 = px.bar(
    city_sales,
    x="Sales",
    y="City",
    orientation="h",
    color="Sales",
    title="Top Cities by Sales",
    text_auto=".2s"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------
# Geographic Details
# ---------------------------------------

st.subheader("📋 Geographic Details")

st.dataframe(filtered, use_container_width=True)