import unittest
import SimpleCalculator 

class TestOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(5,7),12)
        self.assertEqual(SimpleCalculator.subtract(5,7),12)
        self.assertEqual(SimpleCalculator.multiply(5,7),35)
        self.assertEqual(SimpleCalculator.divide(8,4),2)

#run
unittest.main()       

  
