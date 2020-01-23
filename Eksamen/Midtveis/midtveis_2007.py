# Ex 1 

# Ex 2 

C = 21
F = 9*C/5 + 32
print F

# Ex 3

a = 2; b = 5
c = b**a/a
print c

# Ex 4

 

# Ex 5 

values = []
value = 0.1
stop = 1
while value <= stop:
    values.append(value)
    value += 0.1

print values

print [0.1*i for i in range(10)]
# print range(0.1,1.1,0.1)
print [0.1+i for i in range(10) ]
print [(i+1)*0.1 for i in range(10)]


[0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 0.9999999999999999]
[0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9]
[0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1]
[0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9, 1.0]

# Ex 6 

print [i for i in range(15, 55, 10)]
print [15,25] + [45, 55] + [35]
print [i for i in range(15, 45, 10)] + [i for i in range(45, 65, 10)]
print [5 + 10*i for i in range(5)]


[15, 25, 35, 45]
[15, 25, 45, 55, 35]
[15, 25, 35, 45, 55]
[5, 15, 25, 35, 45]

# Ex 7 

def f(x):
    return a*x**2
x = 5; a = 2
print '%g' % f(x + a)

# Ex 8 

n = 5
C = []
for i in range(n):
    x = i**2
    C.append(i+x)
print C


# Exercise 9:
x = range(3)
y = [x[1], x[0] + 4, x[2] + x[1]]
xy = [x, y]
print xy[1][2]

# 3 



>>> from numpy import *
>>> a = array(4)
>>> a
array(4)
>>> a
array(4)
>>> b = zeros(4)
>>> b
array([ 0.,  0.,  0.,  0.])
>>> b = [0,2,3]
>>> type(b)
<type 'list'>
>>> b = array(b)
>>> b
array([0, 2, 3])
>>> type(b)
<type 'numpy.ndarray'>
>>> b = eye(4)
>>> b
array([[ 1.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.],
       [ 0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  1.]])
>>> x = linspace(0, 10,3)
>>> x
array([  0.,   5.,  10.])
>>> s = x
>>> s += 5
>>> s
array([  5.,  10.,  15.])

# Ex. 14:

def g(t, a):
    g_t = exp(-a*t**2)
    dg_t = -2*a*t*g_t
    return g_t, dg_t


# Ex. 15:

def area(vertices):
    x1 = vertices[0][0]; y1 = vertices[0][1]
    x2 = vertices[1][0]; y2 = vertices[1][1]
    x3 = vertices[2][0]; y3 = vertices[2][1]
    A = 0.5*(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A


# Ex. 16:

from scitools.std import *

def f(x, t):
    return exp(-(x - 3*t)**2)*sin(3*pi*(x - t))
	
t = 0
x = linspace(-4, 4, 101)
y = f(x, t)
plot(x, y)


# Ex. 17:

L = 10000
p = 5.
N = 36
x0 = L
xnm1 = x0
n = 1
while n <= N:
    xn = (1 + p/1200.)*xnm1 - L/float(N)
    xnm1 = xn
    n += 1
print xn

