class quadratic:
    
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c

 def value(self, x):
      return self.a*x**2 + self.b*x + self.c

   def __call__(self, x):
      return self.a*x**2 + self.b*x + self.c  

   def table(self, L, R, n):
      import numpy as np
      a, b, c = self.a, self.b, self.c
      x = np.linspace(L, R, n)
      y = np.zeros(len(x))
      for i in xrange(len(x)):
         y[i] = a*x**2 + b*x + c
      for xi, yi in zip(x, y):
         return xi, yi
   
        
   def roots(self):
      from numpy.lib.scimath import sqrt
      x1 = (-self.b + sqrt(self.b**2 - 4*self.a*self.c))/float(2*self.a)
      x2 = (-self.b - sqrt(self.b**2 - 4*self.a*self.c))/float(2*self.a)
      return x1, x2
