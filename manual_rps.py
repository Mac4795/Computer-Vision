import random 


def get_computer_choice():
    computer_guess = ['Rock', 'Paper', 'Scissors']
    return random.choice(computer_guess)
    
def get_user_choice():
    user_guess = input('Please enter a guess; either Rock, Paper or Scissors: ')
    return user_guess.capitalize()

def get_winner(computer, player):
    print(f'Computer chose {computer}')
    if player == 'Rock' and computer == 'Scissors' or player == 'Paper' and computer == 'Rock' or player == 'Scisors' and computer == 'Paper':
        return 'Congratulations! You beat the computer!'
    elif player == computer:
        return 'Looks like its a draw.'
    else:
        return 'The computer has won. Better luck next time.'

def play():
    player = get_user_choice()
    computer = get_computer_choice()
    print(get_winner(computer, player))

play()