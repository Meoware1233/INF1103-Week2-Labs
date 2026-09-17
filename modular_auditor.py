# 2601582 INF1103 Week 3 Lab
def get_valid_input():
    inventory = 0
    rejected_entries = 0
    while True:
        stock_quantity_input = input("Enter stock quantity (or type 'quit' to finish): ")
        if stock_quantity_input == 'quit':
            return inventory, rejected_entries
        else:
            try: 
                if int(stock_quantity_input) < 0:
                    rejected_entries += 1
                    print("Invalid negative input. Please enter a positive whole number for stock quantity.")
                else:
                    inventory = inventory + int(stock_quantity_input)
                    if inventory > 500:
                        print("Inventory warning, inventory has exceeded 500 units. Exiting program.")
                        return inventory, rejected_entries
                    else:
                        print("Current inventory: ", inventory)
            except ValueError:
                rejected_entries += 1
                print("Invalid text input. Please enter a positive whole number for stock quantity.")


def process_delivery(current_total, new_value):
    delivery_cost = current_total * new_value
    return delivery_cost

def calculate_tax(amount):
    tax = 0.10 #10 percent tax
    tax_amount = amount * tax
    return tax_amount

# def generate_report(inventory, rejected_entries, cost_of_delivery, tax_cost):
#     print("")
#     print(f'Description                        Qty/Cost')
#     print("-----------------------------------------------------------")
#     print(f'Total Units Processed               {inventory}')
#     print(f'Number of Failed/Rejected Entries   {rejected_entries}')
#     print(f'Cost of Delivery                    ${cost_of_delivery:.2f}')
#     print(f'Tax Cost                            ${tax_cost:.2f}')
#     print(f'Total cost with tax                 ${cost_of_delivery + tax_cost:.2f}')
#     print("-----------------------------------------------------------")
def generate_report(inventory, rejected_entries):
    print("")
    print(f'Description                        Qty/Cost')
    print("-----------------------------------------------------------")
    print(f'Total Units Processed               {inventory}')
    print(f'Number of Failed/Rejected Entries   {rejected_entries}')
    print(f'Cost of Delivery                    ${cost_of_delivery:.2f}')
    print(f'Tax Cost                            ${tax_cost:.2f}')
    print(f'Total cost with tax                 ${cost_of_delivery + tax_cost:.2f}')
    print("-----------------------------------------------------------")



inventory, rejected_entries = get_valid_input()

# Example usage of process_delivery function with cost of delivery being $10
cost_of_delivery = process_delivery(inventory, 10)  

tax_cost = calculate_tax(cost_of_delivery)

# generate_report(inventory, rejected_entries, cost_of_delivery, tax_cost)
generate_report(inventory, rejected_entries)

