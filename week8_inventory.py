# 2601582 INF1103 Week 8 Lab
# from week8_product import Product
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)  

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("")
        print("Current Inventory:")
        print("-----------------------------------------------------------")
        for product in self.__products:
            product.display_information()
        print("-----------------------------------------------------------")
        print("")

    def all_to_dict(self):
        result = {}
        for product in self.__products:
            result[product.get_product_id()] = product.to_dict()
        return result



# inv = Inventory()
# inv.add_product(Product("P001", "Laptop", 1200.00, 15))
# inv.add_product(Product("P002", "Mouse", 25.50, 40))
# print(inv.all_to_dict())
