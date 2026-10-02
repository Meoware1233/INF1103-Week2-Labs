# 2601582 INF1103 Week 5 Lab
import json
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
        json.dump(inventory, file,indent=4)
    print("Inventory sucessfully saved into inventory.json")

def display_all(inventory):
    print("")
    print("Current Inventory:")
    print("-----------------------------------------------------------")
    for i in inventory:
        print(f"ID: {i}| Name: {inventory[i]['name']} | Price: ${inventory[i]['price']:.2f} | Stock: {inventory[i]['quantity']}")
    print("-----------------------------------------------------------")
    print("")


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
            display_all(inventory)
        elif choice == '2':
            while True:
                try:
                    print("Add new products")
                    prodID = input("Product ID: ")
                    prodName = input("Product Name: ")
                    prodPrice = float(input("Price: $"))
                    prodQuantity = int(input("Stock Quantity: "))

                    inventory[prodID] = {
                        "name": prodName,
                        "price": prodPrice,
                        "quantity": prodQuantity
                    }
                    break
                    
                except ValueError:
                    print("Invalid input. Please enter valid values.")
                

        elif choice == '3':
            # Add code to update products here
            print("Update Stock")
            prodID = input("Enter Product ID: ")

            for i in inventory:
                if i == prodID:
                    try:
                        print("-----------------------------------------------------------")
                        print("Product Found:")
                        print("Name: ", inventory[i]['name'])
                        print("Current Stock: ", inventory[i]['quantity'])
                        new_stock = int(input("Enter new stock quantity: "))
                        inventory[i]['quantity'] = new_stock
                        print("Stock updated successfully.")
                    except ValueError:
                        print("Invalid input. Please enter a valid stock quantity.")
                else:
                    print("Product not found.")


        elif choice == '4':
            # Add code to search products here
            print("Search Product")
            prodID = input("Enter Product ID: ")
            for i in inventory:
                if i == prodID:
                    print("-----------------------------------------------------------")
                    print("Product Found:")
                    print("Name: ", inventory[i]['name'])
                    print("Price: $", inventory[i]['price'])
                    print("Current Stock: ", inventory[i]['quantity'])
                    print("-----------------------------------------------------------")
                else:
                    print("Product not found.")

        elif choice == '5':
            save_inventory(inventory)
        elif choice == '6':
            print("Exiting program.")
            break




exist_inventory = load_inventory()
get_valid_input(exist_inventory)


