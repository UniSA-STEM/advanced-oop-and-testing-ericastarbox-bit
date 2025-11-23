"""
File: swan.py
Description: Defines the swan class, representing swans in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animals.bird import Bird


class Swan(Bird):
    """
    Represents a swan in the zoo.
    Inherits from the bird class.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name, age):
        super().__init__(name, "bird", age, "omnivore")

    # ===============================
    #        BEHAVIOR METHODS
    # ===============================

    def speak(self):
        """Prints a message indicating that the swan makes a honking noise."""
        print(f"{self._name} honks!")
