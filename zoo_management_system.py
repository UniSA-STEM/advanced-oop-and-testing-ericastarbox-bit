"""
File: zoo_management_system.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Reptile, Mammal, Bird, Animal
from enclosure import Enclosure, Terrestrial, Terranium, Aviary
from staff import Staff

# TODO Separate all classes into their own files.

class ZooManagementSystem:
    def __init__(self):
        self.animals = []
        self.enclosures = []
        self.staff = []

    def generate_report(self):   # TODO: Should print a report across the zoo, including animals, enclosures, and staff.
        print("Generating report...")

    def schedule_daily_routines(self):  # TODO: Such as cleanings and feedings

    """
    Validation: animals can only be assigned to certain environment types.
    Mammals to terrestrial
    Reptiles to terrarium
    Birds to aviary
    Note: Is there any way to use a dictionary to map and validate these and shorten the code?
    """

    def assign_animal(self, animal, enclosure):  # Assign animal to enclosure.
        animal_enclosures = {Mammal: Terrestrial, Reptile: Terranium, Bird: Aviary}

        def validate_enclosure(animal_obj, enclosure_obj):  # Check that the correct enclosure type is assigned.
            required_enclosure = animal_enclosures.get(type(animal_obj))
            return isinstance(enclosure_obj, required_enclosure)

        if validate_enclosure(animal, enclosure):  # If correct enclosure type, add animal to enclosure.
            enclosure.animals.append(animal)
        else:
            print("Invalid assignment.")

    """
    Helper method to add and remove animals, enclosures, or staff to the ZooManagementSystem. 
    This was originally two separate methods, but I decided to combine them into one.
    """

    def modify(self, choice: str, item):
        # Validate the choice.
        if choice not in ["add", "remove"]:
            print("Invalid choice.")
            return

        # Dictionary to map class types to the correct list.
        class_to_attribute = {
            Animal: self.animals,
            Enclosure: self.enclosures,
            Staff: self.staff
        }

        # Look up the correct list for this item type
        target_list = class_to_attribute.get(type(item))

        if target_list is None:
            print("Invalid item type.")
            return

        # Perform the change
        if choice == "add":
            target_list.append(item)
        elif choice == "remove":
            target_list.remove(item)
