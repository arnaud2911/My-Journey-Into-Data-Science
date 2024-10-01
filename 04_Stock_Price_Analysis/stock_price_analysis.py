# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load stock data from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file containing stock data.

    Returns:
    - df (DataFrame): The loaded data as a Pandas DataFrame.
    """
    # Reading the data from CSV file
    df = pd.read_csv(file_path)
    # Cobvert the "date" column to datetime
    df["date"] = pd.to_datetime(df["date"])
    return df

def clean_data(df):
    """
    Clean the stock data.

    Parameters:
    - df (DataFrame): The stock data as a Pandas DataFrame
    
    Returns:
    - df (DataFrame): The cleaned stock data as a Pandas DataFrame
    """
    # Replacing Invalid Entries with np.nan
    df["stock_price"] = df["stock_price"].replace(["missing", "error", None], np.nan)
    # Converting the "stock_price" column to float
    df["stock_price"] = df["stock_price"].astype(float)
    # Check and handle missing value
    df["stock_price"] = df["stock_price"].interpolate(method="linear") # Interpolate missing values
    return df

def calculate_daily_returns(df):
    """
    Calculate the daily returns of the stock.

    Parameters:
    - df (DataFrame): The cleaned stock data as a Pandas DataFrame

    Returns:
    - df (DataFrame): The stock data with the "daily_return" as a new column
    """
    # Calculate the daily returns
    df["daily_return"] = df["stock_price"].pct_change() * 100
    df.loc[0, "daily_return"] = np.nan  # Set first day's return to NaN
    return df

def perform_statistical_analysis(df):
    """
   Perform statistical analysis on daily returns.

    Parameters:
    - df (DataFrame): The stock data with daily returns.

    Returns:
    - stats (dict): A dictionary containing mean, median, std of daily returns.
    - high_return_days (list): A list of dates with high daily returns.
    """
    # Calculate statistics
    daily_return_mean = df["daily_return"].mean()
    daily_return_median = df["daily_return"].median()
    daily_return_std = df["daily_return"].std()
    # Identify days with daily return above one standard deviation from the mean
    threshold = daily_return_mean + daily_return_std
    high_return_days = df[df["daily_return"] > threshold]["date"].dt.strftime("%Y-%m-%d").tolist()
    # Compile stats into a dictionary
    stats = {
        "mean": daily_return_mean,
        "median": daily_return_median,
        "std": daily_return_std,
        "threshold": threshold
    }
    return stats, high_return_days

def simulate_stock_prices(df, stats, num_days = 30):
    """Simulate future stock prices using a random walk model.

    Parameters:
    - df (DataFrame): The stock data with daily returns.
    - stats (dict): Statistical measures of daily returns.
    - days (int): Number of days to simulate.

    Returns:
    - simulated_prices (list): A list of simulated stock prices.
    """
    # Set seed for reproducibility
    np.random.seed(42)
    # Get the last known stock price which is the starting price
    starting_price = df["stock_price"].iloc[-1]
    # Generate random daily returns
    simulated_returns = np.random.normal(
        loc = stats["mean"],
        scale = stats["std"],
        size = num_days
    )
    # Calculae simulated stock prices
    simulated_prices = [starting_price]
    for r in simulated_returns:
        next_price = simulated_prices[-1] * (1 + r / 100)
        simulated_prices.append(next_price)
    # Remove the starting price to match the number of days
    simulated_prices = simulated_prices[1: ]
    return simulated_prices

def visualize_data(df, simulated_prices):
    """
    Create and save plots of stock prices, daily returns, and simulated prices.

    Parameters:
    - df (DataFrame): The stock data with daily returns.
    - simulated_prices (list): The simulated future stock prices.
    """
    # Set the style for Seaborn
    sns.set_theme(style = "darkgrid")

    # Plot the stock prices over time
    plt.figure(figsize = (12, 6))
    sns.lineplot(data = df, x = "date", y = "stock_price", marker = "o")
    plt.title("Stock Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig("visualizations/stock_prices_over_time.png")
    plt.close()

    # Plot the histogram of daily returns
    plt.figure(figsize = (12, 6))
    sns.histplot(df["daily_return"].dropna(), bins = 50, kde = True)
    plt.title("Histogram of Daily Returns")
    plt.xlabel("Daily Return (%)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("visualizations/histogram_of_daily_returns.png")
    plt.close()

    # Plot simulated stock prices
    plt.figure(figsize = (12, 6))
    sns.lineplot(x = range(1, len(simulated_prices) + 1), y = simulated_prices, color = "green", marker = "o")
    plt.title("Simulated Stock Price Path for the Next 30 Days")
    plt.xlabel("Day")
    plt.ylabel("Stock Price")
    plt.tight_layout()
    plt.savefig("visualizations/simulated_stock_price.png")
    plt.close()

def main():
    """
    Main function to execute the stock price analysis and simulation.
    """
    # step 1: Load the data
    df = load_data("data/stock_data.csv")

    # step 2: Clean the data
    df = clean_data(df)

    # step 3: Calculate daily returns
    df = calculate_daily_returns(df)

    # step 4: Perform statistical analysis
    stats, high_return_days = perform_statistical_analysis(df)

    # step 5: Simulate future stock prices
    simulated_prices = simulate_stock_prices(df, stats, num_days = 30)

    # step 6: Visualize the data
    visualize_data(df, simulated_prices)

    # step 7: Print insights and interpretation
    print("Statistical Analysis of Daily Returns:")
    print(f"mean of daily returns: {stats['mean']:.2f}%")
    print(f"median of daily returns: {stats['median']:.2f}%")
    print(f"standard deviation of daily returns: {stats['std']:.2f}%")

    print("Days when the daily return was above one standard deviation from the mean:")
    for day in high_return_days:
        print(day)
    
    print("\nInterpretation of Simulation:")
    print("Based on historical daily returns, the randomly simulated stock price path over next the 30 days shows an initial rise in the first 10 days, before starting to experience a non-stop decline.")
    print("This provides an estimate but does not guarantee actual future performance due to market volatility and unforeseen factors.")

if __name__ == "__main__":
    main()