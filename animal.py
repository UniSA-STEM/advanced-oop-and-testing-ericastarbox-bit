"""
File: animal.py
Description: An abstract animal base class that defines common attributes
and methods for all animals in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
import random
from abc import ABC, abstractmethod

from health_record import HealthRecord

"""
This is a abstract parent class, in which we define the common attributes and methods
for all animals. Only the 'speak' method is abstract, and it is defined in the grandchild classes.
"""


class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, dietary_needs: str):
        self._name = name
        self._species = species
        self._age = age
        self._dietary_needs = dietary_needs
        self._on_display = True

        # Health-related attributes
        self._health_records: list[HealthRecord] = []
        self._undergoing_treatment = False

    @abstractmethod
    def speak(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age

    @property
    def dietary_needs(self):
        return self._dietary_needs

    @property
    def health_records(self):
        return self._health_records

    @health_records.setter
    def health_records(self, record: HealthRecord):
        self._health_records.append(record)

    @property
    def undergoing_treatment(self):
        return self._undergoing_treatment

    @undergoing_treatment.setter
    def undergoing_treatment(self, value):
        self._undergoing_treatment = value

    @property
    def treatment_status(self) -> str:
        """Human-readable status for reports."""
        return "Yes" if self.undergoing_treatment else "No"

    @property
    def display_status(self) -> str:
        """Human-readable status for reports."""
        return "Yes" if self._on_display else "No"

    @property
    def on_display(self):
        return self._on_display

    @on_display.setter
    def on_display(self, value):
        self._on_display = value

    def eat(self):
        foods = {"herbivore": ["grass", "leaves", "bark", "fruit", "flowers"],
                 "omnivore": ["insects", "nuts", "small fish", "grains"],
                 "carnivore": ["meat", "eggs", "fish"]}
        food = random.choice(foods[self._dietary_needs])
        print(f"{self._name} is eating {food}.")

    def sleep(self):
        print(f"{self._name} is sleeping.")

    def __str__(self):
        return f"I am {self._name} the {self._species} and I am {self._age} years old."

    def add_health_record(
            self,
            issue_type: str,
            description: str,
            severity: int,
            treatment_plan: str = "",
            notes: str = ""
    ):
        record = HealthRecord(
            issue_type=issue_type,
            description=description,
            severity=severity,
            treatment_plan=treatment_plan,
            notes=notes
        )
        self.health_records.append(record)
        print(f"Health record added for {self._name}: {record}")
