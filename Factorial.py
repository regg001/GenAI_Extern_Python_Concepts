# Program to calculate the factorial of a number given user input 

user_input = int(input("What number would you like to check: "))
result = 1
for number in range(1, user_input +1 ):
    result *= number 


print(result)