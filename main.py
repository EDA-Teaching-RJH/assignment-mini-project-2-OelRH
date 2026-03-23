from Deckclass import deck
from Playerclass import player
from Dealerclass import dealer
from Decksclass import decks
from time import sleep

def main():
    deck = decks(6)
    deck.shuffle()
    player =player()
    dealer = dealer()

    print(f"Welcome to the Black Parade \n Starting cash: {player.cash()}\n ")

    while True:
        print(f"Current cash: {player.GetCash()}\n ")

        bet = handle_bet(player)
        player.SetCash()
   
        player.showhand()
        dealer.showhand(1)








main()
