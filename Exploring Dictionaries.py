# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:37:18 2025

@author: regg0
"""

my_dict = {'name' : 'reginal' , 'age' : 21 , 'city' : 'Queens NY'}

my_dict.update({'favorite color' : 'green'})

print(my_dict)

my_dict.update({'city' : 'Long Island'})
key_list = []

key_list = list(my_dict.keys())


value_list = list(my_dict.values())






print("Keys:", ", ".join(my_dict.keys()))

print("Values:", ", ".join(str(value) for value in my_dict.values()))