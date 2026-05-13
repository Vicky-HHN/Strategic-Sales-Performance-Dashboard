import pandas as pd
from sqlalchemy import create_engine
import unittest

class TestSalesData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine("postgresql://sales_admin:admin123@localhost/sales_db")

    def test_row_counts(self):
        """Verify that the fact table has the expected number of records."""
        count = pd.read_sql("SELECT count(*) FROM fact_sales", self.engine).iloc[0, 0]
        self.assertEqual(count, 12000, "Fact table should have exactly 12,000 records.")

    def test_negative_prices(self):
        """Ensure there are no negative prices or quantities."""
        query = "SELECT count(*) FROM fact_sales WHERE unit_price < 0 OR quantity < 0"
        count = pd.read_sql(query, self.engine).iloc[0, 0]
        self.assertEqual(count, 0, "There should be no negative prices or quantities.")

    def test_referential_integrity(self):
        """Check for orphaned records in the fact table (though FKs should prevent this)."""
        queries = [
            "SELECT count(*) FROM fact_sales s LEFT JOIN dim_customers c ON s.customer_id = c.customer_id WHERE c.customer_id IS NULL",
            "SELECT count(*) FROM fact_sales s LEFT JOIN dim_products p ON s.product_id = p.product_id WHERE p.product_id IS NULL",
            "SELECT count(*) FROM fact_sales s LEFT JOIN dim_regions r ON s.region_id = r.region_id WHERE r.region_id IS NULL"
        ]
        for q in queries:
            count = pd.read_sql(q, self.engine).iloc[0, 0]
            self.assertEqual(count, 0, f"Referential integrity check failed for query: {q}")

    def test_kpi_logic(self):
        """Verify basic KPI calculation logic (Revenue = Qty * Price * (1-Discount))."""
        # We allow for small floating point differences (rounding effects)
        query = "SELECT count(*) FROM fact_sales WHERE ABS(total_sales - (quantity * unit_price * (1 - discount))) > 0.05"
        count = pd.read_sql(query, self.engine).iloc[0, 0]
        self.assertEqual(count, 0, f"KPI calculation logic (total_sales) is inconsistent. Found {count} mismatches.")

if __name__ == "__main__":
    unittest.main()
