# -*- coding: utf-8 -*-
"""
Created on Mon May 12 22:45:08 2025

@author: regg0
"""

#palidrome 



user_input = input("Please enter a word: ")


user_in_back = user_input[::-1]

print(user_in_back)


if user_in_back == user_input:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome ")