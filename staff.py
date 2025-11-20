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

    def feed_animal(self, animal, enclosure):
        """
        Feeds a single animal and reduces the cleanliness of its enclosure by 1.
        Cleanliness will not go below 0.
        """
        # Animal eats
        animal.eat()

        # Reduce cleanliness, ensuring it doesn't go below 0'
        new_level = max(0, enclosure.cleanliness - 1)
        enclosure.cleanliness = new_level

        print(
            f"{self.name} fed {animal.name}. "
            f"{enclosure.name}'s cleanliness is now level {enclosure.cleanliness}."
        )


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

    def clean_enclosure(self, enclosure):
        """
        Cleans a single enclosure.
        """
        enclosure.cleanliness = 5
        print(
            f"{self.name} cleaned {enclosure.name}. "
            f"Cleanliness is now level {enclosure.cleanliness}."
        )


