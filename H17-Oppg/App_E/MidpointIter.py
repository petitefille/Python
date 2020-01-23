# Do this exercise first without eps (i.e., grab code from MidpointIter_class.py
# and insert in a subclass of ODESolver). Then add eps statements.

from ODESolver import ODESolver, np
from matplotlib.pyplot import plot, show

class MidpointIter(ODESolver):

    def __init__(self, f, N=20, eps=1E-6):
        ODESolver.__init__(self, f)
        self.N = N
        self.eps = eps

#    Need to make self.v. Can be done when we know the length of U0,
#    either in a new set_initial_condition or (with less code) as shown
#    below in advance.

#    def set_initial_condition(self, U0):
#        ODESolver.set_initial_condition(self, U0)
#        self.v = np.zeros((self.N+1,self.neq))

    def advance(self):
        """Advance the solution one time step."""
        # Make sure we have self.v array
        #if k == 0:
        #    self.v = np.zeros((self.N+1,self.neq))

        if not hasattr(self, 'v'):
            if self.neq == 1:
                self.v = np.zeros(self.N+1)  # scalar ODE
            else:
                self.v = np.zeros((self.N+1,self.neq))  # vector ODE

        # Load attributes into local variables to
        # obtain a formula that is as close as possible
        # to the mathematical notation.
        u, f, k, t, v, N, eps = \
           self.u, self.f, self.k, self.t, self.v, self.N, self.eps

        dt = t[k+1] - t[k]

        # (it's usually dangerous to assign values to a v that was
        # set as v = self.v, but in lists this is ok, and moreover,
        # v is only an internal help array)

        v[0] = u[k]
        diff = 10  # larger than eps
        q = 0
        while diff > eps and q < N:
            q += 1
            v[q] = u[k] + 0.5*dt*(f(v[q-1], t[k+1]) + f(u[k], t[k]))
            diff = abs(v[q] - v[q-1]) if self.neq == 1 else \
                   np.abs(v[q] - v[q-1]).max()
            #print 'q=%d, diff=%s, v[%d]=%s' % (q, diff, q, v[q])
        u_new = v[q]
        self.q = q    # Save q to see where the iteration stopped
        return u_new

def test_MidpointIter_against_hand_calculations():
    def f(u, t):           # u' = -2*u
        return -2*u

    dt = 1./4
    U0 = 1
    # Hand calculations
    # 1. time step:
    U0 = 1
    t0 = 0
    u0 = U0
    v0 = U0
    t1 = dt
    v1 = u0 + 0.5*dt*(f(v0, t1) + f(u0, t0))
    v2 = u0 + 0.5*dt*(f(v1, t1) + f(u0, t0))
    u1 = v2

    # 2. time step:
    t2 = t1 + dt
    v0 = u1
    v1 = u1 + 0.5*dt*(f(v0, t2) + f(u1, t1))
    v2 = u1 + 0.5*dt*(f(v1, t2) + f(u1, t1))
    u2 = v2

    exact_u_2 = u2
    N = 2
    T = 2*dt
    n = 2
    solver = MidpointIter(f, N)
    solver.set_initial_condition(U0)
    time_points = np.linspace(0, T, n+1)
    u, t = solver.solve(time_points)
    computed_u_2 = u[2]
    tol = 1E-14
    success = abs(exact_u_2 - computed_u_2) < tol
    print 'success:', success
    assert success

def demo():
    # Solve a system!
    # u'' + u = 0
    # u_1' = u_2
    # u_2' = -u_1
    def f(u, t):
        u_1, u_2 = u
        return [u_2, -u_1]

    solver = MidpointIter(f, N=3)
    solver.set_initial_condition([1, 0])  # u(t) = u_1(t) = cos(t)
    T = 4*np.pi
    dt = 2*np.pi/20   # 20 intervals per period of cos(t)
    n = int(round(T/dt))
    time_points = np.linspace(0, T, n+1)
    u, t = solver.solve(time_points)
    # u: two-dimensional array u[i,j]
    u_1 = u[:,0]
    plot(t, u_1)
    show()  # plot cos(t) for two periods?

def test_MidpointIter_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    # Note: this function is just copied from MidpointIter_class.py
    # and not testet
    u_exact = lambda t: 0.2*t + 3
    # Should reproduce u_exact for any N and eps, but test here that
    # the loop ended because diff <= eps
    eps = 1E-9
    solver = MidpointIter(lambda u, t: 0.2 + (u - u_exact(t))**2,
                          N=200, eps=eps)
    #solver = MidpointIter(lambda u, t: 0.2, N=200, eps=eps)

    # Solve for first time interval [0, 1.2]
    solver.set_initial_condition(u_exact(0))
    u1, t1 = solver.solve([0, 0.4, 1, 1.2])
    # Continue with a new time interval [1.2, 1.5]
    solver.set_initial_condition(u1[-1])
    u2, t2 = solver.solve([1.2, 1.4, 1.5])
    # Append u2 to u1 and t2 to t1
    u = np.concatenate((u1, u2))
    t = np.concatenate((t1, t2))
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    assert error < 1E-14, '|exact - u| = %g != 0' % error
    assert abs(solver.v[solver.q] - solver.v[solver.q-1]) <= eps, \
           'solver did not converge with eps=%g' % eps


if __name__ == '__main__':
    test_MidpointIter_against_hand_calculations()
    test_MidpointIter_against_linear_solution()
    demo()
	
"""

[emilyd@sudur App_E]$ python MidpointIter.py
success: True

"""