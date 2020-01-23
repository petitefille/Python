from integrate import Integrator
import random
import numpy as np

#import integrate
#class MCint(integrate.Integrator)

class MCint(Integrator):
    def construct_method(self):
        # Points
        x = [random.uniform(self.a, self.b) 
             for i in range(self.n)]
        # Weights
        w = [(self.b - self.a)/float(self.n)]*self.n
        return x, w

    def construct_method(self):
        """Vectorized version."""
        x = np.random.uniform(self.a, self.b, self.n)
        w = np.zeros(len(x)) + float(self.b - self.a)/self.n
        return x, w

def g(t):
    return 2*t   # G(t) = t**2, a=1, b=3, integral=8

def demo():
    integrator = MCint(a=1, b=3, n=10000)
    I = integrator.integrate(g)
    I = integrator.vectorized_integrate(g)  # much faster!
    print I

#demo()

def test_MCint():
    np.random.seed(10)  # last definition of construct_method counts
    a = 1; b = 3
    """
>>> import numpy as np
>>> np.random.seed(10)
>>> x = np.random.uniform(1, 3, 3)
>>> for x_ in x: print '%.16f' % x_
... 
2.5426412865334918
1.0415038987188030
2.2672964698525506
    """
    t = [2.5426412865334918, 1.0415038987188030, 2.2672964698525506]
    I_expected = (b - a)/float(len(t))*(g(t[0]) + g(t[1]) + g(t[2]))
    integrator = MCint(a, b, 3)
    I_computed1 = integrator.integrate(g)
    I_computed2 = integrator.vectorized_integrate(g)
    tol = 1E-15
    success1 = abs(I_expected - I_computed1) < tol
    success2 = abs(I_expected - I_computed2) < tol
    assert success1 and success2

test_MCint()

"""

"""
