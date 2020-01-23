import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

def Heun(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt        
        u_star = u[k] + dt*f(u[k], t[k])
        u[k+1] = u[k] +0.5*dt*(f(u[k],t[k])+f(u_star,t[k+1]))
    return u, t


def f(u,t):
    return 0.1*u

def exact(t):
    return u0*np.exp(0.1*t)

Tstop = 50
u0 = 0.2
dt = 5.0
n = int(round(Tstop/float(dt)))
u1,t1 = ForwardEuler(f,u0,Tstop,n)
u2,t2 = Heun(f,u0,Tstop,n)

plt.plot(t1,u1,t2,u2,t1,exact(t1))
legends = ['Euler','Heun','Exact']
plt.legend(legends)
plt.show()


"""
Verification 1: Solve a problem where the solution
is a linear function. In this case both Heun, Euler and most
numerical methods should reproduce the exact solution. This
method of verification is suitable for implementation in a
test function.
"""


def test_Heun():
    def f_const(u,t):
        return 1.0
    tol = 1e-13
    
    u,t = Heun(f_const,0,5,5)
    expected = 5.0 #solution u = t
    computed = u[-1]
    assert abs(expected-computed)< tol

test_Heun()

"""
Verification 2: We know Heun's method is a second
order, so we have error = C*dt**2, with C unknown.
Solve a problem where we know the exact solution, reduce the
time step and verify that the error behaves as expected.
This method is useful for visual inspection, and not that
suitable for implentation in a test function. 
"""


dt_list = [dt/float(2**i) for i in range(10)]
error = []

for dt in dt_list:
    n = int(round(Tstop/float(dt)))
    u,t = Heun(f,u0,Tstop,n)
    error.append(abs(u[-1]-exact(Tstop)))

for dt, e in zip(dt_list,error):
    print "%6.4f %6.4f %6.4f" %(dt, e, e/dt**2)
    



"""

[emilyd@sudur App_E]$ python Heuns_method.py
5.0000 4.0045 0.1602
2.5000 1.2572 0.2011
1.2500 0.3500 0.2240
0.6250 0.0921 0.2357
0.3125 0.0236 0.2415
0.1562 0.0060 0.2445
0.0781 0.0015 0.2459
0.0391 0.0004 0.2466
0.0195 0.0001 0.2470
0.0098 0.0000 0.2472

"""
    

    