import os
import matplotlib.pyplot as plt


CHART_FOLDER = "outputs/charts"


def save_chart(file_name):
    os.makedirs(CHART_FOLDER, exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"{CHART_FOLDER}/{file_name}", dpi=300)
    plt.close()


def plot_sales_by_category(df):
    sales = df.groupby("Category")["Sales"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(sales.index, sales.values)

    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    save_chart("sales_by_category.png")


def plot_monthly_sales(df):
    monthly_sales = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
    )

    plt.figure(figsize=(12, 5))
    plt.plot(
        monthly_sales.index.astype(str),
        monthly_sales.values,
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)

    save_chart("monthly_sales.png")


def plot_sales_by_region(df):
    region_sales = df.groupby("Region")["Sales"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(region_sales.index, region_sales.values)

    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")

    save_chart("sales_by_region.png")


def plot_profit_by_category(df):
    category_profit = df.groupby("Category")["Profit"].sum()

    plt.figure(figsize=(8, 5))
    plt.bar(category_profit.index, category_profit.values)

    plt.title("Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")

    save_chart("profit_by_category.png")


def plot_sales_by_segment(df):
    segment_sales = df.groupby("Segment")["Sales"].sum()

    plt.figure(figsize=(8, 6))
    plt.pie(
        segment_sales.values,
        labels=segment_sales.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Sales Distribution by Segment")

    save_chart("sales_by_segment.png")