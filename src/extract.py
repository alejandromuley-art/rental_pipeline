import pandas as pd
import os

def extract_rentals_data(file_name):
    """
    Function to extract data from a CSV file located in the 'data' directory.
    Returns a pandas DataFrame.
    """
    # We use '..' because the script is inside 'src' and data is in a sibling folder
    file_path = os.path.join("data", file_name)
    
    try:
        # Loading the dataset
        df = pd.read_csv(file_path)
        print(f"✅ SUCCESS: {len(df)} rows extracted from {file_name}")
        return df
    except FileNotFoundError:
        print(f"❌ ERROR: File {file_name} not found in 'data/' folder.")
        return None
    except Exception as e:
        print(f"❌ ERROR: Something went wrong. {e}")
        return None

if __name__ == "__main__":
    # Local test to verify the extraction works
    raw_data = extract_rentals_data("rentals.csv")
    if raw_data is not None:
        print(raw_data.head()) # Shows the first 5 rows to confirm