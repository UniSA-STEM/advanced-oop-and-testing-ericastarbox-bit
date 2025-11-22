"""
File: lion.py
Description: Defines the lion class, representing lions in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from mammal import Mammal


class Lion(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "mammal", age, "carnivore")

    def speak(self):
        print(f"{self._name} says 'roar!'")
