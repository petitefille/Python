# Ex. 1 

# (a)

a = 2
b = a
a = 3
print b


>>> a = 2
>>> a
2
>>> b = a
>>> b
2
>>> a = 3
>>> a
3
>>> b
2
>>> print b
2


>>> t = linspace(0, 1, 3)
>>> y = t**2
>>> t
array([ 0. ,  0.5,  1. ])
>>> y
array([ 0.  ,  0.25,  1.  ])
>>> a = y[1]
>>> a
0.25
>>> print '%.1f' % a
0.2
>>> b = 0.25
>>> print '%.1f' % b
0.2
>>> b = 0.251
>>> print '%.1f' % b
0.3
>>> b = 0.256
>>> print '%.1f' % b
0.3
>>> b = 0.231
>>> print '%.1f' % b
0.2



# (b)

from numpy import linspace
t = linspace(0, 1, 3)
y = t**2
for t_, y_ in zip(t, y):
    print '%.1f %.1f' % (y_, t_)
	

>>> from numpy import linspace
>>> t = linspace(0, 1, 3)
>>> y = t**2
>>> t
array([ 0. ,  0.5,  1. ])
>>> y
array([ 0.  ,  0.25,  1.  ])
>>> zip(t,y)
[(0.0, 0.0), (0.5, 0.25), (1.0, 1.0)]
>>> for t_, y_ in zip(t,y):
...     print '%.1f %.1f' % (y_, t_)
...
0.0 0.0
0.2 0.5
1.0 1.0



# (c)

def g(x):
    return 1 - x/4
x = 2
print 'g(%g)=%g' % (x, g(x))


# (d)

A = [1, 2, 3]
if A[2] < 3:
    del A[1]
else:
    del A[0]
if A[0] > 1:
    A.append(4)
print A


# (e)

B = [x**2 for x in range(5)]
print B[1:-1]


# (f)
def iterate(f, x, dfdx, tolerance=1.0E-2, max_n=5):
    n = 0
    while abs(f(x)) > tolerance and n <= max_n:
        x = x - f(x)/dfdx(x)
        n += 1
    if n > max_n:
        raise ValueError('Iteration did not converge')
    else:
        return x, f(x)
		
def g(t):
    return (1-t)*(2-t) #2 -3t +t^2
	
def dgdt(t):
    return 2*t - 3
	
def g(t):
    return 1-t
	
def dgdt(t):
    return -1
	
print iterate(g, 1, dgdt)
print iterate(g, 12.5, dgdt)

# (g)

import numpy as np
x = np.linspace(1, 5, 5)
y = x
for x_ in x[1:-1]:
    for y_ in y[1:-1]:
        if x_ != y_ and x_ > y_ + 1:
            print x_, y_


>>> import numpy as np
>>> x = np.linspace(1,5,5)
>>> x
array([ 1.,  2.,  3.,  4.,  5.])

x = [1., 2., 3., 4., 5.]
y = x
for x_ in x[1:-1]:
    for y_ in y[1:-1]:
        if x_ != y_ and x_ > y_ + 1:
            print x_, y_



		
# (h)

A = [[0, 0], [0, -1], [1, 3], [2, 4], [0, -2]]
print A[2]
print A[3][1]
print A[2:]


# (i)

numbers = (1, 4, 8, 3, 2)
k = numbers[2]
try:
    element = float(numbers[k])
    print 'element=%f' % element
except IndexError:
    print 'Index %d > %d' % (k, len(numbers))
except ValueError:
    print 'Could not convert %d to float' % (numbers[k])


		
# (j)

u = [1, 2]; v = [-1, 1]
print u + v
from numpy import array
u = array(u); v = array(v)
print u + v


>>> u = [1, 2];
>>> u
[1, 2]
>>> v = [-1, 1]
>>> v
[-1, 1]
>>> print u + v
[1, 2, -1, 1]
>>> from numpy import array
>>> u = array(u)
>>> u
array([1, 2])
>>> v = array(v)
>>> v
array([-1,  1])
>>> print u + v
[0 3]


# Ex. 2: 

def fts2ms(v):
    foot = 12*0.0254 # 1 foot measured in meters
    return v*foot
	
print fts2ms(3)

# Ex. 3: 

def area(vertices):
    x1 = vertices[0][0]; y1 = vertices[0][1]
    x2 = vertices[1][0]; y2 = vertices[1][1]
    x3 = vertices[2][0]; y3 = vertices[2][1]
    A = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A
	
quadrilateral_area = area([[0,0], [3, 0.5], [2,4]]) + \
                     area([[2,4], [3, 0.5], [4,3]])
print quadrilateral_area


# Ex. 4 

from scitools.std import array, plot, show, log
# or
# from numpy import array
# from matplotlib.pyplot import plot, show

def terms(ti, x_0, N):
    return array([ti(x_0, i) for i in range(N+1)])
	
def visualize(t):
    plot(range(len(t)), log(abs(t)), ’ro’)
    # or just plot(log(abs(t)), ’ro’)
    show()
	
from math import factorial, pi

def ti_sin(x, i):
    return (-1)**i*x**(2*i+1)/factorial(2*i+1)
	
t = terms(ti_sin, pi, 10)
visualize(t)


# Ex. 5:

def Newton(g, x, dgdx, epsilon=1.0E-2, max_n=50):
    n = 0
    x_all = []
    g_all = []
    while abs(g(x)) > epsilon and n <= max_n:
        x = x - g(x)/dgdx(x)
        x_all.append(x)
        g_all.append(g(x))
        n += 1
    if n > max_n:
        raise ValueError(’Iteration did not converge’)
    else:
        return x_all, g_all
		
from math import sin, cos, exp

def g(x):
    return sin(x) + cos(x)**2 - exp(x)
	
def dgdg(x):
    return cos(x) - 2*cos(x)*sin(x) - exp(x)
	
x, g = Newton(g, -4, dgdg)
print ’Approximation to the root:’, x[-1]

from scitools.std import plot
plot(range(len(x)), x, ’bo’)



