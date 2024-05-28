#Function (indentation)
import random

def get_choices():
    # variable name = value (string)
  player_choice = input("Enter a choice (rock, paper scissors :")
  #List store multiple items in single variable
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  # Dictionary {key : value}
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

#parsing the data in function
def check_win(player, computer):
    #Concatenating
    # print("You chose" + player + ", Computer chose" + computer)
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Player Win"
        else:
            return "You Lose"
    elif player == "scissor":
        if computer == "paper":
             return "Player Win"
        else:
            return "You Lose"
    elif player == "paper":
        if computer == "rock":
             return "Player Win"
        else:
            return "You Lose"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)

# To get to the dic_data
# choices = {"player" : "rock" , "computer" : "paper"}
# p_choice = choices["player"]