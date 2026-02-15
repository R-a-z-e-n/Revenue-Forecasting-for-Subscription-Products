


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

# -----------------------------
# Helper Functions
# -----------------------------
def load_data(file_path="Netflix Dataset.csv"):
    df = pd.read_csv(file_path)
    df['StartDate'] = pd.to_datetime(df['StartDate'])
    df['EndDate'] = pd.to_datetime(df['EndDate'])
    df['Month'] = df['StartDate'].dt.to_period('M')
    monthly_revenue = df.groupby('Month')['Revenue'].sum().reset_index()
    monthly_revenue['Month'] = monthly_revenue['Month'].dt.to_timestamp()
    return monthly_revenue

def prophet_forecast(monthly_revenue, horizon=12):
    prophet_df = monthly_revenue.rename(columns={'Month':'ds','Revenue':'y'})
    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=horizon, freq='M')
    forecast = model.predict(future)
    return forecast

def arima_forecast(monthly_revenue, horizon=12):
    model = ARIMA(monthly_revenue['Revenue'], order=(1,1,1))
    fit = model.fit()
    forecast = fit.forecast(steps=horizon)
    return forecast

def simulate_churn(mrr, churn_rate):
    return mrr * (1 - churn_rate)

def simulate_pricing(mrr, price_increase):
    return mrr * (1 + price_increase)

# -----------------------------
# Streamlit Interface
# -----------------------------
st.title("📊 Revenue Forecasting for Subscription Products")
st.write("Forecast Monthly Recurring Revenue (MRR) and analyze churn/pricing impact.")

# File upload
uploaded_file = st.file_uploader("Upload Netflix Dataset CSV", type="csv")
if uploaded_file:
    monthly_revenue = load_data(uploaded_file)

    # Forecast horizon
    horizon = st.slider("Forecast horizon (months)", 6, 24, 12)

    # Model selection
    model_choice = st.selectbox("Choose forecasting model", ["Prophet", "ARIMA"])

    if model_choice == "Prophet":
        forecast = prophet_forecast(monthly_revenue, horizon)
        st.subheader("Prophet Forecast")
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(monthly_revenue['Month'], monthly_revenue['Revenue'], label="Historical")
        ax.plot(forecast['ds'], forecast['yhat'], label="Forecast")
        ax.legend()
        st.pyplot(fig)
    else:
        forecast = arima_forecast(monthly_revenue, horizon)
        st.subheader("ARIMA Forecast")
        fig, ax = plt.subplots(figsize=(10,5))
        ax.plot(monthly_revenue['Month'], monthly_revenue['Revenue'], label="Historical")
        ax.plot(pd.date_range(monthly_revenue['Month'].iloc[-1], periods=horizon, freq='M'),
                forecast, label="Forecast")
        ax.legend()
        st.pyplot(fig)

    # Sensitivity Analysis
    st.subheader("Sensitivity Analysis")
    base_mrr = monthly_revenue['Revenue'].iloc[-1]
    churn_rate = st.slider("Churn rate increase (%)", 0, 20, 5) / 100
    price_increase = st.slider("Price increase (%)", 0, 20, 5) / 100

    churn_mrr = simulate_churn(base_mrr, churn_rate)
    price_mrr = simulate_pricing(base_mrr, price_increase)

    st.write(f"Base MRR: {base_mrr:.2f}")
    st.write(f"MRR after churn impact: {churn_mrr:.2f}")
    st.write(f"MRR after price increase: {price_mrr:.2f}")

    # Executive Summary
    st.subheader("Executive Summary")
    st.text(f"""
    Forecast Horizon: {horizon} months
    Model Used: {model_choice}
    Base MRR: {base_mrr:.2f}
    Churn Impact: {churn_rate*100:.1f}% → {churn_mrr:.2f}
    Pricing Impact: {price_increase*100:.1f}% → {price_mrr:.2f}

    Recommendation:
    - Monitor churn closely; even small increases reduce MRR significantly.
    - Pricing adjustments can offset churn losses.
    - Consider gradual rollout of pricing changes with churn mitigation strategies.
    """)
else:
    st.warning("Please upload the Netflix Dataset CSV to begin.")
