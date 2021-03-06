from math import cos, sin, exp
"""
Given the expression: cos(sin(x)) + exp(1./t), where x and t are
vectors/arrays and cos, sin, and exp are from numpy and can take
array arguments.

This expression is computed as follows:

r1 = sin(x)
r2 = cos(r1)
r3 = 1/t
r4 = exp(r3)
r5 = r2 + r4

The goal of the exercise is to carry out these intermediate
computational steps using plain loops over lists and compare
the result with a vectorized expression (without loops and
intermediate r1, r2, ..., r5 quantities).
"""

# We use straight lists here, but we could use numpy arrays instead
x = [0, 2]
t = [1, 1.5]
n = len(x)

# r1 = sin(x)
r1 = [0]*n   # allocate result list in memory, so we can index it
for i in range(n):
    r1[i] = sin(x[i])

# r2 = cos(r1)
r2 = [0]*n
for i in range(n):
    r2[i] = cos(r1[i])

# r3 = 1/t
r3 = [0]*n
for i in range(n):
    r3[i] = 1.0/t[i]

# r4 = exp(r3)
r4 = [0]*n
for i in range(n):
    r4[i] = exp(r3[i])

# r5 = r2 + r4
r5 = [0]*n
for i in range(n):
    r5[i] = r2[i] + r4[i]

print 'result:', r5

# check the computations by straight vector computing:
from numpy import sin, cos, exp, array
x = array(x, float)
t = array(t, float)

r = cos(sin(x)) + exp(1./t)
print 'result, using numpy:', r