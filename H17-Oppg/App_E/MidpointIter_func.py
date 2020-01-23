"""Function implementing the iterated Midpoint method for scalar ODEs."""
import numpy as np

def iterated_Midpoint_method(f, U0, T, n, N):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    #v = [0]*(N+1)  # list
    v = np.zeros(N+1)
    for k in range(n):
        t[k+1] = t[k] + dt
        v[0] = u[k]
        for q in range(1, N+1):
            v[q] = u[k] + 0.5*dt*(f(v[q-1], t[k+1]) + f(u[k], t[k]))
        u[k+1] = v[N]
    return u, t

def test_iterated_Midpoint_method():
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
    u, t = iterated_Midpoint_method(f, U0, T, n, N)
    computed_u_2 = u[2]
    tol = 1E-14
    success = abs(exact_u_2 - computed_u_2) < tol
    assert success

def gaussian():
    import sys
    try:
        dt = float(sys.argv[1])
        N = int(sys.argv[2])
    except (IndexError, ValueError):
        print 'Wrong use!'
        sys.exit(1)
    T = 8
    def f(u, t):
        return -2*(t-4)*u

    from math import e
    U0 = e**(-16)
    n = int(round(T/dt))

    u, t = iterated_Midpoint_method(f, U0, T, n, N)
    u_e = np.exp(-(t-4)**2)  # exact solution
    from matplotlib.pyplot import plot, show, legend
    plot(t, u, 'r-', t, u_e, 'b-')
    legend(['numerical, N=%d, dt=%g' % (N, dt),
            'exact'])
    show()
if __name__ == '__main__':
    test_iterated_Midpoint_method()
    gaussian()
	
"""

[emilyd@sudur App_E]$ python MidpointIter_func.py 5 100


"""