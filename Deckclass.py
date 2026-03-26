import random
from Cardclass import card


class deck:

    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #This is a list of cards in a deck
    suits =  ["♦", "♥", "♠", "♣"]

    def __init__(self): 
        self.cards = []

        for rank in deck.ranks: 
            for suit in deck.suits:
                self.cards.append(card(suit,rank))
                

    def shuffle(self): #using an already built function, this easily shuffles the list of cards in deck
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()




