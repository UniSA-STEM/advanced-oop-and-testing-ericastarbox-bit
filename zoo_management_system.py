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
from vet import Vet
from cleaner import Cleaner
from zoo_keeper import ZooKeeper
from swan import Swan


class ZooManagementSystem:
    """ A class representing a Zoo Management System."""

    def __init__(self, name):
        self.name = name
        self.animals = []
        self.enclosures = []
        self.staff = []
        self.enclosure_rules = [
            (Mammal, Terrestrial),
            (Reptile, Terranium),
            (Bird, Aviary)
        ]

        # Staff assignment rules
        self.animal_staff_types = (ZooKeeper, Vet)  # can be assigned to ANIMALS
        self.enclosure_staff_types = (ZooKeeper, Cleaner)  # can be assigned to ENCLOSURES

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
            print(f" - {animal.name}\n"
                  f"     Species: {animal.__class__.__name__}\n"
                  f"     Age: {animal.age}\n"
                  f"     Undergoing treatment: {animal.treatment_status}"
                  f"     On display: {animal.on_display}")
        print()

        print("ENCLOSURES")
        print(f"Total Enclosures: {len(self.enclosures)}")
        for enclosure in self.enclosures:
            if enclosure.animals:
                animals_str = ", ".join(
                    f"{animal.name} ({animal.__class__.__name__})"
                    for animal in enclosure.animals
                )
            else:
                animals_str = "None"

            print(
                f" - {enclosure.name}\n"
                f"     Size: {enclosure.size}m\u00b2\n"
                f"     Cleanliness: Level {enclosure.cleanliness}\n"
                f"     Animals: {animals_str}"
            )
            print()
        print()

        print("STAFF")
        print(f"Total Staff: {len(self.staff)}")
        for staff in self.staff:
            animal_names = ", ".join(a.name for a in staff.animals) if staff.animals else "None"
            enclosure_names = ", ".join(e.name for e in staff.enclosures) if staff.enclosures else "None"

            print(
                f" - {staff.name}\n"
                f"     Job: {staff.job}\n"
                f"     Assigned Animals: {animal_names}\n"
                f"     Assigned Enclosures: {enclosure_names}\n"
            )
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
        """Returns the enclosure class required for a given animal type."""
        for animal_type, enclosure_type in self.enclosure_rules:
            if isinstance(animal, animal_type):
                return enclosure_type

        # If no rule matched
        return None

    def is_valid_enclosure(self, animal, enclosure):
        """Returns True if the enclosure is appropriate for the animal."""
        required = self.get_required_enclosure(animal)
        if required is None:
            print("No enclosure rule defined for this type of animal.")
            return False
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
            except ValueError:
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

        print(f"\nChoose {item} type:")
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
        name = input(f"\nWhat is the name of the {item}? ").title()

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
        print(f"Added {obj.__class__.__name__} named {obj.name} to {self.name}'s {item} list.")

    def remove_item(self, obj, target_list, item):
        """ Removes an item from the target list."""
        if obj in target_list:
            target_list.remove(obj)
            print(f"Removed {obj.__class__.__name__} named {obj.name} from {self.name}'s {item} list.\n")
        else:
            print("Item not found.\n")

    def _handle_add(self, item: str, target_list: list):
        """Handles adding animals, enclosures, or staff."""
        # Special handling for animals – enforce enclosure assignment
        if item == "animal":
            # Must have at least one enclosure in the zoo
            if not self.enclosures:
                print("You must add at least one enclosure before adding animals.\n")
                return

            cls = self.get_item_class(item)
            if cls is None:
                return

            # Create the animal object
            animal = self.create_object(item, cls)

            # Select a suitable enclosure based on the animal type
            enclosure = self._select_enclosure_for_animal(animal)
            if enclosure is None:
                print(
                    f"{animal.name} was not added because no suitable enclosure "
                    "was selected or available.\n"
                )
                return

            # Add animal to the zoo list and assign to enclosure
            self.add_item(animal, target_list, item)
            self.assign_animal(animal, enclosure)
            return  # done with the animal branch

        # Default add logic for enclosure/staff
        cls = self.get_item_class(item)
        if cls is None:
            return

        obj = self.create_object(item, cls)
        self.add_item(obj, target_list, item)

    def _handle_remove(self, item: str, target_list: list):
        """Handles removal of animals, enclosures, or staff."""
        if not target_list:
            print(f"No {item}s to remove.\n")
            return

        print(f"Select a {item} to remove: ")
        for i, obj in enumerate(target_list, start=1):
            print(f"{i}. {obj.name} ({obj.__class__.__name__})")

        idx = self._select_index(target_list, "Enter number: ")
        if idx is None:
            return

        obj = target_list[idx]
        self.remove_item(obj, target_list, item)

    def _select_staff_member(self, staff_class, role_name: str):
        """
        Returns a staff member of the given type selected by the user,
        or None if no staff of that type exist or selection fails.
        """
        staff_of_type = [member for member in self.staff if isinstance(member, staff_class)]
        if not staff_of_type:
            print(f"No {role_name}s available.")
            return None

        # If only one available, auto-select
        if len(staff_of_type) == 1:
            selected = staff_of_type[0]
            print(f"{role_name.capitalize()} selected: {selected.name}")
            return selected

        # Otherwise, give the user the choice to select
        print(f"Select a {role_name}:")
        for index, member in enumerate(staff_of_type, start=1):
            print(f"{index}. {member.name}")

        idx = self._select_index(staff_of_type, f"Enter the number of the {role_name.lower()}: ")
        if idx is None:
            return None

        return staff_of_type[idx]

    def _select_enclosure(self):
        """ Returns an Enclosure instance selected by the user, or None if selection fails."""
        if not self.enclosures:
            print("There are no enclosures to clean.")
            return None

        print("Available enclosures:")
        for index, enclosure in enumerate(self.enclosures, start=1):
            print(f"{index}. {enclosure.name.capitalize()} (Cleanliness level: {enclosure.cleanliness})")

        idx = self._select_index(self.enclosures, "Enter the number of the enclosure to select: ")
        if idx is None:
            return None

        return self.enclosures[idx]

    def _select_enclosure_for_animal(self, animal):
        """ Returns an enclosure of the correct type for the given animal"""
        required_type = self.get_required_enclosure(animal)
        if required_type is None:
            print("No enclosure rule defined for this type of animal.")
            return None

        # Filter enclosures to only those of the required type
        valid_enclosures = [
            enclosure for enclosure in self.enclosures
            if isinstance(enclosure, required_type)
        ]

        if not valid_enclosures:
            print(f"No {required_type.__name__} enclosures available for this animal.")
            return None

        print(f"\nSelect an enclosure for {animal.name}:")
        for index, enclosure in enumerate(valid_enclosures, start=1):
            print(
                f"{index}. {enclosure.name} "
                f"(Cleanliness level: {enclosure.cleanliness})"
            )

        choice_str = input("Enter the number of the enclosure: ").strip()
        if not choice_str.isdigit():
            print("Invalid selection. Please enter a number.")
            return None

        choice_index = int(choice_str) - 1
        if not (0 <= choice_index < len(valid_enclosures)):
            print("Invalid selection. Number out of range.")
            return None

        return valid_enclosures[choice_index]

    def _select_animal(self):
        """ Returns an Animal selected by the user, or None if selection fails."""
        if not self.animals:
            print("There are no animals available.")
            return None

        print("Available animals:")
        for index, animal in enumerate(self.animals, start=1):
            print(f"{index}. {animal.name} ({animal.__class__.__name__}, age {animal.age})")

        idx = self._select_index(self.animals, "Enter the number of the animal: ")
        if idx is None:
            return None

        return self.animals[idx]

    def _select_index(self, items, prompt: str) -> int | None:
        """
        Generic helper to let the user select an item by index.
        Returns the selected index or None if selection fails.
        """
        if not items:
            print("There are no items to select from.")
            return None

        choice_str = input(prompt).strip()
        if not choice_str.isdigit():
            print("Invalid selection. Please enter a number.")
            return None

        idx = int(choice_str) - 1
        if not (0 <= idx < len(items)):
            print("Invalid selection. Number out of range.")
            return None

        return idx

    def _find_enclosure_for_animal(self, animal):
        """ Returns the enclosure that contains the given animal, or None if not found."""
        for enclosure in self.enclosures:
            if animal in enclosure.animals:
                return enclosure
        return None

    def clean_enclosure(self):
        """ Selects a cleaner and an enclosure to clean, then cleans the enclosure."""

        cleaner = self._select_staff_member(Cleaner, "Cleaner")
        if cleaner is None:
            return

        enclosure = self._select_enclosure()
        if enclosure is None:
            return

        cleaner.clean_enclosure(enclosure)

    def feed_animals(self):
        """
        Coordinates selection of a Zoo Keeper and an animal,
        then asks the Zoo Keeper to feed the animal.
        Feeding reduces the cleanliness of the animal's enclosure by 1.
        """
        # Select a Zoo Keeper
        zoo_keeper = self._select_staff_member(ZooKeeper, "Zoo Keeper")
        if zoo_keeper is None:
            return

        # Select an animal
        animal = self._select_animal()
        if animal is None:
            return

        # Find the animal's enclosure
        enclosure = self._find_enclosure_for_animal(animal)
        if enclosure is None:
            print(f"{animal.name} is not currently assigned to any enclosure.")
            return

        # Ask the Zoo Keeper to feed the animal
        zoo_keeper.feed_animal(animal, enclosure)

    def view_animal_health(self):
        """Let the user select an animal and view its health records."""
        if not self.animals:
            print("There are no animals in the zoo yet.")
            return

        print("\nAnimals in the zoo:")
        for index, animal in enumerate(self.animals, start=1):
            print(f"{index}. {animal.name} ({animal.__class__.__name__}, age {animal.age})")

        choice_str = input("Enter the number of the animal to view health issues: ").strip()
        if not choice_str.isdigit():
            print("Invalid selection. Please enter a number.")
            return

        idx = int(choice_str) - 1
        if not (0 <= idx < len(self.animals)):
            print("Invalid selection. Number out of range.")
            return

        animal = self.animals[idx]

        treatment_status = "Yes" if getattr(animal, "undergoing_treatment", False) else "No"
        print(f"\nHealth issues for {animal.name} (Undergoing treatment: {'Yes' if animal.undergoing_treatment
        else 'No'}):")

        if not getattr(animal, "health_records", []):
            print(" - No health records have been recorded for this animal.")
            return

        for record in animal.health_records:
            print(f" - {record}")

    def record_animal_health(self):
        """Choose a Vet and an Animal, then let the Vet perform a health check."""
        vet = self._select_staff_member(Vet, "Vet")
        if vet is None:
            return

        animal = self._select_animal()
        if animal is None:
            return

        vet.health_check(animal)

    def move_animal(self):
        """
        Lets the user move an animal from its current enclosure
        to another suitable enclosure, so long as the animal is
        not undergoing treatment.
        """
        if not self.animals:
            print("There are no animals in the zoo yet.")
            return

        # Select the animal to move
        animal = self._select_animal()
        if animal is None:
            return

        # Check if the animal is undergoing treatment
        if getattr(animal, "undergoing_treatment", False):
            print(f"{animal.name} is currently undergoing treatment and cannot be moved.")
            return

        # Find the current enclosure
        current_enclosure = self._find_enclosure_for_animal(animal)
        if current_enclosure is None:
            print(f"{animal.name} is not currently assigned to any enclosure.")
            return

        # Work out what type of enclosure this animal needs
        required_type = self.get_required_enclosure(animal)
        if required_type is None:
            print("No enclosure rule defined for this type of animal.")
            return

        # Find all valid enclosures of the right type, excluding the current one
        valid_enclosures = [
            enclosure for enclosure in self.enclosures
            if isinstance(enclosure, required_type) and enclosure is not current_enclosure
        ]

        if not valid_enclosures:
            print(f"There are no other {required_type.__name__} enclosures to move {animal.name} into.")
            return

        # Pick a new enclosure from the valid ones
        print(f"\nCurrent enclosure for {animal.name}: {current_enclosure.name}")
        print(f"Select a new enclosure for {animal.name}:")
        for index, enclosure in enumerate(valid_enclosures, start=1):
            print(
                f"{index}. {enclosure.name} "
                f"(Cleanliness level: {enclosure.cleanliness})"
            )

        idx = self._select_index(valid_enclosures, "Enter the number of the new enclosure: ")
        if idx is None:
            return

        new_enclosure = valid_enclosures[idx]

        # Perform the move
        if animal in current_enclosure.animals:
            current_enclosure.animals.remove(animal)
        new_enclosure.animals.append(animal)

        print(f"{animal.name} has been moved from {current_enclosure.name} to {new_enclosure.name}.")

    def assign_staff_to_animal(self):
        """Assign a Zoo Keeper or Vet to an animal."""
        # Pick staff
        staff_member = self._select_staff_member(
            self.animal_staff_types, "staff member (Zoo Keeper or Vet)"
        )
        if staff_member is None:
            return

        # Pick the animal
        animal = self._select_animal()
        if animal is None:
            return

        # Link them up
        if animal not in staff_member.animals:
            staff_member.animals.append(animal)

        print(f"{staff_member.name} is now assigned to {animal.name}.")

    def assign_staff_to_enclosure(self):
        """Assign a Zoo Keeper or Cleaner to an enclosure."""
        staff_member = self._select_staff_member(
            self.enclosure_staff_types, "staff member (Zoo Keeper or Cleaner)"
        )
        if staff_member is None:
            return

        enclosure = self._select_enclosure()
        if enclosure is None:
            return

        if enclosure not in staff_member.enclosures:
            staff_member.enclosures.append(enclosure)

        print(f"{staff_member.name} is now responsible for enclosure {enclosure.name}.")

    def modify(self, choice: str, item: str):
        """Modify the Zoo Management System by adding or removing animals, enclosures, or staff."""
        item = item.lower()
        choice = choice.lower()

        if not self.validate_choice(choice):
            return

        if not self.validate_item(item):
            return

        target_list = self.get_target_list(item)

        if choice == "add":
            self._handle_add(item, target_list)
        else:
            self._handle_remove(item, target_list)
