
import json
from week8_product import Product
from week8_inventory import Inventory

# inv = Inventory()
# inv.add_product(Product("P001", "Laptop", 1200.00, 15))
# inv.add_product(Product("P002", "mouse", 200.00, 15))
# inv.display_all()
# print(inv.search_product("P002"))   # a Product object
# print(inv.search_product("P999"))   # None





def load_inventory():
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


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory.all_to_dict(), file,indent=4)
    print("Inventory sucessfully saved into inventory.json")

def get_valid_input(inventory):
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
                    product = Product(prodID, prodName, prodPrice, prodQuantity)
                    inventory.add_product(product)
                    break
                    
                except ValueError:
                    print("Invalid input. Please enter valid values.")
                

        elif choice == '3':
            # Add code to update products here
            print("Update Stock")
            prodID = input("Enter Product ID: ")
            product = inventory.search_product(prodID)

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
            product = inventory.search_product(prodID)


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
    product = Product(prod_id, details["name"], details["price"], details["quantity"])
    inventory.add_product(product)




get_valid_input(inventory)