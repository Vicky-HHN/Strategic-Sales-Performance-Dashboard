# Project Architecture: Strategic Sales Dashboard

## Overview
This project implements a complete end-to-end data engineering and analytics pipeline for a retail enterprise. It transforms raw synthetic sales data into actionable business insights through a structured ETL process and a PostgreSQL analytical database.

## System Components

### 1. Data Generation (Python/Faker)
- **Source:** `python/generate_data.py`
- **Function:** Generates ~12,000 realistic sales transactions across 4 regions and 4 years.
- **Logic:** Includes seasonality (Q4 peaks), regional performance variations (West & North as top performers), and category-specific profitability.

### 2. Data Storage (PostgreSQL)
- **Design:** Star Schema for optimized analytical querying.
- **Tables:**
    - `fact_sales`: Transactional data (Sales, Profit, Quantity, etc.)
    - `dim_customers`: Customer demographics and segments.
    - `dim_products`: Product catalog and categories.
    - `dim_regions`: Geographical hierarchy and managers.
    - `dim_sales_reps`: Sales team details linked to regions.

### 3. ETL Pipeline (Python/SQLAlchemy)
- **Source:** `python/etl_pipeline.py`
- **Process:**
    1. Extracts raw CSV files from `data/raw/`.
    2. Performs data cleaning (duplicate removal, null handling).
    3. Loads data into PostgreSQL using SQLAlchemy ORM.

### 4. Analytical Layer (SQL)
- **Queries:** `sql/kpi_queries.sql`
- **Features:**
    - Materialized views for dashboard performance.
    - Window functions for YoY growth and regional ranking.
    - Multi-table joins for deep-dive analysis.

### 5. Visualization (Matplotlib & Power BI)
- **Python Reports:** Automated chart generation for monthly trends and regional comparisons.
- **Power BI (Planned):** Interactive dashboard with drill-down capabilities.

## Data Flow
`Raw CSVs` -> `Python ETL` -> `PostgreSQL (Star Schema)` -> `SQL KPI Layer` -> `BI Dashboards`
