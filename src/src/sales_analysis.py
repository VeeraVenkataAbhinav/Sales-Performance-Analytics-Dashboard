def sales_summary(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()
    average_sales = df["Sales"].mean()

    print("\n========== SALES SUMMARY ==========")
    print(f"Total Sales      : ${total_sales:,.2f}")
    print(f"Total Profit     : ${total_profit:,.2f}")
    print(f"Total Orders     : {total_orders}")
    print(f"Total Customers  : {total_customers}")
    print(f"Average Sale     : ${average_sales:.2f}")