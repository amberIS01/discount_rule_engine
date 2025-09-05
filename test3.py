from discount_engine.rules.rule_wednesday import WednesdayRule

rule = WednesdayRule()

order = {
    "customerType": "PREMIUM",
    "orderTotal": 8000,
    "dayOfWeek": "WEDNESDAY"
}

print("Applies?", rule.applies(order))   # True
print("Discount:", rule.calculate(order))  # 400.0
