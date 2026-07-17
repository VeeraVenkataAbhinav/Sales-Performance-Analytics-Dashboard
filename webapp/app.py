import streamlit as st

from data_loader import load_data
from metrics import get_metrics
from filters import apply_filters
from charts import (
    sales_by_category,
    sales_by_region,
    monthly_sales_trend,
    top_products,
    top_customers
)
from insights import generate_insights

st.set_page_config(
    page_title="Sales Performance Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)
st.markdown(
    """
    <style>
    .main-title{
        font-size:64px !important;
        font-weight:800 !important;
        color:#1E88E5 !important;
        margin-bottom:0px !important;
        line-height:1.1 !important;
    }

    .subtitle{
        font-size:22px;
        color:#666666;
        margin-top:-5px;
        margin-bottom:25px;
    }

    .footer{
        text-align:center;
        color:gray;
        font-size:14px;
        margin-top:30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p class="main-title">📊 Sales Performance Analytics Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Interactive Business Analytics Dashboard</p>',
    unsafe_allow_html=True
)
# Load Data
df = load_data()

# Apply Filters
df = apply_filters(df)


# KPI Cards
metrics = get_metrics(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${metrics['Total Sales']:,.2f}")

with col2:
    st.metric("📈 Total Profit", f"${metrics['Total Profit']:,.2f}")

with col3:
    st.metric("📦 Total Orders", metrics["Total Orders"])

with col4:
    st.metric("👥 Total Customers", metrics["Total Customers"])

st.divider()

# Sales Charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        sales_by_category(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        sales_by_region(df),
        use_container_width=True
    )

st.divider()

# Monthly Trend
st.subheader("📈 Monthly Sales Trend")

st.plotly_chart(
    monthly_sales_trend(df),
    use_container_width=True
)

st.divider()

# Products & Customers
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        top_products(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        top_customers(df),
        use_container_width=True
    )

st.divider()

# AI Insights
st.subheader("🤖 AI Business Insights")

for insight in generate_insights(df):
    st.success(insight)

st.divider()

# Download Section
st.subheader("📥 Download Filtered Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered CSV",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        Developed by Abhinav | Powered by Python • Plotly • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)