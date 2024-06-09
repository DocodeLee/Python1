import json

# number = [1,2,3,4,5]

# filename = 'numbers.json'
# with open(filename,"w") as  f:
#     json.dump(number,f)

# filename = "numbers.json"
# with open(filename) as f:
#     numbers = json.load(f)
# print(numbers)


# username = input("What is your name: ")
# filename = "username.json"
# with open(filename,"w") as f:
#     json.dump(username,f)
#     print(f"Until you comeback {username}")

# with open(filename) as f:
#     user = json.load(f)
#     print(f"Welcomeback {user}")

## Load the name it has been stored or store the new data
# def get_stored_username():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             user = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return user
# def get_new_username():
#     username = input("What is your name?> ")
#     filename = 'username.json'
#     with open(filename,"w") as f:
#         json.dump(username,f)
        
    
# def greetuser():
#     username = get_stored_username()
#     if username:
#         print(f"We will remember {username}")
#     else:
#         username = get_new_username()
#         print(f"We will remember you {username}")        
# greetuser()



## Practcie
## 10 -11
# prompt = input("Enter your favorite number: ")

# filename = "favnum.json"
# with open(filename,"w") as f:
#     json.dump(prompt,f)

# with open(filename) as f:
#     content = json.load(f)
# print(f"You like number {content}")

## 10-12
# def new_user_fav_num():
#     favnum = input("Enter your favorite number: ")
#     filename = "favnum.json"
#     with open(filename,"w") as f:
#         json.dump(favnum,f)
        
    
# def call_user_fav_num():
#     filename = "favnum.json"
#     try:
#         with open(filename) as f:
#             content = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return content 
    
# def num_guess():
#     number = call_user_fav_num()
#     if number:
#         print(f"You like number {number}")
#     else:
#         number = new_user_fav_num()
# num_guess()
# num_guess()


## -----------------------------------------
## 10-13

# def get_stored_username():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             user = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return user
# def get_new_username():
#     username = input("What is your name?> ")
#     filename = 'username.json'
#     with open(filename,"w") as f:
#         json.dump(username,f)
        
    
# def greetuser():
#     username = get_stored_username()
#     current = input("Who are you? : ")
    
#     if username == current:
#         print(f"Welcome back {username}")
#     else:
#         username = get_new_username()
#         print(f"We will remember you {username}")        
# greetuser()

