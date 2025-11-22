"""
File: aviary.py
Description: Defines the Aviary class, used to house bird species in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure


class Aviary(Enclosure):
    def __init__(self, name):
        super().__init__(name, size=300)
