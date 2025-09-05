from typing import List, Optional, Dict
from .rules.base import Rule
from .rules.rule_new_customer import NewCustomerRule
from .rules.rule_large_order import LargeOrderRule
from .rules.rule_wednesday import WednesdayRule


class DiscountResult:
    def __init__(self, rule_id: Optional[str], discount: float, final_amount: float):
        self.rule_id = rule_id
        self.discount = discount
        self.final_amount = final_amount

    def __repr__(self):
        return f"<DiscountResult rule={self.rule_id}, discount={self.discount}, final={self.final_amount}>"


class DiscountEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def apply_best_rule(self, order: Dict) -> DiscountResult:
        applicable = [r for r in self.rules if r.applies(order)]

        if not applicable:
            return DiscountResult(None, 0.0, order.get("orderTotal", 0))

        # find the highest priority (lowest number)
        best_priority = min(r.priority for r in applicable)
        best_rules = [r for r in applicable if r.priority == best_priority]

        # tie-breaker → choose rule with max discount
        discounts = [(r.calculate(order), r) for r in best_rules]
        best_discount, best_rule = max(discounts, key=lambda t: t[0])

        final_amount = order.get("orderTotal", 0) - best_discount
        return DiscountResult(best_rule.id, best_discount, final_amount)


# Helper: create default engine with all rules
def create_default_engine() -> DiscountEngine:
    rules = [NewCustomerRule(), LargeOrderRule(), WednesdayRule()]
    return DiscountEngine(rules)
