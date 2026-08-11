from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
from .core import model, get_risk_band, explain_risk_band

app = FastAPI()

class SupplierInput(BaseModel):
    financial_stability_score: float = Field(
        ...,
        description="Financial health score (0–100, higher is better)",
        example=60
    )

    on_time_delivery_rate: float = Field(
        ...,
        description="On-time delivery rate in percentage (0–100, higher is better)",
        example=80
    )

    defect_rate: float = Field(
        ...,
        description="Defect rate in percentage (0–20, lower is better)",
        example=5
    )

    geopolitical_risk_index: float = Field(
        ...,
        description="Geopolitical risk index (0–100, higher means more external risk)",
        example=30
    )

    lead_time_days: float = Field(
        ...,
        description="Average lead time in days (0–90, lower is better)",
        example=25
    )

    previous_disruptions: int = Field(
        ...,
        description="Number of previous major supply disruptions (0–10)",
        example=1
    )

    delivery_quality_index: float = Field(
        ...,
        description="Delivery quality index (0–100, higher is better)",
        example=75
    )

    supplier_dependency_score: float = Field(
        ...,
        description="Supplier dependency score (0–1, higher means more dependent)",
        example=0.30
    )

@app.get("/")
def read_root():
    return {"message": "SupplierIQ backend is running"}


@app.post("/risk-score")
def predict_risk(input_data: SupplierInput):
    features = [
        input_data.financial_stability_score,
        input_data.on_time_delivery_rate,
        input_data.defect_rate,
        input_data.geopolitical_risk_index,
        input_data.lead_time_days,
        input_data.previous_disruptions,
        input_data.delivery_quality_index,
        input_data.supplier_dependency_score,
    ]
    X = np.array(features).reshape(1, -1)

    # model is a Pipeline: it will scale + apply LogisticRegression
    proba = model.predict_proba(X)[0][1]  # probability of risky class

    risk_band = get_risk_band(proba)
    message = explain_risk_band(proba, risk_band)

    return {
        "risk_score": round(float(proba), 4),
        "risk_band": risk_band,
        "message": message,
    }
