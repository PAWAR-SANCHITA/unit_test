import sys
import os

# Add the parent directory (unit_testing) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import unittest
from app.helpers import subtract

class TestHelpers(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-3, 1), -4)
        self.assertEqual(subtract(2, -1), 3)
        self.assertEqual(subtract(-5, -5), 0)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
