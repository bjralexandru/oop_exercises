# Check type of an object

# Write a program to determine which class a given Bus object belongs to.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


class Bus(Vehicle):
    pass


School_bus = Bus("School Volo", 12, 50)

print(type(School_bus))

# Determine if School_bus is also an instance of the Vehicle class

print(isinstance(School_bus, Vehicle))
