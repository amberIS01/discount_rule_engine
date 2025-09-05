import pytest
from src.discount_engine.engine import create_default_engine

engine = create_default_engine()

def test_new_customer_large_order_wednesday():
    order = {"customerType": "NEW", "orderTotal": 12000, "dayOfWeek": "WEDNESDAY"}
    result = engine.apply_best_rule(order)
    assert result.rule_id == "RULE_NEW_CUSTOMER"
    assert result.discount == 1200.0
    assert result.final_amount == 10800.0

def test_regular_large_order_friday():
    order = {"customerType": "REGULAR", "orderTotal": 12000, "dayOfWeek": "FRIDAY"}
    result = engine.apply_best_rule(order)
    assert result.rule_id == "RULE_LARGE_ORDER"
    assert result.discount == 500.0
    assert result.final_amount == 11500.0

def test_premium_small_order_wednesday():
    order = {"customerType": "PREMIUM", "orderTotal": 8000, "dayOfWeek": "WEDNESDAY"}
    result = engine.apply_best_rule(order)
    assert result.rule_id == "RULE_WEDNESDAY"
    assert result.discount == 400.0
    assert result.final_amount == 7600.0
