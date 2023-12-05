from Player import *

class PairPlus(object):
  def __init__(self):
    self.player= Player()
    self.dealer=Player()

    self.wager=0
  
  def getPayout(self):
    """
    Determines multiplying factor based on the players hand 

    Inputs: Players hand represented by a number

    Outputs: A number that the winnings will be multiplied by
    """

    hand=self.player.getHand()
    #Assigning number values to each hand 
    #High card = 0 
    #Pair= 1
    #Flush = 2
    #Straight = 3
    #Three of a kind = 4
    #Straight Flush = 5
    if hand==0:
      #lose money
      return 0
    if hand==1:
      #return money
      return 1
    if hand==2:
      #triple money
      return 3
    if hand==3:
      #6 times money
      return 6
    if hand==4:
      #30 times
      return 30
    if hand==5:
      return 40

  def play(self):
    """
    Goes through the game step by step, accepting the users decisions 

    Inputs: user inputs wagers

    Output: outputs the users cards, and wether they won or lost money 
    """

    if self.player.pocket>0:
      print("\nYou have",self.player.pocket,"dollars in your pocket.")

      amount=int(input("\nEnter an amount you would like to wager ($):"))

      if amount<=self.player.pocket:

        self.wager=amount
        self.player.pocket-= amount

        for i in range(3):
          self.player.addToHand()
    
        print("\nYour Hand:", str(self.player.hand[0]),", ",str(self.player.hand[1]),", ",str(self.player.hand[2]))
    
        result=self.getPayout()

        if result==0:
          print("You have lost your wager.")
          print("\nYou now have",self.player.pocket,"dollars in your pocket.")
          self.playAgain()

        if result==1:
          self.player.pocket += self.wager
          print("You have been given back your wager")
          print("\nYou now have",self.player.pocket,"dollars in your pocket.")
          self.playAgain()
        if result==2:
          self.player.pocket += self.wager *3
          print("You have tripled your wager")
          print("\nYou now have",self.player.pocket,"dollars in your pocket.")
          self.playAgain()
        if result==3:
          self.player.pocket += self.wager * 6
          print("You have made 6 times your wager")
          print("\nYou now have",self.player.pocket,"dollars in your pocket.")
          self.playAgain()
        if result==4:
          self.player.pocket += self.wager * 30
          print("You have made 30 times your wager")
          print("\nYou now have",self.player.pocket,"dollars in your pocket.")
          self.playAgain()
        if result==5:
          self.player.pocket += self.wager * 40
          print("You have made 40 times your wager")
          print("\nYou now have",self.player.pocket,"dollars in your pocket.")
          self.playAgain()
      else:
        print("Sorry you have input more money that you have.")
        
        self.playAgain()
    elif self.player.pocket<=0:
      print("Sorry you have insufficient funds")
      


  def welcome(self):
    """
    Welcomes the user and explains the rules of the game 
    
    outputs: Welcome and rules 
    """

    print("\nWelcome to Pair Plus")
    print("\nIn this game, you are gambling that you will be dealt a pair, or a higher hand")

  def playAgain(self):
    
    """
    Asks the user wether they would like to play again after they win or lose 

    inputs: yes or no 
    outputs: Woudl you like to play again

    """

    #Asks the user if they want to play again 
    again=input("Would you like to play again?(yes/no):")

    if again.lower()=="no":
      print ("Goodbye")
      print("You are walking away with",self.player.pocket)
    elif again.lower()=="yes":
      self.wager=0
      self.player.hand=[]
      self.play()

  

