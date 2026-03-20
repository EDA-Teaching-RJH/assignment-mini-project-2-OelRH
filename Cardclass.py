import random

class card:
    def __init__(self, suit, rank): #This defines the class of the cards
        self.suit = suit
        self.number = rank

    def __str__(self):
        return f"{self.suit} {self.number}" #This returns the objects as a string
   


