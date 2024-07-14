"""
Basic Program for unit testing in Python by writing tests for a provided SimpleCalculator
class that supports addition, subtraction, multiplication, and division operations.
"""

# import 'unittest' module and import 'SimpleCalculator'
import unittest
from simple_calculator import SimpleCalculator

# 'TestSimpleCalculator' class that inherits from unittest.TestCase
class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
# Set up the SimpleCalculator instance before each test.
        self.calc = SimpleCalculator()

    def test_addition(self):
# Test the addition method.
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(-5, -6), -11)
        self.assertEqual(self.calc.add(9, -11), -2)

    def test_subtraction(self):
# Test the subtraction method.
        self.assertEqual(self.calc.subtract(7, 9), -2)
        self.assertEqual(self.calc.subtract(-5, -7), 2)
        self.assertEqual(self.calc.subtract(-12, 1), -13)

    def test_multiplication(self):
# Test the multiplication method.
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        self.assertEqual(self.calc.multiply(5, -3), -15)

    def test_division(self):
# Test the division method.
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-15, -5), 3)
        self.assertEqual(self.calc.divide(20, -10), -2)


if __name__ == "__main__":
    unittest.main()
