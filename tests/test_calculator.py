import unittest
import sys
sys.path.append('..')

from src.calculator import calculator


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.calculator.add(1, 6), 7)

    def test_times(self):
        self.assertEqual(calculator.calculator.times(2, 8), 16)

if __name__ == "__main__":
    unittest.main()