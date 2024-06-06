# def greet():
#     """Display the greeting."""
#     print("hello".upper())
# greet()
    
# def greet(user):
#     """display the greeting"""
#     print(f"Hello {user}")
# greet("brand")

## Practice
# def display():
#     """Display what you are learning
#     """
#     print("You are learning functions")

# display()

# def fav_book(book):
#     """display book what you like
#     """
#     print(f"You like {book} it's good")
    
# fav_book("Zordan")

## positional arguments , and keyword argument
## if you set the several parameter you can set it as positional (order) or keyword (parameter = argument)

# def describe_pet(spiece,name):
#     """display info about a pet
#     """
#     print(f"I have a {spiece}")
#     print(f"My {spiece} 's name is {name.title()}")
    
# describe_pet("Hamster",name = "jack") 
# describe_pet("Pig","max") # for the positional argument you need to follow order
# describe_pet(name="Jax",spiece="Bird") # Now you see? the keyword argument doesn't follow order


## Default parameter
# def describe_pet(name,spiece ="dog"):
#     ## You need to use defalut value after all the parameters it helps python to interpret positional argument
#     """display info about a pet
#     """
#     print(f"I have a {spiece}")
#     print(f"My {spiece} 's name is {name.title()}")
# describe_pet("william")

## Practice
# def make_shirt(size ="large"):
#     """Display shirt_info
#     """
#     if size.lower() == "large":
#         print("I love python")
#     elif size.lower() == "medium":
#         print("size is medium")
#     else:
#         print(f"size is {size}")
        
# make_shirt("large")
# make_shirt("medium")
# make_shirt("dd")

# def describe_city(name , country ="Korea"):
#     print(f"{name} is in {country}")

# describe_city("seoul")
# describe_city("Jeju")
# describe_city("tokyo","japan")

# def get_formatted_name(first_name, last_name, middle_name=""):
#     """Return full name
#     """
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name("james", "max")
# print(musician)

# musician = get_formatted_name("james", "max","lee")
# print(musician)

# def person(first, last , middle = ""):
#     if middle:
#         person = {"first" : first, "middle" : middle, "last" : last , }
#     else:
#         person = {"first" : first,  "last" : last}
#     return person
# m = person("amy" ,  "kim")
# print(m)
# m = person("rod", "emily","a")
# print(m)

# def person(first, last , middle = "",age = None):
#     person = {"first" : first,  "last" : last}
#     if middle:
#         person["middle"] = middle
#     if age:
#         person["age"] = age
#     return person

# dic = []
# musician = person('jimi', 'hendrix', age=27)
# dic.append(musician)
# musician = person('amy', 'dron', age=11)
# dic.append(musician)
# print(dic)

## Funciton with a while loop
# def get_full(first, last):
#     full  = f"{first} {last}"
#     return full.title()

# while True:
#     print("please tell me your name")
#     ff = input("first name :")
#     if ff == "q" :
#         break
#     ll = input("last name :")
#     if ll == "q" :
#         break
    
#     fullname = get_full(ff ,ll)
#     print(f"Hello, {fullname}")


## Practice
# def city_country(city , country):
#     info = f"{city.title()},{country.title()}"
#     return info
# print(city_country("seoul", "korea"))

## --------------------------------------

# def make_album(artist_name, title , year = None):
#     if year:
#         album = {
#         "artist" : artist_name.title(),
#         "title" : title.title(),
#         "year" : year
#     }
#     else: 
#         album = {
#         "artist" : artist_name.title(),
#         "title" : title.title()
#     }
    
#     return album
# print (make_album("akmu","200%"))
# print (make_album("ive","i am"))
# print (make_album("akmu","200%",2022))

## ----------------------------------

# def make_album(artist_name, title , year = None):
#     if year:
#         album = {
#         "artist" : artist_name.title(),
#         "title" : title.title(),
#         "year" : year
#     }
#     else: 
#         album = {
#         "artist" : artist_name.title(),
#         "title" : title.title()
#     }
#     return album
        
# while True:
#     print("please give me the album info")
#     a = input("artist name:")
#     if a == "q" :
#         break
#     t = input("title: ")
#     if t == "q" :
#         break
#     y = input("year")
#     if y == "q" :
#         break
#     full = make_album(a,t,y)
#     print(full)

## passing arbitrary number of arguments

# def pizza(*toppings):
#     print("Making a pizza with following toppings :")
#     for topping in toppings:
#         print(f"{topping}")

# pizza("a","b","c","d")

## mixing positional and arbitrary arguments
# def pizza(size, *toppings):
#     """summarzie about the pizza"""
#     print(f"You are going to make {size} inch pizza")
#     for topping in toppings:
#         print(f"={topping}")

# pizza(12, "a","b","c","d")

## Using arbitrary keyword arguments
# def profile(first, last, **user_info):
#     """Build the profile"""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info
# user_p = profile("albert","aeinstein", location= "princeton",field = "physics")
# print(user_p)


## Practice
# def sandwichi(*item):
#     print(f"Toppings : {item}")
# sandwichi("a","b","C")

## ------------------------------------

# def profile(first, last, **user):
#     """Build port"""
#     user["first name"] = first
#     user["last name"] = last
#     return user
# user = profile("a","b",location = "tokyo", field = "python")
# print(user)

## ==========================================

# def car_profile (manu, model, **info):
#     info["manufacuturer"] = manu
#     info["model name"] = model
#     return info
# car = car_profile("honda","z10",color="blue",year = 2010) 
# print(car)

## Store function in module
# import module

# module.pizza(16,"peparoni")
# module.pizza(15,"pine")

## from . import .
# from module import pizza
# pizza(16, "tomato")
# pizza(13, "beef")

##from . import . as .
# from module import pizza as mp
# mp(16,"tomato")

## import all
# from module import *