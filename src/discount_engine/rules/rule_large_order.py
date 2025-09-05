from .base import Rule

class LargeOrderRule(Rule):
    id = "RULE_LARGE_ORDER"
    priority = 2

    def applies(self, order: dict) -> bool:
        return order.get("orderTotal", 0) > 10000

    def calculate(self, order: dict) -> float:
        return 500.0
