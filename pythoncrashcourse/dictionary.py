## Dictionary in a variable you can store many values in the key
## dictionay = {key : value , key : value}

# alien_0 = {"color": "green", "points": 5}
# print(alien_0['color'])
# print(alien_0['points'])
## pull the value with the key
# new_point = alien_0["points"]
# print(new_point)

## adding new key-value pairs
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)

# alien_0 = {}
# alien_0["color"] = "green"
# alien_0["point"] = 5
# print(alien_0)
# ## change the value
# alien_0["color"] = "yellow"
# print(alien_0["color"])

# ## Moving the alien
# alien_0["x"] =  0
# alien_0["y"] = 20
# alien_0["speed"] = "medium"

# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     ## for fast alien
#     x_increment =3

# alien_0["x"] = alien_0["x"] + x_increment
# print(f"new position is {alien_0["x"]}")

## removing key-vallue pair

# alien = {"color" : "green" , "points" : 5}
# del alien["points"]
# print(alien)

# fav_lang = {
#     "jen" : "python",
#     "sarah": "c"
# }

# language = fav_lang["sarah"].title()
# print(f"Sarah like {language}")

# alien_0 = {'color': 'green', 'speed': 'slow',"points" : 5}
# point_val=alien_0.get("points","No points value assigned")
# ## it shows points or if there is no value in points it shows default" No points
# print(point_val)

## Practice
# person = {
#     "first name":"James",
#     "Last name" :"Mac",
#     "age" : "28",
#     "city" : "Seoul",
# }  
# print(person["first name"])
# print(person["Last name"])
# print(person["age"])
# print(person["city"])

# fav_num = {
#     "james" : 24,
#     "sarah" : 10,
#     "kim" : 1,
# }
# jm_num = fav_num["james"]
# sr_num = fav_num["sarah"]
# kim_num = fav_num["kim"]
# print(f"jaems likes {jm_num}")
# print(f"sarah likes {sr_num}")
# print(f"kim likes {kim_num}")

# glossary = {
#     "list" : "sequence data type which is used to store the collection of data",
#     "value" : "data",
#     "if" : "checkk the condition to run the code",
#     "for": "loop the code while it gives ture",
# }
# print(glossary["list"])
# print(glossary["value"])

## Looping throguh key-value pair
## items()
# user ={
#     "username" : "emily",
#     "first": "enrico",
#     "last" : "fermi",
# }
# for k, v in user.items():
#     print(f"\nKey:{k}")
#     print(f"Value:{v}")
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
# for name, lang in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {lang.title()}")

# ## Only key
# for name in favorite_languages.keys():
#     print(f"{name}")

# friends = ["jen","sarah"]
# for name in favorite_languages.keys():
#     print(name.title())
    
#     if name in friends:
#         lang = favorite_languages[name].title()
#         print(f"\t{name.title()} likes {lang}")

## find a key using keys()
# if 'erin' not in favorite_languages.keys():
#     print("erin, please take our poll")

## changing the order
# for name in sorted(favorite_languages.keys()):
#     print(name)
    
## chasing with values
# for lang in favorite_languages.values():
#     print(lang)

## Practice

# rivers = {
#     "nile" : "egypt",
#     "han" : "korea",
#     "hwang": "china",
#           }

# for r,n in rivers.items():
#     print(f"{r} runs through {n}")

# print(rivers.keys())
# print(rivers.values())

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }

# users = ["jen","emily"]
# for user in users:
#     if user in favorite_languages.keys():
#         print(f"Welcome {user}")
#     else:
#         print(f"Why not {user}")

## multiple dictionary

# aliens_0 = {"color" : "red" , "points": 5}
# aliens_1 = {"color" : "green" , "points": 15}
# aliens_2 = {"color" : "yellow" , "points": 10}
# aliens = [aliens_0, aliens_1, aliens_2]
# print(aliens)

##empty list
# aliens = []

## making 30 aliens
# for alien_num in range(30):
#     new_al= {"color":"red","point":5,"speed":"slow"}
#     aliens.append(new_al)
    
## changing aliens
# for alien in aliens[:3]:
#     if alien["color"] == "red":
#         alien["color"] = "blue"
#         alien["point"] = 10
#         alien["speed"] = "fast"
# #show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"total num of aliens: {len(aliens)}")

# pizza = {
#  'crust': 'thick',
#  'toppings': ['mushrooms', 'extra cheese'],
#  }
# print(f"you ordered crust: {pizza['crust']}")
# for topping in pizza["toppings"]:
#     print(f"topping : {topping}")
    
# favorite_languages = {
#  'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'edward': ['ruby', 'go'],
#  'phil': ['python', 'haskell'],
#  }

# for name, languages in favorite_languages.items():
#     print(f"{name.title()}'s favorite langues are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# users = {
#     "aeinstein" : {
#         "first" : "albert",
#         "last" : "einstein",
#         "location": "princeton",
#     },
#     "mcurie" : {
#         "first" : "marie",
#         "last" : "curie",
#         "location": "paris",
#     },
# }
# for username, user_info in users.items():
#     print(f"Username: {username}")
#     full_name = f"{user_info["first"]} {user_info["last"]}"
#     location = f"{user_info["location"]}"
    
#     print(f"\tFull name is : {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

## Practice

# james = {
#     "first":"james",
#     "last":"carol",
# }
# emily = {
#     "first":"emily",
#     "last":"wood",
# }
# people = [james , emily]
# for info in people:
#     print(f"he is {info["first"]} {info["last"]}")
        
# pet_1 = {
#     "species":"cat",
#     "owner":"max",    
# }
# pet_2 = {
#     "species":"dog",
#     "owner":"John",
# }
# pets = [pet_1, pet_2]
# for pet in pets:
#     print(f"pet is {pet["species"]}, owner is {pet["owner"]}")

# favorite_place = {
#     "sam" : ["america", "china"],
#     "max" : ["japan", "korea"],
#     "lin" : ["Aus", "germany"],
# }
# for name, places in favorite_place.items():
#     print(f"{name} likes :")
#     for place in places:
#         print(f"\t{place}")

# fav_num = {
#     "sam" : [12,23],
#     "ka" : [122,223],
#     "mkion" : [1222,2322],
# }

# for name, numbers in fav_num.items():
#     print(f"{name} lieks:")
#     for number in numbers:
#         print(f"\t {number}")

# cities = {
#     "Paris" : {
#         "country" : "France",
#         "people" : "1 million"
#     },
#     "New York" : {
#         "country" : "USA",
#         "people" : "3 million"
#     },
#     "Seoul" : {
#         "country" : "Korea",
#         "people" : "2 million"
#     },   
# }
# for name, city_infos in cities.items():
#     print(f"{name}:")
#     for k,v in city_infos.items():
#         print(f"\t{k}:{v}")