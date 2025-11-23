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
    """
    Represents a Lion in the zoo.
    Inherits from the Mammal class.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name, age):
        super().__init__(name, "mammal", age, "carnivore")

    # ===============================
    #        BEHAVIOR METHODS
    # ===============================

    def speak(self):
        """Prints a message indicating that the lion makes a roar."""
        print(f"{self._name} says 'roar!'")
