# CLASS: AI
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021
import random

class AI():

# Properties

    def __init__(self):
        self.name = "Computer"
        self.chosen_gesture = ""
        self.score = 0
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
        

# Methods

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        
    def __str__(self):
        return self.name
