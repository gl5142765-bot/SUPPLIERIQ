Day 17 – FastAPI Backend (Part 2)

1\. Load trained model in FastAPI

Exported the final Logistic Regression model from Colab as supplier\_model.joblib using the cleaned dataset and 8 numeric features.



Updated the backend to load this artifact once at startup (in core.py), avoiding repeated model initialisation.



Confirmed the model is a pipeline that includes scaling and classification, keeping inference consistent with training.



2\. Define clear input schema and metrics

Implemented the SupplierInput Pydantic model with 8 fields:



* financial\_stability\_score
* on\_time\_delivery\_rate
* defect\_rate
* geopolitical\_risk\_index
* lead\_time\_days
* previous\_disruptions
* delivery\_quality\_index
* supplier\_dependency\_score



Added descriptions and realistic example values based on the supplier dataset:



* Financial stability: 2–100, typically 40–80.
* On-time rate: 30–100, typically 70–95.
* Defect rate: 0–19, typically 2–7.
* Geopolitical risk index: 11–87.
* Lead time: 0–88 days, typically 15–35.
* Previous disruptions: integers, typically 0–2.
* Delivery quality index: 30–100, typically 66–82.
* Supplier dependency score: 0–1 normalised.



Ensured Swagger documentation exposes these metrics so users understand the valid ranges.



3\. Implement /risk-score prediction endpoint

Created POST /risk-score that:



Accepts SupplierInput JSON.



Builds the 8-feature vector in the correct order.



Passes it to supplier\_model.joblib (pipeline) via predict\_proba.



Reads probability of the risky class (Risk\_Level = 1).



Defined risk bands and business messages:



0.00–0.25 → Low.



0.25–0.50 → Moderate.



0.50–0.75 → High.



0.75–1.00 → Critical.



Implemented get\_risk\_band(prob) and explain\_risk\_band(prob, band) to convert probabilities into clear supplier risk narratives.



4\. Test endpoint locally with real samples

Used Swagger UI to send realistic payloads taken directly from the dataset, including samples with Risk\_Level = 1.



Verified that:



A clearly risky supplier (low stability, non-trivial defects, longer lead time, disruptions) returns risk\_score ≈ 0.98 and risk\_band = "Critical" with a strong mitigation message.



Less risky suppliers produce lower probabilities and appropriate bands (Low/Moderate/High).



Confirmed that the earlier bug (everything returning Low) was resolved by aligning training and inference pipelines.



5\. Design notes for Streamlit and next phase

Decided that Streamlit inputs must show feature ranges clearly (min, max, typical) so users know the scale of each metric.



Plan to implement sliders/number inputs with these ranges:



* **Financial stability: 0–100.**
* **On-time rate: 0–100.**
* **Defect rate: 0–20.**
* **Geopolitical risk index: 0–100.**
* **Lead time days: 0–90.**
* **Previous disruptions: 0–10.**
* **Delivery quality index: 0–100.**
* **Supplier dependency score: 0–1.**



Backend is now stable and ready to be consumed by the Streamlit dashboard and later deployed to AWS.

