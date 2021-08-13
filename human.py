# CLASS: Human
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

from player import Player

class Human(Player):

# Properties
    def __init__(self, player_number):
        super().__init__()
        self.identify_player_one_details(player_number)


# Methods

    def choose_gesture(self):
        print("Please choose your gesture")
        index = 0
        for element in self.gesture_list:
            print(f'Type {index} for {element}')
            index += 1
        user_input = input()
        self.chosen_gesture = self.gesture_list[user_input]

            # Not given more than the [0] option for player gesture choice. AI IS randomly selecting from list. However, the line that displays both player and AI gestures, is not reading correctly.

    def identify_player_one_details(self, player_number):
        self.name = input(f'What is the name for player number {player_number}?')
        print(f'Hello {self.name}!')

   

    def __str__(self):
        return self.name