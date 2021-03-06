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
  
   def test_Line(self):
      l = Line(self.x0, self.y0), (self.x1, self.y1))
      computed_y = l.value()
      a = (self.y1 - self.y0)/float(self.x1 - self.x0)
      b = self.y0 - a*self.x0
      exact_y = a*x + b
      diff = abs(exact_y - computed_y)
      tol = 1E-14
      assert diff < tol, 'bug in Line.value, diff=%s' % dif
