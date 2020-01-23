"""Function implementing the RungeKutta4 method for scalar ODEs."""
import numpy as np

def RK4(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt*f(u[k],t[k])
        K2 = dt*f(u[k]+0.5*K1,t[k]+0.5*dt)
        K3 = dt*f(u[k]+0.5*K2,t[k]+0.5*dt)
        K4 = dt*f(u[k]+K3, t[k]+dt)
        u[k+1] = u[k] + 1.0/6*(K1+2*K2+2*K3+K4)
        #u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

# Simple test problem: u'=u
def f(u, t):
    return u

u, t = RK4(f, U0=1, T=4, n=4)

# Compare numerical solution and exact solution in a plot
import matplotlib.pyplot as plt
from numpy import exp, linspace
t_exact = linspace(0,4,100)
u_exact = exp(t_exact)
plt.plot(t_exact, u_exact, 'r-')
plt.plot(t, u, 'b-')
plt.plot(t, u, 'ro')
plt.legend(['exact', 'numerical']),
plt.title("Solution of the ODE u'=u, u(0)=1")
plt.show()

"""
To test the function, we define an equation which has
a known solution u, where u is a linear function og t. The
function f chosen below is motivated by this, but also chosen
to have some degree of complexity, since simply setting f(u,t) = 0.2
will be less suited for uncovering errors in the code.
For a linear solution, both the RK4 and ForwardEuler method should
reproduce the solution to machine precision. The code below is copied
directly from ForwardEuler_func.py.
"""

def test_RK4_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    def f(u, t):
        return 0.2 + (u - u_exact(t))**4

    def u_exact(t):
        return 0.2*t + 3

    u, t = RK4(f, U0=u_exact(0), T=3, n=5)
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    success = error < 1E-14
    assert success, '|exact - u| = %g != 0' % error

test_RK4_against_linear_solution()

"""
Terminal> python RK4_func.py

"""