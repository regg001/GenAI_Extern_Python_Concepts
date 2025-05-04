import random

number_to_guess = random.randint(1, 100)
tries = 0
tries_allowed = 10

print("Welcome to Number Guesser! You have 10 tries to guess the number.")

while tries < tries_allowed:  # Ensures game stops after max attempts
    user_guess = int(input("Please guess a number (between 1 and 100): "))

    tries += 1
    tries_remaining = tries_allowed - tries

    if user_guess > number_to_guess:
        print(f"Too high! Try again... Tries Remaining: {tries_remaining}")
    elif user_guess < number_to_guess:
        print(f"Too low! Try again... Tries Remaining: {tries_remaining}")
    else:
        if tries_remaining == 0:  
            print("Congratulations!! You guessed it right on the last try!")
        else:
            print(f"Congratulations! You guessed the number! It took you {tries} tries.")
        break  # Exit loop if guessed correctly

else:  # Executes only when user runs out of tries
    print(f"You ran out of tries. Game Over! The correct number was {number_to_guess}. Better luck next time!")
    