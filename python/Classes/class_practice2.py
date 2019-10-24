#! python3

class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "a {self.color} car".format(self=self)
my_car = Car("red", 30000)
print(my_car)
print(str(my_car))

class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"Car({self.color}, {self.mileage})".format(self=self)

my_car = Car("red", 37281)

print(my_car)