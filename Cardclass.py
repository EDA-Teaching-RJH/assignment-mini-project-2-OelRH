class card:
    def __init__(self, rank, suit): #This defines the class of the cards
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} {self.suit}" #This returns the objects as a string

