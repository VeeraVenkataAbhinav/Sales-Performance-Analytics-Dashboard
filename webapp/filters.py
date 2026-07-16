import streamlit as st


def apply_filters(df):
    st.sidebar.header("Filters")

    region = st.sidebar.multiselect(
        "Select Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    category = st.sidebar.multiselect(
        "Select Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    segment = st.sidebar.multiselect(
        "Select Segment",
        options=sorted(df["Segment"].unique()),
        default=sorted(df["Segment"].unique())
    )

    filtered_df = df[
        (df["Region"].isin(region)) &
        (df["Category"].isin(category)) &
        (df["Segment"].isin(segment))
    ]

    return filtered_df