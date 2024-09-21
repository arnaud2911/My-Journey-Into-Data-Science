# generate_stock_data.py

import numpy as np
import pandas as pd
import os

# Generate date range for 20 years (2000-01-01 to 2019-12-31)
date_range = pd.date_range(start='2000-01-01', end='2019-12-31', freq='D')

# Generate random stock prices using a log-normal distribution
np.random.seed(42)  # For reproducibility
prices = np.random.lognormal(mean=0.0005, sigma=0.02, size=len(date_range)).cumprod() * 100

# Convert prices to a Pandas Series
prices_with_anomalies = pd.Series(prices)

# Introduce anomalies and missing values
num_anomalies = int(0.05 * len(prices_with_anomalies))  # 5% anomalies
anomalies_indices = np.random.choice(len(prices_with_anomalies), size=num_anomalies, replace=False)

for idx in anomalies_indices:
    anomaly_type = np.random.choice(['missing', 'error', None])
    prices_with_anomalies.iloc[idx] = anomaly_type

# Create DataFrame
data = {
    'date': date_range,
    'stock_price': prices_with_anomalies
}

df = pd.DataFrame(data)

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Save DataFrame to CSV
df.to_csv('data/stock_data.csv', index=False)

print("Dataset generated and saved to 'data/stock_data.csv'")