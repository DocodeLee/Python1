## Object oriented programming


# class Dog:
#     """ model a dog"""
#     def __init__(self, nmae, age):
#         # Python runs __init__ automatically whenever we create a new instance
#         """initialize name and age"""
#         self.name = nmae
#         self.age = age
    
#     def sit(self):
#         """sitting response to a command"""
#         print(f"Now {self.name} is sitting")
    
#     def roll_over(self):
#         """rolling over response to a commnad"""
#         print(f"{self.name} is roling over")
    
# mydog = Dog("max", 7)
# youdog = Dog("lucy", 3)

# print(f"my pet is {mydog.name}, he is {mydog.age} old")
# mydog.sit()
# mydog.roll_over()

# print(f"my pet is {youdog.name}, he is {youdog.age} old")
# youdog.sit()
# youdog.roll_over()



## Practice

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#     def describe_res(self):
#         print(f"here is {self.name}, they are good at {self.cuisine}")
    
#     def open_res(self):
#         print(f"{self.name}is opened ! Hurry up")
        
# myres = Restaurant("abura","ramen")
# seres = Restaurant("don","katsudon")
# thres = Restaurant("sushiro","sushi")
# myres.describe_res()
# seres.describe_res()
# thres.describe_res()


## working with class and instances

# class Car:
#     """ simple attempt to car """
#     def __init__(self, make, model, year):
#         """initialize attribute to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   
        
#     def get_descriptive_name(self):
#         """return a formatted name"""
#         long_name = f"{self.year}, {self.make}, {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"car has runned {self.odometer_reading} miles")
        
#     def update_odometer(self, mileage):
#         """
#         set the odometer reading to given value,
#         reject the change if it attempts to roll back
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#             print("check by read_odometer()")
#         else:
#             print("Don't roll back odometer")
#     def increment_odometer(self, miles):
#         """Add given amount to the odometer reading"""
#         self.odometer_reading += miles

# mycar = Car("subaru", "outback", 2015)
# print(mycar.get_descriptive_name())

# mycar.update_odometer(23_500)
# mycar.read_odometer()

# mycar.increment_odometer(100)
# mycar.read_odometer()

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#         self.num_served = 0
        
#     def describe_res(self):
#         print(f"here is {self.name}, they are good at {self.cuisine}")
    
#     def open_res(self):
#         print(f"{self.name}is opened ! Hurry up")
    
#     def read_num_served(self):
#         print(f"This restaurant served{self.num_served}")
    
#     def set_num_served(self,num):
#         self.num_served = num
        
#     def increment_num_served(self,num):
#         self.num_served += num

        

# myres = Restaurant("Abura", "Ramen")
# # print(myres.num_served)
# # myres.num_served = 123
# # print(myres.num_served)
# myres.increment_num_served(2)
# myres.increment_num_served(2)
# myres.read_num_served()

## -----------------------------------------------------------

# class User:
#     def __init__(self, first, last, location):
#         self.first = first
#         self.last = last
#         self.location = location
#         self.login_attempt = 0
    
#     def describe_user(self):
#         print(f"{self.first} {self.last} {self.location}")
        
#     def greet_user(self):
#         print(f"Hello {self.first.title()} {self.last.title()}, How are you doing ing {self.location.title()}")
        
#     def increment_login_attempt(self):
#         self.login_attempt += 1
#     def reset_login_attempt(self):
#         self.login_attempt = 0

# user1 = User("James","Lee","New York")
# user2 = User("rora","emily","Paris")
# user1.describe_user()
# user1.greet_user()
# user2.describe_user()
# user2.greet_user()
# user1.increment_login_attempt()
# user1.increment_login_attempt()
# print(user1.login_attempt)
# user1.reset_login_attempt()
# print(user1.login_attempt)

## Inheritance

# class Car:
#     """ simple attempt to car """
#     def __init__(self, make, model, year):
#         """initialize attribute to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   
        
#     def get_descriptive_name(self):
#         """return a formatted name"""
#         long_name = f"{self.year}, {self.make}, {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"car has runned {self.odometer_reading} miles")
        
#     def update_odometer(self, mileage):
#         """
#         set the odometer reading to given value,
#         reject the change if it attempts to roll back
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#             print("check by read_odometer()")
#         else:
#             print("Don't roll back odometer")
#     def increment_odometer(self, miles):
#         """Add given amount to the odometer reading"""
#         self.odometer_reading += miles

# class Battery:
#     def __init__(self, battery = 75):
#         self.battery = battery
    
#     def describe_battery(self):
#         print(f"this car has {self.battery} size battery")

#     def get_range(self):
#         if self.battery == 75:
#             range = 260
#         elif self.battery == 100:
#             range = 316
#         print(f"This car goes {range} miles at once")
            
# class ElectricCar(Car):
#     """specific to e-car"""
#     def __init__(self, make, model, year):
#         """initialize attribute of the parent"""
#         # special function that allows you to call a method from the parent class. 
#         super().__init__(make, model, year)
#         self.battery = Battery()
        

        
# mycar = ElectricCar('tesla','model s',2019)
# print(mycar.get_descriptive_name())
# mycar.read_odometer()
# mycar.battery.describe_battery()
# mycar.battery.get_range()


## PRACTICE 9.6

# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#         self.num_served = 0
        
#     def describe_res(self):
#         print(f"here is {self.name}, they are good at {self.cuisine}")
    
#     def open_res(self):
#         print(f"{self.name}is opened ! Hurry up")
    
#     def read_num_served(self):
#         print(f"This restaurant served{self.num_served}")
    
#     def set_num_served(self,num):
#         self.num_served = num
        
#     def increment_num_served(self,num):
#         self.num_served += num
# class IceCreamStand(Restaurant):
    
#     def __init__(self, name, cuisine):
#         super().__init__(name,cuisine)
#         self.flavors = []
        
#     def describe_flavor(self):
#         print(f"{self.flavors}")

# mint =IceCreamStand("BR31","Ice cream")
# mint.flavors = ["banana","choco","mint"]
# mint.describe_flavor()

## Practice 9-7

# class User:
#     def __init__(self, first, last, location):
#         self.first = first
#         self.last = last
#         self.location = location
#         self.login_attempt = 0
    
#     def describe_user(self):
#         print(f"{self.first} {self.last} {self.location}")
        
#     def greet_user(self):
#         print(f"Hello {self.first.title()} {self.last.title()}, How are you doing ing {self.location.title()}")
        
#     def increment_login_attempt(self):
#         self.login_attempt += 1
#     def reset_login_attempt(self):
#         self.login_attempt = 0

# class Permission:
#     def __init__(self, permission = ["delete","edit"]):
#         self.permission = permission
            
#     def show_permission(self):
#         print(f"admin can {self.permission}")
        
        
# class Admin(User):
#     def __init__(self, first, last, location):
#         """specific to admin"""
#         """initialize attribute of the parent"""
#         super().__init__(first, last, location)
#         self.permission =  Permission()
        

### when you make class Permission, if you set the default value in the child class you can jsut do Permission()
### But if you don't set default value you need to define the permission under child class and when you make instance
### you need to give the value to the attribute
    


# admin = Admin("Musk", "Elon", "California")
# admin.permission.show_permission()


## --------------------------------------------------------
## 9.9

# class Car:
#     """ simple attempt to car """
#     def __init__(self, make, model, year):
#         """initialize attribute to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   
        
#     def get_descriptive_name(self):
#         """return a formatted name"""
#         long_name = f"{self.year}, {self.make}, {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"car has runned {self.odometer_reading} miles")
        
#     def update_odometer(self, mileage):
#         """
#         set the odometer reading to given value,
#         reject the change if it attempts to roll back
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#             print("check by read_odometer()")
#         else:
#             print("Don't roll back odometer")
#     def increment_odometer(self, miles):
#         """Add given amount to the odometer reading"""
#         self.odometer_reading += miles

# class Battery:
#     def __init__(self, battery = 75):
#         self.battery = battery
    
#     def describe_battery(self):
#         print(f"this car has {self.battery} size battery")

#     def get_range(self):
#         if self.battery == 75:
#             range = 260
#         elif self.battery == 100:
#             range = 316
#         print(f"This car goes {range} miles at once")
        
#     def upgrade_battery(self):
#         print(f"{self.battery}")
#         if self.battery == 75:
#             self.battery = 100
#             print(f"battery size{self.battery}")
            
# class ElectricCar(Car):
#     """specific to e-car"""
#     def __init__(self, make, model, year):
#         """initialize attribute of the parent"""
#         # special function that allows you to call a method from the parent class. 
#         super().__init__(make, model, year)
#         self.battery = Battery()
# mycar = ElectricCar("Hyundai","EV6",2022)

# mycar.battery.get_range()
# mycar.battery.upgrade_battery()
# mycar.battery.get_range()

##Importing class
# from classmd import Car
# from classmd import ElectricCar

# new = Car('audi','a4',2022)
# print(new.get_descriptive_name())
# new.odometer_reading = 23
# new.read_odometer()

# newt = ElectricCar("Tesla","S model", 2023)
# print(new.get_descriptive_name())
# newt.battery.describe_battery()
# newt.battery.get_range()

## Importing all

# import classmd

# new =classmd.Car('audi','a4',2022)
# print(new.get_descriptive_name())
# new.odometer_reading = 23
# new.read_odometer()

# newt =classmd.ElectricCar("Tesla","S model", 2023)
# print(new.get_descriptive_name())
# newt.battery.describe_battery()
# newt.battery.get_range()


## Python standard library
# import random

# players = ["a","b","c","D"]
# first = random.choice(players)
# print(first)

## Practice
## 9-13

# import random

# class Die:
#     def __init__(self, sides = 6):
#         self.sides = sides
    
#     def roll_die(self):
#         result= random.randint(1, self.sides)
#         print(f"{result}")

# side6 = Die(6)
# side6.roll_die()
# side10 = Die(10)
# side10.roll_die()

## 9-14
import random
list = [1,2,3,4,5,6,7,8,9,"a","b","c","d"]
doing =True
count = 0
while doing:

    result = random.sample(list,4)
    my_ticket = [1,"a","b",3]
    count += 1
    
    if result == my_ticket:
        doing = False
        print(f"I ran the code {count} time")
    else:
        continue
    
    