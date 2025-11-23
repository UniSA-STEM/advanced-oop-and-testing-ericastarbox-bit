"""
File: crocodile.py
Description: Defines the crocodile class, representing crocodiles in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""


from reptile import Reptile


class Crocodile(Reptile):
    """
    Represents a crocodile in the zoo.
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
        """Prints a message indicating that the crocodile makes a clucking noise."""
        print(f"{self._name} says 'cluck!'")
