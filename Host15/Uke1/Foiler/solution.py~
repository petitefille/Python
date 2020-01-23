g = 9.81   # m/s**2
v0 = 15   # km/h
theta = 60   # degrees
x = 0.5   # m
y0 = 1   # m

print """v0 = %1.f km/h
theta = %d degrees
y0 = %1.f m
x = %1.f m""" % (v0, theta, y0, x)

# convert v0 to m/s and theta to radians   
v0 = v0/3.6
from math import pi, tan, cos
theta = theta*pi/180

y = x*tan(theta) - 1/(2*v0)*g*x**2/((cos(theta))**2) + y0

print'y = %.1f m' % y


