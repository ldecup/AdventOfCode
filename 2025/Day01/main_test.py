import unittest

from main import incrementPosition
from main import decrementPosition

class test_decrementPosition(unittest.TestCase):
    def test_decrement_no_pass_zero(self):
        self.assertEqual(decrementPosition(37, 15), (22, 0))
    def test_decrement_pass_zero(self):
        self.assertEqual(decrementPosition(30, 80), (50, 1))
    def test_decrement_land_on_zero(self):
        self.assertEqual(decrementPosition(62, 62), (0, 1))
    def test_decrement_start_from_zero(self):
        self.assertEqual(decrementPosition(0, 15), (85, 0))

class test_incrementPosition(unittest.TestCase):
    def test_increment_no_pass_zero(self):
        self.assertEqual(incrementPosition(20, 40), (60, 0))
    def test_increment_pass_zero(self):
        self.assertEqual(incrementPosition(30, 80), (10, 1))
    def test_increment_land_on_zero(self):
        self.assertEqual(incrementPosition(62, 38), (0, 1))
    def test_increment_start_from_zero(self):
        self.assertEqual(incrementPosition(0, 38), (38, 0))







if __name__ == '__main__':
    unittest.main()