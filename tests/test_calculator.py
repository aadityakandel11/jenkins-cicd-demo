import unittest

from calculator import add, divide, modulo, multiply, power, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_by_zero_raises(self):
        with self.assertRaises(ValueError):
            modulo(5, 0)


if __name__ == "__main__":
    unittest.main()
