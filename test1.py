from discount_engine.rules.rule_new_customer import NewCustomerRule

rule = NewCustomerRule()

order = {
    "customerType": "NEW",
    "orderTotal": 12000,
    "dayOfWeek": "WEDNESDAY"
}

print("Applies?", rule.applies(order))   # True
print("Discount:", rule.calculate(order))  # 1200.0
