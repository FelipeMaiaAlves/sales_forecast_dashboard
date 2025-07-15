# 🛒 Sales Forecast Dashboard — Weekly Retail Sales Prediction Pipeline

This project implements an end-to-end pipeline for forecasting **weekly product sales** at a fictional retail chain (similar to Walmart), leveraging Python, machine learning, and a Power BI dashboard for visualization and insights.

---

## 🚀 Project Overview

The goal is to predict weekly sales per product and store, capturing multiple influencing factors such as:

- 🏪 Store and product specifics  
- 📦 Product category details  
- 💰 Unit price variations  
- 🎯 Promotional campaigns  
- 🎉 Holiday effects  
- 📊 Historical sales trends (including moving averages and lag features)

---

## 🧠 Model & Performance

The final predictive model is a **Random Forest Regressor** trained on a rich set of engineered features.

| Metric   | Value   |
|----------|---------|
| R² Score | 0.498   |
| MAE      | 38.63   |
| MSE      | 2368.58 |

---

## 🧰 Technologies Used

- Python (Pandas, Scikit-learn, Seaborn, Matplotlib)  
- Machine Learning: Random Forest Regressor  
- Feature Engineering: Rolling averages, lag features  
- Power BI (for interactive dashboard visualization)  
- Git & GitHub (version control)

---

## 📁 Project Structure

sales_forecast_dashboard/
├── data/
│   ├── raw/                      # Simulated raw sales data
│   ├── processed/                # Cleaned and feature-engineered datasets
│   └── future_sales_forecast.csv # Future forecast output
├── dashboards/
│   ├── sales_forecast_dashboard.pbix  # Power BI dashboard file
│   └── dashboard_print.png             # Dashboard screenshot
├── scripts/
│   ├── generate_sales_data.py    # Synthetic sales data generator
│   ├── preprocess.py             # Feature engineering scripts
│   └── forecast_future.py        # Model inference and forecasting
├── notebooks/
│   ├── eda_vendas.py             # Exploratory data analysis (overview)
│   ├── eda_detalhado.py          # Detailed EDA
│   └── model_training.py         # Model training and evaluation
├── model/
│   └── sales_forecast_model.pkl  # Trained Random Forest model
└── README.md



---

## ⚡ Quick Start

1. Clone this repo  
2. Install dependencies: `pip install -r requirements.txt`  
3. Generate synthetic data or load your own in `/data/raw/`  
4. Run preprocessing: `python scripts/preprocess.py`  
5. Train model: `python notebooks/model_training.py`  
6. Forecast future sales: `python scripts/forecast_future.py`  
7. Open Power BI dashboard in `/dashboards/sales_forecast_dashboard.pbix` to explore results

---

Feel free to open issues or submit pull requests if you'd like to contribute!

---

© 2025 Felipe Maia Alves. Licensed under MIT License.
