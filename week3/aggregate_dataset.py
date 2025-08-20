import pandas as pd

def aggregate_sales(input_path, output_path):
    df = pd.read_csv(input_path, parse_dates=["date"])
    # Drop missing values in key columns
    df = df.dropna(subset=["category","revenue","units"])

    # Daily revenue per category
    daily = df.groupby(["date","category"]).agg(
        revenue_sum=("revenue","sum"),
        units_sum=("units","sum")
    ).reset_index()

    # Overall stats
    overall = df.agg(revenue_total=("revenue","sum"),
                     units_total=("units","sum"))

    daily.to_csv(output_path, index=False)
    print("Saved daily aggregates to", output_path)
    print("Overall totals:\n", overall)

if __name__ == "__main__":
    aggregate_sales("../data/sales.csv", "../data/daily_aggregates.csv")