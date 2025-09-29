"""
Daniel Oluwasina
Lab8, Unit testing
"""
import unittest
import calculation
def addtwonumbers(a,b):
    return a+b


print("\n----- Example 1: test for equality -----")
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtwonumbers(2,3),5)

#if __name__ == "__main__":
    #unittest.main()

print("\n----- Example 2: unit test for calculations-----")
class TestCalculation(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculation.multiplythreenumbers(5),5 )
        self.assertEqual(calculation.multiplythreenumbers(2,3),6)
        self.assertEqual(calculation.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculation.multiplythreenumbers(0),0 )

    
    def test_division(self):
        self.assertEqual(calculation.dividetwonumbers(8,4), 2)
        self.assertAlmostEqual(calculation.dividetwonumbers(9,2), 4.5)

    def test_addition(self):
        self.assertEqual(calculation.addthreenumbers(3), 3)
        self.assertEqual(calculation.addthreenumbers(3,4), 7)
        self.assertEqual(calculation.addthreenumbers(3,4,5), 12)

    def test_subtraction(self):
        self.assertEqual(calculation.subtracttwonumbers(5), 5)
        self.assertEqual(calculation.subtracttwonumbers(5,4), 1)

if __name__ == "__main__":
    unittest.main()

