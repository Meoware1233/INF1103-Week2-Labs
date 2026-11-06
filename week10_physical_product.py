# 2601582 INF1103 Week 10 Lab
from week10_product import Product
from week10_can_be_shipped import CanBeShipped
from week10_supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, prodID: str, prodName:str, prodPrice:float, prodQuantity:int, weight:float, supplier: Supplier):
        super().__init__(prodID, prodName, prodPrice, prodQuantity, supplier)
        self.__weight = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_cost = self.__weight * 5 #5 dollar per kg
        return shipping_cost

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data

# test = PhysicalProduct("P001", "Laptop", 1200, 10, 2.1)
# test.display_information()
# test.update_stock(20)
# test.display_information()

# physical = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.1)
# print(physical.to_dict())