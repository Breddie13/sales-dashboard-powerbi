import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "sales_data_sample.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Convert ORDERDATE to proper datetime format
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Fill missing values (e.g., replace missing state with "Unknown")
df.fillna({'STATE': 'Unknown', 'TERRITORY': 'Unknown', 'POSTALCODE': '00000'}, inplace=True)

# Total Sales by Year
sales_by_year = df.groupby('YEAR_ID')['SALES'].sum()
sales_by_year.plot(kind='bar', color='royalblue')
plt.title("Total Sales Per Year")
plt.ylabel("Total Revenue ($)")
plt.xlabel("Year")
plt.show()

top_products = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
top_products.plot(kind='bar', color='teal')
plt.title("Top-Selling Product Categories")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.show()

top_countries = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10)
top_countries.plot(kind='barh', color='darkorange')
plt.title("Top 10 Countries by Sales")
plt.xlabel("Total Sales ($)")
plt.show()
