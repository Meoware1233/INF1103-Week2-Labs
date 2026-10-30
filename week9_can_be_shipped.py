# 2601582 INF1103 Week 9 Lab
from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost():
        pass