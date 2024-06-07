
class Car:
    """ simple attempt to car """
    def __init__(self, make, model, year):
        """initialize attribute to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   
        
    def get_descriptive_name(self):
        """return a formatted name"""
        long_name = f"{self.year}, {self.make}, {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"car has runned {self.odometer_reading} miles")
        
    def update_odometer(self, mileage):
        """
        set the odometer reading to given value,
        reject the change if it attempts to roll back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("check by read_odometer()")
        else:
            print("Don't roll back odometer")
    def increment_odometer(self, miles):
        """Add given amount to the odometer reading"""
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery = 75):
        self.battery = battery
    
    def describe_battery(self):
        print(f"this car has {self.battery} size battery")

    def get_range(self):
        if self.battery == 75:
            range = 260
        elif self.battery == 100:
            range = 316
        print(f"This car goes {range} miles at once")
        
    def upgrade_battery(self):
        print(f"{self.battery}")
        if self.battery == 75:
            self.battery = 100
            print(f"battery size{self.battery}")
            
class ElectricCar(Car):
    """specific to e-car"""
    def __init__(self, make, model, year):
        """initialize attribute of the parent"""
        # special function that allows you to call a method from the parent class. 
        super().__init__(make, model, year)
        self.battery = Battery()
