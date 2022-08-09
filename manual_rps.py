import random 


class RockPaperScissors():
    def __init__(self):
        self.guess = input()

    def get_computer_choice(self):
        self.computer_guess = input()
    
    def get_user_choice(self):
        self.user_choice = input()
