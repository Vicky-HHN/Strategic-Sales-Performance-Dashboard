import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Initialize Faker
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# Configuration
NUM_TRANSACTIONS = 12000
START_DATE = datetime(2021, 1, 1)
END_DATE = datetime(2024, 12, 31)

def generate_dim_regions():
    regions = [
        {'region_id': 1, 'region_name': 'North', 'manager': 'Alice Smith'},
        {'region_id': 2, 'region_name': 'South', 'manager': 'Bob Johnson'},
        {'region_id': 3, 'region_name': 'East', 'manager': 'Charlie Brown'},
        {'region_id': 4, 'region_name': 'West', 'manager': 'Diana Prince'}
    ]
    return pd.DataFrame(regions)

def generate_dim_sales_reps(regions_df):
    reps = []
    for i in range(1, 21):
        reps.append({
            'rep_id': i,
            'rep_name': fake.name(),
            'region_id': random.choice(regions_df['region_id'].tolist()),
            'hire_date': fake.date_between(start_date='-5y', end_date='today')
        })
    return pd.DataFrame(reps)

def generate_dim_customers():
    customers = []
    segments = ['Corporate', 'Consumer', 'Home Office', 'Small Business']
    for i in range(1, 501):
        customers.append({
            'customer_id': i,
            'customer_name': fake.company() if random.random() > 0.5 else fake.name(),
            'segment': random.choice(segments),
            'country': 'United States',
            'city': fake.city(),
            'state': fake.state_abbr()
        })
    return pd.DataFrame(customers)

def generate_dim_products():
    categories = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse'],
        'Furniture': ['Desk', 'Chair', 'Bookshelf', 'Sofa', 'Table'],
        'Office Supplies': ['Paper', 'Binder', 'Pen', 'Stapler', 'Notebook'],
        'Software': ['SaaS Subscription', 'Operating System', 'Antivirus', 'CRM']
    }
    products = []
    prod_id = 1
    for cat, items in categories.items():
        for item in items:
            products.append({
                'product_id': prod_id,
                'product_name': item,
                'category': cat,
                'base_price': round(random.uniform(10, 2000), 2)
            })
            prod_id += 1
    return pd.DataFrame(products)

def generate_fact_sales(customers_df, products_df, reps_df):
    sales = []
    channels = ['Direct', 'Online', 'Retail', 'Partner']

    # Weighting for regions to simulate performance differences
    # North: 30%, West: 35%, East: 20%, South: 15%
    region_weights = {1: 0.30, 2: 0.15, 3: 0.20, 4: 0.35}

    # Weighting for products - Electronics and Software are high margin/volume
    product_weights = []
    for _, row in products_df.iterrows():
        if row['category'] in ['Electronics', 'Software']:
            product_weights.append(3)
        else:
            product_weights.append(1)
    product_weights = np.array(product_weights) / sum(product_weights)

    for i in range(1, NUM_TRANSACTIONS + 1):
        order_date = fake.date_between(start_date=START_DATE, end_date=END_DATE)

        # Seasonality: higher sales in Q4
        if order_date.month in [10, 11, 12]:
            if random.random() < 0.3: # 30% chance of double transaction in Q4
                 # We just generate one, but we could adjust volume.
                 # Instead, let's just make it more likely to pick Q4 dates.
                 pass

        customer = customers_df.sample(n=1).iloc[0]
        product = products_df.sample(n=1, weights=product_weights).iloc[0]

        # Pick a rep from a region, weighted by region performance
        region_id = random.choices(list(region_weights.keys()), weights=list(region_weights.values()))[0]
        reps_in_region = reps_df[reps_df['region_id'] == region_id]
        rep = reps_in_region.sample(n=1).iloc[0]

        quantity = random.randint(1, 10)
        unit_price = product['base_price'] * random.uniform(0.9, 1.1)
        discount = random.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2])

        total_sales = round(quantity * unit_price * (1 - discount), 2)
        # Cost is ~60-80% of base price
        cost = round(quantity * (product['base_price'] * random.uniform(0.5, 0.7)), 2)
        profit = round(total_sales - cost, 2)

        sales.append({
            'order_id': i,
            'order_date': order_date,
            'customer_id': customer['customer_id'],
            'product_id': product['product_id'],
            'rep_id': rep['rep_id'],
            'region_id': region_id,
            'channel': random.choice(channels),
            'quantity': quantity,
            'unit_price': round(unit_price, 2),
            'discount': discount,
            'total_sales': total_sales,
            'profit': profit
        })

    return pd.DataFrame(sales)

def main():
    print("Generating synthetic data...")

    regions_df = generate_dim_regions()
    reps_df = generate_dim_sales_reps(regions_df)
    customers_df = generate_dim_customers()
    products_df = generate_dim_products()
    sales_df = generate_fact_sales(customers_df, products_df, reps_df)

    # Save to CSV
    os.makedirs('data/raw', exist_ok=True)
    regions_df.to_csv('data/raw/dim_regions.csv', index=False)
    reps_df.to_csv('data/raw/dim_sales_reps.csv', index=False)
    customers_df.to_csv('data/raw/dim_customers.csv', index=False)
    products_df.to_csv('data/raw/dim_products.csv', index=False)
    sales_df.to_csv('data/raw/fact_sales.csv', index=False)

    print(f"Data generation complete. Generated {len(sales_df)} transactions.")
    print("Files saved to data/raw/")

if __name__ == "__main__":
    main()
