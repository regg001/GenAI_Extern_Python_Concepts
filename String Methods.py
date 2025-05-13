# -*- coding: utf-8 -*-
"""
Created on Mon May 12 22:03:22 2025

@author: regg0
"""


string1 = " hello, python world! "

stripped_string = string1.strip()

print(stripped_string)


cap_string = stripped_string.capitalize()

print(cap_string)

replaced_string = cap_string.replace('world', 'universe')

print(replaced_string)

upper_string = replaced_string.upper()

print(upper_string)