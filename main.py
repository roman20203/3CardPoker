from Ante import *
from PairPlus import *

def main():
  """
  Asks use what game they would like to play
  """
  print("Welcome to 3 Card poker")

  choice=input("Would you like to play Ante or Pair Plus?(a/p): ")

  if choice.lower()=="a":
    antegame=Ante()
    antegame.welcome()
    antegame.play()
  if choice.lower()=="p":
    ppGame=PairPlus()
    ppGame.welcome()
    ppGame.play()

main()