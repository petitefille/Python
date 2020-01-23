# INF1100 Midtveis 2013

# Exercise 1: 

# (a)

counter1 = 10
counter2 = counter1 
counter1 = 11
print 'counter2=%d' % counter2

# (b)

counter1 = 10 
counter2 = counter1 
counter1 = 11 
counter2 += 2 + counter1 
print counter2 

# (c)

A = [1,2,3,-1]
if A[2] < 3:
   A[2] = 0
else:
   A[2] = 10 
if A[-1] <= 0:
   A.append(4)
print A

# (d)

B = [2*x+1 for x in range(5)]
print B[1:-1]


>>> range(5)
[0, 1, 2, 3, 4]

# (e)

>>> from numpy import linspace
>>> x = linspace(0,2,3)
>>> x
array([ 0.,  1.,  2.])
>>> v = x + 2
>>> v
array([ 2.,  3.,  4.])
>>> zip(x,v)
[(0.0, 2.0), (1.0, 3.0), (2.0, 4.0)]
>>> for x_, v_ in zip(x,v):
...    print '%.1f %.1f' % (x_, v_)
...
0.0 2.0
1.0 3.0
2.0 4.0

# (f)

def Q(y):
   r = 4*y 
   r = r + 1
   return r 

x = 2 
print 'Q(%g)=%g' % (x, Q(x))




>>> i = 1
>>> j = 2.19
>>> print '%g' % i
1
>>> print '%g' % j
2.19
>>> print '%.1g' % j
2
>>> print '%.1f' % j
2.2
>>> j = 2.99999999
>>> print '%.1g' % j
3
>>> print '%g' % j
3
>>> j
2.9999999900000001
>>> j
2.9999999900000001
>>> print '%g' % j
3
>>> j = 2.99
>>> print '%g' % j
2.99
>>> j = 2.999
>>> print '%g' % j
2.999
>>> j = 2.9999999
>>> print '%g' % j
3
>>> j = 2.999999
>>> print '%g' % j
3
>>> j = 2.99999
>>> print '%g' % j
2.99999


>>> j = 2.99999
>>> print '%g' % j
2.99999
>>> print '%.2g' % j
3
>>> j = 2.1111
>>> print '%.2g' % j
2.1

# (g)

x = range(1, 17, 5)
y = x 
for x_ in x[1:-1]:
   for y_ in y[1:-1]:
      if x_ != y_ and x_ > y_ + 1:
	     print x_, y_

>>> x = range(1,17,5)
>>> x
[1, 6, 11, 16]
>>> x[1:-1]
[6, 11]

# (i)

u = [-1, -2]
v = [1, 2]
print u + v 
from numpy import array 
u = array(u)
v = array(v)
print u + v 


>>> u = [-1, -2]
>>> u
[-1, -2]
>>> v = [1, 2]
>>> v
[1, 2]
>>> print u + v
[-1, -2, 1, 2]
>>> from numpy import array
>>> u = array(u)
>>> u
array([-1, -2])
>>> v = array(v)
>>> v
array([1, 2])
>>> print u + v
[0 0]

# (j)

def equal(a, b, eps=1E-14):
   """Test if a==b with tolerance eps."""
   return abs(a - b) < eps 

def some_function(Q):
   if Q < 0:
      raise ValueError('Q<0 is not allowed')

   if equal(Q,0):
      return 0, None 
   else:
      return 1, 2 

def run_some_function():
   try: 
      r1, r2 = some_function(-1)
      print 'Something is wrong with some_function(-1)!'
      ok = False 
   except: 
      ok = True 
   r1, r2 = some_function(0)
   if not equal(r1,0) or not r2 == None:
      print 'Something is wrong with some_function(0)!'
      ok = False 
   r1, r2 = some_function(2)
   if not equal(r1, 1) or not equal(r2, 2):
      print 'Something is wrong with some_function(2)!'
      ok = False 
   if ok: 
      print 'All tests passed!'
   else: 
      print 'Some test(s) failed!'
	  
run_some_function()

# Exercise 2: 

from math import exp 

def g(t):
    return exp(-a*t), -a*exp(-a*t)

a = 2
g_value, dg_value = g(0.1)
print dg_value 

# Exercise 3: 

from math import exp
import sys

def g(t):
    return exp(-a*t), -a*exp(-a*t)
	
try:
    t = float(sys.argv[1])
    a = float(sys.argv[2])
except IndexError:
    print ’Not enough command-line arguments (two are needed)’, sys.argv[1:]
    sys.exit(1)
except ValueError:
    print ’Cannot convert command-line arguments to floats’, sys.argv[1:]
    sys.exit(1)
	
g_value, dg_value = g(t)
print dg_value


# Ex. 4: 

from numpy import exp # need vectorized exp now

def g(t):
    return exp(-a*t), -a*exp(-a*t)
	
a = 2
import numpy as np
t = np.linspace(0, 5/float(a), 101)
g_curve, dg_curve = g(t)

# Plotting with matplotlib
import matplotlib.pyplot as plot
plt.plot(t, g_curve, t, dg_curve)
plt.xlabel('t')
plt.legend(['g', "g'"])
plt.savefig('plot.png')
plt.show()

# Alternative plotting with scitools
from scitools.std import *
plot(t, g_curve, t_dg_curve,
     legend=['g', "g'"],
     xlabel='t', savefig='plot.png')



# Ex. 5: 

def solve_quadratic_equation(a, b, c):
    q = b**2 - 4*a*c
    if q < -1E-14: # q < 0 with tolerance
        raise ValueError('q=%g<0 is not allowed' % q)
    x1 = (-b + sqrt(q))/(2*a)
    x2 = (-b - sqrt(q))/(2*a)
    if q > 1E-14: # q > 0 with tolerance
        return x1, x2
    else:
        return x1, None
		
from math import sqrt
print solve_quadratic_equation(1, 3, 1)



# Ex. 6:

def equal(a, b, eps=1E-14):
    """Test a==b with tolerance eps."""
    return abs(a - b) < eps
	
def test_solve_quadratic_equation():
    ok = True # True if all tests pass
    eps = 1E-14 # tolerance for testing equality of floats
    # Case 1: q > 0
    # x1 = 1, x2 = -1 (x-1)*(x+1)=0 => x**2 - 1 = 0
    x1, x2 = solve_quadratic_equation(1, 0, -1)
    if not equal(x1, 1) or not equal(x2, -1):
        print 'Test with q>0 failed.'
        ok = False
		
    # Case 2: q = 0
    # x1 = 2, x2 = 2 (x-2)*(x-2)=0 => x**2 - 4*x + 4 = 0
    x1, x2 = solve_quadratic_equation(1, -4, 4)
    if not equal(x1, 2) or not x2 == None:
        print 'Test with q==0 failed.'
        ok = False

    # Case 3: q < 0
    # b=1, a=1, c=1 => b**2 - 4*a*c = 1 - 4 = -3
    try:
        x1, x2 = solve_quadratic_equation(1, 1, 1)
        print 'Test with q<0 failed.'
        ok = False
    except ValueError:
    # Do nothing
        pass # or do print ''
    if ok:
        print 'OK'
