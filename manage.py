#Function (indentation)
import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper scissors :")
  # variable name = value (string)
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  # Dictionary {key : value}
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

choice = get_choices()
print(choice)


#List store multiple items in single variable
# food =["pizza", "carrots","eggs"]
# dinner = random.choice(food)