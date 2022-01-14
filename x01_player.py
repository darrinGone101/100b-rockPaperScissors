
def playerChoice():
  x = input("rock paper or scissors: ")
  if x == "rock":
    value = 0
  if x == "paper":
    value = 1
  if x == "scissors":
    value = 2
  
  return value


if __name__ == "__main__":
  player = playerChoice()
  print(player)
