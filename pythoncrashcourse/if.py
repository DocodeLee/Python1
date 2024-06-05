## if statement run when the condition is true
# cars =["audi", "bentli", "hyunddai","bmw"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.lower())
        
## Checking equality
# num = "audi"
# print(num == "bmw")

## python detect the upper case also
# num = "One"
# print(num == "one")
# print(num.lower() == "one" ) # True

## Checking for inequality

# food = "mushroom"
# if food != "salt":
#     print("I need the salt")

# Numercial comparison
# age = 19
# age < 21 #True
# age <= 19 #True
# age > 21 #False
# age >= 20 #False

## Checking Multiple condition
# age = 12
# print(age>9 and age < 18) #True
# print(age>14 or age < 14) #True

## Checking wheter value in a List
# food = ["water", "anchovies", "mushrooms"]

# print("water" in food) #True
# print("pepper" in food) #False
# new_food = ["melon","water","mushrooms"]

# for new in new_food:
#     if new in food:
#         print(f"We already have {new}")
#     if new not in food:
#         print(f"we don't have {new}")

## Practice
# car = "kia"
# print("Is car == 'kia'? i predict True")
# print(car == "kia")

# age = 17

# if age < 4:
#     print("Your fee is zero")
# elif age < 18:
#     print("Your fee is 200")
# else:
#     print("Your fee is 400")
    
# age = 40

# if age < 4:
#     price = "$25"
# elif age < 18 or age > 65:
#     price = "$40"
# else:
#     price = "$50"
# print(f"Your cost is {price}")

## else is not essential in python you can choose wheter to use or not to Use

# food = ["mushrooms","extra cheese",]

# if "mushrooms" in food:
#     print("adding mushrooms") # cdoe will stop here
# elif "pepperoni" in food:
#     print("adding pepperoni")
# ## if-elif-else chain only check one block code

## Practice
# alien_color = "green"
# if alien_color == "green":
#     print("got it")
# elif alien_color == "red":
#     print("you are wrong. -5")
# elif alien_color == "yellow":
#     print("not yellow. -3")

# if alien_color == "green":
#     print("green! you got 5 points")
# else:
#     print("good job you got 2 points")

# age = 22
# if age < 2:
#     you = "baby"
# elif age < 4:
#     you = "toddler"
# elif age < 13:
#     you = "kid"
# elif age < 20:
#     you = "teenager"
# elif age < 65:
#     you = "adult"
# else:
#     you = "elder"
# print(f"You are {you}")

# fav_fruits = ['apple','melon','orange']
# if "apple" in fav_fruits:
#     print("You like apple")
# if "strawberry" in fav_fruits:
#     print("Strawberry is also good")


## Checking for special item
# toppings = ["mushroom","green pepper","extra cheese"]
# for topping in toppings:
#     print(f"Adding toppings")
# print("\nFinish")
# for topping in toppings:
#     if topping == "green pepper":
#         print("sorry we don't have green pepper")
#     else:
#         print(f"Adding {topping}")
# print("\nFinish")

# toppings = []
# if toppings: #When you use if statement to list python return true if list has at least one item
#     for top in toppings:
#         print(f"Adding {top}")
#     print("\nFinish")
# else:
#     print("No materials")
    
## Multiple list

# available = ["Mushroom","Olive","Green Pepper","Pineapple","Cheese"]
# requested = ["Mushroom","Potato","Shrimp","Pineapple"]
# for request in requested:
#     if request in available:
#         print(f"Adding {request}")
#     else:
#         print(f"Sorry we don't have {request}")
# print("\nFinish")

## Practice
# users = ["Jam","Sara","Bob","Admin","Jax"]

# if users:
#     for user in users:
#         if user == "Admin":
#          print("Hello Admin, do you want to see the data?")
#         else:
#          print(f"Hi {user}, Thank you for coming back here")
# else:
#     print("No users in users")

# currents = ["Max","Jane","Lee","Park","Kim"]
# current_lower = [current.lower() for current in currents]
# print(current_lower)
# news = ["lee","park","jasmin","maro"]

# for new in news:
#     if new in current_lower:
#         print(f"{new} is already in name. change please")
#     else:
#         print(f"welcome {new} is available name")

## list comprehension practice
# numbers = [1,2,3,4,5]
# odd = [num for num in numbers if num % 2 != 0]
# print(odd)

# nested = [[1,2,3],[4,5,6],[7,8,9]]
# flatten = [num for sub in nested for num in sub]
# print(flatten)

# names = ["Alice", "Bob", "Charlie"]
# name_len = [[name,len(name)] for name in names]
# print(name_len)