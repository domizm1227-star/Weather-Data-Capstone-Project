import sqlite3
import pandas as pd

def save_to_database():
    db_name = "weather_data.db"
    print(f"Connecting to database '{db_name}'...")
    
    # Establishing a connection to SQLite
    conn = sqlite3.connect(db_name)

    try:
        # Loading raw CSV data and write to SQLite
        raw_df = pd.read_csv("raw_weather_data.csv")
        raw_df.to_sql(name="raw_weather", con=conn, if_exists="replace", index=False)
        print("Successfully loaded 'raw_weather_data.csv' into 'raw_weather' table.")

        # Loading clean CSV data and write to SQLite
        cleaned_df = pd.read_csv("cleaned_weather_data.csv")
        cleaned_df.to_sql(name="cleaned_weather", con=conn, if_exists="replace", index=False)
        print("Successfully loaded 'cleaned_weather_data.csv' into 'cleaned_weather' table.")

        # Quick database check
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM cleaned_weather")
        row_count = cursor.fetchone()[0]
        print(f"Verification: 'cleaned_weather' table contains {row_count} rows.")

    except FileNotFoundError as e:
        print(f"Error finding CSV file: {e}")
    except Exception as e:
        print(f"Error transferring data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    save_to_database()