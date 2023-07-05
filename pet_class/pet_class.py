# Ken Leam G. Gamboa
# BSCPE 1-5
# creating a pet class which contains the following 
# data attributes and methods required for the Assignment #9.

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
    