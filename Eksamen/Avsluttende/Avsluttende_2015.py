# Exercise 1:

# a)

>>> print '4' in '37.5 degrees'
False

# b)

q = -2
for k in range(2, 5, 2):
    q += 1
print q
>>> 0 
# c)


>>> q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
>>> print q[1]
['d', 'e', 'f']
>>> print q[-1][-1]
h

# d)

>>> import sys
>>> C = '20.0 degrees'
>>> try:
...     C = float(C)
... except ValueError:
...     print 'Cannot convert %s to float' %type(C)
...     sys.exit(1)
...
Cannot convert <type 'str'> to float
[emilyd@austur Avsluttende]$ 

# (e)

def test_sum():
    expected = 1+2+3+4+5
	computed = sum(range(6))
	assert expected == computed
test_sum()


# Exercise 2: 

def piece_lin(x):
    if x < 0:
        y = -x
    else:
        y = x
    return y

def test_piece_lin():
    tol = 1e-10
    x = -1
    expected = 1
    computed = piece_lin(x)
    assert abs(expected-computed) < tol
    x = 1
    expected = 1
    computed = piece_lin(x)
    assert abs(expected-computed) < tol
    
# Alternative, simpler solution (the test function will be exactly the same):

def piece_lin(x):
    return abs(x)


# Exercise 3:

# (a)

#(b)


>>> def add(a, b):
...     return a + b
...
>>> print add(1, 2)
3
>>> print add([1,2,3],[0,1,2])
[1, 2, 3, 0, 1, 2]

# (c)

>>> method1 = "ForwardEuler"
>>> method2 = method1
>>> method1 = "RK2"
>>> print method2
ForwardEuler

# (d)


>>> class Y:
...     def __init__(self,v0):
...         self.v0 = v0
...     def __str__(self):
...         return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0
...
>>> y = Y(5)
>>> print y
v0*t - 0.5*g*t**2; v0=5

# (e)

>>> from random import randint
>>> heads = 0
>>> for i in range(N):
...     result = randint(0,1)
...     if result == 0:
...         heads += 1
...
>>> p = heads/N
>>> print p
0

# Exercise 4:

# (a)

from random import randint 

def throw_dice(n):
    N = 100000
    sixes = 0
    for i in range(N):
	    for j in range(n):
		    dice = randint(1,6)
            if dice == 6:
			    sixes += 1
			    break
    return float(sixes)/N
	
# (b)
>>> import numpy as np
>>> def vec_dice(n):
...     N = 100000
...     dice = np.random.random_integers(1,6,(n,N))
...     sixes = np.sum(dice==6,0)
...     return float(np.sum(sixes>0))/N

# Exercise 5:
# (a)
# (b)
# (c)
# (d)
# (e)

