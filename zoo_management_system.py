"""
File: zoo_management_system.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from animal import Animal
from bird import Bird
from crocodile import Crocodile
from elephant import Elephant
from enclosure import Enclosure, Terrestrial, Terranium, Aviary
from lion import Lion
from mammal import Mammal
from peacock import Peacock
from reptile import Reptile
from snake import Snake
from staff import Staff, Cleaner, Vet, ZooKeeper
from swan import Swan


# TODO Separate all classes into their own files.

class ZooManagementSystem:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.enclosures = []
        self.staff = []

    def generate_report(self):  # TODO: Should print a report across the zoo, including animals, enclosures, and staff.
        print("\n=========================================")
        print(f"         {self.name.upper()} MANAGEMENT REPORT")
        print("=========================================")
        print()

        print("ANIMALS")
        print(f"Total Animals: {len(self.animals)}")
        for animal in self.animals:
            print(f" - {animal.name}\n    Species: {animal.__class__.__name__}\n    Age: {animal.age}\n")
        print()

        print("ENCLOSURES")
        print(f"Total Enclosures: {len(self.enclosures)}")
        for enclosure in self.enclosures:
            print(f" - {enclosure.name}\n    Size: {enclosure._size}\n    Cleanliness: {enclosure._cleanliness}\n"
                  f"Animals: {enclosure._animals}\n   ")
        print()

        print("STAFF")
        print(f"Total Staff: {len(self.staff)}")
        for staff in self.staff:
            print(f" - {staff.name}\n    Job: {staff.job}\n   Assigned Animals: {staff.animals}\n")
        print()

        print("End of Report")
        print("----------------------------------------")

    def schedule_daily_routines(self):  # TODO: Such as cleanings and feedings
        print("Scheduling daily routines...")

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

    def modify(self, choice: str,
               item: str):  # TODO this will need to be broken into several functions, as there is too much logic in one.
        # Validate the choice.
        choice_list = ["add", "remove"]
        if choice.lower() not in choice_list:
            print(f"Invalid choice. Choice must be one of the following: {choice_list}.")
            return

        # Validate the item.
        item_list = ["animal", "enclosure", "staff"]
        if item.lower() not in item_list:
            print(f"Invalid item. Item must be one of the following: {item_list}.")
            return

        # An item matrix, linking the item type to the correct list.
        item_matrix = {
            "animal": {"lion": Lion, "crocodile": Crocodile, "elephant": Elephant, "peacock": Peacock,
                       "snake": Snake, "swan": Swan},
            "enclosure": {"terrestrial": Terrestrial, "terranium": Terranium, "aviary": Aviary},
            "staff": {"vet": Vet, "zoo keeper": ZooKeeper, "cleaner": Cleaner}
        }

        keys = list(item_matrix[item].keys())

        # Give the user a list of available items to choose from.
        options = "\n".join(f"{i + 1}. {key}" for i, key in enumerate(keys))
        print(f"Choose {item} type to add to {self.name}:")
        print(options)
        new_item = input("Enter your choice: ")  # TODO now should create an instance of the object

        # Validate the user's choice.
        # If the user entered a number:
        if new_item.isdigit():
            index = int(new_item) - 1
            selected_key = keys[index]
            # find class in item matrix
            cls = item_matrix[item][selected_key]

        # If the user entered the name directly
        elif new_item in keys:
            selected_key = new_item
            cls = item_matrix[item][selected_key]
        else:
            print("Invalid selection.")
            return

        # Ask for attributes
        name = input(f"What is the name of the {item}? ")

        if item == "animal":
            age = int(input(f"How many years old is {name}? "))
            obj = cls(name, age)
        else:
            obj = cls(name)

        # Dictionary to map class types to the correct attribute list.
        class_to_attribute = {
            "animal": self.animals,
            "enclosure": self.enclosures,
            "staff": self.staff
        }

        # Defines which attribute list to add/remove the item to/from.
        target_attribute_list = class_to_attribute[item.lower()]

        # Perform the change
        if choice == "add":
            target_attribute_list.append(obj)
            print(f"Added {obj.__class__.__name__} named {obj.name} to {self.name}'s {item} list.")
        elif choice == "remove":
            if obj in target_attribute_list:
                target_attribute_list.remove(obj)
                print(f"Removed {obj.__class__.__name__} named {obj.name} from {self.name}'s {item} list.")
            else:
                print("Item not found.")


zoopac = ZooManagementSystem("Zoopac")
zoopac.modify("add", "animal")
zoopac.modify("add", "staff")
zoopac.modify("add", "enclosure")
zoopac.generate_report()
