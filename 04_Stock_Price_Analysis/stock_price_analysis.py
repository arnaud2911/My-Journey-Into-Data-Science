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

# Random Simulation
# Let's simulate the stock price for the next 30 days
np.random.seed(42) # Set seed for reproducibility
starting_price = df["stock_price"].iloc[-1]
simulated_returns = np.random.normal(loc = daily_return_mean, scale = daily_return_std, size = 30)
simulated_prices  = [starting_price]
for r in simulated_returns:
    next_price = simulated_prices[-1] * (1 + r / 100)
    simulated_prices.append(next_price)
simulated_prices = simulated_prices[1: ] # Remove the starting price
#Plot Simulated Stock Price Path
plt.figure(figsize = (12, 6))
sns.lineplot(x = range(1, 31), y = simulated_prices, color = "green", marker="o")
plt.title("Simulated Stock Price Path for the Next 30 Days")
plt.xlabel("Day")
plt.ylabel("Stock Price")
plt.tight_layout()
#plt.show()
plt.savefig("visualizations/simulated_stock_price.png")

#Insights And Interpretation
# Print statistical analysis results
print("Statistical Analysis of Daily Returns:")
print(f"mean of daily returns: {daily_return_mean:.2f}%")
print(f"median of daily returns: {daily_return_median:.2f}%")
print(f"standard deviation of daily returns: {daily_return_std:.2f}%")

print("Days when the daily return was above one standard deviation from the mean:")
for day in high_return_days:
    print(day)
print("\nInterpretation of Simulation:")
print("Based on historical daily returns, the randomly simulated stock price path over next the 30 days shows an initial rise in the first 10 days, before starting to experience a non-stop decline.")
print("This provides an estimate but does not guarantee actual future performance due to market volatility and unforeseen factors.")
