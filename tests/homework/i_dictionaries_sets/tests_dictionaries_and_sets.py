import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, del_inventory

class Test_Config(unittest.TestCase):
    def test_add_inventory_1(self):
        self.assertEqual(add_inventory('Widget1', 10), {'Widget1':10})
    def test_add_inventory_2(self):
        self.assertEqual(add_inventory('Widget1', 25), {'Widget1':35})
    def test_add_inventory_3(self):
        self.assertEqual(add_inventory('Widget1', -10), {'Widget1':25})
    def test_del_inventory_1(self):
        self.assertEqual(del_inventory('Widget1'), {})
    def test_del_inventory_2(self):
        self.assertEqual(del_inventory('Widget2'), {})