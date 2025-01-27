import math
class Shape:
    def __init__(self):
      pass
    def area(self):
      raise NotImplementedError
   
class Rectangle(Shape):
    def __init__(self, length, width):
       super().__init__()
       self.length = length
       self.width = width

    def area(self):
       rectangle_area = self.length * self.width
       return rectangle_area
        
    
class Circle(Shape):
   def __init__(self, radius):
      super().__init__()
      self.radius = radius

   def area(self):
       circle_area = math.pi * self.radius ** 2
       return circle_area
       
      

         

      