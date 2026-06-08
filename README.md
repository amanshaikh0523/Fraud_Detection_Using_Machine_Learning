# Fraud Detection Using Machine Learning

## Project Overview

This project develops a machine learning-based fraud detection system using financial transaction data. Multiple models including Logistic Regression, Random Forest, and XGBoost were evaluated to identify fraudulent transactions.

## Dataset

- Total Transactions: 11,142
- Fraud Transactions: 1,142
- Features: Transaction type, balances, transaction amount, engineered balance features

## Feature Engineering

- Sender Balance Difference
- Receiver Balance Difference
- Sender Balance Zero Indicator
- Receiver Balance Zero Indicator

## Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

## Results

| Metric | Value |
|----------|----------|
| Accuracy | 99% |
| Precision | 96% |
| Recall | 99% |
| F1 Score | 98% |
| ROC-AUC | 99.89% |
| Cross-Validated F1 | 98.07% |

## Key Insights

- Sender balance difference was the strongest fraud indicator.
- XGBoost achieved the best overall performance.
- SHAP analysis improved model interpretability.

## Technologies Used

- Python
- Pandas
- Scikit-Learn
- XGBoost
- SHAP
- Streamlit
- Power BI

## Author

Aman Shaikh