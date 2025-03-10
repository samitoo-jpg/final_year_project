import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 🔹 Load dataset
df = pd.read_csv("retail_store_inventory.csv")  # Ensure it's the correct dataset

# 🔹 Convert 'Date' column to datetime and extract 'Day'
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day

# 🔹 Feature Engineering: Create missing columns (Same as training)
df['Units_Sold_Rolling7'] = df['Units Sold'].rolling(window=7, min_periods=1).sum()
df['Stock_to_Sales'] = df['Inventory Level'] / (df['Units Sold'] + 1)  # Avoid division by zero
df['Demand_Change'] = df['Demand Forecast'].pct_change().fillna(0)
df['Log_Inventory'] = np.log1p(df['Inventory Level'])  # Log transform

# 🔹 Define Features (Same as training)
features = [
    'Day', 'Price', 'Units Sold', 'Units Ordered', 'Demand Forecast',
    'Units_Sold_Rolling7', 'Stock_to_Sales', 'Demand_Change', 'Log_Inventory'
]
target = "Inventory Level"

# 🔹 Select the Correct Columns
X = df[features]
y_actual = df[target]

# 🔹 Load Trained Model
model = joblib.load("inventory_xgboost_model.pkl")

# 🔹 Make Predictions
y_pred = model.predict(X)

# 🔹 Compute Evaluation Metrics
mae = mean_absolute_error(y_actual, y_pred)
rmse = np.sqrt(mean_squared_error(y_actual, y_pred))  # RMSE (Manual Calculation)
mape = (abs((y_actual - y_pred) / y_actual).mean()) * 100  # MAPE
r2 = r2_score(y_actual, y_pred)  # R² Score

# 🔹 Save Predictions
predictions_df = pd.DataFrame({"Actual": y_actual, "Predicted": y_pred})
predictions_df.to_csv("predictions.csv", index=False)

# 🔹 Print Results
print("\n✅ Model Evaluation Complete!")
print(f"📉 Mean Absolute Error (MAE): {mae:.2f}")
print(f"📊 Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"📌 Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
print(f"🎯 R² Score: {r2:.4f}")
print("✅ Predictions saved to 'predictions.csv'")




