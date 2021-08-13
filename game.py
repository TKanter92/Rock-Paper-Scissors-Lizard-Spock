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
        self.game_rounds()

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
            # Maybe at some point we could add in computer vs. computer as an option of "0" players? 
        else:
            self.player_one = Human(1)
            self.player_two = Human(2)

    def game_rounds(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            print(f"Thanks {self.player_one}!")
            self.player_two.choose_gesture()
            print(f"Thanks {self.player_two}!")
            print("Let's begin!")
            self.game_logic()
        else:
            self.display_winner()



    def game_logic(self):
        print(f'{self.player_one} has chosen {self.player_one.chosen_gesture}')
        print(f'{self.player_two} has chosen {self.player_two.chosen_gesture}')
        while self.player_one.chosen_gesture == "Rock":
            if self.player_two.chosen_gesture == "Rock":
                print("It's a Draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Paper":
                print(f'{self.player_two} wins!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Scissors":
                print(f'{self.player_one} wins!')
                self.player_one.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Lizard":
                print(f'{self.player_one} wins!')
                self.player_one.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Spock":
                print(f'{self.player_two} wins!')
                self.player_two.score + 1
                self.game_rounds()
        while self.player_one.chosen_gesture == "Paper":
            if self.player_two.chosen_gesture == "Rock":
                print(f'{self.player_one} wins!')
                self.player_one.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Paper":
                print(f"It's a draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Scissors":
                print(f'{self.player_two} has won!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Lizard":
                print(f'{self.player_two} has won!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Spock":
                print(f'{self.player_one} has won!')
                self.player_one.score + 1
                self.game_rounds()
        while self.player_one.chosen_gesture == "Scissors":
            if self.player_two.chosen_gesture == "Rock":
                print(f'{self.player_two} has won!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Paper":
                print(f'{self.player_one} has won!')
                self.player_one.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Scissors":
                print(f"It's a draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Lizard":
                print(f'{self.player_two} has won!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Spock":
                print(f'{self.player_two} has won!')
                self.player_two.score + 1
                self.game_rounds()
        while self.player_one.chosen_gesture == "Lizard":
            if self.player_two.chosen_gesture == "Rock":
                print(f'{self.player_two} wins!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Paper":
                print(f'{self.player_one} wins!')
                self.player_one.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Scissors":
                print(f'{self.player_two} wins!')
                self.player_two.score + 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Lizard":
                print(f"It's a draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "Spock":
                print(f'{self.player_one} wins!')
                self.player_one.score + 1
                self.game_rounds()
        while self.player_one.chosen_gesture == "Spock":
            if self.player_two.chosen_gesture == "Rock":
                print(f'')
            elif self.player_two.chosen_gesture == "Paper":
                print(f'')
            elif self.player_two.chosen_gesture == "Scissors":
                print(f'')
            elif self.player_two.chosen_gesture == "Lizard":
                print(f'')
            elif self.player_two.chosen_gesture == "Spock":
                print(f"It's a draw! Play again!")


        # function that identifies a winner based on the outline provided (about which gesture beats what) in user stories should be placed here
        # some sort of display or print should then be placed here, to identify the winner of the round
        # function to increase the count for winner should be placed here
        # If the score has not reached 2 for any player, another round should start. If 2 wins have taken place, the round should be over and announced here. (LOOP?)


    def display_winner(self):
        if self.player_one.score == 2 or self.player_two.score == 2:
            print(f"Congratulations, {self.player_one or self.player_two}! You have won the game!")
            print("Game Over")

   
    


    

