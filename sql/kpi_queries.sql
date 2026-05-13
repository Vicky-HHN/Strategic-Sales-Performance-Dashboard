-- Strategic Sales KPIs and Analytical Queries

-- 1. High-Level Executive Summary
SELECT
    SUM(total_sales) AS total_revenue,
    SUM(profit) AS total_profit,
    ROUND((SUM(profit) / SUM(total_sales)) * 100, 2) AS profit_margin_pct,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_units_sold
FROM fact_sales;

-- 2. Yearly Revenue Growth (YoY)
WITH yearly_sales AS (
    SELECT
        EXTRACT(YEAR FROM order_date) AS sales_year,
        SUM(total_sales) AS annual_revenue
    FROM fact_sales
    GROUP BY 1
)
SELECT
    sales_year,
    annual_revenue,
    LAG(annual_revenue) OVER (ORDER BY sales_year) AS prev_year_revenue,
    ROUND(((annual_revenue - LAG(annual_revenue) OVER (ORDER BY sales_year)) / LAG(annual_revenue) OVER (ORDER BY sales_year)) * 100, 2) AS yoy_growth_pct
FROM yearly_sales;

-- 3. Top 10 Performing Products
SELECT
    p.product_name,
    p.category,
    SUM(s.total_sales) AS total_revenue,
    SUM(s.profit) AS total_profit
FROM fact_sales s
JOIN dim_products p ON s.product_id = p.product_id
GROUP BY 1, 2
ORDER BY total_revenue DESC
LIMIT 10;

-- 4. Regional Performance Breakdown
SELECT
    r.region_name,
    r.manager,
    SUM(s.total_sales) AS total_revenue,
    SUM(s.profit) AS total_profit,
    ROUND((SUM(s.profit) / SUM(s.total_sales)) * 100, 2) AS profit_margin_pct
FROM fact_sales s
JOIN dim_regions r ON s.region_id = r.region_id
GROUP BY 1, 2
ORDER BY total_revenue DESC;

-- 5. Monthly Sales Trends (Current Year)
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS month_year,
    SUM(total_sales) AS monthly_revenue,
    COUNT(order_id) AS order_count
FROM fact_sales
WHERE order_date >= '2024-01-01'
GROUP BY 1
ORDER BY 1;

-- 6. Sales Rep Performance
SELECT
    sr.rep_name,
    r.region_name,
    SUM(s.total_sales) AS total_revenue,
    COUNT(s.order_id) AS total_deals
FROM fact_sales s
JOIN dim_sales_reps sr ON s.rep_id = sr.rep_id
JOIN dim_regions r ON s.region_id = r.region_id
GROUP BY 1, 2
ORDER BY total_revenue DESC;

-- 7. Customer Segmentation Analysis
SELECT
    c.segment,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    SUM(s.total_sales) AS total_revenue,
    ROUND(AVG(s.total_sales), 2) AS avg_order_value
FROM fact_sales s
JOIN dim_customers c ON s.customer_id = c.customer_id
GROUP BY 1
ORDER BY total_revenue DESC;
