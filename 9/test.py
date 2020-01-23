
from Diff import * 

class Diff2(Diff):
    def __init__(self, f, h=1E-5, dfdx_exact=None):
        Diff.__init__(self, f, h)
        self.exact = dfdx_exact

    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
            return df_exact - df_numerical


class Backward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff2):
   def __call__(self, x):
      f, h = self.f, self.h
      return (f(x-2*h) - 4*f(x-h) + 3*f(x))/(2*h)

if __name__ == '__main__':
   from math import *
   # h =
   mycos =(Backward2(sin, dfdx_exact= cos)
   x = pi
   mycos_error = mycos_error(x)
   print 'Error in derivative is', mycos_error  

