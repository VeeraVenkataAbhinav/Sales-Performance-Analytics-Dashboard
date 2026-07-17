import os


REPORT_FOLDER = "outputs/reports"


def generate_report(summary, category_df, region_df, segment_df):
    os.makedirs(REPORT_FOLDER, exist_ok=True)

    report_path = os.path.join(REPORT_FOLDER, "business_report.txt")

    with open(report_path, "w") as file:
        file.write("Sales Performance Analytics Dashboard\n")
        file.write("=" * 50)
        file.write("\n\n")

        file.write("Sales Summary\n")
        file.write("-" * 50)
        file.write("\n")

        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

        file.write("\n")

        file.write("Category Performance\n")
        file.write("-" * 50)
        file.write("\n")
        file.write(category_df.to_string())

        file.write("\n\n")

        file.write("Region Performance\n")
        file.write("-" * 50)
        file.write("\n")
        file.write(region_df.to_string())

        file.write("\n\n")

        file.write("Segment Performance\n")
        file.write("-" * 50)
        file.write("\n")
        file.write(segment_df.to_string())