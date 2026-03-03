from src.extract import extract_rentals_data
from src.transform import clean_rental_data
from src.load import load_data_to_sqlite  # <-- New Import

def run_pipeline():
    print("--- Starting Rental Pipeline ---")

    # 1. EXTRACTION
    raw_data = extract_rentals_data("rentals.csv")

    if raw_data is not None:
        # 2. TRANSFORMATION
        clean_data = clean_rental_data(raw_data)

        # 3. LOADING (New Step!)
        load_data_to_sqlite(clean_data)

        print(f"\nPipeline finished perfectly. You are now a Data Engineer! 🚀")
    else:
        print("❌ Pipeline stopped due to extraction error.")

if __name__ == "__main__":
    run_pipeline()