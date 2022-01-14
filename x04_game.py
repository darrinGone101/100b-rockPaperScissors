#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *
def game():
  x = playerChoice()
  y = computerChoice()
  if playerWins(y,x) == 0:
      print ("Its a tie")
  if playerWins(y,x) == -1: 
    print ("you lost")
  if playerWins(y,x) == 1:
    print ("you win")


if __name__ == "__main__":
  game()

