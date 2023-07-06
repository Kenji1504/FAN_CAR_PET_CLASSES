# Ken Leam G. Gamboa
# BSCPE 1-5
# Creating a Fan class containing the following attributes and 
# methods required by Assignment #9.

import time

SLOW = 1
MEDIUM = 2
FAST = 3 
# create a class named 'Fan'
class Fan:
    # create a constructor, contains the fan's data attributes 
    def __init__(self, speed= SLOW, power_indicator= False, radius= 5.0, color= "Blue"):
        # validate inputs first
        try:
            speed = int(speed)
            power_indicator = bool(power_indicator)
            radius = float(radius)
            color = str(color)
        except:
            raise ValueError("attribute does not match assigned type.")
    
    # such as speed, power indicator, radius, and color
        self.__speed = speed
        self.__power_indicator = power_indicator
        self.__radius = radius
        self.__color = color
    # create a method that access the fan's speed
    def get_speed(self):
        match(self.__speed):
            case 1:
                return "SLOW"
            case 2:
                return "MEDIUM"
            case 3:
                return "FAST"
 
# create a method that access the fan's power indicator
    def get_power_indicator(self):
        match(self.__power_indicator):
            case True:
                return "ON"
            case False:
                return "OFF"
# create a method that access the fan's radius
    def get_radius(self):
        return self.__radius
# create a method that access the fan's color
    def get_color(self):
        return self.__color 
# create a method that will set the fan's speed
    def set_speed(self, speed):
        self.__speed = speed
# create a method that will set the fan's power indicator
    def set_power_indicator(self, power_indicator):
        self.__power_indicator = power_indicator
# create a method that will set the fan's radius
    def set_radius(self, radius):
        self.__radius = radius
# create a method that will set the fan's color
    def set_color(self, color):
        self.__color = color

# to display fan's properties
    def display_fan(self):
        time.sleep(1)
        print("\033[1m" + "\033[94m" + f"Speed : {self.get_speed()}")
        time.sleep(1)
        print(f"Power: {self.get_power_indicator()}")
        time.sleep(1)
        print(f"Radius: {self.get_radius()}")
        time.sleep(1)
        print(f"Color: {self.get_color()}")
        time.sleep(1)
        print("\n")
        time.sleep(1)
