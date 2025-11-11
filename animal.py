"""
File: filename.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC, abstractmethod

"""
This is a abstract parent class, in which we define the common attributes and methods
for all animals. Only the 'speak' method is abstract, and it is defined in the grandchild classes.
"""


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs

    @abstractmethod
    def speak(self):
        pass

    def eat(self):
        print(f"{self.__name} is eating {self.__dietary_needs}.")

    def sleep(self):
        print(f"{self.__name} is sleeping.")

    def __str__(self):
        return f"I am {self.__name} the {self.__species} and I am {self.__age} years old."


# This is an abstract subclass — no new methods or attributes.
class Mammal(Animal):
    pass


# This is an abstract subclass — no new methods or attributes.
class Reptile(Animal):
    pass


# This is an abstract subclass — no new methods or attributes.
class Bird(Animal):
    pass


class Elephant(Mammal):
    def speak(self):
        print(f"{self.__name} says 'roar!'")

class Lion(Mammal):
    def speak(self):
        print(f"{self.__name} says 'roar!'")

class Snake(Reptile):
    def speak(self):
        print(f"{self.__name} says 'hiss!'")

class Crocodile(Reptile):
    def speak(self):
        print(f"{self.__name} says 'cluck!'")

class Peacock(Bird):
    def speak(self):
        print(f"{self.__name} screams!")

class Swan(Bird):
    def speak(self):
        print(f"{self.__name} honks!")