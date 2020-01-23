# Midtveis 2014

# Ex. 1:

# (a)

a = 4
b = a
a = 2
print 'b:', b

# (b)

>>> range(2)
[0, 1]

a = 2
for i in range(2):
    a += 2
print a

# (c)

A = [1,2,3,-1]
del A[-1]
A.append(-2)
print A

# (d)

a = 4
b = 6
c = a + b 
# a = sys.agv[1] = '1'
a = '1'
# b = sys.argv[2] = '2'
b = '2'
print c 

# (e)

>>> import numpy as np
>>> x = np.linspace(0, 4, 3)
>>> x
array([ 0.,  2.,  4.])
>>> y = x**2
>>> y
array([  0.,   4.,  16.])
>>> zip(x, y)
[(0.0, 0.0), (2.0, 4.0), (4.0, 16.0)]

>>> for x_, y_ in zip(x, y):
...     print '%.1f %.1f' % (x_, y_)
... 
0.0 0.0
2.0 4.0
4.0 16.0

# (f)

def P(x):
    return x + 1
    
def Q(y):
    return 2*y

print Q(P(Q(3)))

# (g)

# (h)

>>> u = [0, 1]
>>> u
[0, 1]
>>> v = [2, 3]
>>> v
[2, 3]
>>> print u + v
[0, 1, 2, 3]
>>> from numpy import array
>>> u = array(u)
>>> u
array([0, 1])
>>> v = array(v)
>>> v
array([2, 3])
>>> print u+v
[2 4]

# (i)

def plus1(x):
    return x + 1
    
def test_plus1():
    x = 4.5
    exact = 5.5
    computed = plus1(x)
    tol = 1E-14
    success = abs(exact - computed) < tol
    msg = 'exact=%g, computed=%g' % (exact, computed)
    assert success, msg
    
test_plus1()

# (j)
>>> range(-1,1,2)
[-1]
>>> range(3)
[0, 1, 2]

for i in range(-1, 1, 2):
    for j in range(3):
        if i == j:
            print i, j 

			
# Ex. 2: 

from math import factorial

def K(x, N):
    x = float(x) # avoid integer division
    s = 0 # summation variable
    for k in range(N+1):
        s += (-1)**k*x**(2*k+1)/factorial(2*k+1)
    return s
	
from math import pi
print K(pi, 4)


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

def K(x, N):
    sn_prev = 0 # here s[0], stores in general s[n-1]
    an_prev = x # here a[0], stores in general a[n-1]
    for n in range(1, N+1):
        sn = sn_prev + an_prev
        an = an_prev*(-1)*x**2/((2*n+1)*(2*n))
        # change contents (be ready for next pass in the loop):
        sn_prev = sn
        an_prev = an
    return sn

from math import pi
print K(pi, 4)


# Ex. 3:

import sys

try:
    x = float(sys.argv[1])
    N = int(sys.argv[2])
except IndexError:
    print 'Not enough command-line arguments! Need x and K.'
    sys.exit(1)
except ValueError:
    print 'Cannot convert %s and %s to numbers' % \
          (sys.argv[1], sys.argv[2])
    sys.exit(1)
	
print 'K(%g, %d)=%g' % (x, N, K(x, N))

# Ex. 4:

import numpy as np
x = np.linspace(0, 2*np.pi, 101)
N = 5
y = K(x, N)
import matplotlib.pyplot as plt
# import scitools.std as plt
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['N=%d' % N])
plt.savefig('tmp.png')
plt.show()


# Ex. 5:

def test_K():
    x = 0.5
    N = 1
    exact = 23.0/48
    computed = K(x, N)
    tol = 1E-14
    success = abs(exact - computed) < tol
    assert success, 'exact=%g, computed=%g' % (exact, computed)


 



# Ex. 6:

# Read file data into lists
infile = open('simulations.dat', 'r')
infile.readline(); infile.readline() # skip first two lines

# Start with empty lists since we do not know how 
# many lines the file has 
time = []
measurement = []
prediction = []

for line in infile:
    words = line.split()
	floats = [float(word) for word in words]
	time.append(floats[0])
	measurement.append(floats[1])
	prediction.append(floats[2])
infile.close()

# Convert to numpy arrays
import numpy as np
time = np.array(time)
measurement = np.array(measurement)
prediction = np.array(prediction)

# Plot measurement with red circles and 
# prediction with solid blue line 
import matplotlib.pyplot as plt 
plt.plot(time, measurement, 'ro',
         time, prediction, 'b-')
plt.legend(['measurement', 'prediction'])
plt.xlabel('time')
plt.show()



for line in infile: 
    time.append(float(line[0:8]))
	measurement.append(float(line[8:22]))
	prediction.append(float(line[22:]))

			






