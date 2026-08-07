&#x20;**Correlation Summary**



\- Most features have very weak correlation with each other, so they capture different parts of supplier risk.

\- The strongest positive relationship is between On\_Time\_Delivery\_Rate and Delivery\_Quality\_Index, which means better delivery performance is closely linked with better delivery quality.

\- The strongest negative relationship is between Alternative\_Suppliers\_Available and Supplier\_Dependency\_Score, which means more backup suppliers usually means lower dependency risk.

\- Defect\_Rate has a mild negative relationship with Delivery\_Quality\_Index, so higher defect rates tend to reduce delivery quality.

\- Financial\_Stability\_Score, Geopolitical\_Risk\_Index, Lead\_Time\_Days, Contract\_Length\_Months, Environmental\_Compliance, and Previous\_Disruptions mostly show weak relationships with other columns.

\- Overall, the heatmap suggests that the dataset has a few strong patterns but most features are fairly independent.





**-Unusual suppliers and outliers**

* Financial\_Stability\_Score: Mostly around 50–65, with outliers on both low and high sides.
* On\_Time\_Delivery\_Rate: Mostly high, around 70–85, with some lower outliers around the 30s–40s.
* Defect\_Rate: Mostly low, around 3–7, with a few higher outliers near 15–20.
* Geopolitical\_Risk\_Index: Mostly around 30–45, with a few high outliers near 80–90.
* Lead\_Time\_Days: Mostly around 20–35, with many high outliers around 65–85.
* Alternative\_Suppliers\_Available: Mostly around 0–3, with a few higher outliers near 6–10.
* Contract\_Length\_Months: Mostly around 10–25, with some high outliers around 40–60.
* Environmental\_Compliance: Mostly around 60–85, with some low outliers near 0–20.\\
* Previous\_Disruptions: Mostly 0–1, with a few higher outliers around 4–6.
* Delivery\_Quality\_Index: Mostly around 65–85, with some lower outliers around 30–45.
* Supplier\_Dependency\_Score: Mostly very low, around 0.1–0.3, with a few high outliers near 1.0.







**Final 8 columns to be useful**

***On\_Time\_Delivery\_Rate: a strong indicator of supplier reliability and delay risk.***

***Delivery\_Quality\_Index: captures delivery quality issues that affect operations.***

***Financial\_Stability\_Score: useful for identifying suppliers likely to fail or become unstable.***

***Previous\_Disruptions: past problems often predict future problems.***

***Supplier\_Dependency\_Score: high dependency increases business risk.***

***Geopolitical\_Risk\_Index: external instability can disrupt supply.***

***Lead\_Time\_Days: longer lead times usually mean slower response and higher disruption risk.***

***Defect\_Rate: direct signal of quality problems.***





**-First business insights**



***Delivery performance matters a lot***: On\_Time\_Delivery\_Rate and Delivery\_Quality\_Index look very useful because they are directly tied to supplier reliability and clearly separate normal from unusual suppliers.



***Risk signal columns are strong***: Financial\_Stability\_Score, Geopolitical\_Risk\_Index, Previous\_Disastrions/Previous\_Disruptions, and Supplier\_Dependency\_Score look useful because unusual values in these columns may indicate supplier risk.



***Operational risk columns are also important***: Lead\_Time\_Days, Defect\_Rate, Contract\_Length\_Months, and Alternative\_Suppliers\_Available can help identify suppliers that may cause delays, quality issues, or dependency problems.



***Environmental and compliance factors matter***: Environmental\_Compliance appears useful because unusually low values may signal policy, regulatory, or reputational risk.













**-CORRELATION DATA**



&#x20;                                 Financial\_Stability\_Score  \\

Financial\_Stability\_Score                         1.000000   

On\_Time\_Delivery\_Rate                            -0.018636   

Defect\_Rate                                      -0.000686   

Geopolitical\_Risk\_Index                           0.042657   

Lead\_Time\_Days                                    0.001245   

Alternative\_Suppliers\_Available                  -0.013482   

Contract\_Length\_Months                            0.021826   

Environmental\_Compliance                         -0.016818   

Previous\_Disruptions                              0.032813   

Delivery\_Quality\_Index                           -0.017895   

Supplier\_Dependency\_Score                         0.010955   



&#x20;                                On\_Time\_Delivery\_Rate  Defect\_Rate  \\

Financial\_Stability\_Score                    -0.018636    -0.000686   

On\_Time\_Delivery\_Rate                         1.000000    -0.005394   

Defect\_Rate                                  -0.005394     1.000000   

Geopolitical\_Risk\_Index                      -0.004278    -0.002780   

Lead\_Time\_Days                                0.008205    -0.005010   

Alternative\_Suppliers\_Available              -0.009028     0.010013   

Contract\_Length\_Months                       -0.000286    -0.000715   

Environmental\_Compliance                     -0.002166     0.000145   

Previous\_Disruptions                          0.002214    -0.004503   

Delivery\_Quality\_Index                        0.975391    -0.225226   

Supplier\_Dependency\_Score                     0.000887    -0.008098   



&#x20;                                Geopolitical\_Risk\_Index  Lead\_Time\_Days  \\

Financial\_Stability\_Score                       0.042657        0.001245   

On\_Time\_Delivery\_Rate                          -0.004278        0.008205   

Defect\_Rate                                    -0.002780       -0.005010   

Geopolitical\_Risk\_Index                         1.000000       -0.002710   

Lead\_Time\_Days                                 -0.002710        1.000000   

Alternative\_Suppliers\_Available                 0.017400       -0.015562   

Contract\_Length\_Months                         -0.012436        0.002972   

Environmental\_Compliance                        0.013218        0.002962   

Previous\_Disruptions                           -0.008729       -0.005569   

Delivery\_Quality\_Index                         -0.003648        0.008899   

Supplier\_Dependency\_Score                      -0.021226        0.011680   



&#x20;                                Alternative\_Suppliers\_Available  \\

Financial\_Stability\_Score                              -0.013482   

On\_Time\_Delivery\_Rate                                  -0.009028   

Defect\_Rate                                             0.010013   

Geopolitical\_Risk\_Index                                 0.017400   

Lead\_Time\_Days                                         -0.015562   

Alternative\_Suppliers\_Available                         1.000000   

Contract\_Length\_Months                                  0.003551   

Environmental\_Compliance                               -0.017583   

Previous\_Disruptions                                    0.010171   

Delivery\_Quality\_Index                                 -0.011036   

Supplier\_Dependency\_Score                              -0.827211   



&#x20;                                Contract\_Length\_Months  \\

Financial\_Stability\_Score                      0.021826   

On\_Time\_Delivery\_Rate                         -0.000286   

Defect\_Rate                                   -0.000715   

Geopolitical\_Risk\_Index                       -0.012436   

Lead\_Time\_Days                                 0.002972   

Alternative\_Suppliers\_Available                0.003551   

Contract\_Length\_Months                         1.000000   

Environmental\_Compliance                       0.002388   

Previous\_Disruptions                          -0.006684   

Delivery\_Quality\_Index                        -0.000024   

Supplier\_Dependency\_Score                     -0.004115   



&#x20;                                Environmental\_Compliance  \\

Financial\_Stability\_Score                       -0.016818   

On\_Time\_Delivery\_Rate                           -0.002166   

Defect\_Rate                                      0.000145   

Geopolitical\_Risk\_Index                          0.013218   

Lead\_Time\_Days                                   0.002962   

Alternative\_Suppliers\_Available                 -0.017583   

Contract\_Length\_Months                           0.002388   

Environmental\_Compliance                         1.000000   

Previous\_Disruptions                             0.005943   

Delivery\_Quality\_Index                          -0.002438   

Supplier\_Dependency\_Score                        0.024470   



&#x20;                                Previous\_Disruptions  Delivery\_Quality\_Index 

Financial\_Stability\_Score                    0.032813               -0.017895   

On\_Time\_Delivery\_Rate                        0.002214                0.975391   

Defect\_Rate                                 -0.004503               -0.225226   

Geopolitical\_Risk\_Index                     -0.008729               -0.003648   

Lead\_Time\_Days                              -0.005569                0.008899   

Alternative\_Suppliers\_Available              0.010171               -0.011036   

Contract\_Length\_Months                      -0.006684               -0.000024   

Environmental\_Compliance                     0.005943               -0.002438   

Previous\_Disruptions                         1.000000                0.003151   

Delivery\_Quality\_Index                       0.003151                1.000000   

Supplier\_Dependency\_Score                   -0.008634                0.002696   



&#x20;                                Supplier\_Dependency\_Score  

Financial\_Stability\_Score                         0.010955  

On\_Time\_Delivery\_Rate                             0.000887  

Defect\_Rate                                      -0.008098  

Geopolitical\_Risk\_Index                          -0.021226  

Lead\_Time\_Days                                    0.011680  

Alternative\_Suppliers\_Available                  -0.827211  

Contract\_Length\_Months                           -0.004115  

Environmental\_Compliance                          0.024470  

Previous\_Disruptions                             -0.008634  

Delivery\_Quality\_Index                            0.002696  

Supplier\_Dependency\_Score                         1.000000  







