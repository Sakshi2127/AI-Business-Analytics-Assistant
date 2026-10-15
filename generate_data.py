
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

random.seed(42)

products = {
    "Electronics": [
        ("Headphones", 1500),
        ("Keyboard", 900),
        ("Mouse", 500),
        ("Monitor", 9000),
    ],
    "Fashion": [
        ("T-Shirt", 600),
        ("Jeans", 1400),
        ("Shoes", 2200),
        ("Backpack", 1200),
    ],
    "Home": [
        ("Mixer", 2500),
        ("Lamp", 800),
        ("Chair", 3500),
        ("Bedsheet", 1000),
    ],
    "Beauty": [
        ("Face Wash", 250),
        ("Moisturizer", 450),
        ("Sunscreen", 350),
        ("Shampoo", 300),
    ],
}

regions = ["West", "North", "South", "East"]
payment_methods = ["UPI", "Card", "Cash", "Net Banking"]

rows = []
start_date = datetime(2025, 1, 1)

for order_id in range(1, 1001):
    category = random.choice(list(products.keys()))
    product, price = random.choice(products[category])
    quantity = random.randint(1, 5)
    discount = random.choice([0, 0.05, 0.10, 0.15])

    unit_price = round(price * (1 - discount), 2)
    revenue = round(unit_price * quantity, 2)
    cost = round(price * random.uniform(0.55, 0.80) * quantity, 2)

    rows.append({
        "order_id": order_id,
        "order_date": (
            start_date + timedelta(days=random.randint(0, 364))
        ).strftime("%Y-%m-%d"),
        "customer_id": f"CUST{random.randint(1, 250):04d}",
        "product": product,
        "category": category,
        "region": random.choice(regions),
        "quantity": quantity,
        "unit_price": unit_price,
        "revenue": revenue,
        "cost": cost,
        "profit": round(revenue - cost, 2),
        "payment_method": random.choice(payment_methods),
    })

df = pd.DataFrame(rows)

output_path = Path(__file__).parent / "data" / "sales_data.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Saved to: {output_path}")
print(df.head())
