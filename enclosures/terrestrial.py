"""
File: terrestrial.py
Description: Defines the terrestrial class, representing terrestrial enclosures in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosures.enclosure import Enclosure


class Terrestrial(Enclosure):
    """
        Represents a terrestrial enclosure of the zoo.
        Inherits from Enclosure.
        """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name):
        super().__init__(name, size=1200)
