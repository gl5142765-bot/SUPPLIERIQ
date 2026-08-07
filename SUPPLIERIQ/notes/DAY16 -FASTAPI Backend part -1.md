Day 16: FastAPI Backend Part 1 – Summary
What we did
Created the backend project structure for SupplierIQ, with a clear app/, models/, and core/ layout.
Implemented a health route (GET /health) to confirm that the FastAPI service is running and reachable.
Designed the prediction endpoint skeleton (POST /risk-score) that accepts supplier data as JSON.

Fixed the model loading flow by:

Training a Logistic Regression model on 11 numeric features that match the API input.
Saving the trained model and scaler from the notebook using joblib.
Loading these artifacts in core.py and exposing a simple predict_risk_from_features function.

Current API behaviour
The /risk-score endpoint:

Accepts a JSON body with 11 supplier features (financial stability, delivery rate, defect rate, geopolitical risk, lead time, alternatives, contract length, environmental compliance, previous disruptions, delivery quality, dependency score).

Scales the inputs using the saved scaler.
Calls the saved Logistic Regression model to compute a risk_score (probability of high risk).
Uses a threshold (≈ 0.52) to assign a risk_band of "High" or "Low".

Why this matters

The backend is now consistent with the training pipeline: the model sees the same 11 features it was trained on.
The prediction endpoint is ready for Day 17, where we will test realistic payloads, refine thresholds if needed, and stabilize the prediction service.

Short note for interview
"On Day 16, I wired the FastAPI backend for SupplierIQ: created a health check, defined a JSON-based /risk-score endpoint, and built a model loading flow that uses a serialized Logistic Regression and scaler trained on the same 11 numeric features the API accepts. This ensures that online predictions match the offline training setup."