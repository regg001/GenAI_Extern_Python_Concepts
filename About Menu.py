# -*- coding: utf-8 -*-
"""
Created on Sun May 18 16:22:04 2025

@author: regg0

"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

while True:
    print("""
    Welcome! Please choose a number:
    1. Calculate the factorial of a number
    2. Find the nth Fibonacci number
    3. Exit
    """)

    user_input = input("Enter your choice: ")

    if user_input == '1':
        num = int(input("What number would you like to calculate the factorial for? "))
        fact_result = factorial(num)
        print(f"Factorial of {num} is {fact_result}.")

    elif user_input == '2':
        num = int(input("What number will we be using? "))
        fibonacci_re = fibonacci(num)
        print(f"The {num}th Fibonacci number is {fibonacci_re}.")

    elif user_input == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")