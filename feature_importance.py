import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
import pickle

# Load the trained model
with open("inventory_xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define feature names
features = [
    'Day', 'Price', 'Units Sold', 'Units Ordered', 'Demand Forecast',
    'Units_Sold_Rolling7', 'Stock_to_Sales', 'Demand_Change', 'Log_Inventory'
]

# Get feature importance
importance = model.feature_importances_

# Create DataFrame
feat_importance = pd.DataFrame({"Feature": features, "Importance": importance})
feat_importance = feat_importance.sort_values(by="Importance", ascending=False)

# Plot
plt.figure(figsize=(10, 5))
plt.barh(feat_importance["Feature"], feat_importance["Importance"])
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Feature Importance in XGBoost Model")
plt.gca().invert_yaxis()
plt.show()

