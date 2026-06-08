import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("fraud_detection_xgboost.pkl")

st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Fraud Detection System")
st.markdown("Predict whether a financial transaction is fraudulent or legitimate.")

st.subheader("Enter Transaction Details")

# Transaction Type
transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"]
)

# Match your Label Encoding
type_mapping = {
    "CASH_IN": 0,
    "CASH_OUT": 1,
    "DEBIT": 2,
    "PAYMENT": 3,
    "TRANSFER": 4
}

type_encoded = type_mapping[transaction_type]

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    "Sender Old Balance",
    min_value=0.0,
    value=5000.0
)

newbalanceOrig = st.number_input(
    "Sender New Balance",
    min_value=0.0,
    value=4000.0
)

oldbalanceDest = st.number_input(
    "Receiver Old Balance",
    min_value=0.0,
    value=2000.0
)

newbalanceDest = st.number_input(
    "Receiver New Balance",
    min_value=0.0,
    value=3000.0
)

# Feature Engineering
sender_balance_diff = oldbalanceOrg - newbalanceOrig

receiver_balance_diff = (
    newbalanceDest - oldbalanceDest
)

sender_balance_zero = (
    1 if newbalanceOrig == 0 else 0
)

receiver_balance_zero = (
    1 if newbalanceDest == 0 else 0
)

if st.button("Predict Fraud"):

    input_data = pd.DataFrame({
        'type': [type_encoded],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest],
        'sender_balance_diff': [sender_balance_diff],
        'receiver_balance_diff': [receiver_balance_diff],
        'sender_balance_zero': [sender_balance_zero],
        'receiver_balance_zero': [receiver_balance_zero]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(
            f"⚠️ Fraudulent Transaction Detected\n\nFraud Probability: {probability:.2%}"
        )
    else:
        st.success(
            f"✅ Legitimate Transaction\n\nFraud Probability: {probability:.2%}"
        )

    st.subheader("Engineered Features")

    st.write(f"Sender Balance Difference: {sender_balance_diff:,.2f}")
    st.write(f"Receiver Balance Difference: {receiver_balance_diff:,.2f}")