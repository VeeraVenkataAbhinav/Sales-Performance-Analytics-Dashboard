def get_metrics(df):
    return {
        "Total Sales": df["Sales"].sum(),
        "Total Profit": df["Profit"].sum(),
        "Total Orders": df["Order ID"].nunique(),
        "Total Customers": df["Customer ID"].nunique(),
    }