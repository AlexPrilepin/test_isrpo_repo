import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),  "..", "src"))

from src.triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):
    
    def test_area_positive(self):
        self.assertEqual(area(6, 4), 12)

    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(0, 2), 0)
        self.assertEqual(area(2, 0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(1, -10)
            area(-10, -50)
            area(-10, 1)

    def test_area_type(self):
        with self.assertRaises(TypeError):
            area("str", 5)
            area(10, "str")
            area(False, 1)
            area(10, None)
    
    def test_area_return_type(self):
        self.assertIsInstance(area(1, 1), (int, float))
        self.assertIsInstance(area(2, 3), (int, float))
        self.assertIsInstance(area(10, 5), (int, float))

    def test_area_large_number(self):
        self.assertEqual(area(999999999999999, 999999999999999), 999999999999999 * 999999999999999 / 2)

    def test_area_small_number(self):
        self.assertEqual(area(1e-7, 1e-7), 1e-7 * 1e-7 / 2)
    
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(0, 2, 2), 4)
        self.assertEqual(perimeter(2, 0, 2), 4)
        self.assertEqual(perimeter(2, 2, 0), 4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-10, 1, 1)
            perimeter(1, -10, 1)
            perimeter(1, 1, -10)
            perimeter(-10, -1, -1)

    def test_perimeter_type(self):
        with self.assertRaises(TypeError):
            perimeter("str", 5, 5)
            perimeter(1, "str", 5)
            perimeter(1, 5, "str")
            perimeter(1, None, 5)
            perimeter(False, "str", 5)
            perimeter(True, True, "str")

    def test_perimeter_return_type(self):
        self.assertIsInstance(perimeter(1, 1, 1), (int, float))
        self.assertIsInstance(perimeter(2, 3, 4), (int, float))
        self.assertIsInstance(perimeter(10, 5, 8), (int, float))

    def test_perimeter_large_number(self):
        self.assertEqual(perimeter(999999999999999, 999999999999999, 999999999999999), 999999999999999 * 3)

    def test_perimeter_small_number(self):
        self.assertEqual(perimeter(1e-7, 1e-7, 1e-7), 1e-7 * 3)
    

if __name__ == '__main__':
    unittest.main()