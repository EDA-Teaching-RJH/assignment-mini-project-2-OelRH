from Deckclass import deck
from Playerclass import player
from Dealerclass import dealer

def main():
    deck.shuffle_deck()
    player =player()
    dealer = dealer()

    print(f"Welcome to the Black Parade \n Starting cash: {player.GetCash()}\n")

main()
