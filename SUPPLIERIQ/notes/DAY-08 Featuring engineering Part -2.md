##### **Day 8 - Feature Engineering Part 2**



Concepts

Feature importance.

Domain reasoning.



**Task Summary**

Thought about which features should matter most.

Kept the feature set unchanged.

Recorded why each feature is kept.

Removed the identifier column from modelling.



**Wrote short interview notes.**



***Final Feature Set***



* Financial\_Stability\_Score.
* On\_Time\_Delivery\_Rate.
* Defect\_Rate.
* Geopolitical\_Risk\_Index.
* Lead\_Time\_Days.
* Alternative\_Suppliers\_Available.
* Previous\_Disruptions.
* Supplier\_Dependency\_Score.



**Why These Features Matter**



* Financial\_Stability\_Score: reflects supplier financial strength.
* On\_Time\_Delivery\_Rate: reflects delivery reliability.
* Defect\_Rate: reflects quality problems.
* Geopolitical\_Risk\_Index: reflects external risk.
* Lead\_Time\_Days: reflects delay risk.
* Alternative\_Suppliers\_Available: reflects backup supplier availability.
* Previous\_Disruptions: reflects past disruption history.
* Supplier\_Dependency\_Score: reflects dependency risk.



**Kept Without Change**

No new derived feature was added.

The selected columns already capture the main supplier risk signals.

Keeping the feature set unchanged makes the model easier to interpret.



**Removed**

**Supplier\_ID was removed because it is only an identifier.**



It helps track suppliers, but it should not be used for prediction.



Interview Notes

Feature importance tells us which variables help the model most.

Domain reasoning uses business knowledge to decide whether a feature should matter.

A good feature should be both useful for prediction and meaningful for the business.

Identifier columns should not be used as model inputs.



**Conclusion**

**The final feature set remains unchanged.**

**The feature selection looks clean, logical, and business-relevant.**

**The project can move forward with this model-ready feature set.**

