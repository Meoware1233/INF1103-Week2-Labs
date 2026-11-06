# 2601582 INF1103 Week 10 Lab
from week10_product import Product
from week10_supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, prodID: str, prodName: str, prodPrice: float, prodQuantity:int, download_size:float, supplier: Supplier):
        super().__init__(prodID, prodName, prodPrice, prodQuantity, supplier)
        self.__download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data


# test = DigitalProduct("P002", "anti-virus", 50, 20, 500)
# test.display_information()
# test.update_stock(30)
# test.display_information()