# Write a program that generates the multiplication table for any number provided by user. 

user_input = int(input("Please enter a number: "))

for i in range(1,13):
    print(f"{user_input} x {i} = {user_input * i}", end=" ") 