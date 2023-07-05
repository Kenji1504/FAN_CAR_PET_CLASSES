from car_class import Car

car_1 = Car("2022", "Honda Civic", 0)

for accelerate in range(5):
    car_1.accelerate()
    car_1.display_speed()
