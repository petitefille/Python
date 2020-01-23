from math import *
class Rectangle:
   def __init__(self, x0, y0, H, W):
      self.x0, self.y0, self.H, self.W = x0, y0, H, W
   
   def area(self):
      return self.H*self.W

   def perimeter(self):
      return 2*self.H + 2*self.W

r = Rectangle(2, -1, 5, 7)
print 'A rectangle with height %g, width %g and left corner (%g, %g), \
has area %g \nand perimeter %g.' % (r.H, r.W, r.x0, r.y0, r.area(), r.perimeter())

def test_Rectangle():
   H = 3
   W = 6
   r = Rectangle(2, 1, H, W)
   area = H*W; perimeter = H*2 + W*2
   diff = abs(r.area() - area)
   tol = 1E-14
   assert diff < tol, 'bug in Rectangle.area diff=%s' % diff
   diff = abs(r.perimeter() - perimeter)
   assert diff < tol, 'bug in Rectangle.perimeter, diff=%s' % diff    

class Triangle:
   def __init__(self, x1, y1, x2, y2, x3, y3):
      self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = x1, y1, x2, y2, x3, y3
   
   def area(self):
     return 0.5*abs(self.x2*self.y3 - self.x3*self.y2 - self.x1*self.y3 + self.x3*self.y1 + self.x1*self.y2 - self.x2*self.y1)

   def circumference(self):
      return sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)+ sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2) + sqrt((self.x1 - self.x3)**2 + (self.y1 - self.y3)**2)

t = Triangle(0, 0, 1, 0, 0, 2)
print 'An arbitrary triangle which coordinates of its vertices \nnumbered  in a counterclockwise direction are (%g, %g), (%g, %g), (%g, %g) \nhas area %.2f and circumference %.2f.' % (t.x1, t.y1, t.x2, t.y2, t.x3, t.y3, t.area(), t.circumference())

def test_Triangle():
   x1 = 15.0; y1 = 15.0
   x2 = 50.0; y2 = 25.0
   x3 = 23.0; y3 = 30.0
   t = Triangle(x1, y1, x2, y2, x3, y3)
   area = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
   circumference = sqrt((x2 - x1)**2 + (y2 - y1)**2)+ sqrt((x3 - x2)**2 + (y3 - y2)**2) + sqrt((x1 - x3)**2 + (y1 - y3)**2)
   diff = abs(t.area() - area)
   tol = 1E-14
   assert diff < tol, 'bug in Triangle.area diff=%s' % diff
   diff = abs(t.circumference() - circumference)
   assert diff < tol, 'bug in Triangle.perimeter(), diff=%s ' % diff

"""
from scitools.StringFunction import StringFunction
import sys
from numpy import *

formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
n = int(sys.argv[4])
filename = str(sys.argv[5])


x = linspace(a, b, n)
f = StringFunction(formula)
f.vectorize(globals())
y = f(x)

outfile = open(filename, 'w')
outfile.write('  x      f(x)  \n')
for xvalue, yvalue in zip(x, y):
    outfile.write('%5.3f %7.3f\n' % (xvalue, yvalue))
outfile.close()

"""
from scitools.StringFunction import StringFunction
import sys
from numpy import *

formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
n = int(sys.argv[4])
filename = str(sys.argv[5])


x = linspace(a, b, n)
f = StringFunction(formula)
f.vectorize(globals())
y = f(x)

outfile = open(filename, 'w')
outfile.write('  x      f(x)  \n')
for xvalue, yvalue in zip(x, y):
    outfile.write('%5.3f %7.3f\n' % (xvalue, yvalue))
outfile.close()

"""
Terminal > python geometric_shapes.py
A rectangle with height 5, width 7 and left corner (2, -1), has area 35 and perimeter 24.
An arbitrary triangle wich coordinates of its vertices 
numbered in a counterclockwise direction are (0, 1), (1, 0), (0, 2) 
has area 1.00 and circumference 5.24.
Terminal > nosetests geometric_shapes.py

---------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
"""
