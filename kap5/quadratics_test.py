class quadratic:
    
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   
        
   def roots(self):
      from numpy.lib.scimath import *
      x1 = (-self.b + sqrt(self.b**2 - 4*self.a*self.c))/float(2*self.a)
      x2 = (-self.b - sqrt(self.b**2 - 4*self.a*self.c))/float(2*self.a)
      return x1, x2

  
      


   
