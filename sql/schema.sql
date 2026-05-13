-- Strategic Sales Dashboard Schema
-- Star Schema Design

-- Drop tables if they exist
-- Drop tables and dependent objects if they exist
DROP TABLE IF EXISTS fact_sales CASCADE;
DROP TABLE IF EXISTS dim_sales_reps CASCADE;
DROP TABLE IF EXISTS dim_products CASCADE;
DROP TABLE IF EXISTS dim_customers CASCADE;
DROP TABLE IF EXISTS dim_regions CASCADE;
DROP TABLE IF EXISTS dim_dates CASCADE;

-- Dimension Tables
CREATE TABLE dim_regions (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(50) NOT NULL,
    manager VARCHAR(100)
);

CREATE TABLE dim_customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    category VARCHAR(50),
    base_price DECIMAL(12, 2)
);

CREATE TABLE dim_sales_reps (
    rep_id INT PRIMARY KEY,
    rep_name VARCHAR(100) NOT NULL,
    region_id INT REFERENCES dim_regions(region_id),
    hire_date DATE
);

CREATE TABLE dim_dates (
    date_key DATE PRIMARY KEY,
    year INT,
    quarter INT,
    month INT,
    day INT,
    month_name VARCHAR(20),
    day_name VARCHAR(20),
    is_weekend BOOLEAN
);

-- Fact Table
CREATE TABLE fact_sales (
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INT REFERENCES dim_customers(customer_id),
    product_id INT REFERENCES dim_products(product_id),
    rep_id INT REFERENCES dim_sales_reps(rep_id),
    region_id INT REFERENCES dim_regions(region_id),
    channel VARCHAR(50),
    quantity INT,
    unit_price DECIMAL(12, 2),
    discount DECIMAL(5, 2),
    total_sales DECIMAL(12, 2),
    profit DECIMAL(12, 2)
);

-- Indexes for performance optimization
CREATE INDEX idx_sales_date ON fact_sales(order_date);
CREATE INDEX idx_sales_customer ON fact_sales(customer_id);
CREATE INDEX idx_sales_product ON fact_sales(product_id);
CREATE INDEX idx_sales_region ON fact_sales(region_id);
CREATE INDEX idx_sales_rep ON fact_sales(rep_id);
