
# supermarket_sales_analysis.py
# Project: Supermarket Sales Analysis
# Author: Federica
# Description: Exploratory Data Analysis using Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("supermarket_sales - Sheet1.csv")

# Create a new column 'Total' to calculate total sales per transaction
data["Total"] = data["Unit price"] * data["Quantity"]

# === ANALYSIS 1: Total Sales per Product Category ===
sales_by_product = data.groupby("Product line")["Total"].sum().sort_values(ascending=False)

# Plot sales by product category
sales_by_product.plot(kind='bar', title='Vendite per categoria', figsize=(8,5))
plt.xlabel("Categoria")
plt.ylabel("Totale vendite")
plt.tight_layout()
plt.show()

# === ANALYSIS 2: Total Sales per City ===
sales_by_city = data.groupby("City")["Total"].sum().sort_values(ascending=False)

# Plot sales by city
sales_by_city.plot(kind='bar', title='Vendite per città', figsize=(8,5), color='skyblue')
plt.xlabel("Città")
plt.ylabel("Totale vendite")
plt.tight_layout()
plt.show()

# === ANALYSIS 3: Total Sales per Day of the Week ===
# Convert 'Date' column to datetime
data["Date"] = pd.to_datetime(data["Date"])
# Extract day of the week
data["Day"] = data["Date"].dt.day_name()
# Group and reorder days
sales_by_day = data.groupby("Day")["Total"].sum()
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sales_by_day = sales_by_day.reindex(ordered_days)

# Plot sales by day
sales_by_day.plot(kind='bar', title='Vendite per giorno della settimana', figsize=(8,5), color='salmon')
plt.xlabel("Giorno")
plt.ylabel("Totale vendite")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === ANALYSIS 4: Payment Method Distribution ===
payment_counts = data["Payment"].value_counts()

# Plot payment method as pie chart
payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(6,6))
plt.title("Distribuzione metodi di pagamento")
plt.ylabel("")
plt.tight_layout()
plt.show()
