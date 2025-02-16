import pandas as pd

# Load cleaned dataset
file_path = r"path\time_series_cleaned.csv"
df = pd.read_csv(file_path, parse_dates=["cet_cest_timestamp"], index_col="cet_cest_timestamp")

# Ensure datetime index is correctly formatted
df.index = pd.to_datetime(df.index, errors="coerce")

# Ensure all required columns exist
required_columns = [
    "DE_load_actual_entsoe_transparency", "DE_load_forecast_entsoe_transparency",
    "DE_solar_capacity", "DE_solar_generation_actual", "DE_solar_profile",
    "DE_wind_capacity", "DE_wind_generation_actual", "DE_wind_profile",
    "DE_wind_offshore_capacity", "DE_wind_offshore_generation_actual", "DE_wind_offshore_profile",
    "DE_wind_onshore_capacity", "DE_wind_onshore_generation_actual", "DE_wind_onshore_profile"
]

for col in required_columns:
    if col not in df.columns:
        df[col] = None

# Generate time-based features
df["hour"] = df.index.hour
df["day_of_week"] = df.index.dayofweek
df["month"] = df.index.month
df["is_weekend"] = df["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

# Generate lag features
lags = [1, 6, 12, 24]
for lag in lags:
    for col in required_columns:
        df[f"{col}_lag_{lag}h"] = df[col].shift(lag)

# **Generate rolling averages**
df["load_rolling_mean_6h"] = df["DE_load_actual_entsoe_transparency"].rolling(6).mean()
df["load_rolling_mean_24h"] = df["DE_load_actual_entsoe_transparency"].rolling(24).mean()

# Drop NaNs from lagged features
df = df.dropna()

# Save processed dataset
df.to_csv(r"path\time_series_featured.csv")
print("Feature engineering complete.")
