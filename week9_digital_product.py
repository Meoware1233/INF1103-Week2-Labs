from week8_product import Product

class DigitalProduct(Product):
    def __init__(self, prodID, prodName, prodPrice, prodQuantity, download_size):
        super().__init__(prodID, prodName, prodPrice, prodQuantity)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")


# test = DigitalProduct("P002", "anti-virus", 50, 20, 500)
# test.display_information()
# test.update_stock(30)
# test.display_information()