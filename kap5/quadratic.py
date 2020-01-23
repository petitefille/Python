class quadratic:
    
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c

   def value(self, x):
      return self.a*x**2 + self.b*x + self.c

   def table(self, L, R, n):
		import numpy as np
		x=np.linspace(L, R, n)
		f=self.value(x)
		print '  x      f(x)'
		for i, j in zip(x, f):
			print '%5.2f    %5.2f' %  (i, j)  
        
   def roots(self):
      from numpy.lib.scimath import sqrt
      x1 = (-self.b + sqrt(self.b**2 - 4*self.a*self.c))/float(2*self.a)
      x2 = (-self.b - sqrt(self.b**2 - 4*self.a*self.c))/float(2*self.a)
      return x1, x2
