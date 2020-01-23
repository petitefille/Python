class Quadratic:
    
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

"""
Terminal> python
Python 2.7.2 (default, Oct 19 2013, 12:29:08)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from Quadratic import Quadratic
>>> f = Quadratic(-5, 1, 10)
>>> print f.value(2)
-8
>>> f.table(-5, 5, 10)
  x        f(x)
-5.00     -120.00
-3.89     -69.51
-2.78     -31.36
-1.67     -5.56
-0.56      7.90
 0.56      9.01
 1.67     -2.22   
 2.78     -25.80
 3.89     -61.73
 5.00     -110.00
>>> f.roots()
(-1.3177446878757826, 1.5177446878757825)
"""
