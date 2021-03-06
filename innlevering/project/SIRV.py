import numpy as np
import ODESolver
import matplotlib.pyplot as plt

class ProblemSIRV:
   def __init__(self, nu, beta, p, S0, I0, R0, V0, T):
      
      if isinstance(nu, (float, int)): 
         self.nu = lambda t: nu 
      elif callable(nu):
         self.nu = nu
      if isinstance(beta, (float, int)): 
         self.beta = lambda t: beta 
      elif callable(beta):
         self.beta = beta
      if isinstance(p, (float, int)): 
         self.p = lambda t: p 
      elif callable(p):
         self.p = p
      self.S0, self.I0, self.R0, self.V0, self.T = S0, I0, R0, V0, T
   
   def __call__(self, u, t):
      """Right-hand side function of the ODE system."""
      S, I, R , V = u
      return [-self.beta(t)*S*I - self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I, self.p(t)*S]




class SolverSIRV:
   def __init__(self,problem,dt):
      self.problem, self.dt = problem, dt

   def solve(self, method=ODESolver.RungeKutta4):
      self.solver = method(self.problem)
      ic = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]
      self.solver.set_initial_condition(ic)
      n = int(round(self.problem.T/float(self.dt)))
      t = np.linspace(0, self.problem.T, n+1)
      u,self.t = self.solver.solve(t)
      self.S, self.I, self.R, self.V = u[:,0], u[:,1], u[:,2], u[:,3]

      

   def plot(self, filename, title):
      self.filename, self.title = filename, title
      filename = 'SIRV_' + str(self.filename) + '.pdf'
      plt.plot(self.t, self.S)
      plt.hold('on')
      plt.plot(self.t, self.I)
      plt.hold('on')
      plt.plot(self.t, self.R)
      plt.hold('on')
      plt.plot(self.t, self.R)
      plt.hold('on')
      plt.legend(["S(t)","I(t)","R(t)", "V(t)"])
      plt.xlabel('t (Days)')
      plt.ylabel('Population')
      name = str(self.title)
      plt.title(name)
      plt.savefig(filename)
      plt.show()

   def find_max_I(self):
      max_I = max(self.I)
      return max_I
                              

problem = ProblemSIRV(nu=0.1,beta=0.0005,p=0.1,S0=1500, I0=1, R0=0,V0=0, T=60)
solvesir = SolverSIRV(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot('beta=0,0005','SIRV model when beta = 0.0005')
I_max_1 = solvesir.find_max_I()
print 'The maximum number of infected people when B(t) = 0.0005 and \n p = 0.1 is I(t) = %d.' % (I_max_1)

problem = ProblemSIRV(nu=0.1,beta=0.0001,p=0.1,S0=1500, I0=1, R0=0,V0=0, T=60)
solvesir = SolverSIRV(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot('beta=0,0001','SIRV model when beta = 0.0001')
I_max_1 = solvesir.find_max_I()
print 'The maximum number of infected people when B(t) = 0.0001 and \n p = 0.1 is I(t) = %d.' % (I_max_1)
print 'Therefore the effect of vaccination is a large reduction in infected people \n when beta = 0.0005, and an even greater reduction when beta = 0.0001.'

"""
Terminal> SIRV.py
The maximum number of infected people when B(t) = 0.0005 and 
 p = 0.1 is I(t) = 64.
The maximum number of infected people when B(t) = 0.0001 and 
 p = 0.1 is I(t) = 1.
Therefore the effect of vaccination is a large reduction in infected people 
 when beta = 0.0005, and an even greater reduction when beta = 0.0001.
"""
