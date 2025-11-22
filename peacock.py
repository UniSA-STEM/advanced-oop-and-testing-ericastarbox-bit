"""
File: peacock.py
Description: Defines the peacock class, representing peacocks in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from bird import Bird


class Peacock(Bird):
    def __init__(self, name, age):
        super().__init__(name, "bird", age, "omnivore")

    def speak(self):
        print(f"{self._name} screams!")
