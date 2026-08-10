from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
from .core import model, get_risk_band, explain_risk_band

from fastapi import FastAPI

app = FastAPI()

class SupplierInput(BaseModel):
    financial_stability_score: float = Field(..., description="Financial health score (0–400, higher is better)", example=250)
    on_time_delivery_rate: float = Field(..., description="On-time delivery rate in percentage (0–100, higher is better)", example=92)
    defect_rate: float = Field(..., description="Defect rate in percentage of units shipped (0–100, lower is better)", example=4)
    geopolitical_risk_index: float = Field(..., description="Geopolitical risk index (0–100, higher means more external risk)", example=35)
    lead_time_days: float = Field(..., description="Average lead time in days (positive, lower is better)", example=28)
    previous_disruptions: int = Field(..., description="Number of previous major supply disruptions (integer, 0 or more)", example=2)
    delivery_quality_index: float = Field(..., description="Delivery quality index (0–100, higher is better)", example=78)
    supplier_dependency_score: float = Field(..., description="Business dependency (1–5 scale, 5 = highly dependent)", example=3)


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
