"""
File: main.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from zoo_management_system import ZooManagementSystem


def print_menu():
    """Print the main menu options for the zoo interface."""
    print("\nWhat would you like to do next?\n")
    print("1. Add enclosure")
    print("2. Add animal")
    print("3. Add staff")
    print("4. Remove enclosure")
    print("5. Remove animal")
    print("6. Remove staff")
    print("7. Clean an enclosure")
    print("8. Feed an animal")
    print("9. View zoo report")
    print("10. View animal health issues")
    print("0. Exit\n")


def print_main_menu():
    """Print the main menu options for the zoo interface."""
    print("\nWhat would you like to do next?")
    print("1. Enclosure management")
    print("2. Animal management")
    print("3. Staff management")
    print("4. Reports")
    print("0. Exit\n")


def print_enclosure_menu():
    """Print the enclosure management menu."""
    print("\nEnclosure Management")
    print("1. Add enclosure")
    print("2. Remove enclosure")
    print("3. Clean an enclosure")
    print("0. Back to main menu\n")


def print_animal_menu():
    """Print the animal management menu."""
    print("\nAnimal Management")
    print("1. Add animal")
    print("2. Remove animal")
    print("3. Feed an animal")
    print("4. View animal health issues")
    print("0. Back to main menu\n")


def print_staff_menu():
    """Print the staff management menu."""
    print("\nStaff Management")
    print("1. Add staff")
    print("2. Remove staff")
    print("0. Back to main menu")


def print_reports_menu():
    """Print the reports menu."""
    print("\nReports")
    print("1. View zoo report")
    print("0. Back to main menu")


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
            zoo.view_animal_health()
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
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


def handle_reports_menu(zoo: ZooManagementSystem):
    """Handle report-related actions."""
    while True:
        print_reports_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            zoo.generate_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


def start_zoo():
    """Create a ZooManagementSystem and run the text-based interface."""
    print("\nWelcome to the Zoo Management System!")
    zoo_name = input("\nEnter a name for your zoo: ").strip() or "Unnamed Zoo"
    zoo = ZooManagementSystem(zoo_name)

    print(f"\nYou’ve just started a zoo called {zoo.name}!")

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


if __name__ == "__main__":
    start_zoo()
