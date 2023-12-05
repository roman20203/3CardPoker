from Card import *
import random

class Deck(object):
    def __init__(self):
          
      self.cards = []
      self.suits = ["c","d","h","s"]
    #creates the deck
      for letter in self.suits:
        for num in range(1,14):
          self.cards.append(Card(letter,num))
    #Shuffles the deck
      random.shuffle(self.cards) 
    
    
              
    def takeTopCard(self): 
        """"
        Takes top Card and resets the deck if there are less than 4 cards in the deck
        """
        if len(self.cards)<4:
            self.reset()
        top_card=self.cards[0] 
        self.cards= self.cards[1:]
        return top_card

    def reset(self):
      """
      Calls the __init__ function again to reset the creation of the deck
      """
      self.__init__()
    
