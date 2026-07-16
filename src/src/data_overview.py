def dataset_overview(df):
    print("\nDataset Shape")
    print(df.shape)

    print("\nColumn Names")
    for column in df.columns:
        print(column)

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nStatistical Summary")
    print(df.describe())

    print("\nUnique Categories")
    print(df["Category"].unique())

    print("\nUnique Regions")
    print(df["Region"].unique())

    print("\nUnique Segments")
    print(df["Segment"].unique())