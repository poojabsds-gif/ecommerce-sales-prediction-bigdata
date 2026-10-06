\# E-Commerce Sales Prediction Using Big Data Analytics



\## 1. Project Overview



This project is a Big Data Analytics solution for analyzing historical e-commerce transactions and predicting daily sales revenue.



The project uses the HCL GUVI × JAIN University Big Data Analytics technology stack, including HDFS, Hive, Spark/PySpark and HBase.



The main objective is to identify sales and demand patterns from historical e-commerce transactions and build a machine learning model for daily sales revenue prediction.



\---



\## 2. Business Problem



E-commerce businesses generate large volumes of transaction data containing information about products, quantities, prices, customers and countries.



Analyzing this historical data can help identify:



\- Sales patterns

\- High-performing countries

\- Monthly demand patterns

\- Daily revenue trends

\- Historical sales relationships

\- Future daily revenue estimates



The project therefore focuses on processing historical e-commerce transaction data using a Big Data architecture and building a sales prediction model.



\---



\## 3. Dataset



\### Dataset



UCI Online Retail II



\### Source



UCI Machine Learning Repository, Online Retail II, Dataset ID 502.



\### Original columns



\- Invoice

\- StockCode

\- Description

\- Quantity

\- InvoiceDate

\- Price

\- Customer ID

\- Country



\### Combined dataset



The two available yearly sheets were combined.



Total original records:



1,067,371



Date range:



2009-12-01 to 2011-12-09



\---



\## 4. Data Cleaning



The raw Excel dataset was preserved locally and the two yearly sheets were combined.



The following cleaning operations were performed:



1\. Removed exact duplicate rows.

2\. Removed cancelled invoice transactions.

3\. Removed transactions with Quantity <= 0.

4\. Removed transactions with UnitPrice <= 0.

5\. Removed missing descriptions where applicable.

6\. Removed invalid dates.

7\. Created Revenue = Quantity × UnitPrice.

8\. Created Year, Month, Day and DayOfWeek features.



\### Cleaning results



| Measure | Result |

|---|---:|

| Original records | 1,067,371 |

| Duplicate rows removed | 34,335 |

| Cancelled invoice rows removed | 19,104 |

| Invalid quantity rows removed | 3,393 |

| Invalid price rows removed | 2,626 |

| Missing description rows removed | 0 |

| Invalid date rows removed | 0 |

| Final records | 1,007,913 |



The final cleaned dataset contains 1,007,913 transaction records and 13 columns.



CustomerID missing values were retained because CustomerID is not mandatory for the sales and demand prediction objective.



\---



\## 5. Big Data Architecture



The project follows this processing flow:



UCI Online Retail II

&#x20;       |

&#x20;       v

Data Cleaning and Transformation

&#x20;       |

&#x20;       v

HDFS

&#x20;       |

&#x20;       +----------------+

&#x20;       |                |

&#x20;       v                v

&#x20;     Hive             Spark

&#x20;       |                |

&#x20;       |                v

&#x20;       |       Feature Engineering

&#x20;       |                |

&#x20;       |                v

&#x20;       |       Machine Learning

&#x20;       |                |

&#x20;       |                v

&#x20;       |        Random Forest

&#x20;       |                |

&#x20;       +--------+-------+

&#x20;                |

&#x20;                v

&#x20;              HBase

&#x20;                |

&#x20;                v

&#x20;       Prediction Results



\### Technology roles



| Technology | Purpose |

|---|---|

| HDFS | Distributed storage of the cleaned dataset |

| Hive | SQL-based data modeling and analytics |

| Spark/PySpark | Distributed processing and machine learning |

| HBase | Key-based storage and retrieval of selected prediction results |

| Git/GitHub | Version control and project reproducibility |



\---



\## 6. HDFS Data Ingestion



The cleaned dataset was transferred through the required workflow:



Jupyter container

&#x20;   -> Windows host

&#x20;   -> NameNode container

&#x20;   -> HDFS



HDFS location:



/data/ecommerce/raw/cleaned\_online\_retail.csv



The dataset was verified using:



hdfs dfs -ls /data/ecommerce/raw



\---



\## 7. Hive Processing



Hive database:



ecommerce\_db



Hive table:



ecommerce\_sales



The table is an external table whose data is stored in the HDFS location:



/data/ecommerce/raw



Example analytics performed using Hive:



\- Country-wise revenue

\- Monthly quantity

\- Monthly revenue

\- Sample transaction retrieval



\### Top revenue countries



The United Kingdom generated the highest revenue in the analyzed dataset, followed by EIRE, Netherlands, Germany and France.



\### Monthly analysis



The monthly analysis showed stronger sales activity during October and November, with November showing particularly high revenue and transaction quantities.



\---



\## 8. Spark/PySpark Processing



Spark 3.1.1 was used to read the cleaned dataset directly from HDFS.



HDFS input:



hdfs://namenode:8020/data/ecommerce/raw/cleaned\_online\_retail.csv



Records processed:



1,007,913



Daily sales were generated by aggregating transaction quantity and revenue by transaction date.



\---



\## 9. Feature Engineering



Historical sales features were created for prediction:



\- Lag\_1\_Day

\- Lag\_7\_Days

\- Lag\_14\_Days

\- Rolling\_7\_Day\_Avg

\- DayOfWeek\_Num

\- Month\_Num

\- Year\_Num



The prediction target was:



Daily\_Revenue



The data was divided chronologically rather than randomly.



\### Training data



472 records



Period:



2009-12-16 to 2011-07-24



\### Testing data



118 records



Period:



2011-07-25 to 2011-12-09



This ensures that the model is evaluated on later unseen transaction days.



\---



\## 10. Machine Learning Models



Three regression approaches were evaluated.



| Model | RMSE | MAE | R2 |

|---|---:|---:|---:|

| Linear Regression - Baseline | 23093.76 | 15123.67 | 0.1651 |

| Linear Regression - Improved | 22048.02 | 14570.02 | 0.2390 |

| Random Forest Regression | 21114.17 | 12645.95 | 0.3021 |



\### Best model



Random Forest Regression produced the best results among the evaluated models.



RMSE:



21,114.17



MAE:



12,645.95



R2:



0.3021



The Random Forest model explains approximately 30.2% of the variation in unseen test-period daily revenue.



R2 is not interpreted as prediction accuracy.



\---



\## 11. HBase Integration



HBase was used as the advanced technology component.



Table:



ecommerce\_daily\_sales



Column family:



sales



Row key:



SalesDate



Stored values:



\- sales:actual\_revenue

\- sales:predicted\_revenue



Selected prediction results generated by Spark were stored in HBase.



Example:



2011-07-25

Actual Revenue: 26876.39

Predicted Revenue: 33936.75



2011-07-26

Actual Revenue: 21635.56

Predicted Revenue: 44368.80



HBase therefore provides a key-based storage layer for retrieving daily prediction results using the sales date.



\---



\## 12. Project Structure



```text

ecommerce-sales-prediction-bigdata/

|

|-- advanced/

|   |-- hbase\_commands.txt

|

|-- docs/

|   |-- data\_quality\_check.py

|   |-- clean\_dataset.py

|   |-- validate\_clean\_data.py

|

|-- hdfs/

|   |-- hdfs\_commands.txt

|

|-- hive/

|   |-- hive\_queries.sql

|

|-- results/

|   |-- data\_cleaning\_report.txt

|   |-- model\_comparison.csv

|

|-- spark/

|   |-- spark\_analysis.txt

|

|-- presentation/

|

|-- .gitignore

|-- README.md

