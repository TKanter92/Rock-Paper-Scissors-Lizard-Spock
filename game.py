# CLASS: Game
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

from human import Human
from player import Player
from ai import AI

class Game():

# Properties
    def __init__(self):
        self.player_one = None
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
        number_of_players = input("Please enter the number of players.")
        if (int(number_of_players)) == 1:
            self.player_one = Human(1)
            self.player_two = AI()
        elif (int(number_of_players)) == 2:
            self.player_one = Human(1)
            self.player_two = Human(2)
        else:
            print("Not a valid number of players. Please re-enter number of players.")
            self.setup_players()

    def game_rounds(self):
        if (self.player_one.score < 2) and (self.player_two.score < 2):
            self.player_one.choose_gesture()
            print(f"Thanks {self.player_one}!")
            self.player_two.choose_gesture()
            print(f"Thanks {self.player_two}!")
            self.game_logic()
        else:
            self.display_winner()



    def game_logic(self):
        print(f'{self.player_one} has chosen {self.player_one.chosen_gesture}')
        print(f'{self.player_two} has chosen {self.player_two.chosen_gesture}')
        if self.player_one.chosen_gesture == "rock":
            if self.player_two.chosen_gesture == "rock":
                print("It's a Draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "paper":
                print(f'{self.player_two} wins!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "scissors":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "lizard":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "spock":
                print(f'{self.player_two} wins!')
                self.player_two.score += 1
                self.game_rounds()
        if self.player_one.chosen_gesture == "paper":
            if self.player_two.chosen_gesture == "rock":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "paper":
                print(f"It's a draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "scissors":
                print(f'{self.player_two} has won!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "lizard":
                print(f'{self.player_two} has won!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "spock":
                print(f'{self.player_one} has won!')
                self.player_one.score += 1
                self.game_rounds()
        if self.player_one.chosen_gesture == "scissors":
            if self.player_two.chosen_gesture == "rock":
                print(f'{self.player_two} has won!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "paper":
                print(f'{self.player_one} has won!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "scissors":
                print(f"It's a draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "lizard":
                print(f'{self.player_one} has won!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "spock":
                print(f'{self.player_two} has won!')
                self.player_two.score += 1
                self.game_rounds()
        if self.player_one.chosen_gesture == "lizard":
            if self.player_two.chosen_gesture == "rock":
                print(f'{self.player_two} wins!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "paper":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "scissors":
                print(f'{self.player_two} wins!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "lizard":
                print(f"It's a draw! Play again!")
                self.game_rounds()
            elif self.player_two.chosen_gesture == "spock":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
        if self.player_one.chosen_gesture == "spock":
            if self.player_two.chosen_gesture == "rock":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "paper":
                print(f'{self.player_two} wins!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "scissors":
                print(f'{self.player_one} wins!')
                self.player_one.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "lizard":
                print(f'{self.player_two} wins!')
                self.player_two.score += 1
                self.game_rounds()
            elif self.player_two.chosen_gesture == "spock":
                print(f"It's a draw! Play again!")
                self.game_rounds()

    def display_winner(self):
        if self.player_one.score == 2:
            print(f"Congratulations, {self.player_one}! You have won the game!")
        else:
            print(f"Congratulations {self.player_two}! You have won the game!")
        print("Game Over")
        self.play_again()
            
    def play_again(self):
        print("Would you like to play again? Type 'yes' or 'no'")
        user_input = input()
        if user_input == "yes":
            self.run_game()
        if user_input == "no":
            print("Thank you for playing. Come back soon.")
        else:
            print("Not a valid option, please try again.")
            self.play_again()


   
    


    

