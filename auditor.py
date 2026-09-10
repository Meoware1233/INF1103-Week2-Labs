
inventory = 0
rejected_entries = 0

while True:
    stock_quantity_input = input("Enter stock quantity (or type 'quit' to finish): ")
    if stock_quantity_input == 'quit':
        break
    else: 
        try: 
            inventory += int(stock_quantity_input)
            print("Current inventory: ", inventory)
        except ValueError:
            rejected_entries += 1
            print("Invalid input. Please enter a valid integer for stock quantity.")


print("Total Units Processed: ", inventory)
print("Number of Failed/Rejected Entries: ", rejected_entries)