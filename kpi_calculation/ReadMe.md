## **SQL KPI ANALYSIS**



1. loaded all 9 cleaned csv files into a SQLite database called olist.db using sqlite3 and pandas to\_sql() — this allows us to run SQL queries directly on our cleaned data from Python

2\. created a kpi\_results folder to store all query outputs as individual csv files for later use in Power BI and README



KPI 1 — Total Revenue

queried SUM(payment\_value) from payments table — total revenue across all orders came out to R$ 16,008,872.12



KPI 2 — Average Order Value (AOV)

queried AVG(payment\_value) from payments table — gives the average amount a customer spends per order 



KPI 3 — Monthly Revenue Trend

joined orders and payments table on order\_id, filtered only delivered orders, used strftime() to extract year-month from order\_purchase\_timestamp, grouped by month to see revenue growth over time



KPI 4 — Top 10 Product Categories by Revenue

joined order\_items, products and category\_translation tables to get english category names, grouped by category and summed price, ordered by revenue descending and limited to top 10



KPI 5 — Customer Repeat Rate

used a subquery to find customers who placed more than one order by grouping on customer\_unique\_id and using HAVING COUNT > 1, divided by total unique customers to get repeat rate percentage



KPI 6 — Late Delivery Rate

used a CASE WHEN statement to flag orders where order\_delivered\_customer\_date was greater than order\_estimated\_delivery\_date, divided by total delivered orders to get late delivery rate percentage



KPI 7 — Review Score Distribution

grouped reviews by review\_score and counted total reviews per score, also calculated percentage share of each score out of total reviews



KPI 8 — Top 10 Sellers by Revenue

joined order\_items and sellers table on seller\_id, grouped by seller and summed price, ordered by revenue descending and limited to top 10 — also pulled seller city and state for context



KPI 9 — Average Delivery Days

used JULIANDAY() function to calculate the difference in days between order\_purchase\_timestamp and order\_delivered\_customer\_date, averaged across all delivered orders to get typical delivery time in days

