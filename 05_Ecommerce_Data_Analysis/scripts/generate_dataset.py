# Importing the necessary libraries
import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

# Define Functions to Generate Data
def generate_customer_data(num_customers):
    """
    Generate customer IDs and demographic information.
    """
    customer_ids = ['CUST' + str(i).zfill(6) for i in range(1, num_customers + 1)]
    ages = np.random.randint(18, 70, size=num_customers)
    genders = np.random.choice(['Male', 'Female', 'Other'], size=num_customers, p=[0.48, 0.48, 0.04])
    return pd.DataFrame({'customer_id': customer_ids, 'age': ages, 'gender': genders})

def generate_product_data(num_products):
    """
    Generate product IDs and attributes.
    """
    product_ids = ['PROD' + str(i).zfill(6) for i in range(1, num_products + 1)]
    categories = np.random.choice(['Electronics', 'Clothing', 'Home', 'Books', 'Toys'], size=num_products)
    prices = np.round(np.random.uniform(5, 500, size=num_products), 2)
    return pd.DataFrame({'product_id': product_ids, 'category': categories, 'price': prices})

def generate_transaction_data(num_transactions, customer_ids, product_ids):
    """
    Generate transaction records.
    """
    transaction_ids = ['TRANS' + str(i).zfill(9) for i in range(1, num_transactions + 1)]
    customer_ids = np.random.choice(customer_ids, size=num_transactions)
    product_ids = np.random.choice(product_ids, size=num_transactions)
    quantities = np.random.randint(1, 5, size=num_transactions)
    transaction_dates = [datetime.now() - timedelta(days=random.randint(0, 365*3)) for _ in range(num_transactions)]
    return pd.DataFrame({
        'transaction_id': transaction_ids,
        'customer_id': customer_ids,
        'product_id': product_ids,
        'quantity': quantities,
        'transaction_date': transaction_dates
    })

# Introduce Anomalies and Missing Values
def introduce_anomalies(df):
    """
    Introduce anomalies and missing values into the dataset.
    """
    num_rows = df.shape[0]
    # Introduce missing values in 'quantity'
    missing_indices = np.random.choice(num_rows, size=int(num_rows * 0.01), replace=False)
    df.loc[missing_indices, 'quantity'] = np.nan

    # Introduce anomalies in 'price'
    anomaly_indices = np.random.choice(num_rows, size=int(num_rows * 0.005), replace=False)
    df.loc[anomaly_indices, 'price'] = df.loc[anomaly_indices, 'price'] * 10  # Inflate price

    return df

# Main Function to Generate and Save Dataset
def main():
    num_customers = 100000
    num_products = 5000
    num_transactions = 1000000

    print("Generating customer data...")
    customers = generate_customer_data(num_customers)

    print("Generating product data...")
    products = generate_product_data(num_products)

    print("Generating transaction data...")
    transactions = generate_transaction_data(num_transactions, customers['customer_id'], products['product_id'])

    print("Merging datasets...")
    df = transactions.merge(customers, on='customer_id').merge(products, on='product_id')

    print("Introducing anomalies and missing values...")
    df = introduce_anomalies(df)

    print("Saving dataset to 'data/ecommerce_data.csv'...")
    df.to_csv('../data/ecommerce_data.csv', index=False)
    print("Dataset generation complete.")

if __name__ == '__main__':
    main()
