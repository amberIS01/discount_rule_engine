from discount_engine.rules.rule_large_order import LargeOrderRule

rule = LargeOrderRule()

order = {
    "customerType": "REGULAR",
    "orderTotal": 12000,
    "dayOfWeek": "FRIDAY"
}

print("Applies?", rule.applies(order))   # True
print("Discount:", rule.calculate(order))  # 500.0
