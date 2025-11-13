"""
File: staff.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC


class Staff(ABC):
    def __init__(self):

    def feed_animals(self):  # Perhaps update to allow for specific animals.
        print("Feeding animals.")

    def cleaning_enclosures(self, enclosure):  # Should alter cleanliness level of enclosure.
        print("Cleaning enclosures.")

    def health_check(self):
        print("Checking animal health.")
