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

# pop : Remove the last item in the list
motorcycle = ['honda', 'yamaha','suzuki']
print(motorcycle)

pop_motor = motorcycle.pop()
print(pop_motor)
print(motorcycle)
print(f"The last thing i bought is {pop_motor}")
# if you use index you can set the item
first_owned = motorcycle.pop(0)
print(first_owned)
print(f"First: {first_owned} Last: {pop_motor}")
# but the item is no-longer in the list