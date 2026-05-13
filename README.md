# Strategic Sales Performance Dashboard

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoftpowerbi&logoColor=black)](https://powerbi.microsoft.com/)

A production-quality, end-to-end sales analytics platform designed for enterprise-level strategic decision-making. This project demonstrates a complete data lifecycle: from synthetic data generation and ETL to SQL optimization and executive-level visualization.

## 🚀 Project Overview

This repository contains a full-stack data analytics solution that replaces manual Excel reporting with an automated, scalable pipeline.

### Core Features
- **Scalable Star Schema:** Normalized PostgreSQL design for high-performance analytical queries.
- **Automated ETL:** Python-based pipeline for data extraction, cleaning, and loading.
- **Realistic Dataset:** 12,000+ transactions with seasonality, regional trends, and profitability logic.
- **Advanced SQL:** Use of CTEs, Window Functions, and Materialized Views for complex KPI calculations.
- **Executive Insights:** Automated Python reports and Power BI dashboard design guidance.

## 🏗️ Architecture

```mermaid
graph LR
    A[Faker Data Gen] --> B[(Raw CSVs)]
    B --> C[Python ETL]
    C --> D[(PostgreSQL)]
    D --> E[SQL KPI Layer]
    E --> F[Python Reports]
    E --> G[Power BI Dashboard]
```

## 📂 Repository Structure

- `data/`: Raw and processed data files (CSVs).
- `sql/`: Database schema, seeds, and optimized analytical queries.
- `python/`: Scripts for data generation, ETL, and automated analytics.
- `dashboard/`: Power BI design files and dashboard mockups.
- `docs/`: Detailed architecture and business requirements.
- `reports/`: Automated visualizations (PNGs).

## 🛠️ Tech Stack
- **Database:** PostgreSQL
- **Language:** Python (Pandas, SQLAlchemy, Psycopg2, Faker)
- **Visualization:** Matplotlib, Power BI
- **Environment:** Docker-ready, modular architecture

## 📊 Key KPIs Tracked
1. **Total Revenue & Profit:** Overall financial health.
2. **Profit Margin %:** Operating efficiency across categories.
3. **Year-over-Year (YoY) Growth:** Historical performance comparison.
4. **Regional Sales Distribution:** Identifying top and bottom performing markets.
5. **Product Performance:** Top 10 products by revenue and profit.

## 🚦 Getting Started

### 1. Prerequisites
- Python 3.8+
- PostgreSQL instance

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline
```bash
# Initialize database schema
psql "postgresql://sales_admin:admin123@localhost/sales_db" -f sql/schema.sql
psql "postgresql://sales_admin:admin123@localhost/sales_db" -f sql/seed.sql

# Generate synthetic data
python python/generate_data.py

# Run ETL pipeline
python python/etl_pipeline.py

# Generate analytics reports
python python/analytics.py
```

## 📈 Dashboard Mockup
The Power BI dashboard is designed with an "Executive Dark Mode" theme, featuring:
- **Top Row:** KPI Cards (Revenue, Profit, Margin).
- **Middle Row:** Revenue Trend Line Chart & Regional Sales Map.
- **Bottom Row:** Product Category Treemap & Top 10 Products Table.

*(See `dashboard/dashboard_layout.md` for detailed design specifications.)*

## 💡 Business Insights
- **Seasonality:** Q4 accounts for ~35% of annual revenue due to holiday demand.
- **Top Region:** The **West** region consistently outperforms others, contributing 35% of total sales.
- **High-Margin Segments:** Electronics and Software categories maintain the highest profit margins (>40%).
