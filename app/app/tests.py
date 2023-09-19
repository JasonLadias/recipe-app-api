"""
Sample Tests
"""
from django.test import SimpleTestCase
from app import calc


class TestCalc(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add_numbers(self):
        """
        Test that two numbers are added together
        """
        self.assertEqual(calc.add(3, 8), 11)
        self.assertEqual(calc.add(-3, 8), 5)
        self.assertEqual(calc.add(-3, -8), -11)

    def test_modulo(self):
        """
        Test the modulo of two numbers
        """
        self.assertEqual(calc.modulo(3, 8), 3)
        self.assertEqual(calc.modulo(-3, 8), 5)
        self.assertEqual(calc.modulo(-3, -8), -3)
        self.assertEqual(calc.modulo(3, -8), -5)
        self.assertEqual(calc.modulo(3, 0), 3)
