import pandas as pd
import pulp

# File paths
forecasted_demand_path = r"C:path\long_term_forecast.csv"
output_optimization_path = r"C:path\optimization_results.csv"

# Load forecasted demand data
df = pd.read_csv(forecasted_demand_path)

# Fix missing timestamp column
if "Unnamed: 0" in df.columns:
    df.rename(columns={"Unnamed: 0": "timestamp"}, inplace=True)

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# Check if timestamp conversion was successful
if df["timestamp"].isna().sum() > 0:
    raise ValueError("ERROR: Some timestamps could not be converted! Check CSV format.")

# Define power plant & renewable constraints
max_conventional = 10000  # Max conventional generation capacity (MW)
max_renewable = 8000  # Max renewable generation capacity (MW)
battery_capacity = 5000  # Max battery storage capacity (MW)

# Define cost per MW for different power sources
cost_conventional_peak = 70  # Peak-time conventional energy cost per MW
cost_conventional_offpeak = 50  # Off-peak conventional cost
cost_renewable = 20  # Renewable energy cost per MW
cost_battery_charge = 5  # Cost per MW to charge battery
cost_battery_discharge = 3  # Cost per MW to use battery storage

# CO₂ emissions (tons per MW) for conventional energy
co2_per_mw = 0.4  # Example: 0.4 tons CO₂ per MW

# Simulated renewable efficiency based on weather (1 = full, 0.5 = 50% efficiency)
simulated_weather_factor = 0.8  # This would normally come from weather forecasts

# Battery state of charge tracker
battery_state = 2000  # Start battery with 2000 MW stored

# Create results storage
optimization_results = []

# Loop through each time period
for i, row in df.iterrows():
    demand = row["forecasted_load"]
    hour = row["timestamp"].hour  # Get hour for peak pricing

    # Adjust cost for peak and off-peak
    cost_conventional = cost_conventional_peak if 7 <= hour <= 20 else cost_conventional_offpeak

    # Adjust renewable output based on weather
    max_renewable_available = max_renewable * simulated_weather_factor

    # Create an optimization problem
    problem = pulp.LpProblem("Energy_Optimization", pulp.LpMinimize)

    # Define decision variables
    conventional = pulp.LpVariable("Conventional", lowBound=0, upBound=max_conventional)
    renewable = pulp.LpVariable("Renewable", lowBound=0, upBound=max_renewable_available)
    battery_discharge = pulp.LpVariable("Battery_Discharge", lowBound=0, upBound=battery_state)
    battery_charge = pulp.LpVariable("Battery_Charge", lowBound=0, upBound=battery_capacity - battery_state)

    # **Binary variable for battery mode (1 = charging, 0 = discharging)**
    charge_mode = pulp.LpVariable("Charge_Mode", cat="Binary")

    # Objective Function: Minimize cost
    problem += (
        cost_conventional * conventional +
        cost_renewable * renewable +
        cost_battery_charge * battery_charge -
        cost_battery_discharge * battery_discharge
    )

    # Constraint: Demand must be met
    problem += conventional + renewable + battery_discharge == demand

    # **Constraint: Battery can either charge or discharge (not both)**
    problem += battery_charge <= charge_mode * battery_capacity  # Battery charges only when charge_mode = 1
    problem += battery_discharge <= (1 - charge_mode) * battery_capacity  # Battery discharges only when charge_mode = 0

    # Solve the optimization problem
    problem.solve()

    # Get optimized values
    conv_power = pulp.value(conventional)
    ren_power = pulp.value(renewable)
    bat_discharge = pulp.value(battery_discharge)
    bat_charge = pulp.value(battery_charge)

    # Update battery storage level
    battery_state += bat_charge - bat_discharge
    battery_state = max(0, min(battery_capacity, battery_state))  # Keep within limits

    # Calculate CO₂ emissions from conventional energy
    co2_emissions = conv_power * co2_per_mw

    # Store results
    optimization_results.append([
        row["timestamp"], demand, conv_power, ren_power, bat_discharge, bat_charge, battery_state, co2_emissions
    ])

# Convert results to a DataFrame
opt_df = pd.DataFrame(optimization_results, columns=[
    "timestamp", "forecasted_demand", "conventional_power",
    "renewable_power", "battery_discharge", "battery_charge",
    "battery_storage", "co2_emissions"
])

# Save optimization results
opt_df.to_csv(output_optimization_path, index=False)
print(f"Optimization results saved to: {output_optimization_path}")
