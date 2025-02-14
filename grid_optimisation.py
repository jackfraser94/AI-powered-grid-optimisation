import pulp
import pandas as pd

# Load dataset
df = pd.read_csv("data/optimization_results_tableau.csv")

# Define problem
prob = pulp.LpProblem("GridOptimization", pulp.LpMinimize)

# Define decision variables
P_c = pulp.LpVariable("Conventional_Power", lowBound=0)
P_b = pulp.LpVariable("Battery_Power", lowBound=0)
P_r = pulp.LpVariable("Renewable_Power", lowBound=0)

# Define objective function (minimize cost)
prob += 40 * P_c + 10 * P_b  # Assume cost of conventional is $40/MWh, battery is $10/MWh

# Constraints
demand = 5000  # Example demand value
prob += P_c + P_b + P_r == demand  # Total supply must meet demand
prob += P_r <= 2500  # Max renewable power available

# Solve optimization problem
prob.solve()

# Output results
print(f"Optimal Power Allocation: Conventional={P_c.varValue} MW, Battery={P_b.varValue} MW, Renewables={P_r.varValue} MW")
