import pandas as pd

def clean_rental_data(df):
    """
    Cleans raw rental data by selecting columns, handling missing values, 
    and ensuring correct data types.
    """
    # 1. Column Selection: We only want relevant features
    relevant_columns = [
        'name', 'neighbourhood', 'room_type', 'price', 
        'minimum_nights', 'number_of_reviews'
    ]
    df_clean = df[relevant_columns].copy()

    # 2. Handling Nulls: Remove rows where price or neighborhood is missing
    df_clean = df_clean.dropna(subset=['price', 'neighbourhood'])

    # 3. Data Formatting: In some datasets, price comes as a string (e.g., "$50.00")
    # Let's make sure it's a clean float for mathematical operations
    if df_clean['price'].dtype == 'object':
        df_clean['price'] = df_clean['price'].str.replace('$', '').str.replace(',', '').astype(float)

    # 4. Feature Engineering: Create a basic metric
    # Total cost for the minimum stay required
    df_clean['min_total_cost'] = df_clean['price'] * df_clean['minimum_nights']

    print(f"✅ SUCCESS: Data transformed. {len(df_clean)} records ready for loading.")
    return df_clean

if __name__ == "__main__":
    # This is for standalone testing only
    print("Transformation module ready.")