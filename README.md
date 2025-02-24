# AI-Powered Smart Grid Optimization

## Project Overview
This project optimizes power grid allocation by balancing conventional, renewable, and battery power sources to meet forecasted energy demand efficiently.  
The optimization model minimizes costs while ensuring that electricity supply meets demand using Linear Programming (PuLP).

It consists of:
- **A machine learning model** that predicts electricity demand based on historical data.
- **An optimization algorithm** that determines the most efficient energy allocation strategy.
- **A Tableau dashboard** for visualizing forecasted demand, power allocation, and cost analysis. (available shortly)

---
Data sourced from https://open-power-system-data.org/

## Repository Structure

```plaintext
AI-Powered-Smart-Grid-Optimization/
│── README.md                   # Project Documentation  
│── dependencies.txt            # Dependencies
|── AI POWERED SMART GRID OPTMISATION.pdf    #Project report
│── data/                       # Required datasets  
│   ├── time_series_15min_singleindex_filtered.csv  # Raw data 
│── scripts/                         # Python scripts
│   ├── data_cleaning.py             # Clean raw data 
│   ├── eda.py                       # Exploratory Data Analysis  
│   ├── feature_engineering.py       # Feature Engineering  
│   ├── forecasting_model.py         # ML Model Training  
│   ├── grid_optimization.py         # Grid Optimization Algorithm  
│   ├── run_predictions.py           # Running Predictions on New Data
│   ├── future_date_prediction.py    # Determine load for a given date and time
│   ├── optimisation_analysis.py     # Takes the optimises model/output and generates desired results and insights
│── images/                       # Saved visualizations  
│   ├── actual_demand.png  
│   ├── correlation_heatmap.png  
│── tableau/                      # Tableau Dashboard Files  
│   ├── tableau_dashboard.twbx  
```
## Version History 

- 1.0 - initial release that went through methods to generate forecast and optimisation models. This version yielded the original project report (The project report may become outdated as fixes and new features are added).
- 1.1 - reworked the .py files functionality
- 1.2. - Updated .pdf for consistency in optimisation results component. 
## Notes

- utilising the data from OPSD the results from this analysis seem high, however, under inspection of the initial dataset the predicted values are in line with the supplied data. Future iterations of this project will take different datasets to test for uniform compliance and overall accuracy. 
- Next version will be updated with API functionality.
