import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run_neighborhood_analysis(db_name="barcelona_rentals.db"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM rentals", conn)
    
    # Analysis
    top_neighborhoods = df.groupby('neighbourhood')['price'].mean().sort_values(ascending=False).head(10)
    
    # --- VISUALIZATION ---
    print("\n📊 Generating chart...")
    plt.figure(figsize=(10, 6))
    top_neighborhoods.plot(kind='bar', color='salmon')
    plt.title('Top 10 Most Expensive Neighborhoods in Barcelona')
    plt.ylabel('Average Price (€)')
    plt.xlabel('Neighborhood')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save the chart as an image
    plt.savefig('neighborhood_prices.png')
    print("✅ SUCCESS: Chart saved as 'neighborhood_prices.png'")
    
    conn.close()

if __name__ == "__main__":
    run_neighborhood_analysis()