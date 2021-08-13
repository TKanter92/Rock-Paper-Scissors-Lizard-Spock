# CLASS: Game
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

from human import Human
from player import Player
from ai import AI

class Game:

# Properties
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()
        self.computer_player = AI()


# Methods
    def run_game(self):
        self.welcome_message()
        self.rules()
        self.setup_players()

    def welcome_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

    def rules(self):
        print("Each player will select their gesture in hopes of beating their opponent. Each game will consist of up to 3 rounds, with a winner being declared after having won two of the three rounds.")

    def setup_players(self):
        number_of_players = input("How many players?")
        if (int(number_of_players)) == 1:
            self.single_player()
        else:
            self.multi_player()

    def single_player(self):
        self.player_one.identify_player_details()
        print(f'Hello {self.player_one.name}!')
        self.player_one.choose_gesture()
        self.computer_player.random_gesture()
        print(f'{self.player_one} has chosen {self.player_one.choose_gesture}')
        print(f'{self.computer_player} has chosen {self.computer_player.random_gesture}')

    
        

    def multi_player(self):
        pass



    def game_rounds(self):
        Human.choose_gesture()
    


    

