"""
File: peacock.py
Description: Defines the peacock class, representing peacocks in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""


from animals.bird import Bird


class Peacock(Bird):
    """
    Represents a peacock in the zoo.
    Inherits from the Bird class.
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
        """Prints a message indicating that the peacock makes a screaming noise."""
        print(f"{self._name} screams!")
