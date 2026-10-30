from week8_product import Product

class PhysicalProduct(Product):
    def __init__(self, prodID, prodName, prodPrice, prodQuantity, Weight):
        super().__init__(prodID, prodName, prodPrice, prodQuantity)
        self.__weight = Weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

# test = PhysicalProduct("P001", "Laptop", 1200, 10, 2.1)
# test.display_information()
# test.update_stock(20)
# test.display_information()