"""
File: demo.py
Description: A text-based, non-interactive demo script that automatically showcases the Zoo Management System's
functionality.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""

from core.zoo_management_system import ZooManagementSystem
from animals.crocodile import Crocodile
from enclosures.terrarium import Terrarium
from enclosures.terrestrial import Terrestrial
from enclosures.aviary import Aviary
from animals.lion import Lion
from animals.peacock import Peacock
from staff.vet import Vet
from staff.cleaner import Cleaner
from staff.zoo_keeper import ZooKeeper
from animals.swan import Swan


def print_header(title):
    print("\n" + "=" * 50)
    print(f"{title}")
    print("=" * 50 + "\n")


def main():
    """Run the demo script."""

    # ===========================================================
    #  1. CREATE A ZOO
    # ===========================================================

    print_header("CREATING ZOO")

    # Create a non-interactive ZooManagementSystem instance for the demo.
    zoo = ZooManagementSystem("Seinfeld Zoo")
    print(f"Zoo created: {zoo.name}")

    # ===========================================================
    #  2. CREATE ENCLOSURES
    # ===========================================================

    print_header("ADDING ENCLOSURES")

    # Create enclosures for the demo.
    monk_cafe = Terrestrial("Monk's Cafe Habitat")
    rochelle_reptile_house = Terrarium("Rochelle Reptile House")
    j_peterman_aviary = Aviary("J. Peterman Exotic Aviary")

    # Add the enclosures to the zoo.
    zoo.enclosures.extend([monk_cafe, rochelle_reptile_house, j_peterman_aviary])

    print("Added enclosures:")
    print(f" - {monk_cafe.name}")
    print(f" - {rochelle_reptile_house.name}")
    print(f" - {j_peterman_aviary.name}")

    # ===========================================================
    #  3. CREATE ANIMALS
    # ===========================================================

    print_header("ADDING ANIMALS")

    # Create animals for the demo.
    jerry = Lion("Jerry", 39)
    kramer = Crocodile("Kramer", 42)
    elaine = Peacock("Elaine", 38)
    newman = Swan("Newman", 41)

    # Add the animals to the zoo.
    zoo.animals.extend([jerry, kramer, elaine, newman])
    print("Created animals: Jerry, Kramer, Elaine, Newman")

    # Assign animals to appropriate enclosures.
    print("\nAssigning animals to enclosures...")
    zoo.assign_animal(jerry, monk_cafe)
    zoo.assign_animal(kramer, rochelle_reptile_house)
    zoo.assign_animal(elaine, j_peterman_aviary)
    zoo.assign_animal(newman, j_peterman_aviary)

    # ===========================================================
    #  4. ADD STAFF
    # ===========================================================

    print_header("ADDING STAFF")

    # Create staff members for the demo.
    george = ZooKeeper("George")
    frank = Cleaner("Frank Costanza")
    dr_sitwell = Vet("Dr. Sitwell")

    # Add staff members to the zoo.
    zoo.staff.extend([george, frank, dr_sitwell])

    print("Added staff: George (Keeper), Frank (Cleaner), Dr Sitwell (Vet)")

    # ===========================================================
    # 5. DEMONSTRATE STAFF ACTIONS
    # ===========================================================

    print_header("DEMONSTRATING STAFF ACTIONS")

    # Demonstrate a keeper feeding an animal.
    print("\nFeeding Jerry...")
    george.feed_animal(jerry, monk_cafe)

    # Demonstrate a cleaner cleaning an enclosure.
    print("\nCleaning Monk’s Cafe Habitat...")
    frank.clean_enclosure(monk_cafe)

    # Perform a demo health check on Newman using the non-interactive method.
    print("\nPerforming a health check on Newman...")
    dr_sitwell.demo_health_check(newman)

    # ===========================================================
    # 6. GENERATE REPORTS
    # ===========================================================

    # Show the zoo's reporting system.
    zoo.generate_report()

    print_header("ANIMAL REPORT")
    zoo.generate_animal_report()

    print_header("ENCLOSURE REPORT")
    zoo.generate_enclosure_report()

    print_header("STAFF REPORT")
    zoo.generate_staff_report()


if __name__ == "__main__":
    main()

