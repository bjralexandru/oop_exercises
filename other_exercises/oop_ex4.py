# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity):
        string = "The seating capacity of a {} is {} pasangers"
        return string.format(self.name, capacity)


class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_bus = Bus("bus", 160, 25000)
print(School_bus.seating_capacity())
