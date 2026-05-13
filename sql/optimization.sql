-- Performance Optimization Demonstrations

-- 1. Materialized View for Regional Monthly Sales
-- Pre-calculates aggregations for faster dashboard loading
CREATE MATERIALIZED VIEW mv_regional_monthly_sales AS
SELECT
    r.region_name,
    DATE_TRUNC('month', s.order_date) AS sales_month,
    SUM(s.total_sales) AS total_revenue,
    SUM(s.profit) AS total_profit,
    COUNT(s.order_id) AS transaction_count
FROM fact_sales s
JOIN dim_regions r ON s.region_id = r.region_id
GROUP BY 1, 2;

CREATE INDEX idx_mv_month ON mv_regional_monthly_sales(sales_month);

-- 2. Query with and without index (Benchmark Example)
-- In a real scenario, we'd compare EXPLAIN ANALYZE results
EXPLAIN ANALYZE
SELECT * FROM fact_sales WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';

-- 3. Optimization using CTE for complex calculations
-- Finding top products per region
WITH regional_product_rank AS (
    SELECT
        r.region_name,
        p.product_name,
        SUM(s.total_sales) as revenue,
        RANK() OVER (PARTITION BY r.region_name ORDER BY SUM(s.total_sales) DESC) as sales_rank
    FROM fact_sales s
    JOIN dim_regions r ON s.region_id = r.region_id
    JOIN dim_products p ON s.product_id = p.product_id
    GROUP BY 1, 2
)
SELECT * FROM regional_product_rank WHERE sales_rank <= 3;
