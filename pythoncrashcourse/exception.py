# with open('ex.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())
## if your file is on the other directory set the path as a variable rather than use directly. it helps your code look clearly

# file = "ex.txt"
# with open(file) as wonder:
#     for line in wonder: ##the default is the line
#         print(line) ## In file object the python read the file as line by line with for loop

# file = "ex.txt"
# with open(file) as wonder:
#     lines = wonder.readlines() ## store the line by line in the list

## storing in the list and call outside the with box

# print(lines)
# for line in lines:
#     print(line.rstrip())


## working with files
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(f"{pi_string[:11]}...") ## object[: number] you can change the range to show on the monitor
# print(len(pi_string))

## working with input
# find = input("Enter the two alphabet combination which you want to find : ")
# if find in pi_string:
#     print("your finding is in file")
# else:
#     print("That combination is no in the file")

## Practice

##10.1

##10.1.1 print the whole file
# filename = "learningpython.txt"
# with open(filename) as file:
#     contents = file.read()

# print(contents)

##10.1.2 print the file line by line
# filename = "learningpython.txt"
# with open(filename) as file:
#     contents = file.readlines()

# for content in contents:
#     print(content)
    
## 10.1.3 print the file in the other files


# filename = "learningpython.txt"
# file2 = ''
# with open(filename) as file:
#     contents = file.readlines()

# for content in contents:
#     back = content.replace("you", "everyone")
#     file2 += back


# print(file2)


## Writing to empty file
## read mode ('r'), write mode ('w'), append mode ('a')

# file = 'progamming.txt'

# with open(file, 'w') as file_obj:
#     file_obj.write("I love programming")
#     file_obj.write("\n Hey Hye")

## when you run the wirte code the content be reset and write from 0
# with open(file,'w')as file_obj:
#     file_obj.write("new")

# with open(file, 'a') as file_obj:
#     file_obj.write("\n this line has appended by append mode")


## Practice
## 10-3
# prompt = input("Enter your name")

# file = 'guest.txt'
# with open(file, 'a') as file_obj:
#     file_obj.write(f"\n{prompt}")

##--------------------------------------
## 10 -4
# polling = True
# file = 'guest_book.txt'
# prompt = "Enter the user name"
# prompt += "('q' to quit) :"
# while polling:
    
    

    
#     with open(file,"a") as file_obj:
#         user = input(prompt)
#         file_obj.writelines(f'\n{user}')
#         if user == "q":
#             break
    
#     with open(file,"r") as file_obj:
#         read = file_obj.readlines()
#         print(read)
        


## Exceptions

## Python uses special objects called exceptions to manage errors
## Exceptions are handled with try-except blocks

# print(5/0) # In here youc can see the error "ZeroDivisionError"

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You cannot divide by zero")

## simple calculator without handling error

# print("give me two numm, I will divide them")
# print("Enter 'q' to quit")

# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break
#     sec_num = input("\nSecond number: ")
#     if sec_num == 'q':
#         break
#     try:
#         answer = int(first_num) / int(sec_num)
#     except ZeroDivisionError:
#         print("You cannot divide by 0")
#     except ValueError:
#         print("Please enter the number")
#     else:
#         print(answer)

## FileNotFoundError
# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         content =f.read()
# except FileNotFoundError:
#     print(f"Sorry {filename} doesn't exist")

# def count_words(filename):
#     """Count the approximate number of words in file"""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         # print(f"Sorry {filename} does not exist")
#         pass
#     else:
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file{filename} has about {num_words} words.")
# filename=["guest_book.txt","ex.txt","guest.txt","alice.txt"]
# for file in filename:
#     count_words(file)


## Practice
##10-6 10-7

# print("If you give two number i will add them")
# print("if you want to stop please enter 'q'")

# while True:
#     first_num = input("Please enter First Number : ")
#     if first_num == "q":
#         break
#     second_num = input("Please enter Second Number : ")
#     if second_num == "q":
#         break
#     try:
#         result = int(first_num) + int(second_num)      
#     except ValueError:
#         print("Please enter the Number")
#     else:
#         print(result)

## 10-8

# def readfile(filename):
#     try:
#         with open(filename,encoding="utf-8") as f:
#             content = f.read()
#             print(content)
#     except FileNotFoundError:
#          #print( "There is no File")
#          pass

# filenames = ['cats.txt','dogs.txt',"bird.txt"]
# for filename in filenames:
#     print(f"{filename}")
#     readfile(filename)


## ----------------------------------------
## 10-9

# file = "10_9.txt"
# with open(file,encoding="utf-8")as f:
#     content = f.read()
#     the = content.lower().count("the ")
#     print(the)


##Storing Data
## JSON data format is not specific to Python, so you can share data you
## store in the JSON format with people who work in many other programming languages