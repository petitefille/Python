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

class test_line:
   
   def __init__(self):
      self.x0 = x0
      self.y0 = y0
      self.x1 = x1
      self.y1 = y1
  
   def test_Line():
      x0 = self.x0
      y0 = self.x0
      x1 = self.x1
      y1 = self.y1
      l= Line((x0, y0), (x1, y1))
      computed_l= l.value(x)
      a = (y1 - y0)/float(x1 - x0)
      b = y0 - a*x0
      y = a*x + b
      diff = abs(y - computed_l)
      tol = 1E-14
      assert diff < tol, 'bug in Line.value, diff=%s' % diff 

if __name__ == '__main__':
   test_Line()
   

   
      
