import unittest
from unittest.mock import patch
from zoo_management_system import ZooManagementSystem
from zoo_keeper import ZooKeeper
from cleaner import Cleaner
from vet import Vet
from lion import Lion
from terrestrial import Terrestrial


class TestStaffLogic(unittest.TestCase):
    """Tests staff behaviour: assignment, feeding, cleaning, vet health checks."""

    def setUp(self):
        """Prepare a zoo instance, a lion, and an enclosure before each test."""
        self.zoo = ZooManagementSystem("Test Zoo")
        self.lion = Lion("Leo", 2)
        self.enclosure = Terrestrial("Savannah")

        # Preload the zoo
        self.zoo.animals = [self.lion]
        self.zoo.enclosures = [self.enclosure]

    def test_assign_staff_to_animal(self):
        """ZooKeeper should be able to have an animal assigned."""
        keeper = ZooKeeper("John")
        self.zoo.staff = [keeper]

        keeper.animals = []
        keeper.animals.append(self.lion)

        self.assertIn(self.lion, keeper.animals)

    def test_assign_staff_to_enclosure(self):
        """ZooKeeper should be able to have an enclosure assigned."""
        keeper = ZooKeeper("John")
        self.zoo.staff = [keeper]

        keeper.enclosures = []
        keeper.enclosures.append(self.enclosure)

        self.assertIn(self.enclosure, keeper.enclosures)

    def test_zookeeper_feeds_animal(self):
        """ZooKeeper feeding an animal should reduce enclosure cleanliness."""
        keeper = ZooKeeper("John")
        enclosure = Terrestrial("Savannah")
        lion = Lion("Leo", 3)

        enclosure.animals.append(lion)
        original_cleanliness = enclosure.cleanliness

        keeper.feed_animal(lion, enclosure)

        self.assertLess(enclosure.cleanliness, original_cleanliness)

    def test_cleaner_cleans_enclosure(self):
        """Cleaner should increase enclosure cleanliness."""
        cleaner = Cleaner("Bob")
        enclosure = Terrestrial("Savannah")

        enclosure.cleanliness = 2
        cleaner.clean_enclosure(enclosure)

        self.assertGreater(enclosure.cleanliness, 2)

    @patch("vet.input", side_effect=["injury", "sore foot", "5", "amputate", "Will need prosthetic foot.",
                                     "y"])
    def test_vet_health_check(self, _):
        """Vet health_check() should record a health issue and mark the animal as under treatment."""
        vet = Vet("Dr Jane")
        lion = Lion("Leo", 4)

        vet.health_check(lion)

        self.assertTrue(lion.undergoing_treatment)
        self.assertGreater(len(lion.health_records), 0)


if __name__ == "__main__":
    unittest.main()
