import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Trim whitespace in object columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Drop rows where all fields are missing or id is NaN
    if "id" in df.columns:
        df = df.dropna(subset=["id"])

    # Optional: fill missing numeric values with median
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())

    # Filter example: keep only rows where city not null/empty
    if "city" in df.columns:
        df = df[df["city"].notna() & (df["city"].str.len() > 0)]

    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    cleaned = clean_data("../data/data_raw.csv", "../data/cleaned.csv")
    print("Cleaned rows:", len(cleaned))
    print(cleaned.head())