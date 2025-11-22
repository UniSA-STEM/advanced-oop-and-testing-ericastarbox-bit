"""
File: terranium.py
Description: Defines
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from enclosure import Enclosure


class Terranium(Enclosure):
    def __init__(self, name):
        super().__init__(name, size=80)
