import pandas as pd
import numpy as np

def generate_robust_validation_data(n_samples=1200):
    """
    Generates a dataset specifically designed to validate a Price-to-Volume 
    prediction model, including edge cases for optimization testing.
    """
    np.random.seed(42)
    
    # 1. Base Setup
    data = {
        'Product_ID': [f'P_{i:04d}' for i in range(n_samples)],
        'Base_Unit_Cost': np.random.uniform(10, 100, n_samples).round(2)
    }
    df = pd.DataFrame(data)
    
    # 2. Feature Generation
    # Current Price sits between 1.1x and 1.9x the cost
    df['Input_Price'] = (df['Base_Unit_Cost'] * np.random.uniform(1.1, 1.9, n_samples)).round(2)
    
    # Competitor prices are randomly distributed around our cost/price
    df['Competitor_Price'] = (df['Base_Unit_Cost'] * np.random.uniform(1.0, 1.8, n_samples)).round(2)
    
    # Price Ratio: Key feature for competitive analysis
    df['Price_Ratio'] = (df['Input_Price'] / df['Competitor_Price']).round(3)
    
    # Binary features: Market triggers
    df['Promotion_Active'] = np.random.choice([0, 1], n_samples, p=[0.8, 0.2])
    df['Is_Weekend'] = np.random.choice([0, 1], n_samples, p=[0.71, 0.29])

    # 3. Target Volume Generation (The Ground Truth Logic)
    # We define a non-linear demand function to test model complexity
    def calculate_ground_truth(row):
        # Base demand for the product
        vol = 450 
        
        # Price Sensitivity: Higher markup = lower volume
        margin_pct = row['Input_Price'] / row['Base_Unit_Cost']
        price_penalty = 130 * (margin_pct ** 1.2)
        
        # Competition Sensitivity: If we are more expensive than competitor (Ratio > 1)
        # the penalty increases exponentially.
        ratio_penalty = 90 * (row['Price_Ratio'] ** 2)
        
        # Market Boosters
        promo_boost = 160 if row['Promotion_Active'] == 1 else 0
        weekend_boost = 45 if row['Is_Weekend'] == 1 else 0
        
        # Add random market noise to prevent over-fitting
        noise = np.random.normal(0, 12)
        
        final_vol = vol + promo_boost + weekend_boost - price_penalty - ratio_penalty + noise
        return max(2, int(final_vol)) # Minimum volume floor

    df['Target_Volume'] = df.apply(calculate_ground_truth, axis=1)

    # 4. Injecting Validation Stress Tests (Edge Cases)
    # Case A: Price Floor - Price is equal to cost (Maximum Volume)
    df.loc[0, ['Input_Price', 'Price_Ratio', 'Promotion_Active']] = [df.loc[0, 'Base_Unit_Cost'], 0.8, 1]
    df.loc[0, 'Target_Volume'] = 750
    
    # Case B: Luxury Trap - Extremely high price (Volume should plummet)
    df.loc[1, ['Input_Price', 'Price_Ratio', 'Promotion_Active']] = [500.0, 5.0, 0]
    df.loc[1, 'Target_Volume'] = 5
    
    # Case C: "The Steal" - Half of competitor price
    df.loc[2, ['Input_Price', 'Competitor_Price', 'Price_Ratio']] = [25.0, 50.0, 0.5]
    df.loc[2, 'Target_Volume'] = 680

    return df

# Create and Export
if __name__ == "__main__":
    df_final = generate_robust_validation_data()
    df_final.to_csv('volume_prediction_validation.csv', index=False)
    
    print("--- DATASET GENERATED SUCCESSFULLY ---")
    print(f"File: volume_prediction_validation.csv")
    print(f"Shape: {df_final.shape}")
    print("\nStatistical Snapshot of Target Volume:")
    print(df_final['Target_Volume'].describe())