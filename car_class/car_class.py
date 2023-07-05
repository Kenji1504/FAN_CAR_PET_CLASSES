# Ken Leam G. Gamboa
# BSCPE 1-5
# Creating a car class that contains attributes and methods 
# required by the Assignment # 9

import time
# create a class named car
class Car:
# create a constructor containing the car's year model, make, and its current speed
    def __init__(self, year_model, make, speed):
        try: 
            year_model = str(year_model)
            make = str(make)
        except:
            raise TypeError("the following properties should be in str.")
        
        try:
            speed = int(speed)
        except:
            raise TypeError("the following attributes should be in int.")
        
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
# create a method that will accelerate the car
    def accelerate(self):
        print(f"{self.__year_model} model {self.__make} is accelarating.")
        time.sleep(1)
        self.__speed += 5
# create a method that can trigger the car's brake
    def brake(self):
        print(f"{self.__year_model} model {self.__make} brakes.")
        time.sleep(1)
        self.__speed -= 5
# create a method that gets the car's current speed
    def get_speed(self):
        return self.__speed
# display car's current speed
    def display_speed(self):
        print(f"The {self.__year_model} model {self.__make} car's current speed is {self.get_speed()}")
        time.sleep(1)