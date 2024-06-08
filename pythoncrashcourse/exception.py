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
polling = True
file = 'guest_book.txt'
prompt = "Enter the user name"
prompt += "('q' to quit) :"
while polling:
    
    

    
    with open(file,"a") as file_obj:
        user = input(prompt)
        file_obj.writelines(f'\n{user}')
        if user == "q":
            break
    
    with open(file,"r") as file_obj:
        read = file_obj.readlines()
        print(read)
        