# CLASS: Game
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

from human import Human
from player import Player
from ai import AI

class Game:

# Properties
    def __init__(self):
        self.player_one =None
        self.player_two = None


# Methods
    def run_game(self):
        self.welcome_message()
        self.rules()
        self.setup_players()
        self.single_player()

    def welcome_message(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

    def rules(self):
        print("Each player will select their gesture in hopes of beating their opponent. Each game will consist of up to 3 rounds, with a winner being declared after having won two of the three rounds.")

    def setup_players(self):
        number_of_players = input("How many players?")
        if (int(number_of_players)) == 1:
            self.player_one = Human(1)
            self.player_two = AI()
        if (int(number_of_players)) > 2:
            print("Not a valid number of players. Please re-enter number of players.")
            self.setup_players()
        else:
            self.player_one = Human(1)
            self.player_two = Human(2)

    def single_player(self):
        
        
        self.player_one.choose_gesture()
        print(f"Thanks {self.player_one}!")
        self.player_two.choose_gesture()
        print(f"Thanks {self.player_two}!")
        print(f'{self.player_one.chosen_gesture} has chosen {self.player_one.chosen_gesture}')
        self.computer_player.random_gesture()
        print(f'{self.computer_player} has chosen {self.computer_player.random_gesture}')
        # function that identifies a winner based on the outline provided (about which gesture beats what) in user stories should be placed here
        # some sort of display or print should then be placed here, to identify the winner of the round
        # function to increase the count for winner should be placed here
        # If the score has not reached 2 for any player, another round should start. If 2 wins have taken place, the round should be over and announced here. (LOOP?)

    
        



    def scoring(self):
        # identify what beats what and then display winner
        pass



   
    


    

