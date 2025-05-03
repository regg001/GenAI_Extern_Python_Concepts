print('Hello! Welcome to the number checker program! \nThis program will check whether a number is positive, negative or zero.')

user_num = int(input('Please input the number you would like to check: '))

if user_num > 0:
    print('This number is positive. Awesome!')
elif user_num <0:
    print('This number is negative. Better luck next time!')
else:
    print('Zero it is! A perfect balance!') 