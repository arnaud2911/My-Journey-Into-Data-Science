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

# Statistical Analysis
# Let's calculate the daily returns
df["daily_return"] = df["stock_price"].pct_change() * 100
df.loc[0, "daily_return"] = np.nan  # Set first day's return to NaN
# Let's Compute Statistics
daily_return_mean = df["daily_return"].mean()
daily_return_median = df["daily_return"].median()
daily_return_std = df["daily_return"].std()
# Let's identfy high return days
threshold = daily_return_mean + daily_return_std
high_return_days = df[df["daily_return"] > threshold]["date"].dt.strftime("%Y-%m-%d").tolist()

# Data Visualization
# Let's set the style for Seaborn
sns.set_theme(style="darkgrid")
# Let's plot the the stock prices over time
plt.figure(figsize = (12, 6))
sns.lineplot(data = df, x = "date", y = "stock_price", marker="o")
plt.title("Stock Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()
plt.savefig("visualizations/stock_prices_over_time.png")

# Let's plot the histogram of daily returns
plt.figure(figsize = (12, 6))
sns.histplot(df["daily_return"].dropna(), bins = 50, kde = True)
plt.title("Histogram of Daily Returns")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.tight_layout()
#plt.show()
plt.savefig("visualizations/histogram_of_daily_returns.png")

# Verify the changes
print(df.head())