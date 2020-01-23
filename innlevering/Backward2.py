
from Diff import *

class Diff2(Diff):
    def __init__(self, f, h, dfdx_exact=None):
        Diff.__init__(self, f, h)
        self.exact = dfdx_exact

    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
            return df_exact - df_numerical

class Forward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Backward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff2):
   def __call__(self, x):
      f, h = self.f, self.h
      return (f(x-2*h) - 4*f(x-h) + 3*f(x))/(2*h)

class Central2(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Central4(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h)   - f(x-h))  /(2*h) - \
               (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)

class Central6(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (3./2) *(f(x+h)   - f(x-h))  /(2*h) - \
               (3./5) *(f(x+2*h) - f(x-2*h))/(4*h) + \
               (1./10)*(f(x+3*h) - f(x-3*h))/(6*h)

class Forward3(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (-(1./6)*f(x+2*h) + f(x+h) - 0.5*f(x) - \
                (1./3)*f(x-h))/h

from math import *
    
s = [1./2**i for i in range(0,15,1)]
import numpy as np
bw2 = []
bw2_error = []
for h in s:
   bb = Backward2(lambda x: exp(-x), h, dfdx_exact=lambda x: -exp(-x) )
   bb2 = bb(x=0)
   bw2.append(bb2)     
   x = 0
   bw2_e = bb.error(x)
   bw2_error.append(bw2_e)
   
s = [1./2**i for i in range(0,15,1)]
bw1 = []
bw1_error = []
for h in s:
   b = Backward1(lambda x: exp(-x), h, dfdx_exact=lambda x: -exp(-x))
   bb1 = b(x=0)
   bw1.append(bb1)  
   x = 0
   bw1_e = b.error(x)
   bw1_error.append(bw1_e)

print '     h        Backward2     Error Backward2    Backward1   Error Backward1\n'  
for si, bw2i, bw2_errori, bw1i, bw1_errori in zip(s, bw2, bw2_error, bw1, bw1_error):
   print '%2.8f   %.8f     %.8f      %.8f     %.8f' % (si, bw2i, bw2_errori, bw1i, bw1_errori)
       
"""
 Terminal > python Backward2.py
     h        Backward2     Error Backward2    Backward1   Error Backward1

1.00000000   -0.24203561     -0.75796439      -1.71828183     0.71828183
0.50000000   -0.87660325     -0.12339675      -1.29744254     0.29744254
0.25000000   -0.97476079     -0.02523921      -1.13610167     0.13610167
0.12500000   -0.99427358     -0.00572642      -1.06518762     0.06518762
0.06250000   -0.99863506     -0.00136494      -1.03191134     0.03191134
0.03125000   -0.99966674     -0.00033326      -1.01578904     0.01578904
0.01562500   -0.99991766     -0.00008234      -1.00785335     0.00785335
0.00781250   -0.99997954     -0.00002046      -1.00391644     0.00391644
0.00390625   -0.99999490     -0.00000510      -1.00195567     0.00195567
0.00195312   -0.99999873     -0.00000127      -1.00097720     0.00097720
0.00097656   -0.99999968     -0.00000032      -1.00048844     0.00048844
0.00048828   -0.99999992     -0.00000008      -1.00024418     0.00024418
0.00024414   -0.99999998     -0.00000002      -1.00012208     0.00012208
0.00012207   -1.00000000     -0.00000000      -1.00006104     0.00006104
0.00006104   -1.00000000     -0.00000000      -1.00003052     0.00003052
"""
        

