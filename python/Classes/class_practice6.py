#! python3

# EXAMPLES OF POLYMORPHISM

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} says WOOF!"


class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} says MEOW!"

niko = Dog(name="Niko")
felix = Cat(name="Felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(felix)
pet_speak(niko)

class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return f"{self.name} says Woof!" 

class Cat(Animal):
    
    def speak(self):
        return f"{self.name} says Woof!" 

fido = Dog(name="Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())

# TRY POLYMORPHISM TO PICK X OR O
# def pet_speak(pet):
#    print(pet.speak())