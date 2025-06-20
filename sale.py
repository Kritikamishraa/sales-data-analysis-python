import pandas as pd
import numpy as np

# Read CSV file
df = pd.read_csv('sales_data.csv')

# 1️⃣ Data Overview
print("Data Sample:\n", df.head())
print("\nData Summary:\n", df.describe(include='all'))

# 2️⃣ Add a new column 'TotalAmount'
df['TotalAmount'] = df['Quantity'] * df['Price']
print("\nAdded TotalAmount column:\n", df[['OrderID', 'TotalAmount']].head())

# 3️⃣ Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# 4️⃣ Group sales by Category
category_sales = df.groupby('Category')['TotalAmount'].sum().reset_index()
print("\nTotal sales by category:\n", category_sales)

# 5️⃣ Regional performance
region_sales = df.groupby('Region')['TotalAmount'].sum().sort_values(ascending=False).reset_index()
print("\nSales by region:\n", region_sales)

# 6️⃣ Most sold product by quantity
product_quantity = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).reset_index()
print("\nMost sold products (by quantity):\n", product_quantity)

# 7️⃣ Use NumPy to compute stats on TotalAmount
mean_sales = np.mean(df['TotalAmount'])
std_sales = np.std(df['TotalAmount'])
max_sales = np.max(df['TotalAmount'])
print(f"\nSales Stats -> Mean: {mean_sales}, Std Dev: {std_sales}, Max: {max_sales}")

# 8️⃣ Filter orders above mean TotalAmount
high_value_orders = df[df['TotalAmount'] > mean_sales]
print("\nHigh value orders:\n", high_value_orders[['OrderID', 'TotalAmount']])

# 9️⃣ Monthly sales trend
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month'] = df['OrderDate'].dt.month
monthly_sales = df.groupby('Month')['TotalAmount'].sum().reset_index()
print("\nMonthly sales trend:\n", monthly_sales)
