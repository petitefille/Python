import numpy as np
import ODESolver
class ProblemSIR:
   def __init__(self, nu, beta, S0, I0, R0, T):
      """
      nu , beta = parameters in the ODE system
      S0, I0, R0 = initial values
      T: simulation for t in [0, T]
      """
      if isinstance(nu, float, int)): # number?
         self.nu = lambda t: nu # wrap as function
      elif callable(nu):
         self.nu
      if isinstance(beta, float, int)):
         self.beta = lambda t: beta
      elif callable(beta):
         self.beta
     self.S0, self.I0, self.R0, self.T = S0, I0, R0, T
   
   def __call__(self, u, t):
      """Right-hand side function of the ODE system."""
      S, I, R = u
      return [-self.beta(t)*S*I, self.beta(t)*S*i - self.nu(t)*I, -self.nu(t)*I]

# Example:
problem = ProblemSIR(beta=lambda t: 0.0005 if t <= 12 else 0.0001, nu=0.1, S0=1500, I0=1, R0=0, T=60)
solver = ODESolver.ForwardEuler(problem)


