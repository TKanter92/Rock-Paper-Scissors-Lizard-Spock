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
        self.player_two = None


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
        input("How many players?")
        if (int(input)) == 1:
            self.single_player()
        else:
            self.multi_player()

    def single_player(self):
        self.identify_player_details()
        

    def multi_player(self):
        pass




    


    

