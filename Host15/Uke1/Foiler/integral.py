from numpy import *

def integrate(f, a, b, n=100):
    """ 
    Integrate f from a to b,
    using the Trapezoidal rule with n intervals.
    """
    x = linspace(a, b, n+1)   # Coordinates of the intervals
    h = x[1] - x[0]           # Interval spacing
    I = h*(sum(f(x)) - 0.5*(f(a) + f(b)))
    return I

# Define my special integrand
def my_function(x):
    return exp(-x**2)

minus_infinity = -20   # Approximation of minus infinity
I = integrate(my_function, minus_infinity, 1, n=1000) 
print I

"""
Terminal> python ball1.py
1.2342
"""

