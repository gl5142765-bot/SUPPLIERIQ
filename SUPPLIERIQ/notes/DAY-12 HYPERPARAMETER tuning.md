Day 12: Hyperparameter Tuning Notes
Chosen model
The chosen model for tuning was Logistic Regression because it had shown the strongest and most stable performance among the earlier baseline models in SupplierIQ.

Hyperparameter used
The main hyperparameter tuned was C, which controls regularisation strength in Logistic Regression. A smaller C means stronger regularisation, while a larger C means weaker regularisation.

Parameter search
RandomizedSearchCV was used to test multiple parameter combinations more efficiently than checking every possible combination through Grid Search. The search tested different random states, and the observed best C values were approximately 0.0466 for seed 42, 0.0803 for seed 7, and 0.1560 for seed 123.

Best setting
Based on the recorded tuning runs, random_state = 42 was selected as the preferred setting for the project notes, with a strong cross-validated F1 score and stable tuned parameters. The differences among seeds were very small, suggesting that the tuned Logistic Regression model is robust to different random searches.

Why tuning helps
Hyperparameter tuning helps by improving how well the model balances fit and generalisation. In SupplierIQ, tuning helps the Logistic Regression model become more reliable, more efficient, and better at making stable supplier-risk predictions on unseen data.