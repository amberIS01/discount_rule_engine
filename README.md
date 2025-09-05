# Discount Rule Engine

A flexible Python engine for applying discount rules to orders. Easily extendable for new business logic and discount scenarios.

## Features
- Modular rule system (add new rules easily)
- Priority-based rule application
- Simple API for checking applicability and calculating discounts
- Unit tests with pytest

## Project Structure
```
.
├── requirements.txt         # Python dependencies
├── scratch.py               # Example usage script
├── src/
│   └── discount_engine/
│       ├── engine.py        # (Main engine logic, if present)
│       └── rules/           # Discount rules
│           ├── base.py      # Base Rule class
│           ├── rule_new_customer.py
│           ├── rule_large_order.py
│           ├── rule_wednesday.py
├── tests/
│   └── test_rules.py        # Unit tests for rules
└── .gitignore
```

## Getting Started
### 1. Clone the repository
```powershell
git clone <your-repo-url>
cd discount-rule-engine
```

### 2. Install dependencies
```powershell
python -m pip install -r requirements.txt
```

### 3. Run Example
```powershell
# Set PYTHONPATH so imports work
$env:PYTHONPATH="D:\Code\NNeeww\discount-rule-engine\src"
python scratch.py
```

### 4. Run Tests
```powershell
$env:PYTHONPATH="D:\Code\NNeeww\discount-rule-engine\src"
python -m pytest -v
```

## Usage Example
See `scratch.py` for a sample usage:
```python
from discount_engine.rules.rule_new_customer import NewCustomerRule

rule = NewCustomerRule()
order = {
    "customerType": "NEW",
    "orderTotal": 12000,
    "dayOfWeek": "WEDNESDAY"
}
print("Applies?", rule.applies(order))   # True
print("Discount:", rule.calculate(order))  # 1200.0
```

## Adding New Rules
1. Create a new file in `src/discount_engine/rules/` (e.g., `rule_special_day.py`).
2. Inherit from `Rule` in `base.py` and implement `applies` and `calculate` methods.
3. Add tests in `tests/test_rules.py`.

## License
MIT
