"""The class below is based on the ForwardEuler_v1 class, copied from ForwardEuler.py.
We could just as easily have based the new RK4 class on the ForwardEuler class
from the same file. This class has a slightly different constructor and solve
function, but to implement the RK4 method we only need to change the advance function.
"""


import numpy as np

class RK4(object):
    """
    Class for solving an ODE,

      du/dt = f(u, t)

    by the RK4 solver.

    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    n: number of time steps in the simulation
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    dt: time step (assumed constant)
    """
    def __init__(self, f, U0, T, n):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))

        self.f, self.U0, self.T, self.n = f, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros(self.n+1)
        self.t = np.zeros(self.n+1)

    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        self.t[0] = float(0)

        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Advance the solution one time step."""
        # Load attributes into local variables to
        # obtain a formula that is as close as possible
        # to the mathematical notation.
        u, dt, f, k, t = \
           self.u, self.dt, self.f, self.k, self.t
        K1 = dt*f(u[k],t[k])
        K2 = dt*f(u[k]+0.5*K1,t[k]+0.5*dt)
        K3 = dt*f(u[k]+0.5*K2,t[k]+0.5*dt)
        K4 = dt*f(u[k]+K3, t[k]+dt)
        u_new = u[k] + 1.0/6*(K1+2*K2+2*K3+K4)
        return u_new

# Compare numerical solution and exact solution in a plot
import matplotlib.pyplot as plt
from numpy import exp, linspace


solver = RK4(lambda u, t: u, U0=1, T=4, n=5)
u, t = solver.solve()
t_exact = linspace(0,4,100)
u_exact = exp(t_exact)
plt.plot(t_exact, u_exact, 'r-')
plt.plot(t, u, 'b-')
plt.plot(t, u, 'ro')
plt.legend(['exact', 'numerical']),
plt.title("Solution of the ODE u'=u, u(0)=1")
plt.show()

def test_RK4_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    def f(u, t):
        return 0.2 + (u - u_exact(t))**4

    def u_exact(t):
        return 0.2*t + 3

    solver = RK4(f, U0=u_exact(0), T=3, n=5)
    u,t = solver.solve()
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    success = error < 1E-14
    assert success, '|exact - u| = %g != 0' % error

test_RK4_against_linear_solution()


"""
Terminal> python RK4_class.py

"""