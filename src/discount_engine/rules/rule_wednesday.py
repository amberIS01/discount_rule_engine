from .base import Rule

class WednesdayRule(Rule):
    id = "RULE_WEDNESDAY"
    priority = 3

    def applies(self, order: dict) -> bool:
        return order.get("dayOfWeek", "").upper() == "WEDNESDAY"

    def calculate(self, order: dict) -> float:
        order_total = order.get("orderTotal", 0)
        return order_total * 0.05
