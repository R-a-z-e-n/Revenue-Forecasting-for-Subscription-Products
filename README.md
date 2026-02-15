
# 📊 Revenue Forecasting for Subscription Products

## Overview
This project builds a forecasting model to predict **Monthly Recurring Revenue (MRR)** for subscription products and analyze the impact of churn and pricing changes.  
It uses time series forecasting models (**ARIMA** and **Prophet**) and provides an interactive **Streamlit dashboard** for product and finance teams.

---

## ✨ Features
- Forecast MRR for the next 6–12 months using ARIMA and Prophet.
- Interactive dashboard with:
  - Model selection (Prophet vs. ARIMA).
  - Forecast horizon slider (6–24 months).
  - Sensitivity analysis for churn and pricing changes.
- Visual comparison of historical vs. forecasted revenue.
- Automated **executive summary** with recommendations.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Pandas / NumPy** – data preparation
- **Statsmodels** – ARIMA forecasting
- **Prophet** – advanced time series forecasting
- **Matplotlib / Seaborn** – visualization
- **Streamlit** – interactive dashboard

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/revenue-forecasting.git
cd revenue-forecasting
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run revenue_forecast_app.py
```

### 4. Open in Browser
Streamlit will provide a local URL (default: `http://localhost:8501`) to interact with the dashboard.

---


---

## 📊 Example Workflow
1. Upload the **Netflix Dataset** or your subscription dataset.
2. Choose forecasting model (Prophet or ARIMA).
3. Set forecast horizon (6–24 months).
4. Adjust churn and pricing sliders for sensitivity analysis.
5. View forecast charts and executive summary.

---

## 📖 Executive Summary Example
- Forecasted MRR shows steady growth over the next 12 months.  
- Prophet predicts ~$X revenue by end of horizon.  
- ARIMA predicts ~$Y revenue by end of horizon.  
- Sensitivity analysis shows:
  - A 5% churn increase reduces MRR significantly.
  - A 10% price increase offsets churn losses.  
- **Recommendation:** Monitor churn closely and consider gradual pricing adjustments.

---

## 📌 Deliverables
- Python notebook (Colab-ready).
- Streamlit app for interactive forecasting.
- Statistical analysis outputs.
- Sensitivity analysis scenarios.
- Executive summary for product/finance teams.

---

## 🧑‍💻 Contributors
- Mohammad Razeen Iqbal  
- Open-source community contributions welcome!

---

