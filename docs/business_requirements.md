# Business Requirements Document (BRD)

## Project Name: Strategic Sales Performance Dashboard

## 1. Problem Statement
Stakeholders currently rely on manual, fragmented Excel reports to track sales across multiple regions. This process is time-consuming, error-prone, and lacks real-time visibility into declining markets or product performance.

## 2. Business Objectives
- **Centralize Data:** Create a single source of truth for all sales transactions.
- **Automate Reporting:** Replace manual extraction with an automated ETL pipeline.
- **Track KPIs:** Monitor Revenue, Profit, and YoY Growth in real-time.
- **Enable Drill-downs:** Allow executives to view performance by Region, Product Category, and Sales Rep.

## 3. Key Performance Indicators (KPIs)
- **Total Revenue:** Gross sales amount.
- **Total Profit:** Net profit after costs and discounts.
- **Profit Margin %:** Efficiency of sales (Profit/Revenue).
- **Year-over-Year (YoY) Growth:** Comparison of revenue against the same period in the previous year.
- **Top 10 Products:** Identifying high-impact items.
- **Sales Rep Performance:** Tracking individual contributions to regional targets.

## 4. Target Audience
- **Executives (C-Suite):** For high-level growth and margin trends.
- **Regional Managers:** For tracking team performance and territory health.
- **Sales Leads:** For identifying top-selling products and customer segments.

## 5. Functional Requirements
- Data must be updated weekly via the ETL pipeline.
- Dashboard must include interactive filters for Date, Region, and Segment.
- System must handle up to 15,000 transactions with sub-second query response times.
