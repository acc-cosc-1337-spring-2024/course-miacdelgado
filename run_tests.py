import unittest

from src.homework.b_in_proc_out.output import get_number, multiply_numbers

class Test_Config(unittest.TestCase):

    def test_get_number_1(self):
        self.assertEqual(1, get_number(1))

    def test_get_number_2(self):
        self.assertEqual(2, get_number(2))

    def test_multiple_numbers_1(self):
        self.assertEqual(multiply_numbers(5,5), 25)

    def test_multiple_numbers_2(self):
        self.assertEqual(multiply_numbers(10,10), 100)
        