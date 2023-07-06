from fan_class import Fan

fan_1 = Fan(3, True, 10.0, "Yellow")
fan_2 = Fan(2, False, 5.0, "Blue" )

print(fan_1.get_speed())
print(fan_1.get_power_indicator())
print(fan_1.get_radius())
print(fan_1.get_color())
