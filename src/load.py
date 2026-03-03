import sqlite3
import pandas as pd

def load_data_to_sqlite(df, db_name="barcelona_rentals.db"):
    """
    Saves a pandas DataFrame into a SQLite database table.
    If the table already exists, it replaces the data.
    """
    try:
        # 1. Establish connection to the database (it creates the file if it doesn't exist)
        conn = sqlite3.connect(db_name)
        
        # 2. Use pandas to write the data to a SQL table named 'rentals'
        # 'if_exists=replace' ensures we have clean data every time we run the pipeline
        df.to_sql('rentals', conn, if_exists='replace', index=False)
        
        conn.close()
        print(f"✅ SUCCESS: {len(df)} records saved to database '{db_name}' in 'rentals' table.")
    except Exception as e:
        print(f"❌ ERROR: Failed to load data to SQL. {e}")

if __name__ == "__main__":
    print("Loader module ready.")