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