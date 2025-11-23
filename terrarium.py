"""
File: terrarium.py
Description: Defines the terrarium class, representing terrarium enclosures in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure


class Terrarium(Enclosure):
    """
    Represents a terrarium enclosure of the zoo.
    Inherits from Enclosure.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name):
        super().__init__(name, size=80)
