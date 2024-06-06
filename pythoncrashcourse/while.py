## for loop execute one time for each item
## while loop run as long as under a certain condition

# num = 1
# while num < 6:
#     print(num)
#     num += 1

# prompt = "Repeat until you say quit"
# prompt += "\n Enter 'quit' to end : "

# mes =""
# while mes != "quit":
#     mes = input(prompt)
#     print(mes)
    
# prompt = "Repeat until you say quit"
# prompt += "\n Enter 'quit' to end : "

# active = True
# while active:
#     mes = input(prompt)
#     if mes =="quit":
#         active = False
#     else:
#         print(mes)

## Using break to exit

# prompt = "Please enter the name of city you have visited"
# prompt += "\n Enther 'quit' if you finished "

# while True: # while True run until this code meet break
#     city = input(prompt)
#     if city =="quit":
#         break
#     else:
#         print(f"I'd been to {city.title()}")

## break : break out a loop entirely without executing the rest of the code
## continue : return to the beginning
# num = 0
# while num < 10 :
#     num +=1
#     if num % 2 == 0:
#         continue
    
#     print(num)


## Practice
# mes = "Put the toppings you want"
# mes += "If you finish to add enter 'quit' "

## 1
# while True:
#     order = input(mes)
#     if order == "quit":
#         break
#     else:
#         print(f"You put the {order} do you want some more?")

## 2
# order = input(mes)
# while order != "quit":
#     print(f"You put {order}")
#     if order == "quit":
#         break

## In here i tried to make break with string but it needs to make try except

# while True:
#     age = input("How old are you? if you want to finish enter over '100'")
#     age = int(age)
#     if age < 3 :
#         print("it's free")
        
#     elif age < 12 :
#         print("$10")
#     elif age < 101:
#         print("$15")
#     else:
#         break;

## To keep track various user and data need to use dictionary or list with while

# unconfirmed_user = ["alice", "brian", "cand"]
# confirmed_user = []
# while unconfirmed_user:
#     current = unconfirmed_user.pop()
    
#     print(f"Verifying:{current}")
#     confirmed_user.append(current)
    
# for confirmed in confirmed_user:
#     print(confirmed.title())

# print(unconfirmed_user)

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")

# print(pets)

## Filling a dicitionaries with user input
# responses = {}
# poling_acttive = True # Set a flag to indicate that polling is active.
# while poling_acttive:
#     #prompt for the key : username and value :user response
#     name = input("What is your name : ")
#     response = input("which food is your best? : ")
    
#     #Storing
#     responses[name] = response
#     repeat = input("Would you like to let another person respond ? (Y/N)")
#     if repeat.lower() == "no" or repeat.lower() =="n" :
#         poling_acttive = False
   

# print("==============Results============")
# for name,response in responses.items():
#     print(f"{name.title()} like {response.title()}")



## Practice
# sandwichies = ["tuna sandwich", "peanut sandwich","meat sandwich"]
# finished_sandwichies  = []

# while sandwichies:
#     order = sandwichies.pop()
#     print(f"We are doing {order}")
#     finished_sandwichies.append(order)
# for finished in finished_sandwichies:
#     print(f"{finished} it's done")

# sandwichies = ["tuna sandwich", "peanut sandwich", "bull" , "bull" , "meat sandwich","bull"]
# while "bull" in sandwichies:
#     sandwichies.remove("bull")
#     print(sandwichies)

buckets = {}
polling = True
while polling :
    user = input("What is your name : ")
    place = input("Please say the place where you want to go at first : ")
    
    buckets[user] = place
    
    repeat = input("Do you want to keep polling the data? (Y/N)")
    if repeat.lower() == "no" or repeat.lower() == "n":
        polling = False

print("===============Results===========")
for name , place in buckets.items():
    print(f"{name.title()} want to go {place.title()}")    