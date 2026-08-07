##### **Day 7 - Feature Engineering Part 1**

##### **Task Summary**



Selected the first model-ready feature set.



Checked the final selected features for leakage risk.



Confirmed no obvious leakage was found.



**Identifier Column**

Supplier\_ID is an identifier column.



It is useful for tracking suppliers, but it should not be used as a model input.



**Final 8 Features**



* Financial\_Stability\_Score
* On\_Time\_Delivery\_Rate
* Defect\_Rate
* Geopolitical\_Risk\_Index
* Lead\_Time\_Days
* Alternative\_Suppliers\_Available
* Previous\_Disruptions
* Supplier\_Dependency\_Score



***Purpose of Final Features***



* Financial strength.
* Delivery reliability.
* Quality problems.
* External risk.
* Delay risk.
* Backup supplier availability.
* Past disruption history.
* Dependency risk.



**Leakage Check**

The selected features were reviewed for data leakage.



No obvious leakage was found.



The features appear available at prediction time and do not directly reveal the target.



**Conclusion**

**The first model-ready feature set is finalised.**

**This feature set is now ready for modelling.**

