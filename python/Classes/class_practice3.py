class Dog():

    # CLASS OBJECT ATRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = "mammal"

    # ATTRIBUTES
    def __init__(self,
                breed,
                name,
                spots,):
        # assigned by using self.attributes_name
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots
    
    # OPERATIONS/Actions -> Methods
    def bark(self, number):
        print(f"WOOF! my name is {self.name} and the number is {number}")

my_dog = Dog(breed="Lab",
            name="Sammy",
            spots=False,)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(23)) # USE THIS TO GET USER TO PICK X OR O

