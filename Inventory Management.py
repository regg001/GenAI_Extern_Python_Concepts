# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:28:52 2025

@author: regg0
"""

# Inventory Management Program 
# key : quantity , price 
# Inventory Management Program
# Key: quantity, price

inventory = {
    'apple': (10, 2.5),
    'banana': (20, 1.2)
}

while True:
    user_input = input("Would you like to add (A), remove (R), update (U), or exit (E)? ").upper()

    if user_input == 'A':
        add_item = input('What would you like to add: ').strip()
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        inventory[add_item] = (quantity, price)  # Adding the item

    elif user_input == 'R':
        remove_item = input('Which item would you like to remove: ').strip()
        if remove_item in inventory:
            inventory.pop(remove_item)
        else:
            print("Item not found in inventory.")

    elif user_input == 'U':
        update_item = input("Which item would you like to update: ").strip()
        if update_item in inventory:
            quantity, price = inventory[update_item]  # Retrieve current values
            decision = input("Update quantity (Q) or price (P)? ").upper()

            if decision == 'Q':
                quantity = int(input("Enter the new quantity: "))
            elif decision == 'P':
                price = float(input("Enter the new price: "))
            else:
                print("Invalid option.")

            inventory[update_item] = (quantity, price)  # Update the selected value

            decision2 = input("Would you also like to update the other attribute? (Y/N) ").upper()
            if decision2 == 'Y':
                if decision == 'Q':  # User initially updated quantity
                    price = float(input("Enter the new price: "))
                else:  # User initially updated price
                    quantity = int(input("Enter the new quantity: "))
                inventory[update_item] = (quantity, price)

        else:
            print("Item not found in inventory.")

    elif user_input == 'E':
        break  # Exiting the loop

    else:
        print("Invalid choice. Please try again.")
for item, (quantity, price) in inventory.items():
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")
