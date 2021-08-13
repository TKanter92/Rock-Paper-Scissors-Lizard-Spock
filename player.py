# CLASS: Player
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

class Player():

# Properties
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]

    def __str__(self):
        return self.name

# Methods
