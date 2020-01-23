# usikker kilde

def RungeKutta2(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    import numpy as np
    t = np.zeros(n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2
    return u, t

def f(u, t):
    return u

U0 = 1
T = 3
n = 30
u, t = RungeKutta2(f, U0, T, n)

from scitools.std import *
u_exact = exp(t)

#plot(t, u, savefig=("t_u.png"))
#plot(t, u_exact, savefig=("t_u_exact.png"))

plot(t, u, 'r-', t, u_exact, 'bo',
    xlabel='t', ylabel='u', legend=('numerical', 'exact'),
    title="Solution of the ODE u'=u, u(0)=1", savefig=("blah.png"))