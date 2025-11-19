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
    def __init__(self, name):
        self._name = name
        self._animals = []
        self._job = None

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        self._job = job


class Vet(Staff):
    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self._animals = []
        self._job = "Veterinarian"

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    @property
    def job(self):
        return self._job


    def health_check(self, animal: Animal):
        print("Checking animal health.")   #TODO should print the Health Report of the animal.


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self._animals = []
        self._job = "Zoo Keeper"

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    @property
    def job(self):
        return self._job

    def feed_animals(self):  # TODO Perhaps update to allow for specific animals.
        print("Feeding animals.")


class Cleaner(Staff):
    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self._animals = None
        self._job = "Cleaning"

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    def cleaning_enclosures(self, enclosure):  # TODO: Should alter cleanliness level of enclosure.
        print("Cleaning enclosures.")
