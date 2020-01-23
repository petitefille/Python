class Line:

   def __init__(self, (x0, y0), (x1, y1)):
      self.x0 = x0
      self.y0 = y0
      self.x1 = x1
      self.y1 = y1



   def value(self, x):
      a = (self.y1 - self.y0)/float(self.x1 - self.x0)
      b = self.y0 - a*self.x0
      y = a*x + b
      return y
"""
class test_line:
   
   def __init__(self):
      self.x0 = x0
      self.y0 = y0
      self.x1 = x1
      self.y1 = y1
"""
  
def test_Line():
   l= Line((0, -1), (2, 4))
   computed_y1= l.value(0.5)
   computed_y2 = l.value(0)
   computed_y3 =l.value(1)
   x0 = 0; y0 = -1
   x1 = 2; y1 = 4
   xa = 0.5; xb = 0; xc = 1
   a = (y1 - y0)/float(x1 - x0)
   b = y0 - a*x0
   exact_y1 = a*xa + b
   exact_y2 = a*xb + b
   exact_y3 = a*xc + b
   diff1 = abs(exact_y1 - computed_y1)
   tol = 1E-14
   assert diff1 < tol, 'bug in Line.value, diff=%s' % diff1
   diff2 = abs(exact_y2 - computed_y2)
   assert diff2 < tol, 'bug in Line.value, diff=%s' % diff2
   diff3 = abs(exact_y3 - computed_y3)
   assert diff3 < tol, 'bug in Line.value, diff=%s' % diff3
       

