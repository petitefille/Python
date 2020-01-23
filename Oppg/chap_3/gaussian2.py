# Exercise 3.16
# Author: Noah Waterfield Price

from math import sqrt, exp, pi


def gauss(x, m=0, s=1):
    gaussian = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)
    return gaussian
print '%8s' % 'x',
for x in range(-5, 6):
    print '%9d' % x,
print "\nGaussian",
for x in range(-5, 6):
    print '%.7f' % gauss(x),
	
"""
 python gaussian2.py
       x        -5        -4        -3        -2        -1         0         1         2         3         4         5
Gaussian 0.0000015 0.0001338 0.0044318 0.0539910 0.2419707 0.3989423 0.2419707 0.0539910 0.0044318 0.0001338 0.0000015

"""	