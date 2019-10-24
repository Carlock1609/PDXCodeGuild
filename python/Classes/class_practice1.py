#! python3

class Mammal():
    def __init__(self,
                name,
                color,
                age=0,
                mean=True):
        self.name = name
        self.color = color
        self.age = age
        self.mean = mean

    def give_birth(self):
        return f"{self.name} is giving birth"
    def give_age(self):
        return f"{self.name} is {self.age} years old."

class Lion(Mammal):
    def __init__(self, has_claws):
        super().__init__(name="Rudy",
                        color="Tan",
                        age="10",
                        mean=False)
        self.has_claws = has_claws

    def fight(self, zebra):
        if self.mean == False:
            return f"{self.name} uses its {self.has_claws} to kill zebra"
        else:
            return f"{self.name} is a nice Lion"


dog = Mammal(name="Spike",
            color="Grey",
            age=15,
            mean=False)

Rudy = Lion(has_claws=True,)
print(Rudy.fight(dog))
print(Rudy.give_age())
print(Rudy.has_claws)