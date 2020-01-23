from numpy import zeros

def K(x, N):
   a = zeros(n+1)
   s = zeros(n+1)
   a[0] = x
   s[0] = 0
   for n in range(1, N+1):
      s[n] = s[n-1] + a[n-1]
      a[n] = a[n-1]*(-1)*x**2/((2*n+1)*(2*n))
   return s[n]
	
from math import pi
print K(pi, 4)