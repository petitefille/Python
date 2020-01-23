def rk4( f, x0, t ):
   n = len( t )
   x = np.array( [ x0 ] * n )
   for i in xrange( n -1 ): 
       h = t[i+1] - t[i]
       k1 = h*f( t[i], x[i]) 
       k2 = h*f( t[i] + 0.5*h, x[i] + 0.5*k1)
       k3 = h*f( t[i] + 0.5*h, x[i] + 0.5 * k2)
       k4 = h*f( t[i] + h, x[i] + k3)
       x[i+1] = x[i] + (1./6.)*k1 + (1./3.)*k2 + (1./3.)*k3 + (1./6.)*k4

   return x


import numpy as np
   
def f(t, x):
   return 1./(2*(x-1))
   
x0 = 1 + np.sqrt(0.001)
t = np.linspace(0,4,12289)
x_rk4 = rk4(f, x0, t)

def ForwardEuler(f, x0, t):
   n = len( t )
   x = np.array( [ x0 ] * n )
   for i in xrange( n -1 ):
      h = t[i+1] - t[i]
      x[i+1] = x[i] + h*f(t[i],x[i])
        
   return x

def f(t, x):
      return 1./(2*(x-1))

x0 = 1 + np.sqrt(0.001)
t = np.linspace(0,4,12289)
x_ForwardEuler = ForwardEuler(f, x0, t)
def f(t):
   return 1 + np.sqrt(t + 0.001)
y = f(t) 


import matplotlib.pyplot as plt
plt.plot(t,x_rk4, 'r-')
plt.hold('on')
plt.plot(t,x_ForwardEuler,'b-')
plt.hold('on')
plt.plot(t, y, 'k-') 
plt.legend(['4rth order Runge-Kutta method','Forward Euler scheme','y(x)'])
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparing ODE Methods')
plt.savefig('tmp4.pdf')
plt.show()

