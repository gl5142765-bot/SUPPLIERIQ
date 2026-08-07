Day 13: Evaluation Part 1
Today we evaluated the final tuned model on the test set and studied its confusion matrix. We also computed the main classification metrics: accuracy, precision, recall, and F1 score.

Test metrics
The final model achieved:

Accuracy: 0.9422
Precision: 0.9418
Recall: 0.9422
F1 score: 0.9418

These scores show that the model performs well on unseen supplier data and is fairly balanced across classes.

Confusion matrix interpretation
Your confusion matrix was:

[[1488, 197], [128, 3807]]

So:

TN = 1488.
FP = 197.
FN = 128.
TP = 3807.


Business meaning
For SupplierIQ, a false negative means a risky supplier was missed, which is usually more dangerous because it can lead to delays, defects, or supply disruption. A false positive means a safe supplier was flagged as risky, which can waste review time but is usually less costly than missing a real risk