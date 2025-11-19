"""
File: animal.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
import random
from abc import ABC, abstractmethod
from symtable import Class

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

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age

    @property
    def dietary_needs(self):
        return self._dietary_needs

    def eat(self):
        foods = {"herbivore": ["grass", "leaves", "bark", "fruit", "flowers"],
                 "omnivore": ["insects", "nuts", "small fish", "grains"],
                 "carnivore": ["meat", "eggs", "fish"]}
        food = random.choice(foods[self._dietary_needs])
        print(f"{self._name} is eating {food}.")

    def sleep(self):
        print(f"{self._name} is sleeping.")

    def __str__(self):
        return f"I am {self._name} the {self._species} and I am {self._age} years old."
