import numpy as np
import matplotlib.pyplot as plt

def RungeKutta2( f, x0, t ):
   n = len( t )
   x = np.array( [ x0 ] * n )
   for i in xrange( n -1 ): 
       h = t[i+1] - t[i]
       k1 = h*f( t[i], x[i]) 
       k2 = h*f( t[i] + 0.5*h, x[i] + 0.5*k1)
       x[i+1] = x[i] + k2
   return x




def f(t, x):
   return 1./(2*(x-1))
   
x0 = 1 + np.sqrt(0.001)

t = np.linspace(0, 4,101)
x = RungeKutta2(f, x0, t)
plt.plot(t, x,'b-')
plt.hold('on')
t = np.linspace(0,4,501)
x = RungeKutta2(f, x0, t)
plt.plot(t, x,'r-')
plt.hold('on')
t = np.linspace(0,4,1001)
x = RungeKutta2(f, x0, t)
plt.plot(t, x,'g-')
plt.hold('on')
t = np.linspace(0,4,5001)
x = RungeKutta2(f, x0, t)
plt.plot(t, x,'y-')
plt.hold('on')
t = np.linspace(0,4,10001)
x = RungeKutta2(f, x0, t)
plt.plot(t, x,'m-')
plt.hold('on')
t = np.linspace(0,4,10001)
x = RungeKutta2(f, x0, t)
plt.plot(t, x,'c-')
plt.hold('on')
t = np.linspace(0,4,12289)
def f(t):
   return 1 + np.sqrt(t + 0.001)
y = f(t) 
plt.plot(t, y, 'k-')
plt.hold('on')
plt.title('Numerical solutions (in colors) and exact solution (in black)')
plt.xlabel('t')
plt.ylabel('x')
plt.show()


   
