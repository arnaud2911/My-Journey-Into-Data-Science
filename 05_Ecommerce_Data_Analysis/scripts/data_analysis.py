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