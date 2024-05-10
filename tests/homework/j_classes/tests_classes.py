import unittest

from src.homework.j_classes.class_a import roll, get_rolled_value

class Test_Config(unittest.TestCase):
    def test_roll_1(self):
        self.assertEqual(roll(1), 1)
    def test_roll_2(self):
        self.assertEqual(roll(2), 2)
    def test_roll_3(self):
        self.assertEqual(roll(3), 3)
    def test_roll_4(self):
        self.assertEqual(roll(4), 4)
    def test_roll_5(self):
        self.assertEqual(roll(5), 5)
    def test_roll_6(self):
        self.assertEqual(roll(6), 6)