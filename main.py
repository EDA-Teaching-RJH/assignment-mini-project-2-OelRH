from Deckclass import deck
from Playerclass import player
from Dealerclass import dealer
from Decksclass import decks
from time import sleep

values = dict(zip(deck.ranks,[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))

def main():
    deck = decks(6)
    deck.shuffle()
    Player = player()
    Dealer = dealer()

    print(f"Welcome to the Black Parade \n Starting cash: {Player.cash}\n ")

    while True:
        print(f"Current cash: £{Player.GetCash()}\n ")

        bet = handle_bet(Player)
        Player.SetCash(Player.GetCash() - bet)
        
        for _ in range(2):
            Player.GetCard(deck.deal())
            dealer.GetCard(deck.deal())

        Player.showhand()
        dealer.showhand(1)

        Player_hand_value = calculate_hand_value(Player.GetHand())

        if Player_hand_value == 21:
            handle_blackjack(Player, Dealer, deck, bet)

            player.EmptyHand()
            dealer.EmptyHand()

            if handle_continual_play():
                continue
            else:
                return
        
        while Player_hand_value < 21:
            next_move = input("Press H to hit or S to stand ")

            if next_move.lower() == "s":
                Dealer_hand_value = handle_dealer(dealer.GetHand(), Dealer, deck)

                if Dealer_hand_value == 21:
                    sleep(0.5)
                    print("BLACK JACK! House wins ")
                
                    if player.GetCash() == 0:
                        print("No more money, you lose!")
                        return
                    
                elif Dealer_hand_value > 21:
                    sleep(0.5)
                    print("Dealer bust, Player wins!")
                    player.SetCash(player.GetCash() + (bet * 2))
                
                elif Dealer_hand_value < player_hand_value:
                    sleep(0.5)
                    print("Player wins!")
                    player.SetCash(player.GetCash() + (bet * 2))
                     
                elif Dealer_hand_value > Player_hand_value:
                    sleep(0.5)
                    print("House wins!")
                    
                    if player.GetCash() == 0:
                        print("No more money, you lose!")

                elif Dealer_hand_value == player_hand_value:
                    sleep(0.5)
                    print("Push, draw")
                    player.SetCash(player.GetCash() + bet)

                player.EmptyHand()
                dealer.EmptyHand()
                
                if handle_continual_play():
                    break
                else:
                    return
            
            if next_move.lower() == "h":
                player.GetCard(deck.deal())
                player.ShowHand()
                player_hand_value = calculate_hand_value(player.GetHand())

                print(f"Hand's Value: {player_hand_value}")

                if Player_hand_value == 21:
                    handle_blackjack(player, dealer, deck, bet)
                    
                if Player_hand_value > 21:
                    print("Bust! House wins!")
                    
                    if player.GetCash() == 0:
                        print("No more money, you lose!")
                        return

                if Player_hand_value >= 21:
                    player.EmptyHand()
                    dealer.EmptyHand()

                    if handle_continual_play():
                        break
                    else:
                        return


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

def handle_blackjack(player, dealer, deck, bet):
    dealer_hand_value = handle_dealer(dealer.GetHand(), dealer, deck)

    if dealer_hand_value == 21:
        sleep(0.5)
        print("Push (Tie)")
        player.SetCash(player.GetCash() + bet)

    else:
        sleep(0.5)
        print("BLACK JACK!")
        player.SetCash(player.GetCash() + (bet * 2))

def handle_dealer(hand, dealer, deck):
    sleep(0.5)
    dealer.ShowHand()
    hand_value = calculate_hand_value(hand)

    while hand_value < 17:
        dealer.GetCard(deck.deal())
        hand_value = calculate_hand_value(hand)
        sleep(0.5)
        dealer.ShowHand()

    return hand_value

def handle_continual_play():
    while True:
        keep_playing = input("Press Q to Quit or C to Continue: ")

        if keep_playing.lower() != "q" and keep_playing.lower() != "c":
            print("please enter q or c")
        else:
            if keep_playing.lower() == "q":
                return False
            if keep_playing.lower() == "c":
                return True
            










main()
