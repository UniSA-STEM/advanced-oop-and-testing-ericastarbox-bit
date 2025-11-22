"""
File: snake.py
Description: Defines the snake class, representing snakes in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from reptile import Reptile


class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, "reptile", age, "carnivore")

    def speak(self):
        print(f"{self._name} says 'hiss!'")
