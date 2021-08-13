# CLASS: Human
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

from player import Player

class Human(Player):

# Properties
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
        super().__init__()


# Methods

    def choose_gesture(self):
        print("choose your gesture")
        index = 0
        for self.chosen_gesture in self.gesture_list:
            self.chosen_gesture = input(f'Type {index} for {self.gesture_list[index]}')
            index += 1
            return self.chosen_gesture

            # Not given more than the [0] option for player gesture choice. AI IS randomly selecting from list. However, the line that displays both player and AI gestures, is not reading correctly.

    def identify_player_details(self):
        self.name = input("what is your name?")