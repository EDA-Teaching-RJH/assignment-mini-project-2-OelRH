from Deckclass import deck
from Playerclass import player
from Dealerclass import dealer
from Decksclass import decks
from time import sleep

values = dict(zip(deck.ranks,[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))

def main():
    deck = decks(6)
    deck.shuffle()
    player = player()
    dealer = dealer()

    print(f"Welcome to the Black Parade \n Starting cash: {player.cash}\n ")

    while True:
        print(f"Current cash: £{player.GetCash()}\n ")

        bet = handle_bet(player)
        player.SetCash(player.GetCash() - bet)
        
        for _ in range(2):
            player.GetCard(deck.deal())
            dealer.GetCard(deck.deal())

        player.showhand()
        dealer.showhand(1)

        player_hand_value = calculate_hand_value(player.GetHand())

        if player_hand_value == 21:
            handle_blackjack(player, dealer, deck, bet)

def handle_bet(player):
    while True:
        bet = int(input("Please enter amount of cash you wish to bet: £"))
        if bet > player.GetCash():
            print("Please bet an amount within your current cash limit. \n")
        elif bet <= 0:
            print("please bet a positive amount of money. \n")
        else:
            print()
            return bet

def calculate_hand_value(hand):
    hand_value = 0
    num_of_aces = 0

    for card in hand:
        if card.rank == "A":
            hand_value += 11
            num_of_aces += 1
        else: 
            hand_value += values[card.rank]

    while hand_value > 21 and num_of_aces > 0:
        hand_value -= 10
        num_of_aces -= 1
    
    return hand_value










main()
