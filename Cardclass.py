class card:
    def __init__(self, suit, rank): #This defines the class of the cards
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} {self.suit}" #This returns the objects as a string

