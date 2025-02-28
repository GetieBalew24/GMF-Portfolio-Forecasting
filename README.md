# Stock Forecasting and Portfolio Optimization

This project provides an end-to-end analysis pipeline for forecasting stock prices, analyzing financial market trends, and optimizing an investment portfolio to maximize returns while minimizing risk. The assets analyzed are Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY), each representing different risk and return profiles within a balanced portfolio.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [Data Collection and Preprocessing](#data-collection-and-preprocessing)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)

---

## Project Overview
The goal of this project is to:
1. **Predict stock price trends** for Tesla (TSLA) using time series models.
2. **Analyze market trends** and volatility, and evaluate risk and opportunities.
3. **Optimize an investment portfolio** using forecasted trends to maximize returns and minimize risk for TSLA, BND, and SPY.

---

## Setup and Installation
### Prerequisites
Ensure that you have the following installed:
- Python 3.8 or higher
- Git for cloning the repository

### Installation Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/GetieBalew24/GMF-Portfolio-Forecasting.git
    cd GMF-Portfolio-Forecasting
    ```

2. **Set up a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
---

## Data Collection and Preprocessing
### Task 1: Preprocess and Explore the Data
Using the Yahoo Finance (YFinance) API, we collect historical price data for Tesla (TSLA), BND, and SPY to represent different risk profiles within a portfolio:
- **TSLA**: High return, high volatility.
- **BND**: Stability with low risk.
- **SPY**: Moderate-risk market exposure.

#### Data Cleaning
- Check for missing values and handle them by filling, interpolating, or removing.
- Ensure data types are appropriate for time series analysis.
- Normalize or scale data as required for machine learning models.

#### Exploratory Data Analysis (EDA)
- Visualize closing prices over time to identify trends and patterns.
- Calculate daily percentage changes to observe volatility.
- Detect outliers and unusual return days.
- Decompose time series into trend, seasonal, and residual components to identify patterns.

---

## Conclusion
This project demonstrates a comprehensive approach to data-driven investment strategy, covering data collection, cleaning and forecasting.

---

## Requirements
The following libraries are required:
- `yfinance`: For data extraction.
- `pandas`: Data manipulation.
- `numpy`: Numerical computations.
- `matplotlib` & `seaborn`: Data visualization.
- `scipy.stats`: Statistical analysis.
- `statsmodels`: Time series decomposition.
- `pmdarima`: ARIMA optimization.
- `keras` & `tensorflow`: For LSTM models.

Install dependencies using:
```bash
pip install -r requirements.txt
```
