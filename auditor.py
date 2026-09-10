
inventory = 0
rejected_entries = 0

while True:
    stock_quantity_input = input("Enter stock quantity (or type 'quit' to finish): ")
    if stock_quantity_input == 'quit':
        print("")
        print("===========================================================")
        print("Total Units Processed: ", inventory)
        print("Number of Failed/Rejected Entries: ", rejected_entries)
        print("===========================================================")
        print("")
        break
    else:
        try: 
            if int(stock_quantity_input) < 0:
                rejected_entries += 1
                print("Invalid negative input. Please enter a positive whole number for stock quantity.")
            else:
                inventory = inventory + int(stock_quantity_input)
                if inventory > 500:
                    print("")
                    print("===========================================================")
                    print("Inventory warning, inventory has exceeded 500 units.")
                    print("Total inventory: ", inventory)
                    print("===========================================================")
                    print("")
                    break
                else:
                    print("Current inventory: ", inventory)
        except ValueError:
            rejected_entries += 1
            print("Invalid text input. Please enter a positive whole number for stock quantity.")


