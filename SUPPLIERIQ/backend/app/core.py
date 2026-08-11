import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "supplier_model.joblib"
FEATURES_PATH = BASE_DIR / "models" / "feature_columns.joblib"

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURES_PATH)


def get_risk_band(prob: float) -> str:
    if prob < 0.25:
        return "Low"
    elif prob < 0.50:
        return "Moderate"
    elif prob < 0.75:
        return "High"
    else:
        return "Critical"


def explain_risk_band(prob: float, band: str) -> str:
    if band == "Low":
        return (
            "Supplier appears low risk based on current "
            "performance and stability metrics."
        )
    elif band == "Moderate":
        return (
            "Supplier shows moderate risk; monitor performance "
            "and consider contingency options."
        )
    elif band == "High":
        return (
            "Supplier shows elevated risk; review before onboarding "
            "or increasing dependency."
        )
    else:
        return (
            "Supplier is assessed as critical risk; strong mitigation "
            "or alternative sourcing is recommended."
        )
