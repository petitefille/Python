import numpy as np
import matplotlib.pyplot as plt

def SIR_model(S0, I0, R0,beta,gamma,dt,tmin,tmax):
   U0 =[S0,I0,R0]
   def ForwardEuler(f_user, dt, U0,tmax):
      n = int(round(tmax/dt))
      t = np.zeros(n+1)
      f = lambda u, t: np.asarray(f_user(u, t))
      if isinstance(U0,(float, int)):
         u = np.zeros(n+1)
      else:
         U0 = np.asarray(U0)
         neq = U0.size
         u = np.zeros((n+1, neq))
      u[0] = U0
      t[0] = tmin
      for k in range(n):
         t[k+1] = t[k] + dt
         u[k+1] = u[k] + dt*f(u[k], t[k])
      return u, t

   def f(u,t):
      ifc = beta*u[0]*u[1]
      rec = gamma*u[1]
      return np.array([-ifc ,ifc-rec ,rec])

  
   u, t = ForwardEuler(f,dt,U0,tmax)
   return u, t



def graph_SIR_model(u,t,filename, title_of_graph):
   p0 = u[:,0]
   p1 = u[:,1]
   p2 = u[:,2]
   plt.plot(t,p0)
   plt. hold('on')
   plt.plot(t,p1)
   plt.hold('on')
   plt.plot(t,p2)
   plt.hold('on')
   plt.legend(["S(t)","I(t)","R(t)"])
   plt.xlabel('t (Days)')
   plt.ylabel('Population')
   plt.title(title_of_graph) 
   plt.savefig(filename)
   plt.show()

beta = [0.0005, 0.0001]


u, t = SIR_model(1500, 1,0,beta[0],0.1,0.5,0,60)
task = graph_SIR_model(u, t,'beta=0,0005','SIR Model when beta = 0.0005')

u, t = SIR_model(1500, 1,0,beta[1],0.1,0.5,0,60)
task = graph_SIR_model(u, t, 'beta=0,0001', 'SIR model when beta = 0.0001')

"""
A reduction in beta influences S(t) as the number of people who can get the disease starts at approximately the same size as the population, and then remains within that size until 60 days have passed.
When beta = 0.0005, the number of people who can get the disease starts  very high and almost equals the size of the population. But as time increases from ten to twenty days, S(t) decreases rapidly. When 25 days have passed, the number of people who can get the disease is reduced to approximatly 0, and remains within that size until 60 days have passed.
Therefore it is possible to conclude that reducing beta will affect S(t) as the number of people who can get the disease will remain very high over time. However, the number of people who have developed the disease and who have recovered from the disease and become immune remains extremely low. After half the time has passed after the disease has broken out, I(t) and R(t) increase by a very small amount that is almost unsignificant. However, When beta is greater in size and equals to 0.0005,I(t) and R(t) change significantly. I(t) increases rapidly to approximately half of the population over one third of the time, and then sinks until it reaches approximately none of the size of the population at the end of the time that has evolved. R(t) starts at size 0 of the population but then rapidly increases and reaches almost the entire size of the population when 100% of the time has evolved.  
"""



def test_SIR():
   S0 = 1500
   I0 = 1
   R0 = 0
   value0 = S0 + I0 + R0
   u, t = SIR_model(1500, 1,0,0.0005,0.1,0.5,0,60)
   p0 = u[:,0] 
   p1 = u[:,1]
   p2 = u[:,2]
   tol = 1
   for p0i, p1i, p2i in zip(p0, p1, p2):
      p = p0i + p1i + p2i
      success = abs(p - value0) < abs
   msg = 'S[i]+ I[i] + R[i] != S0 + I0 + R0' 
   assert success, msg  

  

"""
Terminal> nosetests SIR.py
------------------------------------------------------
Ran 1 test in 0.009s
OK

"""


