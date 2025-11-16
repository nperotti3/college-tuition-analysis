"""
02_simple_trend_model.py
Simple regression model using the sample tuition data.
Illustrates the idea of modeling tuition as a function of time and key predictors.
"""

import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample" / "tuition_sample.csv"

df = pd.read_csv(DATA_PATH)

# Encode REGION as dummy variables
df_dummies = pd.get_dummies(df, columns=["REGION"], drop_first=True)

feature_cols = [
    "YEAR",
    "PCTPELL",
    "ADM_RATE",
    "INEXPFTE_REAL_2024",
    "AVGFACSAL_REAL_2024",
    "DEBT_MDN_REAL_2024",
] + [c for c in df_dummies.columns if c.startswith("REGION_")]

X = df_dummies[feature_cols]
y = df_dummies["TUITIONFEE_OUT_REAL_2024"]

model = LinearRegression()
model.fit(X, y)

print("R²:", model.score(X, y))
print("\nIntercept:", model.intercept_)
print("\nCoefficients:")
for name, coef in zip(feature_cols, model.coef_):
    print(f"{name:25s} {coef:10.2f}")

# Simple visualization: actual vs predicted
y_pred = model.predict(X)

plt.figure()
plt.scatter(y, y_pred)
plt.xlabel("Actual Tuition (2024 dollars)")
plt.ylabel("Predicted Tuition")
plt.title("Simple Regression Model – Actual vs Predicted")
plt.plot([y.min(), y.max()], [y.min(), y.max()])
plt.tight_layout()
plt.show()
