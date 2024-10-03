# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/ecommerce_data.csv")
print(df.head())
# let's print the list of columns in the dataset
print(df.columns)