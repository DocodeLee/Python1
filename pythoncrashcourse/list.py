### Chapter 3
# #  Lists allow you to store sets of information in one place, whether you have just a few items or millions of items
# bicycle = ['trek', 'cannodale', 'redline']
# print(bicycle)
# print(bicycle[0])
# print(bicycle[0].title())
# print(bicycle[0].upper())
# # index start from 0 not 1
# print(bicycle[-1])
# # show the last item

# # practice

# name = ["lee", "kim", "park", "kwang"]
# greeting = f"Hi {name[0]}"
# greeting = f"Hi {name[1]}"
# greeting = f"Hi {name[2]}"
# print(greeting)

# # modifing  elemnt in a list
# motorcycle = ['honda', 'yamaha','suzuki']
# print(motorcycle)
# motorcycle[0] = 'ducati'
# print(motorcycle)

# # Appending : just follow the order 
# motorcycle = []
# motorcycle.append('ducati')
# motorcycle.append('honda')
# motorcycle.append('suzuki')
# print(motorcycle)

# # inserting you can set the index
# motorcycle = ['honda', 'yamaha','suzuki']
# motorcycle.insert(2, "toyota")
# print(motorcycle) 

# # Deleting
# motorcycle = ['honda', 'yamaha','suzuki']
# del motorcycle[1]
# print(motorcycle)
# del motorcycle[0]
# motorcycle.insert(0, "hyundai")
# motorcycle.append("kia")
# print(motorcycle)

# # pop : Remove the last item in the list
# motorcycle = ['honda', 'yamaha','suzuki']
# print(motorcycle)

# pop_motor = motorcycle.pop()
# print(pop_motor)
# print(motorcycle)
# print(f"The last thing i bought is {pop_motor}")
# # if you use index you can set the item
# first_owned = motorcycle.pop(0)
# print(first_owned)
# print(f"First: {first_owned} Last: {pop_motor}")
# # but the item is no-longer in the list

# #Removing an item
# motor = ['honda', 'yamaha', 'suzuki']
# motor.remove("suzuki")
# print(motor)
# motor.append("ducati")
# print(motor)
# expensive = "ducati"
# motor.remove(expensive)
# print(motor)
# print(f"{expensive} is too expensive to me")

# # practice
# guest = ["Lee", "Park", "Kim", "Jin"]
# print(f" Please come to the party {guest[0]}")
# print(f" Please come to the party {guest[1]}")
# print(f" Please come to the party {guest[2]}")
# print(f" Please come to the party {guest[3]}")

# byebye = guest.pop()
# print(guest, byebye)

# guest.append("Chef")
# print(guest)
# guest.remove("Lee")
# print(guest)
# guest.insert(0,"Max")
# guest.insert(-1,"Bob")
# print(guest)

# print(f"I am sorry you need to prepae {byebye}")
# bye = guest.pop(0)
# print(f"We don't have seats for you {bye}")
# print(guest)
# gogo = guest[1]
# print(f"You can participate {gogo}")

# del guest[0]
# print(guest)
# del guest[-1]
# print(guest)

## sorting a list
## permentaly
# car = ["bmw", "toyota", "kia"]
# car.sort()
# print(car)
# car.sort(reverse=True)
# print(car)

## temporarily
# car = ["bmw", "toyota", "kia"]
# print(sorted(car))
# print(car)
## sorted doesn't change the order of originals

## reverse
# car = ["bmw", "toyota", "kia"]
# car.reverse()
# print(car)
## original has changed

## Length 
# car = ["bmw", "toyota", "kia"]
# car_len = len(car)
# print(car_len)

## Practicce

# place = ["kaz","aus","ger","mex","gre"]
# place.sort()
# print(place)
# print(sorted(place))
# print(place)
# print(sorted(place,reverse=True))
# place.reverse()
# print(place)
# place.sort()
# print(place)
# place.sort(reverse=True)
# print(place)

# guest = ["Lee", "Park", "Kim", "Jin"]
# guest_len = len(guest)
# print(guest_len)

## index error
# motorcycles = ['honda', 'yamaha', 'suzuki'] 
# print(motorcycles[3])

### Ch.4
## looping the list
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician)
## for loops run until there's nothing in the list

## you can use for loop for the repeated work
## every indented line work for each value
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great")
#     print(f"i want to see {magician.title()}'s next trick.\n")
# #outside of for loop
# print("Thank you everyone the show is finished")

## only indent when you need to 

## Practice
# pizzas = ["pineapple", "potato", "shrimp"]
# for pizza in pizzas:
#     print(f"I like {pizza.upper()}")
# print("I really like pizzas")

# animals = ["cat", "dog", "lizzard"]
# for animal in animals:
#     print(f"{animal.title()} make great experience")
# print("Every choice would be best")

## Numeral list
## python gives the -1 from the second value
# for value in range(1,5):
#     print(value)

## using range to make a list of numbers
# numbers = list(range(1,6))
# print(numbers)

# even = list(range(2,11,2))
# print(even)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)

## Focus first onwriting code that you understand clearly, 
## which does what you want it to do. Then look for more efficient approaches as you review your code.

# digit = list(range(0,11,2))
# print(digit)
# print(min(digit))
# print(max(digit))
# print(sum(digit))

# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# even = [ value * 2 for value in range(1,20)]
# print(even)

# spare = [value % 3 for value in range (1,100)]
# print(spare)

##Practice
# for value in range(1,21):
#     print(value)

# mili = list(range(1,1000001))
# for value in mili:
#   print(value)
# print(min(mili))
# print(sum(mili))
# print(max(mili))

# odd = [value for value in range(1,20,2)]
# for value in odd:
    # print(value)
# print(odd)
# third = [value * 3 for value in range(3,31)]
# print(third)

# cube = [value ** 3 for value in range(1,10)]
# for value in cube:
#     print(value)

## slicing
# players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# print(players[0:3])
# print(players[1:4])
# print(players[1:])
# print(players[-3:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# for player in players[:3]:
#     print(player.title())
# for winner in players[:1]:
#     print(winner.upper())

# my_food = ['pizza', 'rice','coke']
# fr_food = my_food[:]
# print(fr_food)
# my_food.append("beer")
# fr_food.append("sushi")
# print(my_food)
# print(fr_food)


## Practice
# players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
# print(f"The first three items in the list are:{players[:3]}")
# print(f"In the middle:{players[1:4]}")
# print(f"Last : {players[-3:]}")

my_pizza = ["pine", "sweet-potato", "potato"]
fr_pizza = my_pizza[:]
print(fr_pizza)
my_pizza.append("shirimp")
fr_pizza.append("Hot-chicken")
print(f"My favorite pizzas are: {my_pizza}")
print(f"Friend's favorite pizzas are: {fr_pizza}")

for pizza in my_pizza:
    print(f"I like {pizza}")
    
for f_pizza in fr_pizza:
    print(f"friend likes {f_pizza}")