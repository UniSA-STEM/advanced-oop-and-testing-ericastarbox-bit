"""
File: snake.py
Description: Defines the snake class, representing snakes in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animals.reptile import Reptile


class Snake(Reptile):
    """
    Represents a snake in the zoo.
    Inherits from the Reptile class.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name, age):
        super().__init__(name, "reptile", age, "carnivore")

    # ===============================
    #        BEHAVIOR METHODS
    # ===============================

    def speak(self):
        """Prints a message indicating that the snake makes a hiss sound."""
        print(f"{self._name} says 'hiss!'")
