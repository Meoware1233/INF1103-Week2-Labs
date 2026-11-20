# 2601582 INF1103 Week 10 Lab
import json
from week11_inventory import Inventory
from week10_supplier import Supplier
from week11_factory import ProductFactory


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def get_non_negative_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a whole number of 0 or more.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number, e.g. 10")


def load_inventory() -> dict:
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved inventory found. Starting with an empty inventory.")
        return {}
    except json.JSONDecodeError:
        print("inventory.json is corrupted. Starting with an empty inventory.")
        return {}


def save_inventory(inventory: Inventory) -> None:
    with open("inventory.json", "w") as file:
        json.dump(inventory.all_to_dict(), file, indent=4)
    print("Inventory successfully saved into inventory.json")


def get_or_create_supplier(suppliers: dict[str, Supplier]) -> Supplier:
    supplier_id = input("Supplier ID: ")
    if supplier_id in suppliers:
        return suppliers[supplier_id]  # reuse the existing one
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Email: ")
    supplier = Supplier(supplier_id, supplier_name, supplier_email)
    suppliers[supplier_id] = supplier  # remember it
    return supplier


def add_product(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    print("Add new product")
    prod_id = input("Product ID: ")
    prod_name = input("Product Name: ")
    prod_price = get_positive_float("Price: $")
    prod_quantity = get_non_negative_int("Stock Quantity: ")
    supplier = get_or_create_supplier(suppliers)

    while True:
        product_type = input("Physical or digital? (p/d): ").strip().lower()
        if product_type in ("p", "d"):
            break
        print("Invalid product type.")

    if product_type == "p":
        ptype = "physical"
        extra = get_positive_float("Weight (kg): ")
    else:
        ptype = "digital"
        extra = get_positive_float("Download Size (MB): ")

    try:
        product = ProductFactory.create(ptype, prod_id, prod_name, prod_price,
                                        prod_quantity, supplier, extra)
        inventory.add_product(product)
        print("Product added.")
    except ValueError as e:
        print(f"Could not add product: {e}")


def update_stock(inventory: Inventory) -> None:
    print("Update Stock")
    prod_id = input("Enter Product ID: ")
    product = inventory.find_product(prod_id)

    if product is None:
        print("Product not found.")
        return

    try:
        new_quantity = int(input("Enter new quantity: "))
        product.update_stock(new_quantity)
    except ValueError as e:
        print(f"Invalid input: {e}")


def search_product(inventory: Inventory) -> None:
    print("Search Product")
    prod_id = input("Enter Product ID: ")
    product = inventory.find_product(prod_id)

    if product is None:
        print("Product not found.")
    else:
        product.display_information()


def build_inventory(data: dict, suppliers: dict[str, Supplier]) -> Inventory:
    inventory = Inventory()
    for prod_id, details in data.items():
        try:
            supplier_data = details["supplier"]
            supplier_id = supplier_data["id"]
            if supplier_id in suppliers:
                supplier = suppliers[supplier_id]
            else:
                supplier = Supplier(supplier_id, supplier_data["name"], supplier_data["email"])
                suppliers[supplier_id] = supplier

            extra = details.get("weight", details.get("download_size", 0.0))
            product = ProductFactory.create(details.get("type"), prod_id, details["name"],
                                            details["price"], details["quantity"], supplier, extra)
            inventory.add_product(product)
        except (KeyError, ValueError) as e:
            print(f"Skipping {prod_id}: {e}")
    return inventory


def run_menu(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    while True:
        print("")
        print("1. Display All Products")
        print("2. Add Products")
        print("3. Update Products")
        print("4. Search Products")
        print("5. Save Inventory")
        print("6. Exit")
        choice = input("Enter option: ")
        print("")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory, suppliers)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    suppliers: dict[str, Supplier] = {}
    inventory = build_inventory(load_inventory(), suppliers)
    run_menu(inventory, suppliers)