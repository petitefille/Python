from numpy import *

def yes(self, a, b, c):
   return {'a': a, 'b': b, 'c': c}
   
def yes.value(self, x):
   return self['a']*x**2 + self['b']*x + self['c']


def yes.table(self, L, R, n):
   a, b, c = self['a'], self['b'], self['c']
   x = linspace(L, R, n)
   y = zeros(len(x))
   for i in xrange(len(x)):
      y[i] = self.a*x**2 + b*x + c
   for xi, yi in zip(x, y):
      print xi, yi
      

      
def yes.roots(self): 
   a, b, c = self['a'], self['b'], self['c']
   x1 = (-b + sqrt(b**2 - 4*a*c))/float(2*a)
   x2 = (-b - sqrt(b**2 - 4*a*c))/float(2*a)
   return x1, x2
