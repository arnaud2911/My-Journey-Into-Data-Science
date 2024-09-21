# Stock Price Analysis and Simulation

## Project Description

This capstone project analyzes and cleans stock price data of a fictional company over a **20-year period** (from 2000 to 2019), calculates daily returns, performs statistical analysis, and simulates future stock prices using a random walk model. The project demonstrates data cleaning, manipulation, visualization, and statistical concepts in a real-life data science scenario.

## Objectives

- **Data Generation**: Programmatically generate a large synthetic stock price dataset with anomalies and missing values.
- **Data Cleaning**: Handle missing values and anomalies in the dataset.
- **Data Manipulation**: Calculate daily returns and add new features.
- **Statistical Analysis**: Compute mean, median, standard deviation, and identify significant trends.
- **Data Visualization**: Create plots to visualize stock prices and returns.
- **Random Simulation**: Simulate future stock price paths using statistical methods.

## Key Features

- **Large Dataset Handling**: Worked with a synthetic dataset spanning 20 years to mimic real-world data size.
- **Comprehensive Data Cleaning**: Replacing anomalies and using interpolation techniques.
- **Advanced Visualizations**: Utilizing Seaborn for enhanced plotting.
- **Modular Code Structure**: Organized into functions for clarity and reusability.
- **Realistic Simulation**: Implementing a random walk model based on historical data.

## Learning Outcomes

- Mastered data cleaning techniques for handling missing and anomalous large data.
- Gained experience in data manipulation using Pandas and NumPy.
- Performed statistical analysis and interpreted results.
- Created advanced visualizations using Matplotlib and Seaborn.
- Implemented a random walk model for stock price simulation.

## Future Enhancements

- Use real stock price data from APIs like Yahoo Finance or Alpha Vantage.
- Incorporate more sophisticated statistical models for simulation.
- Develop an interactive dashboard using Plotly Dash or Streamlit.

## Acknowledgment

Some parts of this project, such as fictional data generation, code writing guidance and optimization suggestions, were assisted by AI tools like ChatGPT and GitHub Copilot. However, I have ensured a deep understanding of the core functionality and refined the code to suit my learning objectives.

## How to Run the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/My-Journey-Into-Data-Science.git

2. **Navigate to the Project Directory**

   ```bash
   cd My-Journey-Into-Data-Science/04_Stock_Price_Analysis

3. **Install Dependencies**

   ```bash
   pip install numpy pandas matplotlib seaborn

4. **Generate the Dataset**
   ```bash
  python generate_stock_data.py

5. **Run the Python Script**

   ```bash
   python stock_price_analysis.py

6. **View the Outputs**
The script will display results in the console.
Visualizations will be saved in the visualizations folder.