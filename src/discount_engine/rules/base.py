from abc import ABC, abstractmethod

class Rule(ABC):
    """
    Base class for all discount rules.
    Each rule must define:
    - id (string)
    - priority (int, lower = higher priority)
    - applies(order): returns True/False
    - calculate(order): returns discount amount
    """

    id: str
    priority: int

    @abstractmethod
    def applies(self, order: dict) -> bool:
        pass

    @abstractmethod
    def calculate(self, order: dict) -> float:
        pass
