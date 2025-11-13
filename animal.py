"""
File: animal.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

"""
This is a abstract parent class, in which we define the common attributes and methods
for all animals. Only the 'speak' method is abstract, and it is defined in the grandchild classes.
"""


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        self._name = name
        self._species = species
        self._age = age
        self._dietary_needs = dietary_needs

    @abstractmethod
    def speak(self):
        pass

    def eat(self):
        print(f"{self._name} is eating {self._dietary_needs}.")

    def sleep(self):
        print(f"{self._name} is sleeping.")

    def __str__(self):
        return f"I am {self._name} the {self._species} and I am {self._age} years old."


# This is an abstract subclass — no new methods or attributes.
class Mammal(Animal, ABC):
    pass


# This is an abstract subclass — no new methods or attributes.
class Reptile(Animal, ABC):
    pass


# This is an abstract subclass — no new methods or attributes.
class Bird(Animal, ABC):
    pass


class Elephant(Mammal):   # Need to come through and add attributes to the class
    def speak(self):
        print(f"{self._name} says 'roar!'")

class Lion(Mammal):
    def speak(self):
        print(f"{self._name} says 'roar!'")

class Snake(Reptile):
    def speak(self):
        print(f"{self._name} says 'hiss!'")

class Crocodile(Reptile):
    def speak(self):
        print(f"{self._name} says 'cluck!'")

class Peacock(Bird):
    def speak(self):
        print(f"{self._name} screams!")

class Swan(Bird):
    def speak(self):
        print(f"{self._name} honks!")