import pandas as pd

# File path to optimization results
optimization_results_path = r"C:path\optimization_results.csv"

# Load the optimization results
df = pd.read_csv(optimization_results_path)

# Ensure timestamp is in datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Set analysis period
start_date = df["timestamp"].min()
end_date = df["timestamp"].max()

# Compute total energy use
total_demand = df["forecasted_demand"].sum()
total_conventional = df["conventional_power"].sum()
total_renewable = df["renewable_power"].sum()
total_battery_discharge = df["battery_discharge"].sum()

# Peak and average demand
peak_demand = df["forecasted_demand"].max()
avg_demand = df["forecasted_demand"].mean()

# Peak and average power sources
peak_conventional = df["conventional_power"].max()
avg_conventional = df["conventional_power"].mean()
peak_renewable = df["renewable_power"].max()
avg_renewable = df["renewable_power"].mean()
peak_battery_discharge = df["battery_discharge"].max()
avg_battery_discharge = df["battery_discharge"].mean()

# CO₂ emissions
total_co2_emissions = df["co2_emissions"].sum()
avg_co2_emissions = df["co2_emissions"].mean()

# Contribution percentages
renewable_contribution = (total_renewable / total_demand) * 100
battery_contribution = (total_battery_discharge / total_demand) * 100
conventional_contribution = (total_conventional / total_demand) * 100

# Format and print results
print("\n======================== GRID PERFORMANCE ========================")
print(f"Analysis Period: {start_date} to {end_date}")
print(f"{'Metric':<35}{'Value':>15}")
print("="*65)
print(f"{'Total Forecasted Demand (MW)':<35}{total_demand:>15,.2f}")
print(f"{'Total Conventional Power Used (MW)':<35}{total_conventional:>15,.2f}")
print(f"{'Total Renewable Power Used (MW)':<35}{total_renewable:>15,.2f}")
print(f"{'Total Battery Discharge (MW)':<35}{total_battery_discharge:>15,.2f}")
print(f"{'Peak Demand (MW)':<35}{peak_demand:>15,.2f}")
print(f"{'Average Demand (MW)':<35}{avg_demand:>15,.2f}")
print(f"{'Peak Conventional Power (MW)':<35}{peak_conventional:>15,.2f}")
print(f"{'Average Conventional Power (MW)':<35}{avg_conventional:>15,.2f}")
print(f"{'Peak Renewable Power (MW)':<35}{peak_renewable:>15,.2f}")
print(f"{'Average Renewable Power (MW)':<35}{avg_renewable:>15,.2f}")
print(f"{'Peak Battery Discharge (MW)':<35}{peak_battery_discharge:>15,.2f}")
print(f"{'Average Battery Discharge (MW)':<35}{avg_battery_discharge:>15,.2f}")
print(f"{'Total CO₂ Emissions (tons)':<35}{total_co2_emissions:>15,.2f}")
print(f"{'Average CO₂ Emissions (tons)':<35}{avg_co2_emissions:>15,.2f}")
print(f"{'Renewable Contribution (%)':<35}{renewable_contribution:>15,.2f}")
print(f"{'Battery Contribution (%)':<35}{battery_contribution:>15,.2f}")
print(f"{'Conventional Contribution (%)':<35}{conventional_contribution:>15,.2f}")
print("="*65)
