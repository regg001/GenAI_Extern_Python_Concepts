# -*- coding: utf-8 -*-
"""
Created on Mon May 12 23:59:16 2025

@author: regg0
"""

#password strength checker

user_input = input("Please input the password you would like to check: ")

if len(user_input) >= 8:
    if any(char.isdigit() for char in user_input):
        if any(not char.isalnum() for char in user_input):  # Ensures at least one special character
            print("Awesome! Your password fulfills all requirements!")
        else:
            print("Your password needs a special character!")
    else:
        print("Your password needs to contain a number!")
else:
    print("Your password is less than 8 characters!")