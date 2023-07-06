# Ken Leam G. Gamboa
# BSCPE 1-5
# Creating a Fan class containing the following attributes and 
# methods required by Assignment #9.

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
        return self.__speed
# create a method that access the fan's power indicator
# create a method that access the fan's radius
# create a method that access the fan's color
# create a method that will set the fan's speed
# create a method that will set the fan's power indicator
# create a method that will set the fan's radius
# create a method that will set the fan's color
