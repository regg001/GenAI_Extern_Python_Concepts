# Counting Down With Loops. Create a program to create a countdown timer 

user_input = int(input("What number would you like to start the countdown from: "))

#print(user_input)

while user_input > 0:
   
    print(user_input, end = " ")
    user_input -= 1
    

print("Blast OFf!!!!")