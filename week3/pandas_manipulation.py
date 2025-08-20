import pandas as pd

def main():
    df = pd.read_csv("../data/sales.csv", parse_dates=["date"])
    print("Head:\n", df.head())
    # Indexing & selection
    jan = df[df["date"].dt.month == 2]
    print("Filtered (Feb):", len(jan))
    # Grouping
    by_cat = df.groupby("category").agg(revenue_sum=("revenue","sum"),
                                        units_sum=("units","sum"),
                                        revenue_mean=("revenue","mean"))
    print("By category:\n", by_cat)

if __name__ == "__main__":
    main()