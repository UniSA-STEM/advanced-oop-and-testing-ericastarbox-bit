"""
File: staff.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC

from animal import Animal

# TODO Separate all classes into their own files.

class Staff(ABC):
    def __init__(self):
        self.animals = []
        self.job = None


class Vet(Staff):
    pass

    def health_check(self, animal: Animal):
        print("Checking animal health.")   #TODO should print the Health Report of the animal.


class ZooKeeper(Staff):
    def __init__(self):
        super().__init__()
        self.animals = []
        self.job = ""

    def feed_animals(self):  # TODO Perhaps update to allow for specific animals.
        print("Feeding animals.")


class Cleaner(Staff):
    def __init__(self):
        super().__init__()
        self.animals = None
        self.job = "Cleaning"

    def cleaning_enclosures(self, enclosure):  # TODO: Should alter cleanliness level of enclosure.
        print("Cleaning enclosures.")
