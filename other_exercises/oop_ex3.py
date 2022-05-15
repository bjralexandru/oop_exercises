# Create a Bus object that will inherit all of the variables and methods of
# the parent Vehicle class and display it.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
