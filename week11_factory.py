from week11_product import Product
from week11_physical_product import PhysicalProduct
from week11_digital_product import DigitalProduct
from week10_supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier, extra: float = 0.0) -> Product:
        # extra = weight (kg) for physical, download size (MB) for digital
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")