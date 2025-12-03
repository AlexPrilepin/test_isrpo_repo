import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),  "..", "src"))

from src.square import area, perimeter

class TestSquareFunctions(unittest.TestCase):
    
    def test_area_positive(self):
        self.assertEqual(area(2), 4)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_negative(self):
      with self.assertRaises(ValueError):
        area(-1);
        area(-10);
        area(-1000);

    def test_area_type(self):
      with self.assertRaises(TypeError):
        area("str")
        area(False)
        area(None)
    
    def test_area_return_type(self):
      self.assertIsInstance(area(1), (int, float))
      self.assertIsInstance(area(2), (int, float))
      self.assertIsInstance(area(10), (int, float))

    def test_area_large_number(self):
       self.assertEqual(area(999999999999999), 999999999999999 ** 2)

    def test_area_small_number(self):
       self.assertEqual(area(1e-7), 1e-7 * 1e-7)
    
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(2), 8)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
      with self.assertRaises(ValueError):
        perimeter(-1);
        perimeter(-10);
        perimeter(-1000);

    def test_perimeter_type(self):
      with self.assertRaises(TypeError):
        perimeter("str")
        perimeter(False)
        perimeter(None)

    def test_perimeter_return_type(self):
      self.assertIsInstance(perimeter(1), (int, float))
      self.assertIsInstance(perimeter(2), (int, float))
      self.assertIsInstance(perimeter(10), (int, float))

    def test_perimeter_large_number(self):
       self.assertEqual(perimeter(999999999999999), 999999999999999 * 4)

    def test_perimeter_small_number(self):
       self.assertEqual(perimeter(1e-7), 1e-7 * 4)
    

if __name__ == '__main__':
    unittest.main()