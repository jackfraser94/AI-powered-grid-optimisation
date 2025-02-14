import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/time_series_cleaned.csv")  # Ensure correct file path

# Convert timestamp to datetime and set as index
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# Basic Info
print(df.info())
print(df.describe())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Plot actual electricity demand over time
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["actual_demand"], label="Actual Demand", color="blue")
plt.xlabel("Time")
plt.ylabel("Electricity Demand (MW)")
plt.title("Actual Demand Over Time")
plt.legend()
plt.savefig("images/actual_demand.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("images/correlation_heatmap.png")
plt.show()
