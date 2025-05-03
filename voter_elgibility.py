print('Hello! Welcome to the voters elgibility tester!')

age = int(input('What is your age?'))

if age >= 18:
    print('Congratulations! You are eligible to vote. Go make a difference!')
elif age <18:
    years_till_vote = 0 # Creates a new variable to calculate how long till voting age
    voting_age = 18  # Voting age is 18 so created a variable for it 
    years_till_vote = voting_age - age # Takes the difference between years_till_vote and voting_age 
    print(f'Oops! You’re not eligible yet. But hey, only {years_till_vote} more years to go!')