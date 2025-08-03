import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 15), 5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)
        
        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=1)
        self.assertAlmostEqual(self.calc.add(-1.5, 2.5), 1.0, places=1)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.7, 2.2), 3.5, places=1)
        self.assertAlmostEqual(self.calc.subtract(-1.5, 1.5), -3.0, places=1)
        
        # Test subtracting larger from smaller
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(3, 7), 21)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-5, -6), 30)
        self.assertEqual(self.calc.multiply(7, -2), -14)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(1, 15), 15)
        self.assertEqual(self.calc.multiply(25, 1), 25)
        
        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0, places=1)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 3), -4.5, places=1)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)
        
        # Test with floating point numbers
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=1)
        self.assertAlmostEqual(self.calc.divide(-9.6, 3.2), -3.0, places=1)
        
        # Test dividing by one
        self.assertEqual(self.calc.divide(25, 1), 25.0)
        self.assertEqual(self.calc.divide(-17, 1), -17.0)
        
        # Test dividing zero by a number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(3.5, 0))

    def test_edge_cases(self):
        """Test additional edge cases and boundary conditions."""
        # Test very large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        
        # Test very small numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=1)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=10)
        
        # Test operations that result in zero
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.multiply(0, 999), 0)

if __name__ == '__main__':
    # Run the tests when the script is executed directly
    unittest.main()
