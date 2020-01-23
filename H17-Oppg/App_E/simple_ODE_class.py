# Given u - 10*u' = 0
# Generic form u' = f(u, t)
# Solve wrt u':
# u' = (1/10)*u
# f(u, t) = u/10.0

class F:
    # No data to store so we do not write a constructor
    # (Python will equip the class with an empty constructor)
    def __call__(self, u, t):
        return u/10.0

from ForwardEuler import ForwardEuler
from numpy import linspace, exp
U0 = 0.2
T = 20
dt = 5
n = int(round(T/float(dt)))
time_points = linspace(0, T, n+1)

f = F()
solver = ForwardEuler(f)
solver.set_initial_condition(U0)
u,t = solver.solve(time_points)

def exact(t):
    return 0.2*exp(0.1*t)

from scitools.std import plot
plot(t, u, 'r-o', t, exact(t), 'b-',
     legend=['numerical', 'exact'],
     title='dt=%g' % dt)

raw_input()


"""
[emilyd@sudur App_E]$ python simple_ODE_class.py

"""