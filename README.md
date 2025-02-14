# AI-Powered Smart Grid Optimization

## Project Overview
This project optimizes power grid allocation by balancing **conventional, renewable, and battery power sources** to meet forecasted energy demand efficiently.  
The optimization model **minimizes costs while ensuring that electricity supply meets demand** using **Linear Programming (PuLP)**.

It consists of:
- **A machine learning model** that predicts electricity demand based on historical data.
- **An optimization algorithm** that determines the most efficient energy allocation strategy.
- **A Tableau dashboard** for visualizing forecasted demand, power allocation, and cost analysis.

---

## Repository Structure

```plaintext
AI-Powered-Smart-Grid-Optimization/
│── README.md                   # Project Documentation  
│── requirements.txt            # Dependencies  
│── data/                        # Required datasets  
│   ├── time_series_featured.csv  
│   ├── forecasted_demand_tableau.csv  
│   ├── optimization_results_tableau.csv  
│── models/                      # Saved machine learning models  
│   ├── forecasting_model.pkl  
│── scripts/                      # Python scripts  
│   ├── eda.py                      # Exploratory Data Analysis  
│   ├── feature_engineering.py       # Feature Engineering  
│   ├── forecasting_model.py         # ML Model Training  
│   ├── grid_optimization.py         # Grid Optimization Algorithm  
│   ├── run_predictions.py           # Running Predictions on New Data  
│── images/                       # Saved visualizations  
│   ├── actual_demand.png  
│   ├── correlation_heatmap.png  
│── tableau/                      # Tableau Dashboard Files  
│   ├── tableau_dashboard.twbx  

