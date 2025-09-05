from .base import Rule

class NewCustomerRule(Rule):
    id = "RULE_NEW_CUSTOMER"
    priority = 1   # Highest priority

    def applies(self, order: dict) -> bool:
        # Rule: only applies if customerType is NEW
        return order.get("customerType") == "NEW"

    def calculate(self, order: dict) -> float:
        # 10% of orderTotal
        order_total = order.get("orderTotal", 0)
        return order_total * 0.10
