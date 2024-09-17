# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Preparing the dataset
data = {
    'school_name': [
        f'School {chr(65 + i // 10)}{i % 10}' for i in range(100)
    ],
    'borough': [
        'Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten Island'
    ] * 20,
    'average_math': [
        np.random.randint(600, 800) for _ in range(100)
    ],
    'average_reading': [
        np.random.randint(600, 800) for _ in range(100)
    ],
    'average_writing': [
        np.random.randint(600, 800) for _ in range(100)
    ]
}

# Creating DataFrame
schools_df = pd.DataFrame(data)

# Alternatively, you can load the data from a CSV file using the code below
# schools_df = pd.read_csv("your file path here")

# Data Cleaning Steps
# Handling any missing values
if schools_df.isnull().values.any():
    schools_df.dropna(inplace = True)

# Let's ensure the data types are correct
if schools_df.dtypes["average_math"] != "int64":
    schools_df["average_math"] = schools_df["average+math"].astype("int64")
if schools_df.dtypes["average_reading"] != "int64":
    schools_df["average_reading"] = schools_df["average_reading"].astype("int64")
if schools_df.dtypes["average_writing"] != "int64":
    schools_df["average_writing"] = schools_df["average_writing"].astype("int64")
if schools_df.dtypes["borough"] != "object":
    schools_df["borough"] = schools_df["borough"].astype("object")
if schools_df.dtypes["school_name"] != "object":
    schools_df["school_name"] = schools_df["school_name"].astype("object")

# Let's handle any duplicates
if schools_df.duplicated().any():
    schools_df.drop_duplicates(inplace =  True)

# DATA ANALYSIS:
# Let's identify schools with the best math results (at least 80% of the maximum possible score)
max_math_score = 800
threshold = 0.8 * max_math_score
best_math_schools = schools_df[schools_df["average_math"] >= threshold]
best_math_schools = best_math_schools[["school_name", "average_math"]].sort_values(by = "average_math", ascending = False)
print("Best Math Schools:")
print(best_math_schools)
best_math_schools.to_csv("best_math_schools.csv", index = False) # This saves the best math schools to a CSV file

# Let's determine the top 10 performing schools based on combined SAT scores.
combined_SAT_scores = schools_df["average_math"] + schools_df["average_reading"] + schools_df["average_writing"]
schools_df["combined_SAT_scores"] = combined_SAT_scores # Adding a new column to the DataFrame
top_10_schools_combined_SAT = schools_df[["school_name", "combined_SAT_scores"]].sort_values(by = "combined_SAT_scores", ascending = False).head(10)
print("Top 10 Performing Schools Based on Combined SAT Scores:")
print(top_10_schools_combined_SAT)
top_10_schools_combined_SAT.to_csv("top_10_schools_combined_SAT.csv", index = False) # This saves the top 10 schools based on combined SAT scores to a CSV file

# Let's find the borough with the largest standard deviation in combined SAT scores.
borough_stats = schools_df.groupby("borough").agg(
    num_schools = ("school_name", "count"), # Count the number of schools in each borough
    avg_combined_SAT = ("combined_SAT_scores", "mean"), # Compute the mean of combined SAT scores for each borough
    std_combined_SAT = ("combined_SAT_scores", "std")  # Compute the standard deviation of combined SAT scores for each borough
)

largest_std_combined_SAT_borough = borough_stats[borough_stats["std_combined_SAT"] == borough_stats["std_combined_SAT"].max()] # This finds the borough with the largest standard deviation in combined SAT scores
print("Borough with the Largest Standard Deviation in Combined SAT Scores:")
print(largest_std_combined_SAT_borough)
#print(schools_df.head(10))