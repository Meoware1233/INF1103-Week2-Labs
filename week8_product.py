# 2601582 INF1103 Week 8 Lab
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, prodID, prodName, prodPrice, prodQuantity):
        self.__product_id = prodID
        self.__product_name = prodName
        self.__product_price = prodPrice
        self.__product_quantity = prodQuantity


    def get_product_id(self):
        return self.__product_id

    def display_information(self):
        print(f"ID: {self.__product_id}| Name: {self.__product_name} | Price: ${self.__product_price:.2f} | Stock: {self.__product_quantity}")

    def to_dict(self):
        return {
            "name": self.__product_name,
            "price": self.__product_price,  
            "quantity": self.__product_quantity
        }

    def update_stock(self, quantity):
        if quantity >= 0:
            self.__product_quantity = quantity
            print(f"Stock updated successfully. New stock quantity: {self.__product_quantity}")
        else:
            print("Invalid stock, stock cannot be negative.")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    

        
# p = Product("P001", "Laptop", 1200.00, 15)
# print(p.to_dict())
# p = Product("P001", "Laptop", 1200.00, 10)
# p.display_information()
# p.update_stock(15)
# p.display_information()
# p.update_stock(-5)
# p.display_information()
# p.update_stock(0)
# p.display_information()







