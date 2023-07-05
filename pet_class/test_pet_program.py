from pet_class import Pet

pet_1 = Pet("Elsie", "Dog", "12")
print(f"Pet's name: {pet_1.get_name()} \nPet's animal type: {pet_1.get_animal_type()} \nPet's age: {pet_1.get_age()}")
pet_1.set_name("Toby")
pet_1.set_animal_type("hamster")
pet_1.set_age("10")
print(f"Pet's name: {pet_1.get_name()} \nPet's animal type: {pet_1.get_animal_type()} \nPet's age: {pet_1.get_age()}")
