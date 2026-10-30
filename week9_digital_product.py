# 2601582 INF1103 Week 9 Lab
from week8_product import Product

class DigitalProduct(Product):
    def __init__(self, prodID, prodName, prodPrice, prodQuantity, download_size):
        super().__init__(prodID, prodName, prodPrice, prodQuantity)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data


# test = DigitalProduct("P002", "anti-virus", 50, 20, 500)
# test.display_information()
# test.update_stock(30)
# test.display_information()