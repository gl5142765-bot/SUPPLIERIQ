Why the model predicts high risk: for a high-risk supplier, important features are usually in “bad” ranges (low stability, poor delivery, high defects, etc.), and the model combines them into a high probability of risk.





**Likely top drivers of risk (SupplierIQ)**

From your dataset, reasonable top drivers are:



Financial\_Stability\_Score – a low score suggests the supplier may struggle to survive financially.

On\_Time\_Delivery\_Rate – low rate means frequent delays.

Defect\_Rate – high defect rate means quality problems.

Geopolitical\_Risk\_Index – a high index means external country/region risk.

Previous\_Disruptions – many past disruptions hint at instability.

Delivery\_Quality\_Index – a low quality score means inconsistent performance

Supplier\_Dependency\_Score – high dependency means the business is heavily exposed to this supplier.





“SupplierIQ predicts high risk when key indicators look weak.

A supplier is more likely to be flagged as high risk if it has low financial stability, poor on-time delivery, high defect rates, a history of disruptions, or operates in high geopolitical risk regions.

The model looks at these factors together to estimate the chance that the supplier will cause future delays or quality issues.”







Interview answers 

You can practice with these Q\&A:



Q: How does your model explain why a supplier is risky?

A: “We use feature importance to show which variables influence the risk score most. For a given supplier, we highlight the key drivers, such as low financial stability or high defect rate, so business users can see why the model flagged that supplier.”



Q: Which features are most important in SupplierIQ?

A: “The top drivers are financial stability, on-time delivery, defect rate, previous disruptions, and geopolitical risk. These align with how procurement already thinks about supplier risk.”



Q: How do you communicate model results to non-technical stakeholders?

A: “We avoid equations and show a simple explanation: a risk score, a traffic-light label (low/medium/high), and a list of the top 3–5 contributing features with plain-language descriptions.”



Q: How do you ensure the model is not a ‘black box’?

A: “We expose feature importance, show per-supplier drivers, and keep the model relatively interpretable (Logistic Regression + Random Forest) so we can explain patterns rather than just giving a number.”



Q: What if the model flags a supplier as high risk but business users disagree?

A: “We treat the model as an early warning tool, not a final decision. Users can review the drivers, add context we don’t have in the data, and then override or confirm the suggestion.”

