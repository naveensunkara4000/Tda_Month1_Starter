import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("../data/sales.csv", parse_dates=["date"])

    # 1) Histogram of revenue
    plt.figure()
    df["revenue"].plot(kind="hist", bins=10, title="Revenue Distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.savefig("revenue_hist.png", bbox_inches="tight")

    # 2) Scatter: units vs revenue
    plt.figure()
    plt.scatter(df["units"], df["revenue"])
    plt.title("Units vs Revenue")
    plt.xlabel("Units")
    plt.ylabel("Revenue")
    plt.savefig("units_vs_revenue_scatter.png", bbox_inches="tight")

    # 3) Boxplot by category
    plt.figure()
    df.boxplot(column="revenue", by="category")
    plt.title("Revenue by Category")
    plt.suptitle("")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.savefig("revenue_box_by_category.png", bbox_inches="tight")

    # 4) Heatmap (correlation)
    plt.figure()
    corr = df[["revenue","units"]].corr()
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.savefig("corr_heatmap.png", bbox_inches="tight")

    print("Saved plots: revenue_hist.png, units_vs_revenue_scatter.png, revenue_box_by_category.png, corr_heatmap.png")

if __name__ == "__main__":
    main()