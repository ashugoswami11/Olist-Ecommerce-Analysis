import pandas as pd
import sqlite3
import os

# Load cleaned CSVs
orders = pd.read_csv('orders_clean.csv')
customers = pd.read_csv('customers_clean.csv')
order_items = pd.read_csv('order_items_clean.csv')
payments = pd.read_csv('payments_clean.csv')
reviews = pd.read_csv('reviews_clean.csv')
products = pd.read_csv('products_clean.csv')
sellers = pd.read_csv('sellers_clean.csv')
category_translation = pd.read_csv('category_translation_clean.csv')
geolocation = pd.read_csv('geolocation_clean.csv')

# Push to SQLite
conn = sqlite3.connect('olist.db')

orders.to_sql('orders', conn, if_exists='replace', index=False)
customers.to_sql('customers', conn, if_exists='replace', index=False)
order_items.to_sql('order_items', conn, if_exists='replace', index=False)
payments.to_sql('payments', conn, if_exists='replace', index=False)
reviews.to_sql('reviews', conn, if_exists='replace', index=False)
products.to_sql('products', conn, if_exists='replace', index=False)
sellers.to_sql('sellers', conn, if_exists='replace', index=False)
category_translation.to_sql('category_translation', conn, if_exists='replace', index=False)
geolocation.to_sql('geolocation', conn, if_exists='replace', index=False)

print("All tables loaded successfully!")

#to store kpi results
os.makedirs('kpi_results', exist_ok=True)

# kpi_1 total_revenue
query = """
SELECT ROUND(SUM(payment_value), 2) AS total_revenue
FROM payments
"""

result = pd.read_sql_query(query, conn)
result.to_csv('kpi_results/kpi_total_revenue.csv', index=False)


# kpi_2 average_order_value
query = """
SELECT ROUND(AVG(payment_value), 2) AS avg_order_value
FROM payments
"""

result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_avg_order_value.csv', index=False)


# KPI 3 - Monthly Revenue Trend
query = """
SELECT 
    strftime('%Y-%m', order_purchase_timestamp) AS month,
    ROUND(SUM(payment_value), 2) AS monthly_revenue
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE order_status = 'delivered'
GROUP BY month
ORDER BY month
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_monthly_revenue.csv', index=False)


# KPI 4 - Top 10 Product Categories by Revenue
query = """
SELECT 
    ct.product_category_name_english AS category,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN category_translation ct ON p.product_category_name = ct.product_category_name
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 10
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_top_categories.csv', index=False)

# KPI 5 - Customer Repeat Rate
query = """
SELECT 
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(DISTINCT customer_unique_id) FROM customers), 2) AS repeat_rate_percent
FROM (
    SELECT c.customer_unique_id
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
    HAVING COUNT(o.order_id) > 1
)
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_repeat_rate.csv', index=False)

# KPI 6 - Late Delivery Rate
query = """
SELECT 
    ROUND(100.0 * SUM(CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS late_delivery_rate_percent
FROM orders
WHERE order_status = 'delivered'
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_late_delivery_rate.csv', index=False)

# KPI 7 - Review Score Distribution
query = """
SELECT 
    review_score,
    COUNT(*) AS total_reviews,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM reviews), 2) AS percentage
FROM reviews
GROUP BY review_score
ORDER BY review_score DESC
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_review_distribution.csv', index=False)

# KPI 8 - Top 10 Sellers by Revenue
query = """
SELECT 
    oi.seller_id,
    s.seller_city,
    s.seller_state,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM order_items oi
JOIN sellers s ON oi.seller_id = s.seller_id
GROUP BY oi.seller_id
ORDER BY total_revenue DESC
LIMIT 10
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_top_sellers.csv', index=False)

# KPI 9 - Average Delivery Days
query = """
SELECT 
    ROUND(AVG(JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp)), 1) AS avg_delivery_days
FROM orders
WHERE order_status = 'delivered'
"""
result = pd.read_sql_query(query, conn)
print(result)
result.to_csv('kpi_results/kpi_avg_delivery_days.csv', index=False)
