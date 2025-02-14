# AI-powered-smart-grid-optimisation

In the simplest sense, grid optimization means making sure the electricity grid is running as efficiently as possible, with minimal waste and maximum reliability.

Supply and demand: The power company needs to generate or purchase the exact amount of electricity that customers are using at any moment. If they generate too little, there’s a shortage (brownouts or blackouts). If they generate too much, it’s wasteful and can be costly.

Where AI/ML fits: By predicting energy usage—for instance, how much electricity houses in a neighborhood will need at specific times—utilities can plan their generation schedule. That way, they don’t produce unneeded electricity or pay for extra energy from the market.

Distribution optimization: It’s not just predicting how much power each house uses, but also routing and balancing power across different parts of the grid, accounting for factors like power line capacity, local generation (e.g., solar panels), and storage (e.g., batteries).

Ultimately, grid optimization is about balancing supply and demand in the most efficient, cost-effective, and reliable way—often by using advanced data-driven methods to forecast demand and manage available resources (power plants, renewable sources, batteries, etc.).

Data Utilisation: 

Access: https://open-power-system-data.org/

Data Chosen: Time series is good for forecasting consumption, balancing with generation

AI-Powered-Smart-Grid-Optimization/ │── README.md # Project Documentation
│── requirements.txt # Dependencies
│── data/ # Required datasets
│ │── time_series_featured.csv
│ │── forecasted_demand_tableau.csv
│ │── optimization_results_tableau.csv
│── models/ # Saved machine learning models
│ │── forecasting_model.pkl
│── scripts/ # Python scripts
│ │── eda.py # Exploratory Data Analysis
│ │── feature_engineering.py # Feature Engineering
│ │── forecasting_model.py # ML Model Training
│ │── grid_optimization.py # Grid Optimization Algorithm
│ │── run_predictions.py # Running Predictions on New Data
│── images/ # Saved visualizations
│ │── actual_demand.png
│ │── correlation_heatmap.png
│── tableau/ # Tableau Dashboard Files
│ │── tableau_dashboard.twbx
