from Player import *

class Ante(object):
  def __init__(self):
    self.player= Player()
    self.dealer=Player()

    self.pot=0
    self.ante=0


  def getWinner(self):
    """
    Compares player and dealers hands and determines a winner

    Inputs: Users and Dealers hand represented by a number 
    Outputs: The winner after comparing which deck wins 
    """
    if self.player.getHand() > self.dealer.getHand():
      return "player"
    if self.dealer.getHand() > self.player.getHand():
      return "dealer"
    if self.dealer.getHand() == self.player.getHand():
      if self.player.greatestCard() > self.dealer.greatestCard():
        return "player"
      if self.dealer.greatestCard() > self.player.greatestCard():
        return "dealer"

  
  def play(self):
    """
    Goes through the steps of the game taking wagers from user and returning wether the player wins or loses. It only allows the user to play if there balance is above 0. 
    Input: Wagers and decisions(Raise, fold, call)
    Output: Win, Lose 
    """

    print("\nYou have",self.player.pocket,"dollars in your pocket.")

    if self.player.pocket>=1:

      Ante=int(input("Place and Ante ($):"))
      while Ante >= self.player.pocket and Ante <= self.player.pocket/2: 
        Ante=int(input("Place and Ante ($):"))




      if Ante <= self.player.pocket/2:

        self.ante=Ante
        self.pot+=Ante
        self.player.pocket-=Ante

        for i in range(3):
          self.player.addToHand()
        for i in range(3):
          self.dealer.addToHand()

        print("\nYour Hand:", str(self.player.hand[0]),", ",str(self.player.hand[1]),", ",str(self.player.hand[2]))

        print("\nEnter a wager equal or greater than the ante, If you would like to fold, enter '0' ")

        decision=int(input("\nEnter your wager: "))

        while decision > self.player.pocket: 
          decision=int(input("\nEnter your wager: "))


        


        

        if decision >= self.ante or decision == 0 :
          
          if decision>=self.ante:
            self.pot+= decision
            self.player.pocket-=decision
      
            if self.getWinner()=="player":
              self.player.pocket+= self.pot*2
              print("\nYour Hand:", str(self.player.hand[0]),", ",str(self.player.hand[1]),", ",str(self.player.hand[2]))
              print("Dealer Hand:", str(self.dealer.hand[0]),", ",str(self.dealer.hand[1]),", ",str(self.dealer.hand[2]))

              print("\nYou have won the pot!")
              print("\nYou now have",self.player.pocket,"dollars in your pocket.")
              self.playAgain()


            if self.getWinner()=="dealer":
              print("\nYour Hand:", str(self.player.hand[0]),", ",str(self.player.hand[1]),", ",str(self.player.hand[2]))
              print("Dealer Hand:", str(self.dealer.hand[0]),", ",str(self.dealer.hand[1]),", ",str(self.dealer.hand[2]))


              print("\nYou have lost the pot")
              print("\nYou now have",self.player.pocket,"dollars in your pocket.")
              self.playAgain()

          if decision==0:
            self.player.fold()
            self.pot=0
            self.ante=0
            print("\nYou have lost the pot")
            print("\nYou now have",self.player.pocket,"dollars in your pocket.")
            self.playAgain()
        else:
          print("\nSorry You have entered more money that you can afford.")
          print("\n")
          self.player.pocket+=self.ante
          self.playAgain()
      else:
          print("\nSorry You have entered more money that you can afford.")
          print("\n")
          self.playAgain()


    elif self.player.pocket<=0:
      print("Sorry you have insufficient funds")
      print("Good Bye")

  def welcome(self):
    """
    This function simply welcomes the user and explains the rules of the grades
    
    Outputs: Welcome message, rules, and amount of money they have to spend
    """

    print("\n\nWelcome to Ante")
    print("Rules: You and the dealer will both get a hand of 3 cards. Place an Ante and then you will be dealt your cards. Based on your cards you will be asked to call,raise, or fold. The best hand will win. ")
    print("\nYou first start with 200 dollars in your pocket")
    

  
  def playAgain(self):
    """
    Asks the usr wether they wod like to play again 

    Inputs: Yes or no 
    Outputs: Asks user if they would like to play again
    """
  
    again=input("Would you like to play again?(yes/no):")

    if again.lower()=="no":
      print ("\nGoodbye")
      print("You are walking away with ($)",self.player.pocket)
    elif again.lower()=="yes":

      self.pot=0
      self.ante=0
      self.player.hand=[]
      self.dealer.hand=[]
      self.play()






  