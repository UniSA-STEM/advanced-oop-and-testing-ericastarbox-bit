"""
File: elephant.py
Description: Defines the elephant class, representing elephants in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""


from animals.mammal import Mammal


class Elephant(Mammal):
    """
    Represents an elephant in the zoo.
    Inherits from the Mammal class.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name, age):
        super().__init__(name, "mammal", age, "herbivore")

    # ===============================
    #        BEHAVIOR METHODS
    # ===============================

    def speak(self):
        """Prints a message indicating that the elephant makes a 'pawoo' noise."""
        print(f"{self._name} says 'pawoo!'")
