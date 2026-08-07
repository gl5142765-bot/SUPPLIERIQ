##### ***Day 06 - Cleaning Part 2***

##### ***Concepts Covered***

##### ***Encoding categorical columns.***





Deciding whether scaling is needed.



Splitting data into train and test sets.



Documenting preprocessing choices.



Tasks Completed

Split the dataset into training and test sets.



Encoded categorical columns using **OneHotEncoder**.



Kept **Supplier\_ID** separate so it remains unchanged.



Scaled the numeric columns.



Confirmed preprocessing is ready for model training.



Key Preprocessing Notes

Risk\_Level was kept as the target column.



Supplier\_ID was not used as a model feature.



Encoding was applied only after splitting to avoid data leakage.



Scaling was applied to numeric columns to bring them to a similar range.



The final preprocessing pipeline produced model-ready train and test sets.





**Training Summary**

Model used: Logistic Regression.



Accuracy: 0.9413.



Class 0 precision / recall / F1: 0.91 / 0.89 / 0.90.



Class 1 precision / recall / F1: 0.95 / 0.96 / 0.96.



Confusion matrix:



True Negatives: 1504



False Positives: 181



False Negatives: 149



True Positives: 3786



Initial Interpretation

The model performed well on the test set.



The positive class was predicted especially well.



The cleaned features appear to contain strong risk-related signal.



The preprocessing steps seem to have improved model readiness.







**Important Learning**

Always split before fitting encoders and scalers.



Never scale or encode Supplier\_ID.



Keep preprocessing consistent between training and test sets.



Next Step

Evaluate the model more deeply.



Compare with another model if needed.



Move toward feature importance and model improvement.







