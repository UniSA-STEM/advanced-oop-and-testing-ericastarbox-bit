"""
File: enclosure.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from importlib.metadata import pass_none


class Enclosure:
    def __init__(self, size: int, environment_type: str, cleanliness: int, species: str):
        self.__size = size
        self.__environment_type = environment_type
        self.__cleanliness = cleanliness
        self.__species = species
        self.__animals = []

    def report_status(self):
        print(f"Enclosure size: {self.__size} square meters.\n"
              f"Enclosure environment type: {self.__environment_type}.\n"
              f"Enclosure cleanliness: {self.__cleanliness}.\n"
              f"Enclosure species: {self.__species}.")

    def list_animals(self):
        print(f"Animals in the enclosure: {self.__animals}")

Class Terrestrial(Enclosure):   # TODO: detemine if you wish to make this a subclass of Enclosure.
    pass



