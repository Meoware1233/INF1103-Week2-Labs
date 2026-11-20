import csv
from week11_inventory import Inventory
from week10_supplier import Supplier
from week11_factory import ProductFactory

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            for row in reader:
                try:
                    ptype, pid, name, price, qty = row
                    product = ProductFactory.create(ptype, pid, name, float(price), int(qty), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Skipping row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")