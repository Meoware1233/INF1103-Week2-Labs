# 2601582 INF1103 Week 10 Lab
from abc import ABC, abstractmethod
from week10_supplier import Supplier

class Product(ABC):
    def __init__(self, prodID: str, prodName: str, prodPrice: float, prodQuantity: int, supplier: Supplier):
        self.__product_id: str = prodID
        self.__product_name: str = prodName
        self.__product_price: float = prodPrice
        self.__product_quantity: int = prodQuantity
        self.__supplier: Supplier = supplier


    def get_product_id(self) -> str:
        return self.__product_id

    def get_price(self) -> float:
        return self.__product_price

    def display_information(self) -> None:
        print(f"ID: {self.__product_id}| Name: {self.__product_name} | Price: ${self.__product_price:.2f} | Stock: {self.__product_quantity} | Supplier: {self.__supplier.get_name()}")

    def to_dict(self) -> dict:
        return {
            "name": self.__product_name,
            "price": self.__product_price,  
            "quantity": self.__product_quantity,
            "supplier": self.__supplier.to_dict()
        }

    def update_stock(self, quantity: int) -> None:
        if quantity >= 0:
            self.__product_quantity = quantity
            print(f"Stock updated successfully. New stock quantity: {self.__product_quantity}")
        else:
            print("Invalid stock, stock cannot be negative.")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    def get_supplier(self) -> Supplier:
        return self.__supplier


    

        
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







