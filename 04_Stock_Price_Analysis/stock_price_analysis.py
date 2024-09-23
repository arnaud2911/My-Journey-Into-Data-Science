# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data from CSV file
df = pd.read_csv("data/stock_data.csv")

# Converting the "date" column to datetime
df["date"] = pd.to_datetime(df["date"])

# Data Cleaning Steps
# Replacing Invalid Entries with np.nan
df["stock_price"] = df["stock_price"].replace(["missing", "error", None], np.nan)
# Converting the "stock_price" column to float
df["stock_price"] = df["stock_price"].astype(float)
# Check and handle missing value
#print(df.isnull().sum()) # Check for missing values
df["stock_price"] = df["stock_price"].interpolate(method="linear") # Interpolate missing values

# Verify the changes
print(df.head(10))