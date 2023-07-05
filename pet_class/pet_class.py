# Ken Leam G. Gamboa
# BSCPE 1-5
# creating a pet class which contains the following 
# data attributes and methods required for the Assignment #9.

import time
#create a class named "Pet"
class Pet:
    # create the constructors, following attributes are pet's name, animal type, and its age
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
# create a method that sets the name of the pet
    def set_name(self, name):
        try:
            self.__name = str(name)
        except:
            raise ValueError("name is not str type.")
# create a method that sets the pet's animal type
    def set_animal_type(self, animal_type):
        try:
            self.__animal_type = str(animal_type)
        except:
            raise ValueError("animal type is not str type.")
# create a method that sets the pet's age
    def set_age(self, age):
        try:
            self.__age = int(age)
        except:
            raise ValueError("age is not an int.")
# create a method that gets the name of the pet
    def get_name(self):
        return self.__name
# create a method that gets the pet's animal type
    def get_animal_type(self):
        return self.__animal_type
# create a method that gets the pet's age
    def get_age(self):
        return self.__age
# create a method that can indicate the pet's overall properties
    def pet_info(self):
        print("\033[1m" + "\033[95m" + f"Hello owner! my name is {self.get_name()}.")
        time.sleep(2)
        print(f"I am a {self.get_animal_type()}")
        time.sleep(2)
        print(f"And I'm {self.get_age()} years old.")
        time.sleep(2)
        print("I'll be in your care from now on. I hope we'll get along!\n\n")
        time.sleep(2)
