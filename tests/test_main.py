import sys
import os

# using pytest testing i set path for main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))


import unittest
from app.main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-3, -5), -8)
        self.assertEqual(add(1, -4), -3)
        self.assertEqual(add(-4, 5), 1)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()

