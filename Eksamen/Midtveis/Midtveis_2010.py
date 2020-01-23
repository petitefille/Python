
# Ex 1:

# (a)

q = 3.141 
print '%.1f' % q 

q = 3.141 
print '%.1f' % q 

q = 3.151 
print '%.1f' % q 

# (b)

for in in range(2, 6, 2):
    print i-1

# (c)

a = 4
b = 10/a + 1
print b


# (d)

A = [14] + [16, 18] + [25, 40]
del A[1]
print A



# (e) 

A = [-1, 9, 2, 5, 19, 21, 33]
print A[4:-1]

# (f)

values = []
value = 0
stop = 1
incr = 0.2 
while value <= stop:
    values.append(value)
    value += incr
for v in values:
    print v 
	
	

# (g)

print [0.2*i for i in range(6)]

# (h)

def f(x):
    return a*x**2
x = 3; a = -2
print '%g' % f(x + a)

# (i)

for i in range(2, 5):  # [2, 3, 4]
    for j in range(i-1, i+3): # i=2; j=[1,2,3,4]. i=3; j=[2,3,4,5]. i=4; j=[3,4,5,6]
	    if i != j:
		    print i, j+1

# (j)
def branch(argument):
    r = 0
    if argument == -1:
        r = -1
    elif argument == 3:
        r = 3
    elif argument > 3:
        r = -2
    else:
        r = 10
    return r 

print branch(6)


# Ex. 3: 

import sys
n = int(sys.argv[1])
s = 0 # sum of integers
for i in range(1, n, 1):
    s += i
print s


# Ex. 4: 

def p(x):
    return A*exp(-a*x)*sin(w*x)
	
from scitools.std import *
# or from numpy import exp, sin
# import sys

try:
    n = int(sys.argv[1])
    A = float(sys.argv[2])
    a = float(sys.argv[3])
    w = float(sys.argv[4])
except IndexError:
    print 'Usage: %s n A a w' % sys.argv[0]
    sys.exit(1)
except ValueError, e:
    print 'Illegal value - cannot convert to number!', e
    sys.exit(1)
	
if A <= 0:
    #raise ValueError('A must be strictly positive')
    print 'A=%g is not > 0' % A; sys.exit(1)
if a <= 0:
    #raise ValueError('a must be strictly positive')
    print 'a=%g is not > 0' % a; sys.exit(1)
	
x = linspace(0, 5.0/a, n)
y = p(x)

for xi, yi in zip(x, y):
    print '%10.3f %12.7f' % (xi, yi)


# Ex. 5: 

plot(x, y)



# Ex. 6:

from math import sqrt

def triangle(corners):
    x1 = corners[0][0]; y1 = corners[0][1]
    x2 = corners[1][0]; y2 = corners[1][1]
    x3 = corners[2][0]; y3 = corners[2][1]
    A = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    C = sqrt((x2-x1)**2 + (y2-y1)**2) + \
        sqrt((x3-x2)**2 + (y3-y2)**2) + \
        sqrt((x1-x3)**2 + (y1-y3)**2)
    return A, C

corners = [(-3, 0), (3, 0), (0, 4)]
A, C = triangle(corners)
print 'Area:', A, 'Circumference:', C

#(Output: Area: 12.0 Circumference: 16.0)


# Ex. 7: 
def sin_diffeq(x, N):
    aj_prev = x
    sj_prev = 0
    index = range(N+1)
    for j in index[1:]:
        sj = sj_prev + aj_prev
        aj = -x**2/float((2*j+1)*(2*j))*aj_prev
        sj_prev = sj
        aj_prev = aj
    return sj, abs(aj)

N = 20
from math import pi
x = pi
s_N, a_N = sin_diffeq(x, N)
print s_N
