# 2601582 INF1103 Week 10 Lab
import json
from week10_product import Product
from week10_inventory import Inventory
from week10_physical_product import PhysicalProduct
from week10_digital_product import DigitalProduct
from week10_supplier import Supplier
from week10_orderline import OrderLine
from week10_order import Order


def load_inventory() -> dict:
    inventory = {}
    try:
        with open("inventory.json", "r") as file:
            # Read line 1 and remove from file
            inventory = json.load(file)
            return inventory
    except FileNotFoundError:
        print("File not found, creating new json file.")
        with open("inventory.json", "w") as file:
            return inventory
    except ValueError:
        with open("inventory.json", "w") as file:
                return inventory


def save_inventory(inventory) -> None:
    with open("inventory.json", "w") as file:
        json.dump(inventory.all_to_dict(), file,indent=4)
    print("Inventory sucessfully saved into inventory.json")

suppliers: dict[str, Supplier] = {}

def get_valid_input(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
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

        if choice == '1':
            inventory.display_all()
        elif choice == '2':
            while True:
                try:
                    print("Add new products")
                    prodID = input("Product ID: ")
                    prodName = input("Product Name: ")
                    prodPrice = float(input("Price: $"))
                    prodQuantity = int(input("Stock Quantity: "))
                    supplier_id = input("Supplier ID: ")
                    if supplier_id in suppliers:
                        supplier = suppliers[supplier_id]          # reuse the existing one
                    else:
                        supplier_name = input("Supplier Name: ")
                        supplier_email = input("Supplier Email: ")
                        supplier = Supplier(supplier_id, supplier_name, supplier_email)
                        suppliers[supplier_id] = supplier          # remember it
                    product_type = input("Physical or digital? (p/d): ")
                    if product_type == "p":
                        weight = float(input("Weight (kg): "))
                        product = PhysicalProduct(prodID, prodName, prodPrice, prodQuantity, weight, supplier)
                        inventory.add_product(product)
                        break
                    elif product_type == "d":
                        download_size = float(input("Download Size (MB): "))
                        product = DigitalProduct(prodID, prodName, prodPrice, prodQuantity, download_size, supplier)
                        inventory.add_product(product)
                        break
                    else:
                        print("Invalid product type.")              
                except ValueError:
                    print("Invalid input. Please enter valid values.")
                

        elif choice == '3':
            # Add code to update products here
            print("Update Stock")
            prodID = input("Enter Product ID: ")
            product = inventory.find_product(prodID)

            if product is None:
                print("Product not found")
            else:
                try:
                    new_quantity = int(input("Enter new quantity: "))
                except ValueError:
                    print("Invalid input. Please enter a whole number.")
                else:
                    product.update_stock(new_quantity)


        elif choice == '4':
            # Add code to search products here
            print("Search Product")
            prodID = input("Enter Product ID: ")
            product = inventory.find_product(prodID)

            if product is None:
                print("Product not found.")

            else:
               product.display_information()

                

        elif choice == '5':
            save_inventory(inventory)

        elif choice == '6':
            print("Exiting program.")
            break




inventory = Inventory()
data = load_inventory()
for prod_id, details in data.items():
    supplier_data = details["supplier"]
    supplier_id = supplier_data["id"]
    if supplier_id in suppliers:
        supplier = suppliers[supplier_id]
    else:
        supplier = Supplier(supplier_id, supplier_data["name"], supplier_data["email"])
        suppliers[supplier_id] = supplier

    product_type = details.get("type")
    if product_type == "physical":
        product = PhysicalProduct(prod_id, details["name"], details["price"], details["quantity"], details["weight"], supplier)
        inventory.add_product(product)
    elif product_type == "digital":
        product = DigitalProduct(prod_id, details["name"], details["price"], details["quantity"], details["download_size"], supplier)
        inventory.add_product(product)
    else:
        print(f"Skipping {prod_id}: unknown product type.")

get_valid_input(inventory, suppliers)


