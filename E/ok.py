import numpy as np
from scitools.std import *
S0 = 1500
I0 = 1
R0 = 0

beta = [0.0005, 0.0001]
gamma = 0.1
dt = 0.5
tmin = 0
tmax = 60

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

#def diff_eqs(INP, t):
#   Y = np.zeros(3)
#   V = INP
#   Y[0] = beta*V[0]*V[1]
#   Y[1] = beta*V[0]*V[1] - gamma*V[1]
#   Y[2] = gamma*V[1]


   
   u, t = ForwardEuler(f,dt,U0,tmax)
   return u, t



def graph_SIR_model(u,t):
   filename = 'SIR_' + str(self.problem) + '.pdf'
   p0 = u[:,0]
   p1 = u[:,1]
   p2 = u[:,2]
   plot(t,p0)
   hold('on')
   plot(t,p1)
   hold('on')
   plot(t,p2)
   hold('on')
   legend(["S(t)","I(t)","R(t)"])
   xlabel('t (Days)')
   ylabel('Population')
   savefig(filename)
   show()

beta = [0.0005, 0.0001]

for el in beta:
   u, t = SIR_model(1500, 1,0,beta,0.1,0.5,0,60)
   task = graph_SIR_model(u, t)

   u, t = SIR_model(1500, 1,0,beta,0.1,0.5,0,60)
   task = graph_SIR_model(u, t)



def test():
   S0 = 1500
   I0 = 1
   R0 = 0
   value0 = S0 + I0 + R0
   U0 =[1500,1,0]
   T = 60 
   dt = 0.5
   u, t = ForwardEuler(f,dt,U0,T)
   p0 = u[:,0]
   p1 = u[:,1]
   p2 = u[:,2]
   tol = 1
   for p0i, p1i, p2i in zip(p0, p1, p2):
      p = p0i + p1i + p2i
      success = abs(p - value0) < abs
   msg = 'When S = %, I = %, R = % and S0 = %, I0 = % and R0 = %, the sum of these values (S[i]+ I[i] + R[i] != S0 + I0 + R0' % (p0i, p1i, p2i, S0, I0, R0)
   assert success, msg    



