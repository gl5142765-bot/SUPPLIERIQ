# SupplierIQ – AI-Powered Supplier Risk Intelligence Platform

SupplierIQ is a machine learning project that predicts supplier risk from structured business data. The goal is to help procurement teams identify high-risk suppliers before delays, quality issues, compliance problems, or instability affect operations.

The project turns raw supplier records into:
- A binary risk label (`0 = low risk`, `1 = high risk`).
- Model evaluation metrics and confusion matrix.
- A foundation for an API and dashboard for business users.

---

## Project Structure

- `supplier_risk_dataset.csv` – original dataset.
- `supplier_risk_cleaned.csv` – cleaned and preprocessed dataset.
- `SUPPLIER IQ FINAL.ipynb` – main notebook with EDA, preprocessing, modelling, tuning, and evaluation.
- `supply-model.joblib` – saved tuned Logistic Regression model.
- `README.md` – project documentation.
- `requirements.txt` – Python dependencies.

---

## Data and Target

The dataset contains supplier-level features such as:

- Financial stability score  
- On-time delivery rate  
- Defect rate  
- Geopolitical risk index  
- Lead time days  
- Previous disruptions  
- Delivery quality index  
- Supplier dependency score  

**Target variable:** `Risk_Level` (`0 = low risk`, `1 = high risk`).

---

## Workflow

- **Business understanding** – frame supplier risk as a binary classification problem.  
- **Dataset understanding** – inspect schema, distributions, and class balance.  
- **EDA** – visualise key features and risk distribution, study correlations and outliers.  
- **Cleaning** – handle missing values, remove duplicates, and save a cleaned copy.  
- **Preprocessing** – encode categorical features (`Country`, `Region`, `Industry`), scale numeric features, and create train/test splits.  
- **Baseline models** – train Logistic Regression and Decision Tree; compare behaviour using accuracy, precision, recall, F1, and confusion matrices.  
- **Random Forest** – train an ensemble model and evaluate with train/test metrics and cross-validation.  
- **Hyperparameter tuning** – tune Logistic Regression using `GridSearchCV` and `RandomizedSearchCV` to find the best regularization settings.  
- **Evaluation** – compute final test metrics and study the confusion matrix for business interpretation.

---

## Final Model

The final chosen model is a **tuned Logistic Regression** classifier.

**Key test metrics (approximate):**
- Accuracy: ~0.94  
- Precision: ~0.94  
- Recall: ~0.94  
- F1-score: ~0.94  

### Confusion matrix (approximate)

- **True negatives** – safe suppliers correctly classified.  
- **False positives** – safe suppliers flagged as risky.  
- **False negatives** – risky suppliers missed.  
- **True positives** – risky suppliers correctly classified.

These metrics indicate that the model generalises well to unseen suppliers and maintains a good balance between catching risky suppliers and limiting false alarms.

---

## Business Interpretation

For procurement teams:

- **True positives** highlight suppliers that should be monitored, renegotiated, diversified, or replaced.  
- **False negatives** are the most dangerous errors, as they represent risky suppliers that appear safe.  
- **False positives** create extra review work but can be acceptable if the cost of missing a risky supplier is high.

SupplierIQ supports a proactive risk management workflow by giving teams a data-driven view of supplier stability, delivery reliability, and disruption history.

---

## How to Run

1. **Create a Python environment** (e.g. `venv` or `conda`).

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the prediction script (example):**

   ```bash
   python predict_example.py
   ```

   This script:
   - loads the trained model from `supply-model.joblib`,
   - applies the same preprocessing steps used during training,
   - outputs a supplier risk prediction (low risk / high risk) and probability.

If you want to explore the full pipeline, you can open `SUPPLIER IQ FINAL.ipynb` in Jupyter Notebook and run the analysis step by step.

---

## Visuals

_(<img width="978" height="774" alt="image" src="https://github.com/user-attachments/assets/20f44079-e542-4ec2-881d-ca5bb98b0200" />
<img width="1067" height="410" alt="image" src="https://github.com/user-attachments/assets/a3b76262-8b56-4c77-b906-6f6551ce4dba" />
<img width="985" height="818" alt="image" src="https://github.com/user-attachments/assets/2c6adeb0-8215-4c59-8a45-98ec61eb6a2e" />



```

---

## Project Status and Next Steps

- The end-to-end ML pipeline is complete: data cleaning, feature engineering, baseline models, Random Forest, tuning, and final evaluation.  
- The tuned Logistic Regression model is saved as `supply-model.joblib` and can be loaded in scripts or APIs without notebooks.  
- A Streamlit dashboard is under development to visualise supplier risk, feature values, and model outputs.  
- AWS deployment (e.g. EC2) is in progress so that SupplierIQ can be accessed as a web application by procurement teams.
