"""
File: vet.py
Description: Defines the vet class, representing veterinarians in the zoo.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from staff import Staff
from animal import Animal
from health_record import HealthRecord


class Vet(Staff):
    """
    Represents a veterinarian working in the zoo.
    Inherits core staff attributes and methods from the Staff class.
    Provides functionality to perform health checks on animals, record
    medical issues, and update the animal's treatment status.
    """

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name):
        super().__init__(name)
        self._name = name
        self._animals = []
        self._job = "Veterinarian"

    # ===============================
    #           PROPERTIES
    # ===============================

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals

    @property
    def job(self):
        return self._job

    # ===============================
    #           SETTERS
    # ===============================

    @animals.setter
    def animals(self, animals):
        self._animals = animals

    # ===============================
    #        STAFF ACTIONS
    # ===============================

    def health_check(self, animal: Animal):
        """Conducts a health check on the given animal and records the findings."""

        print(f"\n{self.name} is performing a health check on {animal.name}.")

        # Collect health issue details.
        issue_type = self._get_issue_type()
        description = input("Describe the issue: ").strip()
        severity = self._get_valid_severity()

        # Optional details.
        treatment_plan = input("Treatment plan (optional, Enter to skip): ").strip()
        notes = input("Additional notes (optional, Enter to skip): ").strip()

        # Record the health issue using the animal's own method if available.
        self._record_animal_health(
            animal,
            issue_type,
            description,
            severity,
            treatment_plan,
            notes
        )

        # Update treatment and display status.
        self._update_treatment_status(animal)

        print(
            f"Health record added for {animal.name}."
            f"Undergoing treatment: {animal.undergoing_treatment}"
        )

    # ===============================
    #        HELPER METHODS
    # ===============================

    @staticmethod
    def _get_issue_type():
        """Prompt the user for a valid issue type."""
        while True:
            issue = input("Issue type (injury / illness / behavioural): ").strip().lower()
            if issue in HealthRecord.VALID_ISSUE_TYPES:
                return issue
            print(f"Please enter one of: {HealthRecord.VALID_ISSUE_TYPES}")

    @staticmethod
    def _get_valid_severity():
        """Prompt the user for valid severity between 1 and 5."""
        while True:
            severity_str = input("Severity (1–5): ").strip()
            if severity_str.isdigit():
                severity = int(severity_str)
                if 1 <= severity <= 5:
                    return severity
            print("Please enter a whole number between 1 and 5.")

    @staticmethod
    def _record_animal_health(animal, issue_type, description, severity, plan, notes):
        """Adds a health record using the animal's own method, or manually if needed."""

        # If the animal implements add_health_record, use it.
        if hasattr(animal, "add_health_record"):
            animal.add_health_record(
                issue_type=issue_type,
                description=description,
                severity=severity,
                treatment_plan=plan,
                notes=notes,
            )
            return

        # Fallback in case the animal lacks the method (very unlikely).
        record = HealthRecord(
            issue_type=issue_type,
            description=description,
            severity=severity,
            treatment_plan=plan,
            notes=notes,
        )

        # Ensure list exists.
        if not hasattr(animal, "health_records"):
            animal.health_records = []

        animal.health_records.append(record)

    @staticmethod
    def _update_treatment_status(animal):
        """Ask the user whether the animal is under treatment and update attributes."""
        while True:
            status = input(
                f"Is {animal.name} currently undergoing treatment? (y/n): "
            ).strip().lower()

            if status in ("y", "yes"):
                animal.undergoing_treatment = True
                animal.on_display = False  # Remove from public display
                return

            if status in ("n", "no"):
                animal.undergoing_treatment = False
                animal.on_display = True  # Place back on display
                return

            print("Please enter 'y' or 'n'.")

    def demo_health_check(self, animal):
        """
        Non-interactive demo version of health_check() for demo.py.
        Creates a fixed example health record without the users input.
        """

        # Create a health record with demo details
        issue_type = "Injury"
        description = "Minor leg strain"
        severity = 2
        treatment_plan = "Apply rest and cold compress"

        # Create a simple string representation of the health record
        record = (
            f"[DEMO] {issue_type} (Severity {severity}): {description}. "
            f"Treatment: {treatment_plan}"
        )

        # Add the health record to the animal's list of records'
        animal.health_records.append(record)

        # Mark the animal as undergoing treatment
        animal.undergoing_treatment = True

        # Display the health record
        print(f"{self.name} recorded a demo health issue for {animal.name}:")
        print(f" - {record}\n")

