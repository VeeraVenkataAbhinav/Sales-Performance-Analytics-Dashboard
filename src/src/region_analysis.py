def region_analysis(df):
    region_summary = (
        df.groupby("Region")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Profit=("Profit", "sum"),
            Total_Orders=("Order ID", "nunique"),
            Total_Customers=("Customer ID", "nunique")
        )
        .sort_values(by="Total_Sales", ascending=False)
    )

    print("\nRegion Analysis")
    print(region_summary)

    return region_summary