import unittest, os, tempfile
from week10_supplier import Supplier
from week11_product import Product
from week11_order import Order
from week11_orderline import OrderLine
from week11_inventory import Inventory
from week11_factory import ProductFactory
from week11_loader import load_products
from week11_discount import *

S = Supplier("1", "Tech", "a@b.com")

class TestDiscounts(unittest.TestCase):
    def make_order(self, d=None):
        o = Order("O1", d)
        o.add_order_line(ProductFactory.create("physical", "P1", "X", 250.0, 5, S, 1.0), 1)
        return o
    def test_none(self):    self.assertEqual(self.make_order().calculate_total(), 250)
    def test_bulk(self):    self.assertEqual(self.make_order(BulkDiscount(200, 20)).calculate_total(), 230)
    def test_set_discount(self):
        o = self.make_order(BulkDiscount(200, 20)); o.set_discount(PercentageDiscount(10))
        self.assertEqual(o.calculate_total(), 225)
    def test_student(self): self.assertAlmostEqual(self.make_order(StudentDiscount()).calculate_total(), 237.5)

class TestFactoryAndValidation(unittest.TestCase):
    def test_unknown_type(self):
        with self.assertRaises(ValueError): ProductFactory.create("service", "S1", "X", 5.0, 1, S)
    def test_bad_price(self):
        with self.assertRaises(ValueError): ProductFactory.create("physical", "P1", "X", 0, 1, S)
    def test_negative_stock(self):
        with self.assertRaises(ValueError): ProductFactory.create("digital", "D1", "X", 5.0, -1, S)
    def test_orderline_qty(self):
        p = ProductFactory.create("digital", "D1", "X", 5.0, 1, S)
        with self.assertRaises(ValueError): OrderLine(p, 0)
    def test_abstract(self):
        with self.assertRaises(TypeError): Product("P", "X", 1.0, 1, S)

class TestLoader(unittest.TestCase):
    def test_missing_file(self):
        inv = Inventory(); load_products("nope.csv", inv, S)
        self.assertEqual(len(inv.get_products()), 0)
    def test_sample_csv(self):
        path = os.path.join(tempfile.mkdtemp(), "p.csv")
        with open(path, "w") as f:
            f.write("product_type,product_id,name,price,stock_quantity\n"
                    "physical,P001,Lamp,25.00,10\nservice,S1,X,30,5\n"
                    "physical,P2,Chair,abc,3\ndigital,D1,Ed,49.9,100\n")
        inv = Inventory(); load_products(path, inv, S)
        self.assertEqual(len(inv.get_products()), 2)

if __name__ == "__main__":
    unittest.main()