import random 


def get_computer_choice():
    computer_guess = ['Rock', 'Paper', 'Scissors']
    return random.choice(computer_guess)
    
def get_user_choice():
    user_guess = input('Please enter a guess; either Rock, Paper, Scissors: ')
    return user_guess

#def 
