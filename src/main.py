from load_data import load_data
from data_cleaning import clean_data
from export_data import export_dataframe

from analysis import (
    sales_summary,
    category_analysis,
    region_analysis,
    segment_analysis,
    top_products_by_sales,
    top_products_by_profit,
    loss_making_products,
    top_customers_by_sales,
    top_customers_by_profit,
    repeat_customers,
    state_analysis,
    city_analysis,
    monthly_sales_analysis,
    discount_analysis
)

from visualization import (
    plot_sales_by_category,
    plot_monthly_sales,
    plot_sales_by_region,
    plot_profit_by_category,
    plot_sales_by_segment
)


def main():
    # Load and clean the data
    df = load_data()
    df = clean_data(df)

    # Sales Summary
    summary = sales_summary(df)

    print("\n========== SALES SUMMARY ==========")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Category Analysis
    category_df = category_analysis(df)

    print("\n========== CATEGORY ANALYSIS ==========")
    print(category_df)

    export_dataframe(category_df, "category_analysis.csv")
    print("\n========== STATE ANALYSIS ==========")
    print(state_analysis(df).head(10))

    print("\n========== CITY ANALYSIS ==========")
    print(city_analysis(df).head(10))

    print("\n========== MONTHLY SALES ==========")
    print(monthly_sales_analysis(df).head(12))

    print("\n========== DISCOUNT ANALYSIS ==========")
    print(discount_analysis(df))

    # Region Analysis
    print("\n========== REGION ANALYSIS ==========")
    print(region_analysis(df))

    # Segment Analysis
    print("\n========== SEGMENT ANALYSIS ==========")
    print(segment_analysis(df))

    # Top Products by Sales
    print("\n========== TOP 10 PRODUCTS BY SALES ==========")
    print(top_products_by_sales(df))

    # Top Products by Profit
    print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")
    print(top_products_by_profit(df))

    # Loss Making Products
    print("\n========== TOP 10 LOSS MAKING PRODUCTS ==========")
    print(loss_making_products(df))

    # Top Customers by Sales
    print("\n========== TOP 10 CUSTOMERS BY SALES ==========")
    print(top_customers_by_sales(df))

    # Top Customers by Profit
    print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")
    print(top_customers_by_profit(df))

    # Repeat Customers
    print("\n========== REPEAT CUSTOMERS ==========")
    print(repeat_customers(df).head(10))

    # Visualizations
    plot_sales_by_category(df)
    plot_monthly_sales(df)
    plot_sales_by_region(df)
    plot_profit_by_category(df)
    plot_sales_by_segment(df)


if __name__ == "__main__":
    main()