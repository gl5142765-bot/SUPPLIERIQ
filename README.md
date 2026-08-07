SupplierIQ – AI-Powered Supplier Risk Intelligence Platform
Overview
SupplierIQ is a machine learning project that predicts supplier risk from structured business data. The goal is to help procurement teams identify high-risk suppliers before delays, quality issues, compliance problems, or instability affect operations 
.

The project turns raw supplier records into:

A binary risk label (0 = low risk, 1 = high risk).

Model evaluation metrics and confusion matrix.

A foundation for an API and dashboard for business users.

Project Structure
supplier_risk_dataset.csv – original dataset.

supplier_risk_cleaned.csv – cleaned and preprocessed dataset 
.

SupplierIQ_testing.ipynb – main notebook with EDA, preprocessing, modeling, tuning, and evaluation 
.

README.md – project documentation.

requirements.txt – Python dependencies.

Data and Target
The dataset contains supplier-level features such as:

Financial stability score.

On-time delivery rate.

Defect rate.

Geopolitical risk index.

Lead time days.

Alternative suppliers available.

Contract length (months).

Environmental compliance.

Previous disruptions.

Delivery quality index.

Supplier dependency score 
.

Target variable: Risk_Level (0 = low risk, 1 = high risk).

Workflow
Business understanding – frame supplier risk as a binary classification problem.

Dataset understanding – inspect schema, distributions, and class balance.

EDA – visualize key features and risk distribution, study correlations and outliers.

Cleaning – handle missing values, remove duplicates, and save a cleaned copy 
.

Preprocessing – encode categorical features (Country, Region, Industry), scale numeric features, and create train/test splits.

Baseline models – train Logistic Regression and Decision Tree, compare behavior using accuracy, precision, recall, F1, and confusion matrices.

Random Forest – train ensemble model and evaluate with train/test metrics and cross-validation.

Hyperparameter tuning – tune Logistic Regression using GridSearchCV and RandomizedSearchCV to find the best regularization settings.

Evaluation – compute final test metrics and study the confusion matrix for business interpretation.

Final Model
The final chosen model is a tuned Logistic Regression classifier.

Key test metrics:

Accuracy: ~0.94.

Precision: ~0.94.

Recall: ~0.94.

F1-score: ~0.94 
.

Confusion matrix (approximate):

True negatives (safe suppliers correctly classified).

False positives (safe suppliers flagged as risky).

False negatives (risky suppliers missed).

True positives (risky suppliers correctly classified).

These metrics indicate that the model generalizes well to unseen suppliers and maintains a good balance between catching risky suppliers and limiting false alarms.

Business Interpretation
For procurement teams:

True positives highlight suppliers that should be monitored, renegotiated, diversified, or replaced.

False negatives are the most dangerous errors, as they represent risky suppliers that appear safe.

False positives create extra review work but can be acceptable if the cost of missing a risky supplier is high.

SupplierIQ supports a proactive risk management workflow by giving teams a data-driven view of supplier stability, delivery reliability, and disruption history 
.

How to Run
Create a Python environment (e.g., using venv or conda).

Install dependencies:

bash
pip install -r requirements.txt
Open the notebook:

bash
jupyter notebook SupplierIQ_testing.ipynb
Run the cells step by step:

Load and explore the dataset.

Apply cleaning and preprocessing.

Train baseline models.

Train Random Forest and perform cross-validation.

Tune Logistic Regression hyperparameters.

Evaluate the final model and review metrics.

Next Steps
The project is designed to be extended into:

A FastAPI backend that exposes the model via a REST API.

A Streamlit dashboard for interactive supplier risk exploration.

AWS deployment (e.g., EC2) for hosting the full application 
.

These next phases will turn SupplierIQ from a notebook-based model into a production-ready, resume-worthy ML product.
