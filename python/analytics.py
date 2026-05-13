import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

# Database configuration
DB_URL = "postgresql://sales_admin:admin123@localhost/sales_db"

def fetch_data(query):
    engine = create_engine(DB_URL)
    return pd.read_sql(query, engine)

def plot_revenue_trends(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['month_year'], df['monthly_revenue'], marker='o', linestyle='-', color='#1f77b4')
    plt.title('Monthly Revenue Trends (2021-2024)', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('reports/revenue_trends.png')
    plt.close()

def plot_regional_performance(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['region_name'], df['total_revenue'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title('Total Revenue by Region', fontsize=14)
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Total Revenue ($)', fontsize=12)
    plt.tight_layout()
    plt.savefig('reports/regional_revenue.png')
    plt.close()

def plot_category_profitability(df):
    plt.figure(figsize=(10, 6))
    df_sorted = df.sort_values('profit_margin_pct', ascending=False)
    plt.barh(df_sorted['category'], df_sorted['profit_margin_pct'], color='#2ca02c')
    plt.title('Profit Margin % by Product Category', fontsize=14)
    plt.xlabel('Profit Margin (%)', fontsize=12)
    plt.ylabel('Category', fontsize=12)
    plt.tight_layout()
    plt.savefig('reports/category_profitability.png')
    plt.close()

def main():
    print("Starting Python Analytics...")
    os.makedirs('reports', exist_ok=True)

    # 1. Revenue Trends
    query_trends = """
    SELECT TO_CHAR(order_date, 'YYYY-MM') as month_year, SUM(total_sales) as monthly_revenue
    FROM fact_sales
    GROUP BY 1 ORDER BY 1;
    """
    df_trends = fetch_data(query_trends)
    plot_revenue_trends(df_trends)
    print("- Generated revenue_trends.png")

    # 2. Regional Performance
    query_regions = """
    SELECT r.region_name, SUM(s.total_sales) as total_revenue
    FROM fact_sales s
    JOIN dim_regions r ON s.region_id = r.region_id
    GROUP BY 1 ORDER BY 2 DESC;
    """
    df_regions = fetch_data(query_regions)
    plot_regional_performance(df_regions)
    print("- Generated regional_revenue.png")

    # 3. Category Profitability
    query_categories = """
    SELECT p.category,
           ROUND((SUM(s.profit) / SUM(s.total_sales)) * 100, 2) as profit_margin_pct
    FROM fact_sales s
    JOIN dim_products p ON s.product_id = p.product_id
    GROUP BY 1 ORDER BY 2 DESC;
    """
    df_categories = fetch_data(query_categories)
    plot_category_profitability(df_categories)
    print("- Generated category_profitability.png")

    print("Analytics complete. Reports saved in /reports folder.")

if __name__ == "__main__":
    main()
