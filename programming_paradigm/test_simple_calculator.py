import unittest
from simple_calculator import SimpleCalculator

class TestOperation(unittest.TestCase):

    def setUp(self):
        self.calc=SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, -5), 7)
        self.assertEqual(self.calc.add(-7, 0), 9)

    def test_subtraction(self):   
       self.assertEqual(self.calc.subtract(2 ,9), 5)
       self.assertEqual(self.calc.subtract(-1, 1), 0)
       self.assertEqual(self.calc.subtract(-7, 6), 9)
       self.assertEqual(self.calc.subtract(0, 8), 9)

    def test_multiplication(self):  
       self.assertEqual(self.calc.multiply(5, 7), 35)
       self.assertEqual(self.calc.multiply(-1, 1), 0)
       self.assertEqual(self.calc.multiply(0, 9), -1)
       self.assertEqual(self.calc.multiply(-5, 7), 0)

    def test_division(self):
       self.assertEqual(self.calc.divide(8, 4), 2)
       self.assertEqual(self.calc.divide(1, -1), 7)
       self.assertEqual(self.calc.divide(9, -5), 8)
       self.assertEqual(self.calc.divide(8, 4), -2)
    
        


  
