import numpy as np
import ODESolver
from matplotlib.pyplot import plot, figure, savefig, title, show, legend, xlabel, ylabel
class ProblemSIR:
   def __init__(self, nu, beta, p, S0, I0, R0, V0, T):
      """
      nu , beta = parameters in the ODE system
      S0, I0, R0 = initial values
      T: simulation for t in [0, T]
      """
      if isinstance(nu, (float, int)): # number?
         self.nu = lambda t: nu # wrap as function
      elif callable(nu):
         self.nu = nu
      if isinstance(beta, (float, int)): # number?
         self.beta = lambda t: beta # wrap as function
      elif callable(beta):
         self.beta = beta
      if isinstance(p, (float, int)): # number?
         self.p = lambda t: p # wrap as function
      elif callable(p):
         self.p = p
      self.S0, self.I0, self.R0, self.V0, self.T = S0, I0, R0, T, V0
   
   def __call__(self, u, t):
      """Right-hand side function of the ODE system."""
      S, I, R , V = u
      return [-self.beta(t)*S*I - self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I, self.p(t)*S]

# Example


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
      

   def plot(self):
      filename = 'SIR_class_' + str(self.problem) + '.pdf'
      plot(self.t, self.S)
      plot(self.t, self.I)
      plot(self.t, self.R)
      plot(self.t, self.V
      legend(["S(t)","I(t)","R(t)", "V(t)"])
      xlabel('t (Days)')
      ylabel('Population')
      savefig(filename)
      show()

  
      
      # plot S(t), I(t), and R(t)
(self, nu, beta, p, S0, I0, R0, V0, T):
                              

problem = ProblemSIR(nu=0.1,beta=0.0005,p=0.1,S0=1500, I0=1, R0=0,V0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot()

problem = ProblemSIR(nu=0.1,beta=0.0001,p=0.1,S0=1500, I0=1, R0=0,V0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot()






