# -*- coding: utf-8 -*-
"""
Created on Fri May 23 00:10:53 2025

@author: regg0
"""
import logging

# Configure logging
logging.basicConfig(filename="error_log.txt", level=logging.ERROR, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_number(prompt):
    """Function to get valid numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def perform_operation(choice):
    """Function to execute the selected operation."""
    if choice == 5:
        print("Goodbye!")
        return False  # Exit the loop
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == 1:
        print(f"The result is: {num1 + num2}")
    elif choice == 2:
        print(f"The result is: {num1 - num2}")
    elif choice == 3:
        print(f"The result is: {num1 * num2}")
    elif choice == 4:
        try:
            result = num1 / num2
        except ZeroDivisionError as e:
            print("Oops! Division by zero is not allowed.")
            logging.error(f"ZeroDivisionError occurred: {e}")
        else:
            print(f"The result is: {result}")
        finally:
            print("End of division operation.")
    
    return True  # Continue the loop

def main():
    """Main function to display the menu and handle user selection."""
    print("Welcome to the Error-Free Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        try:
            choice = int(input("> "))
            if choice not in range(1, 6):
                raise ValueError("Invalid option. Please choose between 1 and 5.")
        except ValueError as e:
            print(e)
            continue
        
        if not perform_operation(choice):
            break  # Exit loop if user selects 5

if __name__ == "__main__":
    main()