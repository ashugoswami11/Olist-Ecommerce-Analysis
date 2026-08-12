# E-Commerce Customer Insights & Sales Intelligence Platform

**Dataset:** Olist Brazilian E-Commerce — Kaggle
**Tools:** Python, Pandas, SQL, SQLite, Seaborn, Matplotlib, Power BI

---

## Problem Statement
Olist is a Brazilian e-commerce company with 100,000+ orders data spread across 9 tables. The goal was to clean this raw messy data, analyze it using SQL, visualize patterns using Python, and build an interactive Power BI dashboard to help business stakeholders make data-driven decisions.

---

## Project Structure
```
Ecommerce-Project/
├── Raw_data/         → original 9 CSV files
├── cleaned_data/     → 9 cleaned CSV files
├── kpi_calculation/  → SQL queries + KPI results
├── eda/              → EDA script + 7 charts
├── dashboard/        → Power BI .pbix + screenshot
└── README.md
```

---

## Phase 1 — Data Cleaning
- Loaded 9 CSV files with 1M+ rows using Python and Pandas
- Fixed wrong data types — converted 7 date columns to datetime64
- Dropped 3 invalid payment rows with zero value
- Filled 610 missing product categories with 'unknown'
- Fixed 2 column name typos in products table
- Removed 261,831 duplicate zip codes from geolocation table
- Saved all 9 cleaned files separately

---

## Phase 2 — SQL KPI Analysis
Loaded cleaned data into SQLite and wrote 9 KPI queries:

| KPI | Result |
|---|---|
| Total Revenue | R$ 16,008,872 |
| Average Order Value | R$ 154.10 |
| Avg Delivery Days | 12.50 days |
| Late Delivery Rate | 8.11% |
| Avg Review Score | 4.09 / 5 |
| Top Category | Health & Beauty |
| Top State | São Paulo (40% orders) |

---

## Phase 3 — Exploratory Data Analysis
Built 7 Seaborn charts:
- Monthly Revenue Trend — 20x growth from 2016 to 2018
- Top 10 Product Categories by Revenue
- Review Score Distribution
- Late vs On-Time Delivery Rate
- Order Status Distribution
- Freight vs Price Correlation
- Top 10 States by Orders

---

## Phase 4 — Power BI Dashboard
Built 3-page interactive dashboard:

**Page 1 — Sales Overview**
- Total Revenue, Total Orders, AOV cards
- Monthly Revenue Trend line chart
- Top 10 Categories bar chart
- Date range slicer + Order status slicer

**Page 2 — Customer Insights**
- Total Customers, Avg Review Score, Total Reviews cards
- Review Score Distribution bar chart
- Top 10 States by Orders bar chart

**Page 3 — Operational Performance**
- Avg Delivery Days, Late Delivery Rate cards
- Top 10 Sellers by Revenue bar chart
- Order Status Distribution donut chart

---

## Key Findings
- Total revenue of R$16M generated in 2 years
- 20x revenue growth from 2016 to 2018
- Black Friday 2017 was the single highest revenue month
- Health & Beauty is the top earning category at R$1.25M
- 8.11% orders delivered late — directly causing 1 star reviews
- Sao Paulo accounts for 40% of all orders
- Average delivery time is 12.5 days

---

## Business Recommendations
1. Focus more on Health & Beauty category
2. Fix late deliveries to improve review scores
3. Start a loyalty program to bring customers back
4. Target other states beyond Sao Paulo
5. Prepare inventory and logistics for Black Friday every year
