# CLASS: AI
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021
import random
from player import Player
class AI(Player):

# Properties

    def __init__(self):
        super().__init__()
        

# Methods

    def random_gesture(self):
        chosen_gesture = print(random.choice(self.gesture_list))
        return chosen_gesture
        

