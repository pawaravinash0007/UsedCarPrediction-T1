

# UsedCarPrediction-T1

Used Car Price Prediction using Machine Learning

[![Language](https://img.shields.io/badge/Language-Python%20%7C%20HTML-blue?style=flat-square)](.)
[![ML](https://img.shields.io/badge/ML-Scikit--learn-orange?style=flat-square)](.)

## Overview

A machine learning regression project that predicts **used car prices** based on vehicle attributes such as make, model, year, mileage, fuel type, and transmission. Helps buyers and sellers estimate fair market value for pre-owned vehicles.

## Dataset Features

| Feature | Description |
|---------|-------------|
| Year | Manufacturing year |
| Make/Model | Car brand and model |
| Mileage | Odometer reading (km/miles) |
| Fuel Type | Petrol, Diesel, CNG, Electric |
| Transmission | Manual, Automatic |
| Engine Size | Engine displacement (cc) |
| Owner Count | Number of previous owners |
| Price | Target variable (INR/USD) |

## Models Used

| Model | R² Score |
|-------|---------|
| Linear Regression | 0.72 |
| Random Forest | 0.88 |
| Gradient Boosting | 0.90 |
| XGBoost | 0.91 |

# UsedCarPrediction-T1
https://usedcarp.streamlit.app/

## Key Findings

- **Mileage** and **age** are the strongest negative predictors of price
- **Brand** and **fuel type** significantly affect resale value
- Electric and diesel cars retain value better than petrol
- First-owner cars command a 15-20% premium

## Getting Started

```bash
git clone https://github.com/pawaravinash0007/UsedCarPrediction-T1.git
cd UsedCarPrediction-T1
pip install pandas numpy scikit-learn xgboost matplotlib seaborn jupyter
jupyter notebook UsedCar_Prediction.ipynb
```

## Tech Stack

Python, Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn

## Author

**Avinash Pawar** | [@pawaravinash0007](https://github.com/pawaravinash0007)
