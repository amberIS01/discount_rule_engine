from src.discount_engine.engine import create_default_engine

engine = create_default_engine()

orders = [
    {"customerType": "NEW", "orderTotal": 12000, "dayOfWeek": "WEDNESDAY"},
    {"customerType": "REGULAR", "orderTotal": 12000, "dayOfWeek": "FRIDAY"},
    {"customerType": "PREMIUM", "orderTotal": 8000, "dayOfWeek": "WEDNESDAY"},
]

for i, order in enumerate(orders, start=1):
    result = engine.apply_best_rule(order)
    print(f"Case {i}: {result}")
