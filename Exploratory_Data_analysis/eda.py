import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load KPI results
monthly_revenue = pd.read_csv('kpi_results/kpi_monthly_revenue.csv')
top_categories = pd.read_csv('kpi_results/kpi_top_categories.csv')
review_dist = pd.read_csv('kpi_results/kpi_review_distribution.csv')

# Load cleaned tables
orders = pd.read_csv('orders_clean.csv')
order_items = pd.read_csv('order_items_clean.csv')
customers = pd.read_csv('customers_clean.csv')

# Output folder
os.makedirs('eda_plots', exist_ok=True)

# Global style
sns.set_theme(style='whitegrid')

# Chart 1 - Monthly Revenue Trend
plt.figure(figsize=(14, 5))
sns.lineplot(data=monthly_revenue, x='month', y='monthly_revenue', marker='o', color='steelblue')
plt.title('Monthly Revenue Trend', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Revenue (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('eda_plots/01_monthly_revenue_trend.png', dpi=150)
plt.show()


# Chart 2 - Top 10 Product Categories by Revenue
plt.figure(figsize=(12, 6))
sns.barplot(data=top_categories, x='total_revenue', y='category', palette='Blues_r')
plt.title('Top 10 Product Categories by Revenue', fontsize=16)
plt.xlabel('Total Revenue (R$)')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('eda_plots/02_top_categories.png', dpi=150)
plt.show()


# Chart 3 - Review Score Distribution
plt.figure(figsize=(8, 5))
sns.barplot(data=review_dist, x='review_score', y='total_reviews', palette='RdYlGn')
plt.title('Review Score Distribution', fontsize=16)
plt.xlabel('Review Score')
plt.ylabel('Total Reviews')
plt.tight_layout()
plt.savefig('eda_plots/03_review_distribution.png', dpi=150)
plt.show()

# Chart 4 - Late vs On-Time Deliveries
late_delivery = pd.read_csv('kpi_results/kpi_late_delivery_rate.csv')
delivery_data = pd.DataFrame({
    'delivery_status': ['On Time', 'Late'],
    'percentage': [100 - late_delivery['late_delivery_rate_percent'].values[0],
                   late_delivery['late_delivery_rate_percent'].values[0]]
})
plt.figure(figsize=(7, 5))
sns.barplot(data=delivery_data, x='delivery_status', y='percentage', palette=['steelblue', 'tomato'])
plt.title('Late vs On-Time Delivery Rate', fontsize=16)
plt.xlabel('Delivery Status')
plt.ylabel('Percentage (%)')
plt.tight_layout()
plt.savefig('eda_plots/04_delivery_rate.png', dpi=150)
plt.show()

# Chart 5 - Order Status Distribution
plt.figure(figsize=(10, 5))
order_status = orders['order_status'].value_counts().reset_index()
order_status.columns = ['order_status', 'count']
sns.barplot(data=order_status, x='order_status', y='count', palette='Blues_r')
plt.title('Order Status Distribution', fontsize=16)
plt.xlabel('Order Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('eda_plots/05_order_status.png', dpi=150)
plt.show()

# Chart 6 - Freight vs Price Correlation
plt.figure(figsize=(8, 5))
sns.scatterplot(data=order_items.sample(5000), x='price', y='freight_value', alpha=0.4, color='steelblue')
plt.title('Freight Value vs Product Price', fontsize=16)
plt.xlabel('Product Price (R$)')
plt.ylabel('Freight Value (R$)')
plt.tight_layout()
plt.savefig('eda_plots/06_freight_vs_price.png', dpi=150)
plt.show()

# Chart 7 - Top 10 States by Orders
plt.figure(figsize=(10, 5))
top_states = customers['customer_state'].value_counts().head(10).reset_index()
top_states.columns = ['state', 'order_count']
sns.barplot(data=top_states, x='state', y='order_count', palette='Blues_r')
plt.title('Top 10 States by Number of Orders', fontsize=16)
plt.xlabel('State')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('eda_plots/07_top_states.png', dpi=150)
plt.show()