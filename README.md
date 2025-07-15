# 🛒 Sales Forecast Dashboard

This project builds a complete pipeline for **weekly sales forecasting** of a fictional retail chain (Walmart-style), using **Python**, **machine learning**, and a **Power BI dashboard**.

---

## 🚀 Project Overview

The goal is to predict weekly product sales per store and category, incorporating effects of:
- 🏪 Store and product
- 📦 Product category
- 💰 Unit price
- 🎯 Promotions
- 🎉 Holidays
- 📊 Historical sales trends (moving average and lag)

---

## 🧠 Model Performance

Final model: **Random Forest Regressor**, trained on engineered features.

| Metric     | Value     |
|------------|-----------|
| R² Score   | **0.498** |
| MAE        | **38.63** |
| MSE        | **2368.58** |

---

## 🧰 Technologies Used

- Python (Pandas, Scikit-learn, Seaborn, Matplotlib)
- Machine Learning (Random Forest)
- Feature Engineering (Rolling average, lag features)
- Power BI (for dashboard)
- Git & GitHub

---

## 📁 Project Structure
sales_forecast_dashboard/
│
├── data/
│ ├── raw/ # Simulated sales data
│ ├── processed/ # Cleaned + engineered dataset
│ └── future_sales_forecast.csv
│
├── dashboards/
│ ├── sales_forecast_dashboard.pbix # Power BI file
│ └── dashboard_print.png # Screenshot
│
├── scripts/
│ ├── generate_sales_data.py # Synthetic data generator
│ ├── preprocess.py # Feature engineering
│ └── forecast_future.py # Model inference
│
├── notebooks/
│ ├── eda_vendas.py # EDA: sales overview
│ ├── eda_detalhado.py # Detailed EDA
│ └── model_training.py # ML model training
│
├── model/
│ └── sales_forecast_model.pkl # Trained model
│
└── README.md


