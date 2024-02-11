import unittest

from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):
    
    # Test the get_options_ratio using 5 and 20
    def test_get_options_ratio_1(self):
        self.assertEqual(0.25, get_options_ratio(5,20))

    # Test the get_options_ratio using 10 and 20
    def test_get_options_ratio_2(self):
        self.assertEqual(0.5, get_options_ratio(10,20))

    # Test the get_faculty_rating for 'Excellent'
    def test_get_faculty_rating_1(self):
        self.assertEqual(get_faculty_rating(0.91), "Excellent")

    # Test the get_faculty_rating for 'Very Good'.
    def test_get_faculty_rating_2(self):
        self.assertEqual(get_faculty_rating(0.85), "Very Good")

    # Test the get_faculty_rating for 'Good'
    def test_get_faculty_rating_3(self):
        self.assertEqual(get_faculty_rating(0.71), "Good")
        
    # Test the get_faculty_rating for 'Needs Improvement'
    def test_get_faculty_rating_4(self):
        self.assertEqual(get_faculty_rating(0.66), "Needs Improvement")

    # Test the get_faculty_rating for 'Unacceptable'
    def test_get_faculty_rating_5(self):
        self.assertEqual(get_faculty_rating(0.45), "Unacceptable")