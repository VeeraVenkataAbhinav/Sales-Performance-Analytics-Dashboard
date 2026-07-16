import streamlit as st
import plotly.express as px

from data_loader import load_data
from filters import apply_filters

st.set_page_config(
    page_title="Product Intelligence",
    page_icon="📦",
    layout="wide"
)

df = load_data()
df = apply_filters(df)

st.title("📦 Product Intelligence")

# ------------------------------------------------
# Product Search
# ------------------------------------------------

products = sorted(df["Product Name"].unique())

selected_product = st.selectbox(
    "🔍 Search Product",
    ["All Products"] + products
)

if selected_product != "All Products":
    filtered = df[df["Product Name"] == selected_product]
else:
    filtered = df.copy()

# ------------------------------------------------
# KPI Cards
# ------------------------------------------------

sales = filtered["Sales"].sum()
profit = filtered["Profit"].sum()
quantity = filtered["Quantity"].sum()
orders = filtered["Order ID"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Sales", f"${sales:,.2f}")
c2.metric("📈 Profit", f"${profit:,.2f}")
c3.metric("📦 Quantity", quantity)
c4.metric("🛒 Orders", orders)

st.divider()

# ------------------------------------------------
# Top Products by Sales
# ------------------------------------------------

top_sales = (
    df.groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values(by="Sales", ascending=False)
    .head(10)
)

fig1 = px.bar(
    top_sales,
    x="Sales",
    y="Product Name",
    orientation="h",
    color="Sales",
    title="Top 10 Products by Sales",
    text_auto=".2s"
)

st.plotly_chart(fig1, use_container_width=True)

# ------------------------------------------------
# Top Products by Profit
# ------------------------------------------------

top_profit = (
    df.groupby("Product Name", as_index=False)["Profit"]
    .sum()
    .sort_values(by="Profit", ascending=False)
    .head(10)
)

fig2 = px.bar(
    top_profit,
    x="Profit",
    y="Product Name",
    orientation="h",
    color="Profit",
    title="Top 10 Products by Profit",
    text_auto=".2s"
)

st.plotly_chart(fig2, use_container_width=True)

# ------------------------------------------------
# Loss Making Products
# ------------------------------------------------

loss = (
    df.groupby("Product Name", as_index=False)["Profit"]
    .sum()
    .sort_values(by="Profit")
    .head(10)
)

fig3 = px.bar(
    loss,
    x="Profit",
    y="Product Name",
    orientation="h",
    color="Profit",
    title="Top 10 Loss Making Products",
    text_auto=".2s"
)

st.plotly_chart(fig3, use_container_width=True)

# ------------------------------------------------
# Product Details
# ------------------------------------------------

st.subheader("📋 Product Details")

st.dataframe(filtered, use_container_width=True)