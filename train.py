import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load dataset
df = pd.read_csv("retail_store_inventory.csv")

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract time-based features
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday

# Encode 'Product ID' as a numeric value
le = LabelEncoder()
df['Product ID'] = le.fit_transform(df['Product ID'])

# Select necessary columns
features = [
    'Day', 'Price', 'Units Sold', 'Units Ordered', 'Demand Forecast',
    'Units_Sold_Rolling7', 'Stock_to_Sales', 'Demand_Change'
]
target = 'Inventory Level'

# Normalize numerical features
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df[features], df[target], test_size=0.2, random_state=42
)

# Save processed data
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("✅ Data preprocessing complete! Training and testing sets are saved.")