#! python3

# What are classes?
# Inheritance: Properties of an object are inheritied by its children
# Class: Properties and methods & Theyre used to encapsulate data and functionality
# Classes are like an ATM or vending machine. -> give the user an interface when they dont care about the backend
# User gets the basic methods and some bytes* but not the implementation
# Classes is the implementation, animals is what comes out.
# 4. Properties, fields, props, attributes
# instantiation is using the class blueprints to make an object.
# Super() is the parent class you are inheriting from.
# Classes are planned or they will break easily.
# You must have the Robot init inside the super() call to inherit from it.
# Sub class from a super class

# ANYTHING in the parent class is a blueprint, with methods and  attributes you can modifiy when you instantiate it.***

# If you have many sub classes taking from the parent class, and you need to change something on the parent class, then you need to change every single class with it.

class Robot():
    def __init__(self,
                name,
                has_weapons=True,
                has_remote=True,
                has_batteries_for_remote=True,
                charge=0.75
                ):
        self.name = name
        self.has_weapons = has_weapons
        self.has_remote = has_remote
        self.has_batteries_for_remote = has_batteries_for_remote
        self.charge = charge

    def __repr__(self):
        return f"Hi, my name is {self.name}. My weapon status is {self.has_weapons}."

    def kill(self,prey):
        return f"I kill the {prey.name}!"

    def cook(self):
        return f"Nailed it!"

    def watch_soaps(self):
        return f"Why cant i just be left alone to watch my soaps!"

class CannibalBot(Robot):
    def __init__(self, hunger_status):
        super().__init__(name="dahmer",
                    has_weapons=True,
                    hastteri_remote=True,
                    has_baes_for_remote=False,
                    charge=0.33,
                    )
        self.hungry = hunger_status

    def seek_sustencance(self, prey_bot):
        if self.charge <= 0.3:
           return f"{self.kill(prey_bot)} I killed"
        else:
            return f"I am not the hungries!"
            
tob_redrum = Robot(name="redrum",
                    has_weapons=True,
                    has_remote=False,
                    has_batteries_for_remote=True,
                    charge=0.40,
                    )

dahmer = CannibalBot(hunger_status=True,)
print(dahmer.seek_sustencance(tob_redrum))
print(dahmer.cook())
print(dahmer.watch_soaps())