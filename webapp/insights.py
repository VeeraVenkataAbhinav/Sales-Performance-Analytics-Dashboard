def generate_insights(df):
    insights = []

    # Top Category
    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Region
    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Product
    top_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Customer
    top_customer = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Segment
    top_segment = (
        df.groupby("Segment")["Sales"]
        .sum()
        .idxmax()
    )

    # Highest Profit State
    top_state = (
        df.groupby("State")["Profit"]
        .sum()
        .idxmax()
    )

    insights.append(f"🏆 Highest Selling Category: {top_category}")
    insights.append(f"🌍 Best Performing Region: {top_region}")
    insights.append(f"📦 Top Selling Product: {top_product}")
    insights.append(f"👤 Top Customer: {top_customer}")
    insights.append(f"👥 Highest Revenue Segment: {top_segment}")
    insights.append(f"📍 Most Profitable State: {top_state}")

    return insights