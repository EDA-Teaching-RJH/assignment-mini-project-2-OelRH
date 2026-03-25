from Playerclass import player

class dealer(player): #The dealer just shows their hand after the player
    def showhand(self, round_no = 0):
        if round_no == 1:
            print("Dealer's hand:", self.hand[1])
        else:
            print("Dealer's hand:", self.hand)


