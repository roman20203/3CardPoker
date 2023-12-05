class Card(object):
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit
  
    def __str__(self):
      """
      Takes the cards in a rank and suit and turns it into the form of a card, rank of suit. Ex, 12,s -> queen of spades

      Inputs: rank, suit 
      Outputs: rank of suit, 
      """
      strsuit=""
      if self.suit=="c":
        strsuit= "Clubs"
      if self.suit=="d":
        strsuit= "Diamonds"
      if self.suit=="h":
        strsuit= "Hearts"
      if self.suit=="s":
        strsuit= "Spades"
      
      strstring=""
      if self.rank==1:
        strstring="Ace"
      if self.rank==11:
        strstring="Jack"
      if self.rank==12:
        strstring="Queen"
      if self.rank==13:
        strstring="King"
      if self.rank<11 and self.rank>1:
        strstring=self.rank
    
      return str(strstring) + " of " + str(strsuit)

