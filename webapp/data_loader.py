import pandas as pd


def load_data():
    df = pd.read_csv("data/Superstore.csv", encoding="latin1")

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    return df