Day 11: Random Forest and Cross-Validation

we trained a Random Forest model and evaluated it using both a standard train-test split and cross-validation.



Random Forest results:



Train Accuracy: 1.00

Test Accuracy: 0.9304

Train F1: 1.00

Test F1: 0.9290



Cross-validation results:



CV F1 scores: \[0.9206, 0.9228, 0.9255, 0.9188, 0.9265]

CV F1 mean: 0.9228

CV F1 std: 0.0029



How to interpret cross-validation

Cross-validation evaluates the model multiple times on different folds of the training data, so it gives a more stable estimate than a single split.



A low standard deviation like 0.0029 means the model performs consistently across folds, which is a good sign.



Comparison with earlier models

Use this comparison table:



**Model	            Train Accuracy Test Accuracy   Train F1	Test F1  	Comment**

**Logistic Regression	0.9419	    0.9413	    0.9416	0.9411	  Best consistency and strong generalisation** 

**Decision Tree	        1.0000	    0.9037	    1.0000	0.9038	  Clear overfitting on training data** 

**Random Forest	        1.0000	    0.9304	    1.0000	0.9290	  Better than Decision Tree, slightly below Logistic Regression** on test scores. 





Conclusion

Random Forest improves over the single Decision Tree and generalises better, but Logistic Regression still has the strongest test performance and most stable train-test behaviour so far.



So the current ranking is:



1. Logistic Regression.
2. Random Forest.
3. Decision Tree.

