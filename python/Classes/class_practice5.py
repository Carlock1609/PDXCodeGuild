#! python3

class Animal():
    
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # YO ARE ABLE TO OVERWRITE METHODS
    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

my_animal = Animal()
print(my_animal)

print(my_animal.eat())
print(my_animal.who_am_i())

my_dog = Dog()
print(my_dog.who_am_i())
print(my_dog.eat())
print(my_animal.eat())