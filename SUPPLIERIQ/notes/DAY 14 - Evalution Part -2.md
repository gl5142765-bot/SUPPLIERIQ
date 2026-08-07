Day 14: Evaluation Part 2 Notes
ROC-AUC review
We evaluated the final tuned Logistic Regression model for SupplierIQ using the ROC curve and ROC-AUC on the test data. The ROC curve showed how the true positive rate (TPR / recall) and false positive rate (FPR) change as we vary the probability threshold used to classify a supplier as risky. The ROC-AUC score was high, indicating that the model ranks risky suppliers above safe suppliers consistently across different thresholds.[web:184][web:188][web:191]

Threshold choice
Using predict_proba on the test set, we inspected several thresholds:

Threshold ∞: TPR = 0.000, FPR = 0.000 (model never flags any supplier as risky).

Threshold 0.832: TPR ≈ 0.854, FPR ≈ 0.024.

Threshold 0.519: TPR ≈ 0.965, FPR ≈ 0.109.

Threshold 0.000: TPR = 1.000, FPR = 1.000 (every supplier is flagged as risky).

For SupplierIQ, missing a truly risky supplier can be extremely costly because it may lead to supply disruption, quality failures, or compliance issues. Therefore, we prefer a threshold that keeps TPR very high, even if it allows more false positives.[web:187][web:189][web:192]

Based on this reasoning, we chose a threshold around 0.52. At this threshold, the model correctly identifies roughly 96.5% of risky suppliers (high recall / TPR) while accepting a higher false positive rate of about 10.9%. This trade-off is appropriate when the business cares more about catching risky suppliers than avoiding extra reviews of safe ones.[web:185][web:191][web:206]

Cost of error types
In SupplierIQ:

False negatives (FN) occur when the model predicts that a supplier is safe, but the supplier is actually risky.

False positives (FP) occur when the model predicts that a supplier is risky, but the supplier is actually safe.

False negatives are more costly because they can cause stock-outs, missed deadlines, quality issues, and regulatory problems that impact operations and customers. False positives mainly lead to additional manual review or conservative decisions (for example, monitoring or renegotiating with a safe supplier), which is less harmful than failing to detect a genuinely risky supplier.[web:845][web:850][web:852]

Because false negatives are more costly than false positives, the chosen threshold around 0.52 intentionally prioritizes high recall over low FPR. The model will flag more suppliers as risky, but this helps procurement teams catch nearly all high-risk suppliers and take preventive action.

Business interpretation
Under the chosen threshold, SupplierIQ behaves like a safety-focused early warning system:

It treats missing a risky supplier as the most expensive mistake.
It accepts more false alarms so that the majority of risky suppliers are detected.
It supports procurement and risk teams in proactively identifying suppliers that need monitoring, diversification, or remediation.