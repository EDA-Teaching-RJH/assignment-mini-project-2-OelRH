class player:
    def __init__ (self):
        self.hand = []
        self.cash = 500 #some value, will research a better one if needed
        
    def GetHand(self): 
        return self.hand
    def GetCard(self, card):
        self.hand.append(card)
    def ShowHand(self):
        print(f"Current Hand:", ", ".join(str(card) for card in self.hand)) #will show the hand to the user
    def EmptyHand(self):
        self.hand = []
    def GetCash(self):
        return self.cash
    def SetCash(self, NewCash):
        self.cash = NewCash