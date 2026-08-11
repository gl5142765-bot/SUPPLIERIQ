import os

import requests
import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title="SupplierIQ – Risk Dashboard",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto",
)


# ============================================================
# CHECK BACKEND CONFIGURATION
# ============================================================

if not BACKEND_URL:
    st.error(
        "Backend URL is not configured. "
        "Please set the BACKEND_URL environment variable in Railway."
    )
    st.stop()

BACKEND_URL = BACKEND_URL.rstrip("/")


# ============================================================
# PAGE HEADER
# ============================================================

st.title("SupplierIQ – Supplier Risk Prediction")

st.markdown(
    "Estimate how risky a supplier is based on its performance and reliability. "
    "Set the metrics below to see the predicted risk level."
)


# ============================================================
# SUPPLIER METRICS
# ============================================================

st.subheader("Supplier metrics")

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# LEFT COLUMN
# ------------------------------------------------------------

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
        help="External geopolitical risk (0–100, higher is riskier).",
    )


# ------------------------------------------------------------
# RIGHT COLUMN
# ------------------------------------------------------------

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
        help="Number of major supply disruptions in the past.",
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
        value=0.30,
        step=0.05,
        help="Dependency level on this supplier (0–1, higher means more dependent).",
    )


# ============================================================
# PREDICTION
# ============================================================

st.markdown("---")

if st.button("Predict supplier risk", type="primary"):

    # --------------------------------------------------------
    # Prepare input data
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Backend endpoint
    # --------------------------------------------------------

    api_url = f"{BACKEND_URL}/risk-score"

    # --------------------------------------------------------
    # Call FastAPI backend
    # --------------------------------------------------------

    try:

        response = requests.post(
            api_url,
            json=payload,
            timeout=30,
        )

        # ----------------------------------------------------
        # Successful response
        # ----------------------------------------------------

        if response.status_code == 200:

            data = response.json()

            risk_score = data.get("risk_score")
            risk_band = data.get("risk_band")
            message = data.get("message")

            st.success("Prediction received from backend.")

            # ------------------------------------------------
            # KPI CARDS
            # ------------------------------------------------

            kpi1, kpi2, kpi3 = st.columns(3)

            with kpi1:
                if risk_score is not None:
                    st.metric(
                        label="Risk score",
                        value=f"{float(risk_score):.3f}",
                        help=(
                            "Model probability that this supplier "
                            "belongs to the high-risk class."
                        ),
                    )
                else:
                    st.metric(
                        label="Risk score",
                        value="N/A",
                    )

            with kpi2:
                st.metric(
                    label="Risk band",
                    value=risk_band if risk_band else "N/A",
                    help=(
                        "Risk classification returned by the backend."
                    ),
                )

            with kpi3:
                st.metric(
                    label="Previous disruptions",
                    value=int(previous_disruptions),
                    help=(
                        "Number of major supply disruptions "
                        "entered above."
                    ),
                )

            # ------------------------------------------------
            # EXPLANATION
            # ------------------------------------------------

            if message:
                st.info(f"**Explanation:** {message}")

        # ----------------------------------------------------
        # Rate limited
        # ----------------------------------------------------

        elif response.status_code == 429:

            st.warning(
                "The backend returned **429 – Too Many Requests**. "
                "Please wait a moment and try again."
            )

            st.caption(
                f"Backend response: {response.text}"
            )

        # ----------------------------------------------------
        # Validation error
        # ----------------------------------------------------

        elif response.status_code == 422:

            st.error(
                "The backend rejected the submitted data "
                "(422 – Validation Error)."
            )

            st.code(response.text)

        # ----------------------------------------------------
        # Other API errors
        # ----------------------------------------------------

        else:

            st.error(
                f"Backend API error: "
                f"{response.status_code}"
            )

            st.code(response.text)

    # --------------------------------------------------------
    # Connection / request error
    # --------------------------------------------------------

    except requests.exceptions.Timeout:

        st.error(
            "The backend took too long to respond. "
            "Please try again."
        )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect to the SupplierIQ backend. "
            "Please check that the FastAPI backend is running."
        )

    except requests.exceptions.RequestException as e:

        st.error(
            f"Request to backend failed: {e}"
        )

    except Exception as e:

        st.error(
            f"Unexpected error: {e}"
        )
