import unittest
from zoo_management_system import ZooManagementSystem
from lion import Lion
from terrestrial import Terrestrial

class TestEnclosureMethods(unittest.TestCase):
    """Tests enclosure behaviour: assignment, cleaning."""

    def setUp(self):
        """Prepare a zoo instance and an enclosure before each test."""
        self.zoo = ZooManagementSystem("Test Zoo")
        self.terrestrial = Terrestrial("Savannah")
        self.zoo.enclosures = [self.terrestrial]

    def test_cleanliness_reduction(self):
        """Cleanliness should be reduced when an animal is moved into an enclosure."""
        lion = Lion("Leo", 3)
        original_level = self.terrestrial.cleanliness
        self.zoo.assign_animal(lion, self.terrestrial)

        self.assertEqual(self.terrestrial.cleanliness, original_level - 1)

    def test_move_animal_not_allowed_during_treatment(self):
        """Animals should not be moved into an enclosure during treatment."""
        lion = Lion("Leo", 3)
        lion.undergoing_treatment = True
        self.assertFalse(self.zoo._can_animal_be_moved(lion))

    def test_assign_animal(self):
        """
        Animals should be able to be assigned to an enclosure if it is
        a suitable location and the animal is not undergoing treatment.
        """

        lion = Lion("Leo", 3)
        lion.undergoing_treatment = False
        self.zoo.assign_animal(lion, self.terrestrial)
        self.assertIn(lion, self.terrestrial.animals)

if __name__ == "__main__":
    unittest.main()
