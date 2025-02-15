import pandas as pd
import joblib

# Load the trained model
model_file_path = r"C:\Users\jackf\Desktop\Data\load_forecast_model.pkl"
model = joblib.load(model_file_path)

# Load the dataset to extract recent past values
file_path = r"C:\Users\jackf\Desktop\Data\time_series_featured.csv"
df = pd.read_csv(file_path, parse_dates=["cet_cest_timestamp"], index_col="cet_cest_timestamp")

# Ensure the dataset is sorted correctly
df = df.sort_index()

# Fix: Remove timezone information from dataset timestamps
df.index = df.index.tz_localize(None)

# Define the future timestamp
future_timestamp = pd.Timestamp("2030-07-26 03:00:00")  # No timezone

# Define the exact feature list used in training
feature_order = [
    "hour", "day_of_week", "month", "is_weekend",
    "load_lag_1h", "load_lag_6h", "load_lag_12h", "load_lag_24h",
    "solar_lag_1h", "solar_lag_6h", "solar_lag_12h", "solar_lag_24h",
    "wind_lag_1h", "wind_lag_6h", "wind_lag_12h", "wind_lag_24h",
    "load_rolling_mean_6h", "load_rolling_mean_24h",
    "solar_rolling_mean_6h", "solar_rolling_mean_24h",
    "wind_rolling_mean_6h", "wind_rolling_mean_24h"
]

# Create the feature row in the correct order
future_features = {
    "hour": future_timestamp.hour,
    "day_of_week": future_timestamp.dayofweek,
    "month": future_timestamp.month,
    "is_weekend": 1 if future_timestamp.dayofweek >= 5 else 0
}

# Extract lag values dynamically
lags = [1, 6, 12, 24]
for lag in lags:
    past_time = future_timestamp - pd.Timedelta(hours=lag)
    closest_idx = df.index.get_indexer([past_time], method="nearest")[0]  # Find the nearest available time
    future_features[f"load_lag_{lag}h"] = df.iloc[closest_idx]["DE_load_actual_entsoe_transparency"]
    future_features[f"solar_lag_{lag}h"] = df.iloc[closest_idx]["DE_solar_generation_actual"]
    future_features[f"wind_lag_{lag}h"] = df.iloc[closest_idx]["DE_wind_generation_actual"]

# Extract rolling averages using historical data trends
future_features["load_rolling_mean_6h"] = df["DE_load_actual_entsoe_transparency"].rolling(6).mean().iloc[-1]
future_features["load_rolling_mean_24h"] = df["DE_load_actual_entsoe_transparency"].rolling(24).mean().iloc[-1]

future_features["solar_rolling_mean_6h"] = df["DE_solar_generation_actual"].rolling(6).mean().iloc[-1]
future_features["solar_rolling_mean_24h"] = df["DE_solar_generation_actual"].rolling(24).mean().iloc[-1]

future_features["wind_rolling_mean_6h"] = df["DE_wind_generation_actual"].rolling(6).mean().iloc[-1]
future_features["wind_rolling_mean_24h"] = df["DE_wind_generation_actual"].rolling(24).mean().iloc[-1]

# Ensure the feature order is exactly the same as during training
future_df = pd.DataFrame([future_features], columns=feature_order)

# Make the prediction
predicted_load = model.predict(future_df)[0]

print(f"Predicted Electricity Load for {future_timestamp}: {predicted_load:.2f} MW")
