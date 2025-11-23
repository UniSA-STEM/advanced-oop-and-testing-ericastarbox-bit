"""
File: enclosure.py
Description: Defines the enclosure class, representing the zoo's enclosures.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from abc import ABC


class Enclosure(ABC):
    """
    Abstract base class representing an enclosure in the zoo.
    Each enclosure has a name, size, and cleanliness rating, and
    a list of animals that live in it.
    Specific enclosure types (e.g. Aviary, Terrarium, Terrestrial) inherit from this class.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size
        self._cleanliness = 5
        self._animals = []

    # ===============================
    #           PROPERTIES
    # ===============================

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size

    @property
    def cleanliness(self):
        return self._cleanliness

    @property
    def animals(self):
        return self._animals

    # ===============================
    #           SETTERS
    # ===============================
    @cleanliness.setter
    def cleanliness(self, cleanliness):
        self._cleanliness = cleanliness

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    # ===============================
    #          REPORT METHODS
    # ===============================

    def report_status(self):
        """Prints a summary of the enclosure's details"""
        print(f"Enclosure size: {self._size} square meters.\n"
              f"Enclosure environment type: {self.__class__.__name__}.\n"
              f"Enclosure cleanliness: {self._cleanliness}.\n")

    def list_animals(self):
        """Prints the animals currently in the enclosure."""
        print(f"Animals in the enclosure: {self._animals}")
