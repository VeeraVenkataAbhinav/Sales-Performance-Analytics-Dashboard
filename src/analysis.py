def sales_summary(df):
    return {
        "Total Sales": round(df["Sales"].sum(), 2),
        "Total Profit": round(df["Profit"].sum(), 2),
        "Total Orders": df["Order ID"].nunique(),
        "Total Customers": df["Customer ID"].nunique(),
        "Average Sale": round(df["Sales"].mean(), 2)
    }


def category_analysis(df):
    return (
        df.groupby("Category")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Orders=("Order ID", "nunique")
        )
        .sort_values("Total_Sales", ascending=False)
    )


def region_analysis(df):
    return (
        df.groupby("Region")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .sort_values("Total_Sales", ascending=False)
    )


def segment_analysis(df):
    return (
        df.groupby("Segment")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .sort_values("Total_Sales", ascending=False)
    )
def top_products_by_sales(df, top_n=10):
    return (
        df.groupby("Product Name")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Quantity_Sold=("Quantity", "sum")
        )
        .sort_values(by="Total_Sales", ascending=False)
        .head(top_n)
    )


def top_products_by_profit(df, top_n=10):
    return (
        df.groupby("Product Name")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Quantity_Sold=("Quantity", "sum")
        )
        .sort_values(by="Total_Profit", ascending=False)
        .head(top_n)
    )


def loss_making_products(df, top_n=10):
    return (
        df.groupby("Product Name")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .sort_values(by="Total_Profit")
        .head(top_n)
    )
def top_customers_by_sales(df, top_n=10):
    return (
        df.groupby(["Customer ID", "Customer Name"])
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Orders=("Order ID", "nunique")
        )
        .sort_values(by="Total_Sales", ascending=False)
        .head(top_n)
    )


def top_customers_by_profit(df, top_n=10):
    return (
        df.groupby(["Customer ID", "Customer Name"])
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Orders=("Order ID", "nunique")
        )
        .sort_values(by="Total_Profit", ascending=False)
        .head(top_n)
    )


def repeat_customers(df):
    return (
        df.groupby(["Customer ID", "Customer Name"])
        .agg(
            Total_Orders=("Order ID", "nunique")
        )
        .query("Total_Orders > 1")
        .sort_values(by="Total_Orders", ascending=False)
    )
def state_analysis(df):
    return (
        df.groupby("State")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Orders=("Order ID", "nunique")
        )
        .sort_values(by="Total_Sales", ascending=False)
    )


def city_analysis(df):
    return (
        df.groupby("City")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Orders=("Order ID", "nunique")
        )
        .sort_values(by="Total_Sales", ascending=False)
    )


def monthly_sales_analysis(df):
    return (
        df.groupby(["Year", "Month"])
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .reset_index()
    )


def discount_analysis(df):
    return (
        df.groupby("Discount")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum")
        )
        .sort_index()
    )