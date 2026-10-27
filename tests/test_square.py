import unittest

import square


class TestSquare(unittest.TestCase): 
    def test_area_float(self):
        self.assertAlmostEqual(square.area(4.2), 4.2 ** 2)

    def test_perimeter_float(self):
        self.assertAlmostEqual(square.perimeter(4.2), 4.2 * 4)

    def test_zero_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(0)

        with self.assertRaises(ValueError):
            square.perimeter(0)

    def test_negative_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(-1)

        with self.assertRaises(ValueError):
            square.perimeter(-1)

    def test_complex_value_raises(self):
        with self.assertRaises(ValueError):
            square.area(1 + 3j)

        with self.assertRaises(ValueError):
            square.perimeter(1 + 3j)

    def test_string_raises(self):
        with self.assertRaises(TypeError):
            square.area("4.2")

        with self.assertRaises(TypeError):
            square.perimeter("4.2")

    def test_bool_raises(self):
        with self.assertRaises(TypeError):
            square.area(False)

        with self.assertRaises(TypeError):
            square.perimeter(True)
