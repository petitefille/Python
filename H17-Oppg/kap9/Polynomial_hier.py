from Polynomial import Polynomial

class Parabola(Polynomial):
    """Representation of a parabola c0 + c1*x + c2*x**2."""
    def __init__(self, c0, c1, c2):
        Polynomial.__init__(self, [c0, c1, c2])

p = Parabola(1, 2, 3)
print p(1)

class Line(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)

l = Line(1, 2)
print l(1)

"""

[emilyd@sudur kap9]$ python Polynomial_hier.py
6
3

"""
