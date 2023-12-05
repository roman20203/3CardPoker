from Deck import *

class Player(object):
    gamedeck=Deck()
    def __init__(self):
      self.hand=[]
      self.pocket=200
     
    def addToHand(self):
      """
      Calls takeTopCard and appends the top card to the players hand

      Input: Top Card from the deck
      Output:Adds the card to hand
      """

      self.hand.append(self.gamedeck.takeTopCard())

    def fold(self):
      """
      Resets players hand to empty
      outputs : Empty list
      """

      self.hand=[]
    
    def getHand(self):
      
      """
      Takes in players hand and determines wether they have a straight, flush, pair, Etc.

      inputs: the 3 cards in the players hands

      outputs: A number that represets the hand the player has
      """

      #List of ranks in hand
      rankList=[]

      rankList.append(self.hand[0].rank)
      rankList.append(self.hand[1].rank)
      rankList.append(self.hand[2].rank)
    
      #Orders the list of ranks

      end=len(rankList)
      repeat=True

      while repeat:
        repeat=False
        
        for i in range(end-1):
          if rankList[i]>rankList[i+1]:
            rankList[i],rankList[i+1]=rankList[i+1],rankList[i]
            repeat=True
        end-=1

      firstSuit=self.hand[0].suit
      secondSuit=self.hand[1].suit
      thirdSuit=self.hand[2].suit

      #Assigning number values to each hand 
      #High card = 0 
      #Pair= 1
      #Flush = 2
      #Straight = 3
      #Three of a kind = 4
      #Straight Flush = 5

      #Checks Players Hand

      if rankList[0]==rankList[1] and rankList[0] != rankList[2] or rankList[0]==rankList[2] and rankList[0] != rankList[1] or rankList[1]==rankList[2] and rankList[1] != rankList[0]:
        return 1

      #Checks if hand is Flush
      if firstSuit==secondSuit and firstSuit==thirdSuit:
        return 2

      #Checks if hand is Straight
      if rankList[0]==rankList[1]-1 and rankList[1]==rankList[2]-1:
        return 3
      
      #Checks if hand is three of a kind
      if rankList[0]==rankList[1] and rankList[0]==rankList[2]:
        return 4

      #Checks if hand is a straight flush
      if firstSuit==secondSuit and firstSuit==thirdSuit and rankList[0]==rankList[1]-1 and rankList[1]==rankList[2]-1:
        return 5
      
      else:
        return 0

     
    def greatestCard(self):
      """
      Determines the highest card in a players hand

      inputs: The 3 card ranks in the players hand 

      outputs: The greatest rank of the three
      """
      highestRank=0
      for i in range(len(self.hand)):
        if self.hand[i].rank > highestRank:
          highestRank= self.hand[i].rank
        if self.hand[i].rank == 1:
          highestRank= 14
      
      return highestRank

    

    