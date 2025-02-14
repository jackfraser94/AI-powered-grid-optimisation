import pandas as pd

# Load dataset
df = pd.read_csv("data/time_series_cleaned.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.dayofweek
df["month"] = df["timestamp"].dt.month

# Create lag features (previous demand values)
df["lag_1"] = df["actual_demand"].shift(1)
df["lag_6"] = df["actual_demand"].shift(6)
df["lag_24"] = df["actual_demand"].shift(24)

# Create rolling averages
df["rolling_avg_6h"] = df["actual_demand"].rolling(window=6).mean()
df["rolling_avg_24h"] = df["actual_demand"].rolling(window=24).mean()

# Drop NaN values created by lag features
df.dropna(inplace=True)

# Save processed dataset
df.to_csv("data/time_series_featured.csv", index=False)
print("Feature engineering completed and saved.")
