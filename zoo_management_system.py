"""
File: zoo_management_system.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
from bird import Bird
from crocodile import Crocodile
from elephant import Elephant
from enclosure import Terrestrial, Terranium, Aviary
from lion import Lion
from mammal import Mammal
from peacock import Peacock
from reptile import Reptile
from snake import Snake
from staff import Cleaner, Vet, ZooKeeper
from swan import Swan


class ZooManagementSystem:
    """ A class representing a Zoo Management System."""

    def __init__(self, name):
        self.name = name
        self.animals = []
        self.enclosures = []
        self.staff = []

    def generate_report(self):
        """
        Generates a report of the Zoo Management System.
        """
        print("\n=========================================")
        print(f"         {self.name.upper()} MANAGEMENT REPORT")
        print("=========================================")
        print()

        print("ANIMALS")
        print(f"Total Animals: {len(self.animals)}")
        for animal in self.animals:
            print(f" - {animal.name}\n     Species: {animal.__class__.__name__}\n     "
                  f"Age: {animal.age}\n")
        print()

        print("ENCLOSURES")
        print(f"Total Enclosures: {len(self.enclosures)}")
        for enclosure in self.enclosures:
            print(f" - {enclosure.name}\n     Size: {enclosure.size}m\u00b2\n     Cleanliness: "
                  f"Level {enclosure.cleanliness}\n     Animals: {enclosure.animals if enclosure.animals
                  else 'None'}")
        print()

        print("STAFF")
        print(f"Total Staff: {len(self.staff)}")
        for staff in self.staff:
            print(f" - {staff.name}\n    Job: {staff.job}\n     Assigned Animals: {staff.animals if
            staff.animals else 'None'}\n")
        print()

        print("End of Report")
        print("----------------------------------------")

    def schedule_daily_routines(self):  # TODO: Such as cleanings and feedings
        """
        Generates and prints a daily routine schedule for the zoo,
        including feeding times for animals and cleaning tasks for enclosures.
        """
        print("\n==========================================")
        print(f"        {self.name.upper()} DAILY ROUTINES")
        print("==========================================\n")

        # Feeding schedule
        print("FEEDING SCHEDULE")
        if not self.animals:
            print(" - No animals to feed.\n")
        else:
            for animal in self.animals:
                print(f" - Feed {animal.name} ({animal.__class__.__name__})")

        print("\nCLEANING SCHEDULE")
        if not self.enclosures:
            print(" - No enclosures to clean.\n")
        else:
            for enclosure in self.enclosures:
                print(f" - Clean {enclosure.name} (Cleanliness level: {enclosure.cleanliness})")

        print("\nEnd of Daily Routine Schedule")
        print("------------------------------------------\n")

    def get_required_enclosure(self, animal):
        """ Returns the enclosure class required for a given animal type."""
        rules = {
            Mammal: Terrestrial,
            Reptile: Terranium,
            Bird: Aviary
        }
        return rules.get(type(animal))

    def is_valid_enclosure(self, animal, enclosure):
        """ Returns True if the enclosure is appropriate for the animal."""
        required = self.get_required_enclosure(animal)
        return isinstance(enclosure, required)

    def assign_animal(self, animal, enclosure):
        """ Assigns an animal to an enclosure if the enclosure type is valid."""
        if self.is_valid_enclosure(animal, enclosure):
            enclosure.animals.append(animal)
            print(f"{animal.name} assigned to {enclosure.name}.")
        else:
            print("Invalid assignment: enclosure type does not match the animal.")

    def validate_choice(self, choice):
        """ Validate the user's choice when calling the 'modify' method."""
        if choice.lower() not in ["add", "remove"]:
            print("Invalid choice. Must be 'add' or 'remove'.")
            return False
        return True

    def validate_item(self, item):
        """ Validate the item when calling the 'modify' method."""
        if item.lower() not in ["animal", "enclosure", "staff"]:
            print("Invalid item. Must be 'animal', 'enclosure', or 'staff'.")
            return False
        return True

    def get_valid_age(self):
        """
        Prompts the user to enter an animal's age and validates the input.
        Continues prompting until a non-negative whole number is entered,
        then returns the age as an integer.
        """
        while True:
            age_input = input("Enter age: ")
            try:
                age = float(age_input)
                if age.is_integer() and age >= 0:
                    return int(age)
            except:
                pass
            print("Invalid age — please enter a whole number.")

    def get_item_class(self, item):
        """ Returns the class of an item based on user input."""
        item_matrix = {
            "animal": {
                "lion": Lion, "crocodile": Crocodile, "elephant": Elephant,
                "peacock": Peacock, "snake": Snake, "swan": Swan
            },
            "enclosure": {
                "terrestrial": Terrestrial, "terranium": Terranium, "aviary": Aviary
            },
            "staff": {
                "vet": Vet, "zoo keeper": ZooKeeper, "cleaner": Cleaner
            }
        }

        options = list(item_matrix[item].keys())

        print(f"Choose {item} type:")
        for i, key in enumerate(options, start=1):
            print(f"{i}. {key.title()}")

        choice = input("Enter your choice: ").strip().lower()

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                key = options[idx]
                return item_matrix[item][key]

        if choice in options:
            return item_matrix[item][choice]

        print("Invalid selection.")
        return None

    def create_object(self, item, cls):
        """ Creates an object based on user input."""
        name = input(f"What is the name of the {item}? ").title()

        if item == "animal":
            age = self.get_valid_age()
            return cls(name, age)

        return cls(name)

    def get_target_list(self, item):
        return {
            "animal": self.animals,
            "enclosure": self.enclosures,
            "staff": self.staff
        }[item]

    def add_item(self, obj, target_list, item):
        """ Adds an item to the target list."""
        target_list.append(obj)
        print(f"Added {obj.__class__.__name__} named {obj.name} to {self.name}'s {item} list.\n")

    def remove_item(self, obj, target_list, item):
        """ Removes an item from the target list."""
        if obj in target_list:
            target_list.remove(obj)
            print(f"Removed {obj.__class__.__name__} named {obj.name} from {self.name}'s {item} list.\n")
        else:
            print("Item not found.\n")

    def modify(self, choice: str, item: str):
        """ Modify the Zoo Management System."""
        item = item.lower()
        choice = choice.lower()

        if not self.validate_choice(choice):
            return

        if not self.validate_item(item):
            return

        target_list = self.get_target_list(item)

        # Add branch
        if choice == "add":
            cls = self.get_item_class(item)
            if cls is None:
                return
            obj = self.create_object(item, cls)
            self.add_item(obj, target_list, item)

        # Remove branch
        else:
            if not target_list:
                print(f"No {item}s to remove.\n")
                return

            print(f"Select a {item} to remove: ")
            for i, obj in enumerate(target_list, start=1):
                # animals/staff have .name, enclosures .name too
                print(f"{i}. {obj.name} ({obj.__class__.__name__})")

            choice_str = input("Enter number: ").strip()
            if not choice_str.isdigit():
                print("Invalid selection.\n")
                return

            idx = int(choice_str) - 1
            if not (0 <= idx < len(target_list)):
                print("Invalid selection.\n")
                return

            obj = target_list[idx]
            self.remove_item(obj, target_list, item)

#TODO Remove the test code.
zoopac = ZooManagementSystem("Zoopac")
zoopac.modify("add", "animal")
zoopac.modify("remove", "animal")
