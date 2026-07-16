import plotly.express as px


def sales_by_category(df):
    category_sales = (
        df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        color="Category",
        text_auto=".2s",
        title="Sales by Category"
    )

    fig.update_layout(
        title_x=0.3,
        xaxis_title="Category",
        yaxis_title="Sales"
    )

    return fig


def sales_by_region(df):
    region_sales = (
        df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        color="Region",
        text_auto=".2s",
        title="Sales by Region"
    )

    fig.update_layout(
        title_x=0.3,
        xaxis_title="Region",
        yaxis_title="Sales"
    )

    return fig
def monthly_sales_trend(df):
    import plotly.express as px

    monthly_sales = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

    fig = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales ($)",
        title_x=0.35
    )

    return fig
def top_products(df):
    import plotly.express as px

    top = (
        df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top,
        x="Sales",
        y="Product Name",
        orientation="h",
        color="Sales",
        title="Top 10 Products by Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        title_x=0.30
    )

    return fig
def top_customers(df):
    import plotly.express as px

    customers = (
        df.groupby("Customer Name", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        customers,
        x="Sales",
        y="Customer Name",
        orientation="h",
        color="Sales",
        text_auto=".2s",
        title="Top 10 Customers by Sales"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        title_x=0.30,
        xaxis_title="Sales ($)",
        yaxis_title="Customer"
    )

    return fig