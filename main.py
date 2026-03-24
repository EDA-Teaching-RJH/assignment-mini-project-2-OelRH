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

def handle_bet(player):
    while True:
        bet = int(input("Please enter amount of cash you wish to bet: £"))
        if bet > player.GetCash():
            print("Please bet an amount within your current cash limit. \n")
        elif bet <= 0:
            print("please bet a positive amount of money. \n")
        else:
            break

        player.showhand()
        dealer.showhand(1)








main()
