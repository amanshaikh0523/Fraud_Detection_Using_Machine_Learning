# Fraud Detection Using Machine Learning

## Project Overview

This project develops a machine learning-based fraud detection system capable of identifying fraudulent financial transactions. The workflow includes exploratory data analysis, feature engineering, model comparison, explainability analysis, and deployment through a Streamlit web application.

The objective is to help financial institutions detect potentially fraudulent transactions accurately while minimizing false alarms.

---

## Live Demo

Streamlit Application:

https://fraud-monitoring-system.streamlit.app/

---

## Problem Statement

Financial fraud results in significant monetary losses and poses major security risks for organizations. Traditional rule-based systems often fail to detect evolving fraud patterns.

This project leverages machine learning techniques to automatically identify suspicious transactions using transaction details and account balance information.

---

## Dataset Information

* Total Transactions: 11,142
* Legitimate Transactions: 10,000
* Fraudulent Transactions: 1,142
* Target Variable: `isFraud`

### Features Used

* type
* amount
* oldbalanceOrg
* newbalanceOrig
* oldbalanceDest
* newbalanceDest
* sender_balance_diff
* receiver_balance_diff
* sender_balance_zero
* receiver_balance_zero

---

## Exploratory Data Analysis (EDA)

Performed comprehensive EDA to understand transaction behavior and identify fraud patterns:

* Class distribution analysis
* Correlation analysis
* Distribution analysis
* Outlier detection
* Transaction amount analysis
* Fraud rate by transaction type

### Key Findings

* Fraudulent transactions showed significantly larger sender balance differences.
* Transaction amount was positively associated with fraud.
* Engineered balance-based features provided stronger predictive signals than several raw features.

---

## Feature Engineering

Created additional features to improve model performance:

### Sender Balance Difference

sender_balance_diff = oldbalanceOrg - newbalanceOrig

### Receiver Balance Difference

receiver_balance_diff = newbalanceDest - oldbalanceDest

### Sender Balance Zero Indicator

sender_balance_zero = 1 if newbalanceOrig == 0 else 0

### Receiver Balance Zero Indicator

receiver_balance_zero = 1 if newbalanceDest == 0 else 0

These engineered features significantly improved fraud detection performance.

---

## Models Evaluated

### Logistic Regression

* Accuracy: 99%
* Precision: 100%
* Recall: 93%
* F1 Score: 96%

### Random Forest

* Accuracy: 99%
* Precision: 99.7%
* Recall: 97.7%
* F1 Score: 98.7%

### XGBoost (Final Model)

* Accuracy: 99%
* Precision: 96%
* Recall: 99%
* F1 Score: 98%
* ROC-AUC: 99.89%

---

## Model Validation

### 5-Fold Stratified Cross Validation

F1 Scores:

* 0.9825
* 0.9803
* 0.9827
* 0.9735
* 0.9846

### Results

* Mean F1 Score: 98.07%
* Standard Deviation: 0.39%

These results indicate strong model generalization and minimal overfitting.

---

## Feature Importance

Top features identified by XGBoost:

| Feature             | Importance |
| ------------------- | ---------- |
| sender_balance_diff | 54.99%     |
| newbalanceOrig      | 22.26%     |
| amount              | 5.97%      |
| sender_balance_zero | 4.65%      |
| type                | 4.16%      |

### Insight

Abnormal sender-side balance changes were the strongest indicators of fraudulent activity.

---

## Model Explainability (SHAP)

SHAP analysis was used to interpret model predictions.

### Key Insights

* sender_balance_diff was the most influential feature.
* Transaction type significantly impacted fraud probability.
* Sender balance depletion strongly contributed to fraud predictions.
* Balance-related features were more important than transaction amount alone.

---

## Performance Metrics

| Metric             | Score  |
| ------------------ | ------ |
| Accuracy           | 99%    |
| Precision          | 96%    |
| Recall             | 99%    |
| F1 Score           | 98%    |
| ROC-AUC            | 99.89% |
| Cross-Validated F1 | 98.07% |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* SHAP
* Streamlit
* Joblib

---

## Streamlit Application

The deployed Streamlit application allows users to:

* Enter transaction details
* Generate fraud predictions
* View fraud probability scores
* Interactively test transaction scenarios

---



## Conclusion

This project successfully developed a machine learning-based fraud detection system using transaction and balance-related features. Multiple models were evaluated, with XGBoost delivering the best performance. The final model achieved 99% accuracy, 98% F1-score, 99% recall, and a ROC-AUC score of 99.89%, demonstrating exceptional fraud detection capability. Feature engineering and SHAP explainability further highlighted sender balance-related features as the most important indicators of fraudulent transactions.

---

## Author

**Aman Shaikh**

