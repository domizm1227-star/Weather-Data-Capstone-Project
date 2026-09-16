import pandas as pd
import re

def clean_data():
    # 1. Load raw dataset
    raw_df = pd.read_csv("raw_weather_data.csv")
    
    print("--- BEFORE CLEANING ---")
    print(f"Shape: {raw_df.shape}")
    print(raw_df.head(5))
    print("\n" + "="*40 + "\n")

    cleaned_df = raw_df.copy()

    # 2. Drop duplicates and empty records
    cleaned_df.drop_duplicates(inplace=True)
    cleaned_df.dropna(subset=["City", "Temperature_Raw"], inplace=True)
    cleaned_df = cleaned_df[cleaned_df["City"] != "N/A"]

    # 3. Clean and Transform Temperature Values
    def extract_temp_fahrenheit(val):
        if pd.isna(val):
            return None
        # Extract numeric value preceding °F or digits
        match = re.search(r"(-?\d+)\s*°?F?", str(val))
        if match:
            return float(match.group(1))
        return None

    cleaned_df["Temperature_F"] = cleaned_df["Temperature_Raw"].apply(extract_temp_fahrenheit)

    # Calculate Celsius equivalent
    cleaned_df["Temperature_C"] = cleaned_df["Temperature_F"].apply(
        lambda f: round((f - 32) * 5 / 9, 1) if pd.notna(f) else None
    )

    # 4. Clean text fields
    cleaned_df["Condition"] = cleaned_df["Condition"].fillna("Unknown").str.title()

    # Drop unparsed raw columns
    cleaned_df.drop(columns=["Temperature_Raw"], inplace=True)

    print("--- AFTER CLEANING ---")
    print(f"Shape: {cleaned_df.shape}")
    print(cleaned_df.head(5))

    # 5. Save cleaned dataset
    cleaned_df.to_csv("cleaned_weather_data.csv", index=False)
    print("\nSaved clean data to 'cleaned_weather_data.csv'")

if __name__ == "__main__":
    clean_data()