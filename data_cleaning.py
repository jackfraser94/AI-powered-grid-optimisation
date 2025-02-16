import pandas as pd

# Define file paths
input_file_path = r"input\time_series_15min_singleindex_filtered.csv"
output_file_path = r"output"

# Load CSV with correct datetime parsing
df = pd.read_csv(input_file_path, parse_dates=["cet_cest_timestamp"], index_col="cet_cest_timestamp")

# Ensure datetime index is properly formatted
df.index = pd.to_datetime(df.index, errors="coerce")

# **Define required columns** (to prevent KeyErrors)
required_columns = [
    "DE_load_actual_entsoe_transparency", "DE_load_forecast_entsoe_transparency",
    "DE_solar_capacity", "DE_solar_generation_actual", "DE_solar_profile",
    "DE_wind_capacity", "DE_wind_generation_actual", "DE_wind_profile",
    "DE_wind_offshore_capacity", "DE_wind_offshore_generation_actual", "DE_wind_offshore_profile",
    "DE_wind_onshore_capacity", "DE_wind_onshore_generation_actual", "DE_wind_onshore_profile"
]

# **Ensure all required columns exist**
for col in required_columns:
    if col not in df.columns:
        df[col] = None  # Add missing columns with NaN values

# **Forward-fill missing values**
df[required_columns] = df[required_columns].fillna(method="ffill")

# Save cleaned dataset
df.to_csv(output_file_path)
print(f"Cleaned dataset saved to: {output_file_path}")
