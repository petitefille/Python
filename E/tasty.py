
from scitools.std import plot, figure
import numpy as np

class Problem:
   def __init__(self, Ts, T0, dt):
      self.Ts, self.T0, self.dt = Ts, T0, dt
      
      
      # class Problem containing the parameters h, Ts, T0, dt as attributes
      


   def estimate_h(self, t1, T1):  
      # estimate_h should take t1 and T(t1) as arguments, compute h, and assign it to self.h
      h = float(T1 - self.T0)/(t1*(self.Ts - self.T0))
      self.h = h     

      

   

   def __call__(self):
      def f(T, t):
         return -self.h*(T-self.Ts)
      def terminate(T, t, step_no):
    # Most recently computed T value: T[step_no]
         if abs(T[step_no] - self.Ts) < 1:
            return True  # terminate time loop
         else:
            return False
      
      import ODESolver
      solver = ODESolver.RungeKutta4(f)
      solver.set_initial_condition(self.T0)
      import numpy as np
      n = int(round((60*60)/self.dt))
      time_points = np.linspace(0, 60*60, n+1)
      T, t = solver.solve(time_points, terminate)
      return T, t
      # from matplotlib.pyplot import plot, show
      # plot(t, T)
      # show()
      
 # the right hand side of the ODE can be implemented in a __call__ method. 
# If you use a class from the ODESolver hierarchy to solve the ODE, include
#  the terminate function as a method in class Problem

   

  

 
# problem = Problem(Ts=20, T0=200)
# problem.estimate_h(50, 180)
# problem()
# 00000000000
# 370370370352
# 8046029568660
# 0178370380423



def test_against_hand_calculations():
   
  
   problem = Problem(Ts=20, T0=200, dt=1200)
   problem.estimate_h(50, 180)
   T, t = problem()
   exact = np.array([200.000000000000000, 170.370370370370352, 145.618046029568660, 124.940178370380423])
   error = np.abs(exact -T).max()
   assert error < 1E-14, 'exact-u = %g != 0' % error

"""
What are the advantages and disadvantages with class Problem compared to using plain functions (in your view)?
"""

def solve(problem):
   def f(T, t):
         return -self.h*(T-self.Ts)
   def terminate(T, t, step_no):
    # Most recently computed T value: T[step_no]
      if abs(T[step_no] - self.Ts) < 1:
         return True  # terminate time loop
      else:
         return False
      
   import ODESolver
   solver = ODESolver.RungeKutta4(f)
   solver.set_initial_condition(self.T0)
   import numpy as np
   n = int(round((60*60)/self.dt))
   time_points = np.linspace(0, 60*60, n+1)
   T, t = solver.solve(time_points, terminate)
   from matplotlib.pyplot import plot, show
   plot(t, T)
   show()  

problems = {T0: [Problem(Ts, T0, dt=1001)
                  for Ts in 15, 22, 30] for T0 in [250, 200]}

problems.estimate_h(50, 180)

for T0 in problems:
   hold('off')
   for problem in problems[T0]:
      solve(problem)
      hold('on')
   savefig('T0_%g'.pdf % T0)


   


   
