# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data from CSV file
df = pd.read_csv("data/stock_data.csv")

# Converting the "date" column to datetime
df["date"] = pd.to_datetime(df["date"])

print(df.head(10))