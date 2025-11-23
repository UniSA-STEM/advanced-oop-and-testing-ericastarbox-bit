"""
File: main.py
Description: A text-based user interface for the Zoo Management System. Allows the player to create and
manage animals, enclosures, and staff.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from zoo_management_system import ZooManagementSystem


# ===============================
#     UTILITY FORMATTING
# ===============================

def print_header(title: str):
    """Print a formatted section header."""
    print("\n" + "=" * 45)
    print(f"{title.center(45)}")
    print("=" * 45 + "\n")


def wait():
    """Pause after an action to improve readability."""
    input("\nPress Enter to continue... ")


# ===============================
#     MENU PRINT FUNCTIONS
# ===============================

def print_main_menu():
    """Print the main menu options for the zoo interface."""
    print_header("Main Menu")
    print("What would you like to do next?")
    print("1. Enclosure management")
    print("2. Animal management")
    print("3. Staff management")
    print("4. Reports")
    print("0. Exit\n")


def print_enclosure_menu():
    """Print the enclosure management menu."""
    print_header("Enclosure Management")
    print("1. Add enclosure")
    print("2. Remove enclosure")
    print("3. Clean an enclosure")
    print("4. Generate enclosure report")
    print("0. Back to main menu\n")


def print_animal_menu():
    """Print the animal management menu."""
    print_header("Animal Management")
    print("1. Add animal")
    print("2. Remove animal")
    print("3. Feed an animal")
    print("4. Record animal health issue")
    print("5. View animal health issues")
    print("6. Move an animal to a different enclosure")
    print("7. Generate animal report")
    print("0. Back to main menu\n")


def print_staff_menu():
    """Print the staff management menu."""
    print_header("Staff Management")
    print("1. Add staff")
    print("2. Remove staff")
    print("3. Assign staff to an animal")
    print("4. Assign staff to an enclosure")
    print("5. Generate staff report")
    print("0. Back to main menu\n")


def print_reports_menu():
    """Print the report menu."""
    print_header("Reports")
    print("1. Full zoo report")
    print("2. Daily routines")
    print("3. Animal-only report")
    print("4. Enclosure-only report")
    print("5. Staff-only report")
    print("0. Back to main menu\n")


# ===============================
#     MENU HANDLER FUNCTIONS
# ===============================

def handle_enclosure_menu(zoo: ZooManagementSystem):
    """Handle all enclosure-related actions."""
    while True:
        print_enclosure_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            zoo.modify("add", "enclosure")
        elif choice == "2":
            zoo.modify("remove", "enclosure")
        elif choice == "3":
            zoo.clean_enclosure()
        elif choice == "4":
            zoo.generate_enclosure_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


def handle_animal_menu(zoo: ZooManagementSystem):
    """Handle all animal-related actions."""
    while True:
        print_animal_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            zoo.modify("add", "animal")
        elif choice == "2":
            zoo.modify("remove", "animal")
        elif choice == "3":
            zoo.feed_animals()
        elif choice == "4":
            zoo.record_animal_health()
        elif choice == "5":
            zoo.view_animal_health()
        elif choice == "6":
            zoo.move_animal()
        elif choice == "7":
            zoo.generate_animal_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


def handle_staff_menu(zoo: ZooManagementSystem):
    """Handle all staff-related actions."""
    while True:
        print_staff_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            zoo.modify("add", "staff")
        elif choice == "2":
            zoo.modify("remove", "staff")
        elif choice == "3":
            zoo.assign_staff_to_animal()
        elif choice == "4":
            zoo.assign_staff_to_enclosure()
        elif choice == "5":
            zoo.generate_staff_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


def handle_reports_menu(zoo: ZooManagementSystem):
    """Handles report-related actions."""
    while True:
        print_reports_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            zoo.generate_report()
        elif choice == "2":
            zoo.schedule_daily_routines()
        elif choice == "3":
            zoo.generate_animal_report()
        elif choice == "4":
            zoo.generate_enclosure_report()
        elif choice == "5":
            zoo.generate_staff_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


# ===============================
#     ENTRY POINT FUNCTION
# ===============================

def start_zoo():
    """Create a ZooManagementSystem and run the text-based interface."""
    print_header("Welcome to the Zoo Management System")
    zoo_name = input("Enter a name for your zoo: ").strip() or "Unnamed Zoo"
    zoo = ZooManagementSystem(zoo_name)

    print(f"\nYou’ve just started a zoo called {zoo.name}!")
    wait()

    while True:
        print_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            handle_enclosure_menu(zoo)
        elif choice == "2":
            handle_animal_menu(zoo)
        elif choice == "3":
            handle_staff_menu(zoo)
        elif choice == "4":
            handle_reports_menu(zoo)
        elif choice == "0":
            print("Exiting the zoo management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")
            wait()

if __name__ == "__main__":
    start_zoo()
