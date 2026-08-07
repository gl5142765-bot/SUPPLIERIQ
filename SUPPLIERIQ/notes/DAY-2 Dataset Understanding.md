The dataset has 28,100 rows and 17 columns, so each row appears to represent one supplier record.

The target column is (Risk_Level), which means this is a classification problem.

The main input columns include both categorical features like Country, Region, Industry, and Supplier_Tier and numerical features like Financial_Stability_Score, On_Time_Delivery_Rate, and Lead_Time_Days.

Supplier_ID is an ID column, so it should not be used as a model feature.

A few columns have small missing values: Financial_Stability_Score, On_Time_Delivery_Rate, Defect_Rate, Lead_Time_Days, Environmental_Compliance, and Previous_Disruptions.

There are 3447 duplicate rows, which should be fixed for data quality.

Overall, the dataset looks suitable for further cleaning, EDA, and modelling.
