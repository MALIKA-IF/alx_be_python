import unittest
from Simple_calculator import SimpleCalculator

class TestOperation(unittest.TestCase):
    def test_add(self):
        result=SimpleCalculator.add(5,7)
        self.assertEqual(result,12)
       # self.assertEqual(subtract(5,7),12)
       # self.assertEqual(multiply(5,7),35)
       # self.assertEqual(divide(8,4),2)

#run
unittest.main()       

  
