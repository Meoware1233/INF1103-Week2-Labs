from week10_inventory import Inventory
from week10_supplier import Supplier
from week11_loader import load_products

inv = Inventory()
supplier = Supplier("5001", "Tech Pte Ltd", "sales@tech.com")
load_products("products.csv", inv, supplier)