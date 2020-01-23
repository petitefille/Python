import numpy as np
import ODESolver
from matplotlib.pyplot import plot, figure, savefig, title, show, legend, xlabel, ylabel
class ProblemSIR:
   def __init__(self, nu, beta, S0, I0, R0, T):
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
      self.S0, self.I0, self.R0, self.T = S0, I0, R0, T
   
   def __call__(self, u, t):
      """Right-hand side function of the ODE system."""
      S, I, R = u
      return [-self.beta(t)*S*I, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I]

# Example


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
      

   def plot(self):
      filename = 'SIR_class_' + str(self.problem) + '.pdf'
      plot(self.t, self.S)
      plot(self.t, self.I)
      plot(self.t, self.R)
      legend(["S(t)","I(t)","R(t)"])
      xlabel('t (Days)')
      ylabel('Population')
      savefig(filename)
      show()

   def find_max_I(self):
      max_I = max(self.I)
      return max_I
      
      # plot S(t), I(t), and R(t)
                              
problem = ProblemSIR(nu=0.1,beta=lambda t: 0.0005 if t <=12 else 0.0001,S0=1500, I0=1, R0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot()
# solution = SolverSIR(problem, dt=0.5)
I_max_1 = solvesir.find_max_I()
print 'The maximum number of infected people when B(t) = 0.0005 if 0 <= t <= 12 and B(t) = 0.0001 if t > 12 is %d.' % (I_max_1)
#I.max() # Hvis du har satt I til array over infected

problem = ProblemSIR(nu=0.1,beta=0.0005,S0=1500, I0=1, R0=0, T=60)
solvesir = SolverSIR(problem,dt=0.5)
solvesir.solve(method=ODESolver.RungeKutta4)
solvesir.plot()
# solution = SolverSIR(problem, dt=0.5)
I_max_2 = solvesir.find_max_I()
print 'The maximum number of infected people when B(t) = 0.0005 is %d. % (I_max_2)

# hvordan skrive tittel slik at jeg kan informere hva beta er





