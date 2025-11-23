"""
File: cleaner.py
Description: Defines the cleaner class, representing staff members who clean the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff


class Cleaner(Staff):
    """
    Represents a staff member who cleans the zoo.
    Inherits core staff attributes and methods from the Staff class.
    Provides functionality to clean enclosures.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self._animals = None
        self._job = "Cleaning"

    # ===============================
    #           PROPERTIES
    # ===============================

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    # ===============================
    #           SETTERS
    # ===============================

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    # ===============================
    #        STAFF ACTIONS
    # ===============================

    def clean_enclosure(self, enclosure):
        """Cleans the specified enclosure and restores its cleanliness to 5."""
        enclosure.cleanliness = 5
        print(
            f"{self.name} cleaned {enclosure.name}. "
            f"Cleanliness is now level {enclosure.cleanliness}."
        )
