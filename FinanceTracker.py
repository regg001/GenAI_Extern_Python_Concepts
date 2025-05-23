# -*- coding: utf-8 -*-
"""
Created on Fri May 23 00:11:10 2025

@author: regg0
"""
# Finance Tracker 

# finance_tracker.py
import sys

# Dictionary to store expenses (category as key, list of tuples as values)
expenses = {}

def add_expense():
    """Function to add an expense."""
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")

        # Store expense in dictionary
        if category not in expenses:
            expenses[category] = []
        expenses[category].append((description, amount))

        print("Expense added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses():
    """Function to view all expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    for category, expense_list in expenses.items():
        print(f"\nCategory: {category}")
        for description, amount in expense_list:
            print(f"  - {description}: ${amount:.2f}")

def view_summary():
    """Function to view total expenses by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nSummary:")
    for category, expense_list in expenses.items():
        total = sum(amount for _, amount in expense_list)
        print(f"{category}: ${total:.2f}")

def main():
    """Main function for the menu-driven approach."""
    print("Welcome to the Personal Finance Tracker!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                view_summary()
            elif choice == 4:
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid option. Please choose between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()