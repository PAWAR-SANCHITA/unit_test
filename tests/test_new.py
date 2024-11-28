import unittest
from  app.new import shopping_count
class shopping_count(unittest.TestCase):

    def shopping_items(self):
       self.assertEqual(shopping_count(["Dress", "handbag", "soap"]), 3)
       self.assertEqual(shopping_count(["cap", "umbrella"]), 2)
       self.assertEqual(shopping_count([]), 0)

