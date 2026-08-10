import streamlit as st
import requests
import pandas as pd
import os

# -----------------------------
# Config
# -----------------------------

BACKEND_URL = os.getenv("BACKEND_URL")
API_URL = f"{BACKEND_URL}/risk-score"

st.set_page_config(
    page_title="SupplierIQ – Risk Dashboard",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("SupplierIQ – Supplier Risk Prediction")
st.markdown(
    "Estimate how risky a supplier is based on its performance and reliability. "
    "Set the metrics below to see the predicted risk level."
)

# -----------------------------
# Input widgets
# -----------------------------

st.subheader("Supplier metrics")

col1, col2 = st.columns(2)

with col1:
    financial_stability_score = st.slider(
        "Financial Stability Score",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        help="Overall financial health of the supplier (0–100, higher is better).",
    )

    on_time_delivery_rate = st.slider(
        "On-time Delivery Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        help="Percentage of orders delivered on time (0–100, higher is better).",
    )

    defect_rate = st.slider(
        "Defect Rate (%)",
        min_value=0.0,
        max_value=20.0,
        value=5.0,
        help="Percentage of units with defects (0–20, lower is better).",
    )

    geopolitical_risk_index = st.slider(
        "Geopolitical Risk Index",
        min_value=0,
        max_value=100,
        value=30,
        help="External geopolitical risk in the supplier's region (0–100, higher is riskier).",
    )

with col2:
    lead_time_days = st.slider(
        "Lead Time (days)",
        min_value=0,
        max_value=90,
        value=25,
        help="Average delivery lead time in days (0–90, lower is better).",
    )

    previous_disruptions = st.slider(
        "Previous Disruptions (count)",
        min_value=0,
        max_value=10,
        value=1,
        help="Number of major supply disruptions in the past (integer).",
    )

    delivery_quality_index = st.slider(
        "Delivery Quality Index",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        help="Overall delivery quality score (0–100, higher is better).",
    )

    supplier_dependency_score = st.slider(
        "Supplier Dependency Score",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.05,
        help="Dependency level on this supplier (0–1, higher means more dependent).",
    )

# -----------------------------
# Call API
# -----------------------------

st.markdown("---")

if st.button("Predict supplier risk"):
    payload = {
        "financial_stability_score": financial_stability_score,
        "on_time_delivery_rate": on_time_delivery_rate,
        "defect_rate": defect_rate,
        "geopolitical_risk_index": geopolitical_risk_index,
        "lead_time_days": lead_time_days,
        "previous_disruptions": int(previous_disruptions),
        "delivery_quality_index": delivery_quality_index,
        "supplier_dependency_score": supplier_dependency_score,
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            risk_score = data.get("risk_score")
            risk_band = data.get("risk_band")
            message = data.get("message")

            st.success("Prediction received from backend.")

            # -------------------
            # Summary cards (KPIs)
            # -------------------
            kpi1, kpi2, kpi3 = st.columns(3)

            with kpi1:
                st.metric(
                    label="Risk score",
                    value=f"{risk_score:.3f}",
                    help="Model probability that this supplier is high risk (Risk_Level = 1).",
                )

            with kpi2:
                st.metric(
                    label="Risk band",
                    value=risk_band,
                    help="Low, Moderate, High or Critical based on the risk score.",
                )

            with kpi3:
                st.metric(
                    label="Previous disruptions",
                    value=int(previous_disruptions),
                    help="Number of major disruptions in the past.",
                )

            st.write(f"**Explanation:** {message}")

        else:
            st.error(f"API error: {response.status_code} – {response.text}")

    except Exception as e:
        st.error(f"Failed to call backend API: {e}")
