-- E-Commerce Sales Prediction - Hive Processing

CREATE DATABASE ecommerce_db;

USE ecommerce_db;

CREATE EXTERNAL TABLE ecommerce_sales (
    InvoiceNo STRING,
    StockCode STRING,
    Description STRING,
    Quantity BIGINT,
    InvoiceDate STRING,
    UnitPrice DOUBLE,
    CustomerID DOUBLE,
    Country STRING,
    Revenue DOUBLE,
    Year INT,
    Month INT,
    Day INT,
    DayOfWeek STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\"",
    "escapeChar" = "\\"
)
STORED AS TEXTFILE
LOCATION '/data/ecommerce/raw'
TBLPROPERTIES ("skip.header.line.count" = "1");

SHOW TABLES;

SELECT *
FROM ecommerce_sales
LIMIT 5;

SELECT Country, SUM(Revenue) AS Total_Revenue
FROM ecommerce_sales
GROUP BY Country
ORDER BY Total_Revenue DESC
LIMIT 10;

SELECT Year, Month,
       SUM(Quantity) AS Total_Quantity,
       SUM(Revenue) AS Total_Revenue
FROM ecommerce_sales
GROUP BY Year, Month
ORDER BY Year, Month;