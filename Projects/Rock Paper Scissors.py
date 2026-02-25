import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
   player = input("Rock, Paper, or Scissors: ").lower()    # Reducing the size of letters

print("You chose", player)
print("Computer chose", computer)


if player == computer:
    print("Draw")
elif player == "rock":
    if computer == "paper":
        print("You Lose")
    elif computer == "scissors":
        print("You Win")
elif player == "paper":
    if computer == "rock":
        print("You Win")
    elif computer == "scissors":
        print("You Lose")
elif player == "scissors":
    if computer == "rock":
        print("You Lose")
    elif computer == "paper":
        print("You Win")
