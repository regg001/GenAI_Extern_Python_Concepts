# -*- coding: utf-8 -*-
"""
Created on Fri May 23 00:09:46 2025

@author: regg0
"""

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(f"100 divided by {num} is {result}.")
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
    
    
    
    

# IndexError: Attempting to access an index that doesn't exist
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Index 5 is out of range
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError: Trying to access a key that isn't in the dictionary
try:
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["address"])  # 'address' key doesn't exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError: Performing an unsupported operation between incompatible types
try:
    result = "text" + 5  # Attempting to add a string and an integer
except TypeError:
    print("TypeError occurred! Unsupported operand types.")
    
    
    
    
    
    

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter numeric values.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")