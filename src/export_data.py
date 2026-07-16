import os


OUTPUT_FOLDER = "outputs/data"


def export_dataframe(dataframe, filename):
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    dataframe.to_csv(
        os.path.join(OUTPUT_FOLDER, filename),
        index=True
    )

    print(f"{filename} exported successfully.")