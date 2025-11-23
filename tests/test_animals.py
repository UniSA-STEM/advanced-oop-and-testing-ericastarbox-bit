import unittest
from zoo_management_system import ZooManagementSystem
from lion import Lion
from crocodile import Crocodile
from peacock import Peacock
from swan import Swan
from terrestrial import Terrestrial
from terrarium import Terrarium
from aviary import Aviary


class TestAnimalLogic(unittest.TestCase):
    """Tests animal behaviour: assignment, compatibility, finding enclosure."""

    def setUp(self):
        """Prepare a zoo instance and common enclosures before each test."""
        self.zoo = ZooManagementSystem("Test Zoo")

        # Create common enclosures
        self.terrestrial = Terrestrial("Savannah")
        self.terrarium = Terrarium("Reptile House")
        self.aviary = Aviary("Bird Dome")

        self.zoo.enclosures = [
            self.terrestrial,
            self.terrarium,
            self.aviary
        ]

    def test_required_enclosure(self):
        """Animals should be assigned to the correct enclosure based on type."""
        lion = Lion("Leo", 3)
        crocodile = Crocodile("Snap", 5)
        peacock = Peacock("Pia", 2)

        self.assertEqual(self.zoo.get_required_enclosure(lion), Terrestrial)
        self.assertEqual(self.zoo.get_required_enclosure(crocodile), Terrarium)
        self.assertEqual(self.zoo.get_required_enclosure(peacock), Aviary)

    def test_animals_are_compatible_same_species(self):
        """Animals of the same species should be compatible."""
        lion1 = Lion("Leo", 3)
        lion2 = Lion("Simba", 4)
        self.assertTrue(self.zoo.animals_are_compatible(lion1, lion2))

    def test_animals_are_compatible_peacock_swan(self):
        """Swans and peacocks should be compatible."""
        peacock = Peacock("Pia", 2)
        swan = Swan("Snow", 3)
        self.assertTrue(self.zoo.animals_are_compatible(peacock, swan))

    def test_animals_are_not_compatible_lion_crocodile(self):
        """Animals of different species, outside of swans and peacocks, should not be compatible."""
        lion = Lion("Leo", 3)
        crocodile = Crocodile("Snap", 5)
        self.assertFalse(self.zoo.animals_are_compatible(lion, crocodile))

    def test_assign_animal_success(self):
        """Animals should be able to be assigned to valid enclosures."""
        lion = Lion("Leo", 3)
        success = self.zoo.assign_animal(lion, self.terrestrial)
        self.assertTrue(success)
        self.assertIn(lion, self.terrestrial.animals)

    def test_assign_invalid_enclosure(self):
        """Animals should not be able to be assigned to an invalid enclosure."""
        lion = Lion("Leo", 3)
        success = self.zoo.assign_animal(lion, self.terrarium)
        self.assertFalse(success)
        self.assertNotIn(lion, self.terrarium.animals)

    def test_find_enclosure(self):
        """Animals should be able to be found in the correct enclosure."""
        lion = Lion("Leo", 3)
        self.zoo.assign_animal(lion, self.terrestrial)
        found = self.zoo._find_enclosure_for_animal(lion)
        self.assertEqual(found, self.terrestrial)


if __name__ == "__main__":
    unittest.main()
