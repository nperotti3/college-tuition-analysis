# College Tuition Analysis – Personal Portfolio Version

This repository is a **personal, portfolio-ready version** of a team project completed for  
**CSE 6242 – Data & Visual Analytics, Georgia Tech (Spring 2025)**.

The original project was developed by **Team 151** and analyzes nearly three decades of U.S. higher education data from the Department of Education’s **College Scorecard**. The goal is to understand how tuition has evolved over time and which institutional and student factors are most strongly associated with higher tuition levels.

This repo focuses on:

- A **lightweight, reproducible subset** of the full pipeline.
- A clear explanation of **my individual contributions**.
- Example code and sample data suitable for a public portfolio.

> ⚠️ Note: The full project (including large raw datasets and all course deliverables) lives in a **private team repository** for academic integrity reasons. 

---

## 📌 My Role

In the original team project, I contributed to:

- Building and refining the **interactive Tableau dashboard** used for final presentation.
- Supporting the **Python data pipeline** to prepare analysis-ready datasets from College Scorecard, CPI, and regional mapping sources.
- Applying **inflation adjustments** using CPI to express tuition in constant 2024 dollars.
- Assisting with **time series and regression analysis** (ARIMA forecasting, feature importance).
- Organizing the **repository structure** and connecting Python outputs to the Tableau data model.

This personal repo showcases a simplified version of that work.

---

## 🔍 Project Overview

Using U.S. College Scorecard data (1996–2023), the analysis explores:

- How **tuition has changed over time** at U.S. colleges and universities.
- Differences across **regions** (Northeast, Midwest, South, West) and **institutional types**.
- How factors such as **Pell grant share, admission rate, instructional spending per student, faculty salary, and median debt** relate to out-of-state tuition.

The original project included:

- A **four-stage Python pipeline** (merge → cleanse → model → advanced analysis).
- **ARIMA time series forecasting** for national and regional tuition trends.
- **Regression and tree-based models** with **SHAP feature importance**.
- An **interactive Tableau dashboard** for exploring tuition, trends, and drivers.

This repo distills those ideas into a smaller, easy-to-run example.

---

## 🧠 Methods & Tools

- **Languages & Libraries**
  - Python (Pandas, NumPy, Statsmodels, Scikit-learn, SHAP, Matplotlib)
  - Jupyter Notebooks
- **Visualization**
  - Tableau (dashboard design and interactivity)
- **Data**
  - U.S. Department of Education College Scorecard
  - CPI data from FRED (for inflation adjustment)
  - U.S. Census regional classifications

---

## 📂 Repository Structure

```text
college-tuition-analysis/
├── data/
│   └── sample/
│       ├── tuition_sample.csv            # Small sample of cleaned data
│       └── readme.md                     # Notes on sample data
├── notebooks/
│   ├── 01_explore_tuition_sample.ipynb   # Basic exploration & plots
│   └── 02_simple_trend_model.ipynb       # Example forecasting / regression
├── images/
│   └── dashboard_overview.png            # Screenshot of Tableau dashboard
├── tableau/
│   └── README.md                         # Link or notes about dashboard
└── README.md
