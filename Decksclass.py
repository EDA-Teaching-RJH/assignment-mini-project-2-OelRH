from Deckclass import deck

class decks(deck):
    def __init__(self, no_of_decks):
        self.cards = []

        for _ in range(no_of_decks):
            d = deck()

            for card in d.cards:
                self.cards.append(card)

