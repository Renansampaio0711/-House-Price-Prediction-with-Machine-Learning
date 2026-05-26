def clean(df):
    import pandas as pd
    # converting total charges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    # removing rows with null values in total charges
    df = df[pd.to_numeric(df["TotalCharges"], errors="coerce").notna()]
    #converting churn to binary
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df