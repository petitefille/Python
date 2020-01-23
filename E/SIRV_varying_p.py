import numpy as np
import ODESolver
import matplotlib.pyplot as plt

class ProblemSIR:
   def __init__(self, nu, beta, p, S0, I0, R0, V0, T):
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
      if isinstance(p, (float, int)): 
         self.p = lambda t: p 
      elif callable(p):
         self.p = p
      self.S0, self.I0, self.R0, self.V0, self.T = S0, I0, R0, V0, T
   
   def __call__(self, u, t):
      """Right-hand side function of the ODE system."""
      S, I, R , V = u
      return [-self.beta(t)*S*I - self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I, self.p(t)*S]




class SolverSIR:
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
      filename = 'SIRV_varying_p_' + str(self.filename) + '.pdf'
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

  
      
      

                              

problem = ProblemSIR(nu=0.1,beta=0.0005,p=lambda t: 0.1 if 6 <= t <= 15 else 0 ,S0=1500, I0=1, R0=0,V0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot('beta=0,0005','SIRV model with varying p and beta = 0.0005')

problem = ProblemSIR(nu=0.1,beta=0.0001,p=lambda t: 0.1 if 6 <= t <= 15 else 0 ,S0=1500, I0=1, R0=0,V0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot('beta=0,0001','SIRV model with varying p and beta = 0.0001')






