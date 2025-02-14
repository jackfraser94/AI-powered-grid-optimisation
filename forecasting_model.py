import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("data/time_series_featured.csv")

# Define features and target variable
X = df.drop(columns=["actual_demand", "timestamp"])  # Drop non-numeric columns
y = df["actual_demand"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Model Performance: MAE = {mae:.2f}, RMSE = {rmse:.2f}")

# Save trained model
joblib.dump(model, "models/forecasting_model.pkl")
print("Model saved to models/forecasting_model.pkl")
