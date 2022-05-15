# Define a class attribute”color” with a default value white. I.e.,
# Every Vehicle should be white.

class Vehicle:

    color = 'white'

    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus('School Volvo', 180, 12)
car = Car('Audi Q5', 240, 18)

print(School_bus.color, School_bus.name, School_bus.max_speed)
print(car.color, car.name, car.max_speed)
