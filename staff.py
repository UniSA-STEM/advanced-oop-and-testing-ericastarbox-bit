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
        """ Record a health issue for the given animal."""
        print(f"\n{self.name} is performing a health check on {animal.name}.")

        issue_type = input("Issue type (injury / illness / behaviour): ").strip().lower()
        description = input("Describe the issue: ").strip()

        # Get severity 1–5
        while True:
            severity_str = input("Severity (1–5): ").strip()
            if severity_str.isdigit():
                severity = int(severity_str)
                if 1 <= severity <= 5:
                    break
            print("Please enter a whole number between 1 and 5.")

        treatment_plan = input("Treatment plan (optional, Enter to skip): ").strip()
        notes = input("Additional notes (optional, Enter to skip): ").strip()

        if hasattr(animal, "add_health_record"):
            animal.add_health_record(
                issue_type=issue_type,
                description=description,
                severity=severity,
                treatment_plan=treatment_plan,
                notes=notes,
            )
        else:
            record = HealthRecord(
                issue_type=issue_type,
                description=description,
                severity=severity,
                treatment_plan=treatment_plan,
                notes=notes,
            )
            if not hasattr(animal, "health_records"):
                animal.health_records = []
            animal.health_records.append(record)

        while True:
            status = input(
                f"Is {animal.name} currently undergoing treatment? (y/n): "
            ).strip().lower()
            if status in ("y", "yes"):
                animal.undergoing_treatment = True
                break
            elif status in ("n", "no"):
                animal.undergoing_treatment = False
                break
            else:
                print("Please enter 'y' or 'n'.")

        print(
            f"Health record added for {animal.name}. "
            f"Undergoing treatment: {animal.undergoing_treatment}"
        )

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
        """ Cleans a single enclosure."""
        enclosure.cleanliness = 5
        print(
            f"{self.name} cleaned {enclosure.name}. "
            f"Cleanliness is now level {enclosure.cleanliness}."
        )


