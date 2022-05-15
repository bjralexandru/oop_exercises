# Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as
# a maintenance charge. So total fare for bus instance will become the final
# amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final fare amount
# should be 5500.
# You need to override the fare() method of a Vehicle class in Bus class.


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity=50):
        string = "The seating capacity of a {} is {} passangers."
        return string.format(self.name, capacity)

    @property
    def fare(self, capacity=50):
        total_fare = capacity * 100
        return total_fare


class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    @property
    def fare(self, capacity=50):
        total_fare = capacity * 100 * 1.10
        return total_fare


school_bus = Bus("school\'s volvo", 180, 12)
print(school_bus.fare)

# vehicle = Vehicle("Car", 200, 49)
# print(vehicle.fare)
