# CLASS: Human
# AUTHOR: Tyler Kanter & Cody Orr
# Create Date: August 12th, 2021

class Human():

# Properties
    def __init__(self):
        self.name = ""
        self.chosen_gesture = ""
        self.score = 0
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
    
    def __init__(self):


        super().__init__()
        pass

# Methods

    def choose_gesture(self):
        print("choose your gesture")
        index = 0
        for chosen_gesture in self.gesture_list:
            print(f'Type {index} for {chosen_gesture}')
            index += 1

    def identify_player_details(self):
        self.name = input("what is your name?")