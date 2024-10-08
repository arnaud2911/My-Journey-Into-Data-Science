# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Defining functions for each step of the data analysis: We will modularize the code by creating functions for each major step
# Function 1: load's the dataset
def load_data(filepath):
    """
    Load the e-commerce dataset from a CSV file.
    """
    df = pd.read_csv(filepath, parse_dates = ["transaction_date"])
    return df

# Function 2: Perform intial data exploration
def initial_data_exploration(df):
    """
    Perform intial data exploration on the dataset.
    """
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
    print("\nSummary Statistics:")
    print(df.describe(include  = "all"))

# Function 3: Data validation and Summarization
def data_validation(df):
    """
    Validate data and check for inconsistencies.
    """
    print("\nChecking for missing values:")
    print(df.isnull().sum())
    print("\nChecking for duplicate transactions:")
    duplicates = df.duplicated(subset = ["transaction_id"]).sum()
    print(f"The number of duplicate transactions is: {duplicates}")

#Function 4: Handling Missing Values
def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    """
    # Impute missing "quantity" values with the median
    median_quantity = df["quantity"].median()
    df["quantity"] = df["quantity"].fillna(median_quantity)
    return df 

# Function 5: Identifying and handilng outliers
def handle_outliers(df):
    """
    Identify and handle outliers in price.
    """
    # Using IQR method
    Q1 = df["price"].quantile(0.25)
    Q3 = df["price"].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Cap price at upper and loweer bounds
    df["price"] = np.where(df["price"] > upper_bound, upper_bound, df["price"])
    df["price"] = np.where(df["price"] < lower_bound, lower_bound, df["price"])
    return df

# Function 6: Data Visualization
def visualize_data(df):
    """
    Create visualizations for data analysis.
    """
    sns.set(style = "whitegrid")

    # Total transactions per category
    plt.figure(figsize = (10, 6))
    category_counts = df["category"].value_counts()
    sns.barplot(x=category_counts.index, y=category_counts.values, hue=category_counts.index, palette="viridis", legend=False)
    plt.title("Total Transactions per Category")
    plt.xlabel("Category")
    plt.ylabel("Total Transactions")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig("../visualizations/transactions_per_category.png")
    plt.close()

    # Sales over time
    plt.figure(figsize = (12, 6))
    df.set_index("transaction_date").resample("ME")["price"].sum().plot()
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig("../visualizations/sales_over_time.png")
    plt.close()

    # Age distribution of customers
    plt.figure(figsize = (10, 6))
    sns.histplot(df["age"], bins = 50, kde = True, color = "skyblue")
    plt.title("Age Distribution of Customers")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("../visualizations/age_distribution.png")
    plt.close()

# Function 7: Aggregated Analysis
def aggregated_analysis(df):
    """
    Perform aggregated analysis on the dataset.
    """
    # Top 10 products by sales
    top_products = df.groupby("product_id")["price"].sum().sort_values(ascending = False).head(10)
    print(r"n\Top 10 Products by Quantity Sold")
    print(top_products)

    # Sales by gender
    sales_by_gender = df.groupby("gender")["price"].sum()
    print("\nTotal Sales by Gender")
    print(sales_by_gender)

    # Pivot table of sales by category and gender
    pivot_table = df.pivot_table(
        values = "price",
        index = "category",
        columns = "gender",
        aggfunc = "sum"
    )
    print("\nPivot Table of Sales by Category and Gender")
    print(pivot_table)

# Function 8: Save the cleaned dataset
def save_clean_data(df):
    """
    Save the cleaned dataset to a new CSV file.
    """
    df.to_csv("../data/cleaned_ecommerce_data.csv", index = False)
    print("\nCleaned data saved to 'data/cleaned_ecommerce_data.csv'.")

# Main Function to Excecute the Data Analysis
def main():
    # Step 1: Load the dataset
    print("Loading dataset...")
    filepath = "../data/ecommerce_data.csv"
    df = load_data(filepath)

    # Step 2: Perform initial data exploration
    print("\nPerforming initial data exploration...")
    initial_data_exploration(df)

    # Step 3: Data validation and summarization
    print("\nPerforming data validation...")
    data_validation(df)

    # Step 4: Handle missing values
    print("\nHandling missing values...")
    df = handle_missing_values(df)

    # Step 5: Handle outliers
    print("\nHandling outliers...")
    df = handle_outliers(df)

    # Step 6: Data visualization
    print("\nCreating visualizations...")
    visualize_data(df)

    # Step 7: Aggregated analysis
    print("\nPerforming aggregated analysis...")
    aggregated_analysis(df)

    # Step 8: Save the cleaned dataset
    save_clean_data(df)

    print("\nData analysis complete.")

if __name__ == "__main__":
        main()
