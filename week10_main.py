# 2601582 INF1103 Week 10 Lab
import json
from week10_product import Product
from week10_inventory import Inventory
from week10_physical_product import PhysicalProduct
from week10_digital_product import DigitalProduct
from week10_supplier import Supplier
from week10_orderline import OrderLine
from week10_order import Order

# supplier = Supplier("5001", "Tech Pte Ltd", "sales@tech.com")
# laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)
# game = DigitalProduct("P002", "Game", 59.90, 100, 500.0, supplier)

# laptop.display_information()
# game.display_information()

# del supplier

# laptop.display_information()
# game.display_information()
# laptop.get_supplier().display_information()

# print(laptop.get_supplier() is game.get_supplier())   # expect True

# ============================================================

# supplier = Supplier("5001", "Tech Pte Ltd", "sales@tech.com")
# laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)

# inv_a = Inventory()
# inv_b = Inventory()

# inv_a.add_product(laptop)
# inv_a.remove_product("P001")
# laptop.display_information()      # still works?

# inv_b.add_product(laptop)
# inv_b.display_all()

# print(inv_b.find_product("P001") is laptop)   # expect True

# =================================

supplier = Supplier("5001", "Tech Pte Ltd", "sales@tech.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)
game = DigitalProduct("P002", "Game", 59.90, 100, 500.0, supplier)
order1 = Order("O001")
order1.add_order_line(laptop, 2)
order1.add_order_line(game, 1)
# order1.display_information()

order2 = Order("O002")
order2.add_order_line(laptop, 1)   # same product, different order
order2.display_information()

# print(order1.get_order_lines()[0].get_product() is order2.get_order_lines()[0].get_product())  # expect True
# print(order1.get_order_lines()[0] is order2.get_order_lines()[0])                               # expect False

# Same Product in both orders, but separate OrderLine objects
line1 = order1.get_order_lines()[0]
line2 = order2.get_order_lines()[0]
print(line1.get_product() is line2.get_product())   # expect True  (1 shared Product)
print(line1 is line2)                                # expect False (separate OrderLines)

# Remove a line through the Order, then check the product still works
order1.remove_order_line("P002")
order1.display_information()                         # only the laptop line left
game.display_information()                           # game still works