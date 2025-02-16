import pandas as pd
import numpy as np
import joblib
import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

start_time = time.time()
print("Loading dataset...")
df = pd.read_csv(r"path\time_series_featured.csv", parse_dates=["cet_cest_timestamp"], index_col="cet_cest_timestamp")

print("Dataset loaded. Shape:", df.shape)

# Drop NaN values
df = df.dropna()

# Define target variable
target = "DE_load_actual_entsoe_transparency"

# Remove timestamp columns
df = df.drop(columns=[col for col in ["cet_cest_timestamp", "utc_timestamp"] if col in df.columns], errors="ignore")

# Define features
features = [col for col in df.columns if col != target]

# Train-test split
print("Splitting dataset into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Train Random Forest model
print("Training Random Forest model...")
model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
model.fit(X_train, y_train)

print("Model training completed in {:.2f} seconds.".format(time.time() - start_time))

# Make predictions
print("Generating predictions...")
y_pred = model.predict(X_test)

# Evaluate model performance
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

# Print evaluation results
print(f"Model Performance:\nRMSE: {rmse:.2f} MW\nMAE: {mae:.2f} MW")

# Save trained model
joblib.dump(model, r"path\load_forecast_model.pkl")
print("Random Forest model saved.")

# Generate Forecast for Future Period
forecast_horizon = 7 * 24 * 4  # 7 days of 15-minute intervals
last_timestamp = pd.to_datetime(df.index[-1])
future_timestamps = pd.date_range(start=last_timestamp + pd.Timedelta(minutes=15), periods=forecast_horizon, freq='15min')

# Prepare DataFrame
future_df = pd.DataFrame(index=future_timestamps)
future_df["hour"] = future_df.index.hour
future_df["day_of_week"] = future_df.index.dayofweek
future_df["month"] = future_df.index.month
future_df["is_weekend"] = future_df["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

# Ensure all required features exist in `future_df`
for col in features:
    if col not in future_df.columns:
        future_df[col] = df[col].iloc[-1]  # Fill missing features with last known values

# Predict future demand
future_df["forecasted_load"] = model.predict(future_df[features])

# Save forecasted data
forecast_output_path = r"pathlong_term_forecast.csv"
future_df.to_csv(forecast_output_path)
print(f"Forecast saved to: {forecast_output_path}")
