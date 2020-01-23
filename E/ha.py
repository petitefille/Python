import numpy as np
import matplotlib.pyplot as pl
import ODESolver

beta = 1.0/1000
gamma = 0.1
S0 = 1500
I0 = 1
R0 = 0
INPUT = (S0, I0, R0)
  
def f(u, t):
   Y = [[],[],[]]
   V = INP
   Y[0], Y[1], Y[2] = u
   return [beta*V[0]*V[1], beta*V[0]*V[1] - gamma*V[1], gamma*V[1]]


def diff_eqs(INP, t):
   Y = np.zeros(3)
   V = INP
   Y[0] = beta*V[0]*V[1]
   Y[1] = beta*V[0]*V[1] - gamma*V[1]
   Y[2] = gamma*V[1]
   return Y




INP = np.array([S0, I0, R0])  
n = int(round(60/0.5))
t = np.linspace(0, 60, n+1)
RES = ODESolver.RungeKutta4(f)
RES.set_initial_condition(INPUT)

RES_S = [RES[0] for i in range(len(t))] 
# RES_I = [[T[i],RES[i][1]] for k in range(len(T))]
# RES_R = [[T[i],RES[i][2]] for k in range(len(T))]

"""
#Ploting
pl.subplot(211)
pl.plot(RES[:,0], '-g', label='Susceptibles')
pl.plot(RES[:,2], '-k', label='Recovereds')
pl.legend(loc=0)
pl.title('Program_2_1.py')
pl.xlabel('Time')
pl.ylabel('Susceptibles and Recovereds')
pl.subplot(212)
pl.plot(RES[:,1], '-r', label='Infectious')
pl.xlabel('Time')
pl.ylabel('Infectious')
pl.show()
"""

   
"""
# Constants in model
beta =1.0/1000
gamma =1.0/(24*14)
def solving_SIR(beta,S0,I0,R0):
   gamma = 0.1
   n = int(round(60/0.5))
   def f(x, t):
      ifc = beta*x[0]*x[1]
      rec = gamma*x[1]
      return np.array([-ifc, ifc-rec, rec])

   time = np.linspace(0,60,n+1)
   xinit = np.array([S0, I0, R0])
   solver = ODESolver.RungeKutta4(f)
   solver.set_initial_condition(xinit)
   solver_S = [[time[i],solver[i][0]] for i in range(len(time))]   
   solver_I = [[time[i],solver[i][1]] for i in range(len(time))]
   solver_R = [[time[i],solver[i][2]] for i in range(len(time))]
   return solver_S, solver_I, solver_R

# n = int(round(60/0.5))
# solver_S, solver_I, solver_R = solving_SIR(0.0005, 1500, 1, 0)
# time = np.linspace(0,60,n+1)

def plot_SIR():
   n = int(round(60/0.5))
   x = solving_SIR(0.0005, 1500, 1, 0)
   time = np.linspace(0,60,n+1)
   plt.figure()
   plt.plot(time, x[:,0])
   plt.plot(time, x[:,1])
   plt.plot(time, x[:,2])
   plt.legend(["S(t)","I(t)","R(t)"])
   plt.xlabel('t (Hours)')
   plt.ylabel('Population')
   plt.show()

# draw = plot_SIR()
"""
"""
def test():
   S0 =
   I0 =
   R0 =
   value0 = S0 + I0 + R0
   tol = 
   
   for i in x[:,0], x[:,1], x[:,2]:
      value_test = x[:,0] +  x[:,1] + x[:,2]
"""


      
      
   

