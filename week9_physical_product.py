# 2601582 INF1103 Week 9 Lab
from week8_product import Product
from week9_can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, prodID, prodName, prodPrice, prodQuantity, Weight):
        super().__init__(prodID, prodName, prodPrice, prodQuantity)
        self.__weight = Weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 5 #5 dollar per kg
        return shipping_cost

    def to_dict(self):
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