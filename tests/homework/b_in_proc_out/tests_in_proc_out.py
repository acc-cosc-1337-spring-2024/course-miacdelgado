import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.b_in_proc_out.output import get_number, multiply_numbers

class Test_Config(unittest.TestCase):
    self.assertEqual(2, get_number(2))

    def test_multiply_numbers_1(self):
        self.assertEqual(multiply_numbers(5, 5), 25)
    
    def test_multiply_numbers_2(self):
        self.assertEqual(multiply_numbers(10, 10), 100)
