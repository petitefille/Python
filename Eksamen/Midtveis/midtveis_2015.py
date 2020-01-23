# INF1100 midtveis 2015

# Ex. 1

"""

>>> y = 4
>>> y = y*y
>>> y
16
>>> print y
16

"""

# (b)
>>> a = 3
>>> a
3
>>> b = a
>>> b
3
>>>
>>> b = b + a
>>> b
6
>>> a
3
>>

#(c)

a = 1
for i in range(2):
    a = a*2
print a

# (d)

A = [[-1,0,1],[5,6,7]]
print A[0][-1]

# (e)


>>> a = str([0,1])
>>> a
'[0, 1]'
>>> b = str([2,3])
>>> b
'[2, 3]'
>>> eval(a)
[0, 1]
>>> eval(b)
[2, 3]
>>> print eval(a) + eval(b)
[0, 1, 2, 3]

# (f)

dx = 0.25
b = [dx*i for i in range(5)]
print b[-1]

# (g)

>>> from numpy import *
>>> x = linspace(0,1,3)
>>> x
array([ 0. ,  0.5,  1. ])
>>> y = x**2
>>> y
array([ 0.  ,  0.25,  1.  ])
>>> for x_,y_ in zip(x,y):
...     print '%4.2f %4.2f' % (x_,y_)
...
0.00 0.00
0.50 0.25
1.00 1.00
>>> zip(x,y)
[(0.0, 0.0), (0.5, 0.25), (1.0, 1.0)]

# (h)
A = ['5', '6', '7', 'end']
try:
    b = float(A[3])
except IndexError:
    print 'A has length %d' %len(A)
except ValueError:
    print 'Cannot convert "%s" to float' % A[3]
	
# (i)

def f(x):
    return x + 2
	
def test_f():
    x = 1.0
    expected = 3.0
    computed = f(x)
    tol = 1E-14
    success = abs(exact-computed) < tol
    msg = 'expected %g, computed %g' %(expected,computed)
    assert success, msg
    
test_f()

# (j)

def f(x):
    return x + 1
    
def g(y):
    return y**2
    
x=2
print g(f(g(x)))

# Exercise 2:


>>> line  = 'air        0.0012          '
>>> line
'air        0.0012          '
>>> words = line.split()
>>> words
['air', '0.0012']
>>> material = words[:-1]
>>> material
['air']
>>> material = ' '.join(material)
>>> material
'air'
>>> value = float(words[-1])
>>> value
0.0011999999999999999
>>>
>>> materials = []
>>> materials.append(material)
>>> values = []
>>> values.append(value)
>>> materials
['air']
>>> values
[0.0011999999999999999]


>>> zip(materials,values)
[('air', 0.0011999999999999999)]

>>> combined = []
>>> for entry in zip(materials, values):
...     combined.append(entry)
...
>>> combined
[('air', 0.0011999999999999999)]

# Ex. 2: 

infile = open('densities.dat', 'r')

# skip first two lines:
infile.readline()
infile.readline()

# first create tow lists:
materials = []
values = []
for line in infile:
    words = line.split()
	material = words[:-1]
	material = ' '.join(material)
	value = float(words[-1])
	materials.append(material)
	values.append(value)
	
# now create the list of lists or tuples 
combined = []
for entry in zip(materials, values):
    combined.append(entry)
	
"""
Or, alternatively:
for m,v in zip(materials, values):
    combined.append((m,v))
"""



>>> line = 'air                  0.0012'
>>> line
'air                  0.0012'
>>> words = line.split()
>>> words
['air', '0.0012']
>>> material = words[:-1]
>>> material
['air']
>>> material = ' '.join(material)
>>> material
'air'
>>> line
'air                  0.0012'
>>> line = ' '.join(line)
>>> line
'a i r                                     0 . 0 0 1 2'


# Ex. 3:

from math import *

def func_deriv(x):
    f = sin(a*pi*x)
    df = a*pi*cos(a*pi*x)
    return f,df
    
a = 1.0
val, deriv = func(0.5)
print val, deriv 
print func_deriv(1.0)

# Ex. 4: 
#re-use function from previous exc., here saved in file func_deriv1.py:
from func_deriv1 import func_deriv
import sys

try:
    a = float(sys.argv[1])
except IndexError:
    print "Please provide a command-line argument for parameter ’a’"
    sys.exit(1)
except ValueError:
    print "Wrong format of argument, please provide a single number"
    sys.exit(1)



# Ex. 5:

# re-use function from previous exc., here saved in file 
# fun_deriv1.py:
from func_deriv1 import func_deriv
from math import sqrt, pi 

def test_func_deriv():
    x = 0.25
    tol = 1e-13
    comp = func_deriv(x)
    expect = 0.5*sqrt(2), pi*0.5*sqrt(2)
    success = abs(comp[0]-expect[0])<tol and abs(comp[1]-expect[1]) <tol
    msg = "Expected %g, %g, got %g, %g" %(comp[0],comp[1], expect[0],expect[1])
    assert success, msg
test_func_deriv()

# Exercise 6:

from numpy import *
from math import factorial
import matplotlib.pyplot as plt

# Simplest version  using math.factorial

def taylor_sin(x, N):
    s = 0
    for i in range(N+1):
       s += (-1)**i*(x**(2*i+1))/factorial(2*i+1)
	return s 
	
# More efficient version, not using factorial 

def taylor_sin2(x, N):
    factor = 1 
	s = x.copy() # first  term in sum (i=0)
	for i in range(1, N+1):
	    factor *= 2*i*(2*i+1)
		s += (-1)**i*(x**(2*i+1))/factor 
	return s 
	
x = linspace(0, 2*pi, 100)
plt.plot(x, taylor_sin2(x, 3), x, sin(x))
plt.legend(['Taylor', 'Exact'])
plt.show()



