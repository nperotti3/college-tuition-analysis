"""
01_explore_tuition_sample.py
Simple exploration of the tuition_sample.csv dataset.
This script is equivalent to a first Jupyter notebook.
"""

import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Path to data (notebooks folder is a sibling of data/)
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample" / "tuition_sample.csv"

df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nHead:")
print(df.head())

# Tuition over time by region
pivot = df.pivot_table(
    index="YEAR",
    columns="REGION",
    values="TUITIONFEE_OUT_REAL_2024",
    aggfunc="mean",
)

print("\nAverage tuition by year/region:")
print(pivot)

plt.figure()
pivot.plot(marker="o")
plt.title("Out-of-State Tuition Over Time by Region (Sample)")
plt.xlabel("Year")
plt.ylabel("Tuition (2024 dollars)")
plt.tight_layout()
plt.show()

# Average tuition by region (overall)
avg_region = df.groupby("REGION")["TUITIONFEE_OUT_REAL_2024"].mean().sort_values()
print("\nAverage tuition by region (overall):")
print(avg_region)

plt.figure()
avg_region.plot(kind="bar")
plt.title("Average Out-of-State Tuition by Region (Sample)")
plt.xlabel("Region")
plt.ylabel("Average Tuition (2024 dollars)")
plt.tight_layout()
plt.show()
