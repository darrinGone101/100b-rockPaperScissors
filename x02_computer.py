#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""
import random
def computerChoice():
  x = random.randint(0,2)
  if x == 0:
    value = "rock"
  if x == 1:
    value = "paper"
  if x == 2:
    value = "scissors" 
  return value


if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
