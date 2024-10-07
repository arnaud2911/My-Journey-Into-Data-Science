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
    print(f"Tne number of duplicate transactions is: {duplicates}")

#Function 4: Handling Missing Values
def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    """
    # Impute missing "quantity" values with the median
    median_quantity = df["quantity"].median()
    df["quantity"].fillna(median_quantity, inplace = True)
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