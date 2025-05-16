# -*- coding: utf-8 -*-
"""
Created on Thu May 15 19:56:30 2025

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

# Example usage
fact_result = factorial(5)
fib_result = fibonacci(6)

print(f"Factorial of 5 is {fact_result}. The 6th Fibonacci number is {fib_result}.")