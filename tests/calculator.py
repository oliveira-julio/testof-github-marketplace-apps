import unittest
import sys
sys.path.append('..')

from src import calculator


class Test(unittest.TestCase):
    def test_add():
        self.assertEqual(calculator.calculator.add(1, 6), 7)

    def test_times():
        self.assertEqual(calculator.calculator.times(2, 8), 16)