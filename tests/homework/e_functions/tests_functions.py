import unittest

from src.homework.e_functions.value_return import get_hours, get_minutes, get_seconds

class Test_Config(unittest.TestCase):
    def test_get_hours_1(self):
        self.assertEqual(1, get_hours(3800))
    def test_get_hours_2(self):
        self.assertEqual(1, get_hours(3800))
    def test_get_minutes_1(self):
        self.assertEqual(3, get_minutes(3800))
    def test_get_minutes_2(self):
        self.assertEqual(0, get_minutes(3600))
    def test_get_seconds_1(self):
        self.assertEqual(20, get_seconds(3800))
    def test_get_seconds_2(self):
        self.assertEqual(0, get_seconds(3600))
