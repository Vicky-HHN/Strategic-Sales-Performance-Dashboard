# Power BI Dashboard Design Specifications

## Theme & Layout
- **Theme:** Modern Executive Dark Mode
- **Background:** #111111 (Deep Black/Gray)
- **Primary Color:** #1f77b4 (Corporate Blue)
- **Accent Color:** #ff7f0e (Orange for highlights)
- **Text:** Segoe UI, White/Light Gray

## Visualizations

### 1. KPI Header (Top Row)
- **Total Revenue Card:** `SUM(fact_sales[total_sales])`
- **Total Profit Card:** `SUM(fact_sales[profit])`
- **Profit Margin % Card:** `DIVIDE([Total Profit], [Total Revenue])`
- **Total Transactions Card:** `COUNT(fact_sales[order_id])`

### 2. Trends & Geography (Middle Row)
- **Revenue Trend:** Line chart showing `Total Revenue` by `Month`.
- **Regional Sales:** Map visual showing `Total Revenue` by `State` or `Region`.
- **YoY Growth:** Gauge visual showing current year growth vs target.

### 3. Product & Segment Deep-Dive (Bottom Row)
- **Top 10 Products:** Bar chart showing revenue by `Product Name`.
- **Profitability by Category:** Treemap showing `Profit` size and `Margin` color.
- **Segment Breakdown:** Donut chart showing revenue distribution by `Customer Segment`.

## Interactive Features
- **Slicers:** Date Range, Region, Product Category, Sales Channel.
- **Drill-through:** Right-click on a Region to see Sales Rep performance for that region.
- **Tooltips:** Hover over trend points to see exact profit and order count for that month.

## DAX Measures
```dax
Total Revenue = SUM(fact_sales[total_sales])
Total Profit = SUM(fact_sales[profit])
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
Prior Year Revenue = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('dim_dates'[Date]))
YoY Growth % = DIVIDE([Total Revenue] - [Prior Year Revenue], [Prior Year Revenue], 0)
```
