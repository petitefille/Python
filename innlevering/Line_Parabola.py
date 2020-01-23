class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
 
    def __call__(self, x):
        y_Line = self.c0+ self.c1*x
        print 'Line: %.3f' % (y_Line)
        return self.c0+ self.c1*x
       

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        print s



class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)  # let Line store c0 and c1
        self.c2 = c2

    def __call__(self, x):
        y_Parabola = Line.__call__(self, x) + self.c2*x**2
        print 'Parabola: %.3f' % (y_Parabola)
        return Line.__call__(self, x) + self.c2*x**2
        
class Cubic(Parabola):
      def __init__(self, c0, c1, c2, c3):
         Parabola.__init__(self, c0, c1, c2)
         self.c3 = c3
    
      def __call__(self, x):
         y_Cubic = Parabola.__call__(self, x) + self.c3*x**3
         print 'Cubic: %.3f' %  (y_Cubic)
         return Parabola.__call__(self, x) + self.c3*x**3

class Poly4(Cubic):
   def __init__(self, c0, c1, c2, c3, c4):
      Cubic.__init__(self, c0, c1, c2, c3)
      self.c4 = c4
   
   def __call__(self, x):
      y_Poly4 = Cubic.__call__(self, x) + self.c4*x**4
      print 'y_Poly4:%.3f' % (y_Poly4)
      return Cubic.__call__(self, x) + self.c4*x**4

p = Cubic(2, 4,-5, 6)
p1 = p(x= -4.5)

p = Poly4(1, -2, 2, 3, -3)
p1 = p(x=2.5)

"""
Terminal > python Line_Parabola.py 
Line: -16.000
Parabola: -117.250
Line: -16.000
Cubic: -664.000
Line: -16.000
Parabola: -117.250
Line: -16.000
Line: -4.000
Parabola: 8.500
Line: -4.000
Cubic: 55.375
Line: -4.000
Parabola: 8.500
Line: -4.000
y_Poly4:-61.812
Line: -4.000
Parabola: 8.500
Line: -4.000
Cubic: 55.375
Line: -4.000
Parabola: 8.500
Line: -4.000

"""





