import pandas as pd


def load_data():
    df = pd.read_csv("data/Superstore.csv", encoding="latin1")
    return df