"""Class(es) implementing the Forward Euler method for scalar ODEs."""

import numpy as np

class MidpointIter:
    """
    Class for solving an ODE,

      du/dt = f(u, t)

    by the iterated Midpoint method.

    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    dt: time step (assumed constant)
    """
    def __init__(self, f, N):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f = f
        self.N = N
        self.v = np.zeros(N+1)

    def set_initial_condition(self, U0):
        self.U0 = float(U0)

    def solve(self, time_points):
        """Compute u for t values in time_points list."""
        self.t = np.asarray(time_points)
        self.u = np.zeros(len(time_points))
        # Assume self.t[0] corresponds to self.U0
        self.u[0] = self.U0

        for k in range(len(self.t)-1):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Advance the solution one time step."""
        # Load attributes into local variables to
        # obtain a formula that is as close as possible
        # to the mathematical notation.
        u, f, k, t, v, N = self.u, self.f, self.k, self.t, self.v, self.N

        dt = t[k+1] - t[k]
        v[0] = u[k]
        for q in range(1, N+1):
            v[q] = u[k] + 0.5*dt*(f(v[q-1], t[k+1]) + f(u[k], t[k]))
        u_new = v[N]
        return u_new

def test_MidpointIter_against_hand_calculations():
    def f(u, t):
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

def test_ForwardEuler_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    u_exact = lambda t: 0.2*t + 3
    solver = ForwardEuler(lambda u, t: 0.2 + (u - u_exact(t))**4)

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


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_MidpointIter_against_hand_calculations()
        
"""
"""        
