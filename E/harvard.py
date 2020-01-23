import numpy as np
import matplotlib.pyplot as plt
# from scipy.integrate import odeint
# Constants in model
import ODESolver
beta =1.0/1000
gamma =1.0/(24*14)

# Function to calculate derivatives of S(t), I(t), and R(t)
def f(u,t):
   ifc = beta*u[0]*u[1]
   rec = gamma*u[1]
   return np.array([-ifc ,ifc-rec ,rec])
# Solve ODE using the " odeint " library in SciPy
# time =np.linspace(0,2000 ,1000)
uinit =np.array([100 ,1,0])
T = 60 
n = int(round(60/0.5))
u, t = ForwardEuler(f, xinit,T,n)
p0 = u[:,0]
#x= odeint(deriv ,xinit ,time)
# Plot the solutions
"""
plt.figure()
p0 = plt.plot(time ,x[:,0])
p1 = plt.plot(time ,x[:,1])
p2 = plt.plot(time ,x[:,2])
plt.legend([p0,p1,p2],["S(t)","I(t)","R(t)"])
plt.xlabel(’t ( Hours )’)
plt.ylabel(’Population’)
plt.show()
"""
