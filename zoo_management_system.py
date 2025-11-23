"""
File: zoo_management_system.py
Description: A Zoo Management System class that manages animals, enclosures, and staff.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from bird import Bird
from crocodile import Crocodile
from elephant import Elephant
from terrarium import Terrarium
from terrestrial import Terrestrial
from aviary import Aviary
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
    """A class representing a Zoo Management System."""

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================

    def __init__(self, name):
        self._name = name
        self._animals = []
        self._enclosures = []
        self._staff = []
        self._enclosure_rules = [
            (Mammal, Terrestrial),
            (Reptile, Terrarium),
            (Bird, Aviary)
        ]

        # Staff assignment rules
        self._animal_staff_types = (ZooKeeper, Vet)  # Can be assigned to ANIMALS
        self._enclosure_staff_types = (ZooKeeper, Cleaner)  # Can be assigned to ENCLOSURES

    # ===============================
    #    GETTER AND SETTER METHODS
    # ===============================

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, value):
        self._animals = value

    @property
    def enclosures(self):
        return self._enclosures

    @enclosures.setter
    def enclosures(self, value):
        self._enclosures = value

    @property
    def staff(self):
        return self._staff

    @staff.setter
    def staff(self, value):
        self._staff = value

    @property
    def enclosure_rules(self):
        return self._enclosure_rules

    @property
    def animal_staff_types(self):
        return self._animal_staff_types

    @property
    def enclosure_staff_types(self):
        return self._enclosure_staff_types

    # ===============================
    #   PUBLIC INTERFACE METHODS
    # ===============================

    def generate_report(self):
        """Generates a report of the Zoo Management System."""

        # Header and title formatting
        print("\n=========================================")
        print(f"         {self.name.upper()} MANAGEMENT REPORT")
        print("=========================================")
        print()

        # Generates and displays the animal, enclosure, and staff reports
        self.generate_animal_report()
        self.generate_enclosure_report()
        self.generate_staff_report()

        # Footer formatting
        print("End of Report")
        print("----------------------------------------")

    def generate_animal_report(self):
        """Generates an animal report."""

        # Header formatting
        print("\nANIMALS")

        # Shows the total number of animals in the zoo
        print(f"Total Animals: {len(self.animals)}")

        # Loop through each animal and print their details
        for animal in self.animals:
            print(
                f" - {animal.name}\n"
                f"     Species: {animal.__class__.__name__}\n"
                f"     Age: {animal.age}\n"
                f"     Undergoing treatment: {animal.treatment_status}\n"
                f"     On display: {animal.display_status}\n"
                f"     Enclosure: {animal.enclosure.name if animal.enclosure else 'None'}"
            )
        print()

    def generate_enclosure_report(self):
        """Generates an enclosure-only report."""

        # Header formatting
        print("\nENCLOSURES")

        # Shows the total number of enclosures in the zoo
        print(f"Total Enclosures: {len(self.enclosures)}")

        # Loop through each enclosure and print their details
        for enclosure in self.enclosures:

            # Lists animals in the enclosure
            if enclosure.animals:
                animals_str = ", ".join(
                    f"{animal.name} ({animal.__class__.__name__})"
                    for animal in enclosure.animals
                )
            else:
                animals_str = "None"

            # Print enclosure information
            print(
                f" - {enclosure.name}\n"
                f"     Size: {enclosure.size}m\u00b2\n"
                f"     Cleanliness: Level {enclosure.cleanliness}\n"
                f"     Animals: {animals_str}"
            )
        print()

    def generate_staff_report(self):
        """Generates a staff-only report."""

        # Header formatting
        print("\nSTAFF")

        # Shows the total number of staff members in the zoo
        print(f"Total Staff: {len(self.staff)}")

        # Loop through each staff member and print their details
        for staff in self.staff:
            # Create a list of animals and enclosures assigned to the staff member
            animal_names = ", ".join(a.name for a in staff.animals) if staff.animals else "None"
            enclosure_names = ", ".join(e.name for e in staff.enclosures) if staff.enclosures else "None"

            # Print details about the staff member
            print(
                f" - {staff.name}\n"
                f"     Job: {staff.job}\n"
                f"     Assigned Animals: {animal_names}\n"
                f"     Assigned Enclosures: {enclosure_names}\n"
            )
        print()

    def schedule_daily_routines(self):
        """
        Generates and prints a daily routine schedule for the zoo,
        including feeding times for animals and cleaning tasks for enclosures.
        """

        # Header formatting
        print("\n==========================================")
        print(f"        {self.name.upper()} DAILY ROUTINES")
        print("==========================================\n")

        # ---------- Feeding Schedule ----------
        print("FEEDING SCHEDULE")
        if not self.animals:
            print(" - No animals to feed.\n")
        else:
            for animal in self.animals:
                print(f" - Feed {animal.name} ({animal.__class__.__name__})")

        # ---------- Cleaning Schedule ----------
        print("\nCLEANING SCHEDULE")
        if not self.enclosures:
            print(" - No enclosures to clean.\n")
        else:
            for enclosure in self.enclosures:
                print(f" - Clean {enclosure.name} (Cleanliness level: {enclosure.cleanliness})")

        # Footer formatting
        print("\nEnd of Daily Routine Schedule")
        print("------------------------------------------\n")

    def modify(self, choice: str, item: str):
        """Modify the Zoo Management System by adding or removing animals, enclosures, or staff."""

        # Streamline user input
        item = item.lower()
        choice = choice.lower()

        # Validate user action input (must be "add" or "remove")
        if not self.validate_choice(choice):
            return

        # Validate item input (must be "animal", "enclosure", or "staff")
        if not self.validate_item(item):
            return

        # Determine the target-list based on item input
        target_list = self.get_target_list(item)

        # Depending on the user's choice, either add a new item or remove an existing item.
        if choice == "add":
            self._handle_add(item, target_list)
        else:
            self._handle_remove(item, target_list)

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

    def clean_enclosure(self):
        """ Selects a cleaner and an enclosure to clean, then cleans the enclosure."""

        # Ask the user to select a cleaner to do the cleaning.
        cleaner = self._select_staff_member(Cleaner, "Cleaner")
        if cleaner is None:
            return

        # Ask the user to select an enclosure to clean.
        enclosure = self._select_enclosure()
        if enclosure is None:
            return

        # Perform the cleaning.
        cleaner.clean_enclosure(enclosure)

    def view_animal_health(self):
        """Let the user select an animal and view its health records."""

        # Ask the user to select an animal to view its health records.
        animal = self._select_animal()
        if animal is None:
            return

        # Print the health records for the selected animal.
        print(
            f"\nHealth issues for {animal.name} "
            f"(Undergoing treatment: {'Yes' if animal.undergoing_treatment else 'No'}):"
        )

        # If the animal has no health records, display a message.
        if not getattr(animal, "health_records", []):
            print(" - No health records have been recorded for this animal.")
            return

        # Print each health record for the animal.
        for record in animal.health_records:
            print(f" - {record}")

    def record_animal_health(self):
        """Choose a Vet and an Animal, then let the Vet perform a health check."""

        # Ask the user to select a vet to perform the health check.
        vet = self._select_staff_member(Vet, "Vet")
        if vet is None:
            return

        # Ask the user to select an animal to perform the health check on.
        animal = self._select_animal()
        if animal is None:
            return

        # Perform the health check.
        vet.health_check(animal)

    def move_animal(self):
        """
        Lets the user move an animal from its current enclosure
        to another suitable enclosure, so long as the animal is
        not undergoing treatment.
        """

        # If there are no animals, there's nothing to move'
        if not self.animals:
            print("There are no animals in the zoo yet.")
            return

        # Select the animal to move
        animal = self._select_animal()
        if animal is None:
            return

        # Check rules to ensure the animal can be moved
        if not self._can_animal_be_moved(animal):
            return

        # Find the animal's current enclosure
        current_enclosure = self._find_enclosure_for_animal(animal)
        if current_enclosure is None:
            print(f"{animal.name} is not currently assigned to any enclosure.")
            return

        # Find all suitable enclosures for the animal
        valid_enclosures = self._get_valid_target_enclosures(animal, current_enclosure)
        if not valid_enclosures:
            return

        # Choose a new enclosure
        new_enclosure = self._choose_new_enclosure(animal, valid_enclosures)
        if new_enclosure is None:
            # Cancellation or invalid selection
            return

        # Make sure the animal is compatible with the enclosures existing animals
        if not self._is_compatible_with_existing_animals(animal, new_enclosure):
            return

        # Good to move. Perform the move.
        self._perform_animal_move(animal, current_enclosure, new_enclosure)

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

        # Ask the user to select a Zoo Keeper or Cleaner to do the cleaning.
        staff_member = self._select_staff_member(
            self.enclosure_staff_types, "staff member (Zoo Keeper or Cleaner)"
        )
        if staff_member is None:
            return

        # Ask the user to select an enclosure to clean.
        enclosure = self._select_enclosure()
        if enclosure is None:
            return

        # Assign the staff member to the enclosure if they are not already assigned.
        if enclosure not in staff_member.enclosures:
            staff_member.enclosures.append(enclosure)

        # Confirm the assignment.
        print(f"{staff_member.name} is now responsible for enclosure {enclosure.name}.")

    # ===============================
    #       ZOO LOGIC METHODS
    # ===============================

    def _find_enclosure_for_animal(self, animal):
        """Returns the enclosure that contains the given animal, or None if not found."""

        # Loop through all enclosures in the zoo
        for enclosure in self.enclosures:

            # Check if the animal is in the enclosure
            if animal in enclosure.animals:
                return enclosure  # Found it!

        # If no enclosure contains the animal, return None
        return None

    def get_required_enclosure(self, animal):
        """Returns the enclosure class required for a given animal type."""

        # Loop through all enclosure rules
        for animal_type, enclosure_type in self.enclosure_rules:

            # Check if the animal matches the rule
            if isinstance(animal, animal_type):
                return enclosure_type

        # If no rule matched
        return None

    def is_valid_enclosure(self, animal, enclosure):
        """Returns True if the enclosure is appropriate for the animal."""

        # Determine the required enclosure type
        required = self.get_required_enclosure(animal)

        # If there is no rule for this animal type, return False
        if required is None:
            print("No enclosure rule defined for this type of animal.")
            return False

        # Check if the enclosure is of the correct type
        return isinstance(enclosure, required)

    def assign_animal(self, animal, enclosure):
        """Assigns an animal to an enclosure if the enclosure type is valid."""

        # First, check that the enclosure type is valid for the animal
        if not self.is_valid_enclosure(animal, enclosure):
            print("Invalid assignment: enclosure type does not match the animal.")
            return False

        # Check compatibility with animals already in the enclosure
        for existing in enclosure.animals:
            if not self.animals_are_compatible(existing, animal):
                print(
                    f"Cannot assign {animal.name} ({animal.__class__.__name__}) "
                    f"to {enclosure.name}: incompatible with "
                    f"{existing.name} ({existing.__class__.__name__})."
                )
                return False  # Does not add.

        # At this point, the enclosure is valid and compatible with animal.
        enclosure.animals.append(animal)
        animal.enclosure = enclosure
        print(f"{animal.name} assigned to {enclosure.name}.")

        # Reduce cleanliness, ensuring it doesn't go below 0'
        new_level = max(0, enclosure.cleanliness - 1)
        enclosure.cleanliness = new_level
        f"{enclosure.name}'s cleanliness is now level {enclosure.cleanliness}."

        return True

    @staticmethod
    def animals_are_compatible(animal1, animal2):
        """
        Return True if two animals are allowed to share an enclosure.
        Rules:
        - Same species can always share.
        - Peacock and Swan can share (allowed mixed-species pairs).
        - All other combinations are incompatible.
        """

        # Same-species are always compatible
        if animal1.__class__ is animal2.__class__:
            return True

        # Allowed mixed-species pair: Peacock + Swan
        allowed_bird_combo = {"Peacock", "Swan"}
        pair = {animal1.__class__.__name__, animal2.__class__.__name__}
        if pair == allowed_bird_combo:
            return True

        # Everything else is incompatible
        return False

    # ===============================
    #    ADD/REMOVE LOGIC METHODS
    # ===============================

    def _add_animal(self, target_list: list):
        """Handles the full workflow for adding a new animal to the zoo."""

        # Require at least one enclosure before adding animals
        if not self.enclosures:
            print("You must add at least one enclosure before adding animals.\n")
            return

        # Let the user choose the type of animal to create
        cls = self.get_item_class("animal")
        if cls is None:
            return

        # Create the animal (validated name + age)
        animal = self.create_object("animal", cls)

        # Let the user choose a suitable enclosure based on the animal type
        enclosure = self._select_enclosure_for_animal(animal)
        if enclosure is None:
            print(
                f"{animal.name} was not added because no suitable enclosure "
                "was selected or available.\n"
            )
            return

        # Attempt assignment using your existing logic
        if self.assign_animal(animal, enclosure):
            self.add_item(animal, target_list, "animal")
        else:
            print(
                f"{animal.name} was not added to the zoo because no compatible "
                f"enclosure is available.\n"
            )

    def _add_enclosure(self, target_list: list):
        """Handles adding a new enclosure."""

        # Ask the user to choose the type of enclosure to create
        cls = self.get_item_class("enclosure")
        if cls is None:
            return

        # Create the enclosure object
        enclosure = self.create_object("enclosure", cls)

        # Add the newly created enclosure to the target list
        self.add_item(enclosure, target_list, "enclosure")

    def _add_staff(self, target_list: list):
        """Handles adding a new staff member."""

        # Gives the user the option to choose a specific type of staff member
        cls = self.get_item_class("staff")
        if cls is None:
            return

        # Creates the staff member object
        staff_member = self.create_object("staff", cls)

        # Add the newly created staff member to the target list
        self.add_item(staff_member, target_list, "staff")

    def _handle_add(self, item: str, target_list: list):
        """Handles adding animals, enclosures, or staff."""

        # Special handling for animals – enforce enclosure assignment
        if item == "animal":
            self._add_animal(target_list)

        # Add a new enclosure to the zoo.
        elif item == "enclosure":
            self._add_enclosure(target_list)

        # Add a new staff member to the zoo.
        elif item == "staff":
            self._add_staff(target_list)

    def _handle_remove(self, item: str, target_list: list):
        """Handles removal of animals, enclosures, or staff."""

        # If the list is empty, there is nothing to remove.
        if not target_list:
            print(f"No {item}s to remove.\n")
            return

        # Display a list of the items to remove.
        print(f"Select a {item} to remove: ")
        for i, obj in enumerate(target_list, start=1):
            print(f"{i}. {obj.name} ({obj.__class__.__name__})")

        # Ask the user to select an item to remove.
        idx = self._select_index(target_list, "Enter number: ")
        if idx is None:
            return

        # Retrieve the selected item from the list.
        obj = target_list[idx]

        # Remove the selected object from the target list.
        self.remove_item(obj, target_list, item)

    def create_object(self, item, cls):
        """Creates an object using validated name input (and age for animals)."""

        # Ask the user to enter a name for the new item.
        name = ZooManagementSystem.get_valid_name(
            prompt=f"\nWhat is the name of the {item}? "
        )

        # Animals require both a name and age, so collect age separately.
        if item == "animal":
            age = self.get_valid_age()
            return cls(name, age)

        # For enclosures and staff, only the name is required.
        return cls(name)

    def add_item(self, obj, target_list, item):
        """Adds an item to the target list."""
        target_list.append(obj)
        print(f"Added {obj.__class__.__name__} named {obj.name} to {self.name}'s {item} list.")

    def remove_item(self, obj, target_list, item):
        """Removes an item from the target list."""
        if obj in target_list:
            target_list.remove(obj)
            print(f"Removed {obj.__class__.__name__} named {obj.name} from {self.name}'s {item} list.\n")
        else:
            print("Item not found.\n")

    def get_target_list(self, item):
        """Returns the target list for the given item (animals, enclosures, or staff)."""
        return {
            "animal": self.animals,
            "enclosure": self.enclosures,
            "staff": self.staff
        }[item]

    # ===============================
    #        MOVEMENT LOGIC
    # ===============================

    @staticmethod
    def _can_animal_be_moved(animal):
        """
        Checks if an animal can be moved, based on its current state.
        Animals undergoing treatment cannot be moved.
        """

        if getattr(animal, "undergoing_treatment", False):
            print(f"{animal.name} is currently undergoing treatment and cannot be moved.")
            return False
        return True

    def _get_valid_target_enclosures(self, animal, current_enclosure):
        """
        Returns a list of enclosures that are suitable for the given animal.
        Filters by the required enclosure type and excludes the current enclosure.
        """

        # Find all enclosures that this animal can live in.
        required_type = self.get_required_enclosure(animal)

        # If there is no rule for this animal type, return an empty list
        if required_type is None:
            print("No enclosure rule defined for this type of animal.")
            return []

        # Find all enclosures that match the required type, excluding the current one
        valid_enclosures = [
            enclosure for enclosure in self.enclosures
            if isinstance(enclosure, required_type) and enclosure is not current_enclosure
        ]

        # If no alternative enclosures are available, let the user know.
        if not valid_enclosures:
            print(f"There are no other {required_type.__name__} enclosures available.")

        # Returns the list of suitable enclosures
        return valid_enclosures

    def _choose_new_enclosure(self, animal, valid_enclosures):
        """Gives the user a choice of suitable enclosures for the animal."""

        # Display all suitable enclosures for this animal.
        print(f"\nSelect a new enclosure for {animal.name}:")
        for index, enclosure in enumerate(valid_enclosures, start=1):
            print(f"{index}. {enclosure.name} (Cleanliness level: {enclosure.cleanliness})")

        # Ask the user to select a suitable enclosure.
        idx = self._select_index(valid_enclosures, "Enter the number of the new enclosure: ")
        if idx is None:
            return None

        # Return the selected enclosure.
        return valid_enclosures[idx]

    def _is_compatible_with_existing_animals(self, animal, new_enclosure):
        """Return True if compatible, otherwise print a message and return False."""

        # Check the new enclosure's compatibility with existing animals
        for existing in new_enclosure.animals:

            # If the existing animal is incompatible with the one being moved, reject the move.
            if not self.animals_are_compatible(existing, animal):
                print(
                    f"Cannot move {animal.name} ({animal.__class__.__name__}) to "
                    f"{new_enclosure.name}: incompatible with "
                    f"{existing.name} ({existing.__class__.__name__})."
                )
                return False

        # If no incompatibility was found, return True to allow the move.
        return True

    @staticmethod
    def _perform_animal_move(animal, old_enclosure, new_enclosure):
        """Moves the selected animal between enclosures and update tracking."""

        # Remove the animal from the old enclosure and add it to the new one.
        if animal in old_enclosure.animals:
            old_enclosure.animals.remove(animal)

        # Add the animal to the new enclosure.
        new_enclosure.animals.append(animal)

        # Update the animal's enclosure reference to its new enclosure
        animal.enclosure = new_enclosure
        print(f"{animal.name} has been moved from {old_enclosure.name} to {new_enclosure.name}.")

    # ===============================
    #  VALIDATION AND STATIC METHODS
    # ===============================

    @staticmethod
    def validate_choice(choice):
        """
        Validate the user's choice when calling the 'modify' method.
        Only 'add' and 'remove' are valid choices.
        """

        if choice.lower() not in ["add", "remove"]:
            print("Invalid choice. Must be 'add' or 'remove'.")
            return False
        return True

    @staticmethod
    def validate_item(item):
        """
        Validate the item when calling the 'modify' method.
        Only 'animal', 'enclosure', and 'staff' are valid items.
        """

        if item.lower() not in ["animal", "enclosure", "staff"]:
            print("Invalid item. Must be 'animal', 'enclosure', or 'staff'.")
            return False
        return True

    @staticmethod
    def get_valid_age():
        """
        Prompts the user to enter an animal's age and validates the input.
        Continues prompting until a non-negative whole number is entered,
        then returns the age as an integer.
        """

        while True:
            age_input = input("Enter age: ")

            try:
                # Convert the input to an integer
                age = int(age_input)

                # Age must be zero or greater.
                if age >= 0:
                    return age
                else:
                    print("Age must be zero or positive.")

            except ValueError:
                # Triggered when the input cannot be converted to an integer.
                print("Invalid age. Please enter a whole number.")

    @staticmethod
    def get_item_class(item):
        """Returns the class of an item based on user input."""
        try:
            # Map user-friendly keywords to actual classes
            item_matrix = {
                "animal": {
                    "lion": Lion, "crocodile": Crocodile, "elephant": Elephant,
                    "peacock": Peacock, "snake": Snake, "swan": Swan
                },
                "enclosure": {
                    "terrestrial": Terrestrial, "terrarium": Terrarium, "aviary": Aviary
                },
                "staff": {
                    "vet": Vet, "zoo keeper": ZooKeeper, "cleaner": Cleaner
                }
            }

            # Extract valid options for the given item
            options = list(item_matrix[item].keys())

            print(f"\nChoose {item} type:")
            for i, key in enumerate(options, start=1):
                print(f"{i}. {key.title()}")

            # Get the user's choice (either a number or a word).
            choice = input("Enter your choice: ").strip().lower()

            # User enters a number, convert it to an index
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    return item_matrix[item][options[idx]]
                else:
                    print("That number doesn’t match any of the options..")
                    return None

            # If the text matches one of the options, return the corresponding class.
            if choice in options:
                return item_matrix[item][choice]

            # If the user's input doesn't match anything.
            print("Invalid selection.")
            return None

        except KeyError:
            # If the user's input doesn't match anything.
            print("Looks like something went wrong with the item type. (Developer note: KeyError).")
            return None

    @staticmethod
    def get_valid_name(prompt="Enter name: "):
        """
        Gets a name from the user and ensures it is formatted correctly.
        Keeps prompting until a valid name is entered.
        """

        while True:
            # Convert the input to a string and strip leading and trailing whitespace
            name = input(prompt).strip().title()

            # Reject empty input
            if not name:
                print("Please enter a name (it can't be blank).")
                continue

            # Reject numeric-only names
            if name.replace(" ", "").isnumeric():
                print("A name can't be made up of just numbers. Try again.")
                continue

            # Reject names with weird characters (allow letters, spaces, hyphens)
            allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -")
            if not set(name).issubset(allowed):
                print("Names can only contain letters, spaces, and hyphens.")
                continue

            return name

    # ===============================
    #     SELECTION/MENU METHODS
    # ===============================

    @staticmethod
    def _select_index(items, prompt: str) -> int | None:
        """
        Generic helper to let the user select an item by index.
        Returns the selected index or None if selection fails.
        """

        # No items available
        if not items:
            print("There are no items to select from.")
            return None

        # Get user input and validate it
        choice_str = input(prompt).strip()

        # Ensure the input is an integer
        if not choice_str.isdigit():
            print("Invalid selection. Please enter a valid number.")
            return None

        idx = int(choice_str) - 1  # Convert to 0-based index

        # Ensure the index is within range
        if not (0 <= idx < len(items)):
            print("Invalid selection. Number out of range.")
            return None

        return idx

    def _select_staff_member(self, staff_class, role_name: str):
        """
        Returns a staff member of the given type selected by the user,
        or None if no staff of that type exist or selection fails.
        """

        # Filter staff to only include members of the required class.
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
        """Returns an Enclosure instance selected by the user, or None if selection fails."""

        # Ensure there are enclosures to select from.
        if not self.enclosures:
            print("There are no enclosures to clean.")
            return None

        # Display all available enclosures with cleanliness information.
        print("Available enclosures:")
        for index, enclosure in enumerate(self.enclosures, start=1):
            print(f"{index}. {enclosure.name.capitalize()} (Cleanliness level: {enclosure.cleanliness})")

        # Ask the user to select an enclosure and return the selected enclosure.
        idx = self._select_index(self.enclosures, "Enter the number of the enclosure to select: ")
        if idx is None:
            return None
        return self.enclosures[idx]

    def _select_enclosure_for_animal(self, animal):
        """Returns an enclosure of the correct type for the given animal"""

        # Determine what type of enclosure is required for the animal
        required_type = self.get_required_enclosure(animal)
        if required_type is None:
            print("No enclosure rule defined for this type of animal.")
            return None

        # Filter enclosures to only those of the required type
        valid_enclosures = [
            enclosure for enclosure in self.enclosures
            if isinstance(enclosure, required_type)
        ]

        # If no suitable enclosure is available, return None
        if not valid_enclosures:
            print(f"No {required_type.__name__} enclosures available for this animal.")
            return None

        # Display the list of valid enclosures for the user to choose from.
        print(f"\nSelect an enclosure for {animal.name}:")
        for index, enclosure in enumerate(valid_enclosures, start=1):
            print(
                f"{index}. {enclosure.name} "
                f"(Cleanliness level: {enclosure.cleanliness})"
            )

        # Let the user select an enclosure and return it.
        idx = self._select_index(valid_enclosures, "Enter the number of the enclosure: ")
        if idx is None:
            return None
        return valid_enclosures[idx]

    def _select_animal(self):
        """Returns an Animal selected by the user, or None if selection fails."""

        # Ensure there are animals to select from. If not, return None.
        if not self.animals:
            print("There are no animals available.")
            return None

        # Display all available animals with age information.
        print("Available animals:")
        for index, animal in enumerate(self.animals, start=1):
            print(f"{index}. {animal.name} ({animal.__class__.__name__}, age {animal.age})")

        # Ask the user to select an animal and return the selected animal.
        idx = self._select_index(self.animals, "Enter the number of the animal: ")
        if idx is None:
            return None

        return self.animals[idx]
