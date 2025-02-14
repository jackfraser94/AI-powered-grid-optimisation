import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/forecasting_model.pkl")

# Load new data for prediction
df = pd.read_csv("data/new_forecast_input.csv")
X_new = df.drop(columns=["timestamp"])

# Make predictions
predictions = model.predict(X_new)

# Save predictions
df["forecasted_demand"] = predictions
df.to_csv("data/forecasted_demand_output.csv", index=False)
print("Predictions saved to data/forecasted_demand_output.csv")
