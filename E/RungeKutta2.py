from ODESolver import *
import numpy as np
import matplotlib.pylab as plt





class RungeKutta2(ODESolver):
   def advance(self):
      u, f, k, t = self.u, self.f, self.k, self.t
      dt = t[k+1]-t[k]
      dt2= dt/2.0
      K1 = dt*f(u[k], t[k])
      K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
      u_new = u[k] + K2
      return u_new

if __name__ == '__main__':

   def f(u, t):
      return a + (u - u_exact(t))**5

   def u_exact(t):
      """Exact u(t) corresponds to f above."""
      return a*t + b
   plt.figure()
   a = 0.2; b = 3
   solver = RungeKutta2(f)
   solver.set_initial_condition(3.0)
   T = 8
   n = 10
   t_points = np.linspace(0, T, n)
   u, t = solver.solve(t_points)
   plt.plot(t, u)
   plt.legend('numerical')
   plt.hold('on')
   y = u_exact(t)
   plt.plot(t_points, y,'r-')
   plt.legend('analytical')
   plt.savefig('tmp_rk2.eps')
   plt.show()




registered_solver_classes = [RungeKutta2]


def test_exact_numerical_solution():
   a = 0.2; b = 3
   
   def f(u, t):
      return a + (u - u_exact(t))**5
   
   def u_exact(t):
      """Exact u(t) corresponds to f above."""
      return a*t + b

   U0 = u_exact(0)
   T = 8
   n = 10
   tol = 1E-15
   t_points = np.linspace(0, T, n)
   for solver_class in registered_solver_classes:
      solver = solver_class(f)
      solver.set_initial_condition(U0)
      u, t = solver.solve(t_points)
      u_e = u_exact(t)
      max_error = (u_e - u).max()
      msg = '%s failed with max_error = %g' % \
             (solver.__class__.__name__, max_error)
      assert max_error < tol, msg
   
