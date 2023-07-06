from fan_class import Fan

fan_1 = Fan(3, True, 10.0, "Yellow")
fan_2 = Fan(2, False, 5.0, "Blue" )

print("\033[1m" + "\033[94m" + "Fan 1 propeties:")
fan_1.display_fan()
print("Fan 2 propeties:")
fan_2.display_fan()

