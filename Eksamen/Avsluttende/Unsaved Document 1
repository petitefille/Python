# Avsluttende eksamen 2014

# Oppgave 1

# (a)

s = -2
for k in range(2, 5, 2):
    s += 2
print s 

>>> range(2, 5, 2)
[2, 4]

# (b)

# (c) 

def myfunc(a, b):
    s = 0
    for k in a:
        s += a[k]*b**k
    return s
    
print myfunc({1:-1, 3:1}, 3)

# (d)

def myfunc(a, b):
    c = a.copy()
    for k in b:
        if k in c:
            c[k] += b[k]
        else:
            c[k] = b[k]
    return c
    
print myfunc({1:-1, 3:1}, {1:3, 2:2})

# (e) 

from math import factorial

# factorial(n) is N! = N*(N-1)*(N-2)*...*2*1

def test_factorial():
    expected = 5*4*3*2*1
    computed = factorial(5)
    assert expected == computed 

test_factorial()

# Exercise 2 (5 points)

def p(t):
    return 0 if t < 5 else 0.4
    
# or

def p(t):
    if t < 5:
        return 0
    else:
        return 0.4

# Test function

def test_p():
    tol = 1E-15
    assert abs(p(0) - 0) < tol 
    assert abs(p(4) - 0) < tol
    assert abs(p(5) - 0.4) < tol
    assert abs(p(10) - 0.4) < tol
    
test_p()

# Exercise 3 (20 points)

>>> N = 3
>>> from numpy import zeros
>>> y = zeros(N+1, int)
>>> y
array([0, 0, 0, 0])

>>> for i in range(1, N+1):
...     y[i] = i*y[i-1]
...     print i, y[i]
... 
1 0
2 0
3 0
>>> range(1, N+1)
[1, 2, 3]

# (b)

>>> N = 4
>>> from numpy import zeros
>>> y = zeros(N+1, int)
>>> y
array([0, 0, 0, 0, 0])
>>> y[0] = 1
>>> y
array([1, 0, 0, 0, 0])
>>> for i in range(1, N+1):
...     y[i] = i*y[i-1]
...     print i, y[i]
... 
1 1
2 2
3 6
4 24

# (d)

>>> from numpy import zeros
>>> def factorial(N):
...     y = zeros(N+1, int)
...     y[0] = 1
...     for i in range(1, N+1):
...         y[i] = i*y[i-1]
...     return y
... 
>>> y_14 = factorial(14)[-1]
>>> y_14
87178291200





