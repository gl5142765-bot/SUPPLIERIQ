*# Day 3 Numeric Summary Notes and Plot Distribution*



**Financial\_Stability\_Score**

\- Most suppliers have financial stability scores around the mid-50s to mid-60s.

\- The values are fairly spread out, so suppliers differ a lot in financial strength.

\- Scores range from very low to 100, which means some suppliers look financially weak while others look very strong.



Clustered: mostly around 55 to 65.

Leaning: almost balanced, maybe a slight right skew.

Extreme values: no major outliers; only a few low and high values.



&#x20;**On\_Time\_Delivery\_Rate**

\- Most suppliers have on-time delivery rates around the high 70s.

\- The values show moderate variation, so delivery performance is not the same for all suppliers.

\- The range goes from about 31 to 100, which means some suppliers deliver poorly while others are highly reliable.



Clustered: mostly around 70 to 78

Leaning: mostly towards right skew

Extreme values: a sudden rise in high value -100







&#x20;**Defect\_Rate**

\- Most suppliers have defect rates around 4 to 7.

\- The values vary across suppliers, so product or service quality is not consistent for everyone.

\- The range starts at 0 and goes up to about 19, which suggests a few suppliers may have much higher quality problems.



Clustered: mostly around 4.5 to 5.5 

Leaning: fully towards the left

Extreme values: rise of low value - 0.0 



&#x20;**Geopolitical\_Risk\_Index**

\- Many suppliers fall around the low 30s, but some are much higher.

\- The spread is wide, so suppliers operate in regions with very different levels of geopolitical risk.

\- The range from 11 to 87 shows that some suppliers are in stable areas while others may be exposed to serious external risk.



Clustered: mostly around 30 to 35

Leaning: mostly towards left skew

Extreme values:  31 has the most values



&#x20;**Lead\_Time\_Days**

\- Typical lead time is around 25 days.

\- The values are quite spread out, so supplier delivery time differs a lot.

\- The range from 0 to 88 days shows that some suppliers respond very quickly while others take much longer.



Clustered: mostly around 24 to 36

Leaning: mostly towards left skew

Extreme values: 0 value has a rise, and the highest is somewhere 28 -32.



&#x20;**Alternative\_Suppliers\_Available**

\- Most suppliers have around 1 to 4 alternative suppliers available.

\- The values are moderately spread, so backup options are stronger for some suppliers than others.

\- The range from 0 to 10 shows that some suppliers have no backup options, which can increase dependency risk.



Clustered: mostly around 2 to 4.

Leaning: right-skewed.

Extreme values: a few values near 8 to 10, but not many.





**Contract\_Length\_Months**

Most supplier contracts are around 19 months long.

The values vary a lot, so contract lengths are not the same for every supplier.

The range from 1 to 68 months shows that some suppliers have very short contracts while others have long-term agreements.



Clustered: mostly around 15 to 25 months.

Leaning: right skewed.

Extreme values: a few long contracts near 50 to 68 months.



**Environmental\_Compliance**

Most suppliers score around the low 70s on environmental compliance.

The values are spread across a wide range, so some suppliers are much better than others.

The range from about 1.5 to 100.95 shows that some suppliers may have very weak compliance while others are highly compliant.



Clustered: mostly around 72 to 78.

Leaning: almost towards the right

Extreme values:  100, a sudden rise.





**Previous\_Disruptions**

Most suppliers have had around 0 to 1 previous disruption.

The values are low for many suppliers, so past issues are not very common in the dataset.

The range from 0 to 6 shows that a small number of suppliers have faced repeated disruptions.





Clustered: mostly around 0 and 1, with some at 2.

Leaning: right-skewed.

Extreme values: a few values at 4 to 5, but very few. 



**Delivery\_Quality\_Index**

Most suppliers have delivery quality scores around the mid 70s.

The values are fairly spread out, so delivery quality is not equal across all suppliers.

The range from about 30 to 100 shows that some suppliers perform much better than others.



Clustered: mostly around 70 to 80

Leaning: mostly right-skewed

Extreme values: some values in 60-70 and a few in 80 -100



**Supplier\_Dependency\_Score**

Most suppliers have dependency scores around 0.2 to 0.5.

The values are concentrated in the lower range, so many suppliers are not extremely dependent.

The range from about 0.09 to 1.0 shows that some suppliers are much more critical than others.



Clustered: mostly around 0.15 to 0.35.

Leaning: right-skewed.

Extreme values: a few suppliers are near 1.0, which are very high dependency cases.







***The target classes are imbalanced.***



Class 1 has 19,673 records, which is about 70.0%.

Class 0 has 8,425 records, which is about 30.0%.



***Short observation***

Most of the dataset belongs to class 1, so the model may learn that class more easily. This means we should be careful when evaluating performance, because accuracy alone may be misleading.







