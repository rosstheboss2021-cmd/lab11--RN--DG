# https://github.com/rosstheboss2021-cmd/lab11--RN--DG
# Partner 1: Ross Noland
# Partner 2: Daniel Gomez

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    ######### Partner 2

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(3, 4), 7)
        self.assertEqual(calculator.add(5, 6), 11)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)
        self.assertEqual(calculator.subtract(11, 4), 7)
        self.assertEqual(calculator.subtract(10, 5), 5)

    ######### Partner 1

    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 8), 0)
        self.assertEqual(calculator.mul(-3, -4), 12)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(4, 20), 5)
        self.assertEqual(calculator.div(-2, 10), -5)
        self.assertAlmostEqual(calculator.div(3, 1), 1 / 3)

    ######### Partner 2

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    ######### Partner 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(2, -10)

        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    ######### Partner 2

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    ######### Partner 1

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(25), 5)
        self.assertAlmostEqual(calculator.square_root(16), 4)
        self.assertAlmostEqual(calculator.square_root(0), 0)
        self.assertAlmostEqual(
            calculator.square_root(2),
            1.4142135623730951
        )

        with self.assertRaises(ValueError):
            calculator.square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
