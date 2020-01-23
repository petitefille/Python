import numpy as np
import ODESolver
import matplotlib.pyplot as plt
class ProblemSIR:
   def __init__(self, nu, beta, S0, I0, R0, T):
      """
      nu , beta = parameters in the ODE system
      S0, I0, R0 = initial values
      T: simulation for t in [0, T]
      """
      if isinstance(nu, (float, int)): 
         self.nu = lambda t: nu 
      elif callable(nu):
         self.nu = nu
      if isinstance(beta, (float, int)): 
         self.beta = lambda t: beta 
      elif callable(beta):
         self.beta = beta
      self.S0, self.I0, self.R0, self.T = S0, I0, R0, T
   
   def __call__(self, u, t):
      """Right-hand side function of the ODE system."""
      S, I, R = u
      return [-self.beta(t)*S*I, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I]




class SolverSIR:
   def __init__(self,problem,dt):
      self.problem, self.dt = problem, dt

   def solve(self, method=ODESolver.RungeKutta4):
      self.solver = method(self.problem)
      ic = [self.problem.S0, self.problem.I0, self.problem.R0]
      self.solver.set_initial_condition(ic)
      n = int(round(self.problem.T/float(self.dt)))
      t = np.linspace(0, self.problem.T, n+1)
      u,self.t = self.solver.solve(t)
      self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]
      

   def plot(self, filename, title):
      self.filename, self.title = filename, title
      filename = 'SIR_class_' + str(self.filename) + '.pdf'
      plt.plot(self.t, self.S)
      plt.hold('on')
      plt.plot(self.t, self.I)
      plt.hold('on')
      plt.plot(self.t, self.R)
      plt.hold('on')
      plt.legend(["S(t)","I(t)","R(t)"])
      plt.xlabel('t (Days)')
      plt.ylabel('Population')
      name = str(self.title)
      plt.title(name)
      plt.savefig(filename)
      plt.show()

   def find_max_I(self):
      max_I = max(self.I)
      return max_I
      
      
                              
problem = ProblemSIR(nu=0.1,beta=lambda t: 0.0005 if t <=12 else 0.0001,S0=1500, I0=1, R0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot('SIR_model_campaign','SIR Model after campaign')

I_max_1 = solvesir.find_max_I()
print 'The maximum number of infected people when B(t) = 0.0005 if 0 <= t <= 12 \n and B(t) = 0.0001 if t > 12 is I(t) = %d.' % (I_max_1)

problem = ProblemSIR(nu=0.1,beta=0.0005,S0=1500, I0=1, R0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot('SIR_model_beta=0,0005','SIR Model when beta = 0.0005')
I_max_2 = solvesir.find_max_I()
print 'The maximum number of infected people when B(t) = 0.0005 is I(t) = %d.' % (I_max_2)

"""
Terminal> python SIR_class.py
The maximum number of infected people when B(t) = 0.0005 if 0 <= t <= 12  and B(t) = 0.0001 if t > 12 is I(t) = 745.
The maximum number of infected people when B(t) = 0.0005 is I(t) = 897.
"""




