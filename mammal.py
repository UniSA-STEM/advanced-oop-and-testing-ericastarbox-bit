"""
File: mammal.py
Description: Defines the Mammal class, which is a subclass of Animal.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal
from abc import ABC

# This is an abstract subclass — no new methods or attributes.
class Mammal(Animal, ABC):
    pass