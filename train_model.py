import pandas as pd
import numpy as np
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error

# 🔹 Load dataset
df = pd.read_csv("retail_store_inventory.csv")

# 🔹 Convert 'Date' column to datetime and extract 'Day'
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day

# 🛠 Feature Engineering: Create missing columns BEFORE checking
df['Units_Sold_Rolling7'] = df['Units Sold'].rolling(window=7, min_periods=1).sum()
df['Stock_to_Sales'] = df['Inventory Level'] / (df['Units Sold'] + 1)  # Avoid division by zero
df['Demand_Change'] = df['Demand Forecast'].pct_change().fillna(0)
df['Log_Inventory'] = np.log1p(df['Inventory Level'])  # Avoid log(0) issues

# 🔹 Define Features & Target Variable
features = [
    'Day', 'Price', 'Units Sold', 'Units Ordered', 'Demand Forecast',
    'Units_Sold_Rolling7', 'Stock_to_Sales', 'Demand_Change', 'Log_Inventory'
]
target = "Inventory Level"

# 🔹 Check if all required features exist (AFTER feature engineering)
missing_features = [f for f in features if f not in df.columns]
if missing_features:
    raise KeyError(f"Missing columns in dataset: {missing_features}")

# 🔹 Select data
X = df[features]
y = df[target]

# 🔹 Split data into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Define XGBoost model
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)

# 🔹 Define Hyperparameter Grid
param_grid = {
    "n_estimators": [100, 500],
    "max_depth": [3, 4],
    "learning_rate": [0.01, 0.05],
    "subsample": [0.8, 0.9],
    "colsample_bytree": [0.8, 0.9]
}

# 🔹 Perform Hyperparameter Tuning
grid_search = GridSearchCV(xgb_model, param_grid, scoring="neg_mean_squared_error", cv=3, verbose=1, n_jobs=-1)
grid_search.fit(X_train, y_train)

# 🔹 Get Best Model
best_model = grid_search.best_estimator_

# 🔹 Make Predictions & Evaluate
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2_score = best_model.score(X_test, y_test)

# 🔹 Save Model
joblib.dump(best_model, "inventory_xgboost_model.pkl")

# 🔹 Print Results
print("\n✅ Model Training Complete with Hyperparameter Tuning!")
print(f"🏆 Best Parameters: {grid_search.best_params_}")
print(f"📉 Mean Squared Error: {mse:.4f}")
print(f"📊 R² Score: {r2_score:.4f}")
print("💾 Model saved as 'inventory_xgboost_model.pkl'")



