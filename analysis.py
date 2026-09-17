import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def analyze_and_plot():
    conn = sqlite3.connect("weather_data.db")
    
    # Query data back out of SQLite using pandas
    query = "SELECT * FROM cleaned_weather"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    print("--- DATA SUMMARY ---")
    print(df.describe())
    
    # Create a plot: Top 10 Cities by Temperature
    if "Temperature" in df.columns and "City" in df.columns:
        df_sorted = df.sort_values(by="Temperature", ascending=False).head(10)
        
        plt.figure(figsize=(10,6))
        plt.bar(df_sorted["City"], df_sorted["Temperature"], color="skyblue")
        plt.title("Top 10 warmest cities")
        plt.xlabel("Temperature")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("weather_summary_plot.png")
        print("Saved plot to 'weather_summary_plot.png'")


if __name__ == "__main__":
    analyze_and_plot()