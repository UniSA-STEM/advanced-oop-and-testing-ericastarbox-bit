"""
File: enclosure.py
Description: Defines
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from abc import ABC

# TODO Separate all classes into their own files.

class Enclosure(ABC):
    def __init__(self, size: int, cleanliness: int, species: str):
        self.__size = size
        self.__cleanliness = cleanliness
        self.__species = species
        self.__animals = []

    def report_status(self):
        print(f"Enclosure size: {self.__size} square meters.\n"
              f"Enclosure environment type: {self.__class__.__name__}.\n"
              f"Enclosure cleanliness: {self.__cleanliness}.\n"
              f"Enclosure species: {self.__species}.")

    def list_animals(self):
        print(f"Animals in the enclosure: {self.__animals}")


class Terrestrial(Enclosure):
    pass


class Terranium(Enclosure):
    pass


class Aviary(Enclosure):
    pass
