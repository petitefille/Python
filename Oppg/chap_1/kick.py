"""
Bra! Men (v1*(10.**3.))/3600 er vel det samme som v1/3.6? 
Og import-linja bør alltid være først i programmet, kun etter 
kommentaren som forteller hva programmet gjør. Til slutt: Bruk gjerne 
litt mer beskrivende variabelnavn enn y1, y2, y3, y4, y5.
"""

# program that computes the drag force and the gravity force on a football


cd = 0.2   # the drag coefficient
rho = 1.2   # the density of air in kg/m*3
a = 11   # the radius of the football in cm 
m = 0.43   # the mass of the football in kg
g = 9.81   # the gravitational acceleration in m/s**2
v1 = 120.   # the velocity of the football for a hard kick in km/h
v2 = 10.   # the velocity of the ball for a soft kick in km/h

#convert a to m and v1 and v2 to m/s

a = a*(10**(-2))
v1 = (v1*(10.**3.))/3600
v2 = (v2*(10.**3.))/3600

from math import pi

y1 = 0.5*cd*rho*(pi*(a**2))*(v1**2)  # the drag force on the ball for a hard kick with one decimal in Newton
y2 = 0.5*cd*rho*(pi*(a**2))*(v2**2)    # the drag force on the ball for a soft kick with one decimal in Newton
y3 = m*g   # the gravity force on the football in Newton
y4 = y1/y3   # the ratio of the drag force and the gravity force on the ball when kicked hard
y5 = y2/y3   # the ratio of the drag force and the gravity force on the ball when kicked softly

print """
The drag force on a footbal when kicked hard is %.1f N and the drag force\non the football when kicked softly is %.1f N. The gravity force on the\nfootball is %.1f N. The ratio of the drag force and the gravity force on\nthe football when kicked hard is %.1f and the ratio of the drag force and\nthe gravity on the ball when kicked softly is %.1f.
""" % (y1, y2, y3, y4, y5)

"""
Terminal> python kick.py

The drag force on a footbal when kicked hard is 5.1 N and the drag force
on the football when kicked softly is 0.0 N. The gravity force on the
football is 4.2 N. The ratio of the drag force and the gravity force on
the football when kicked hard is 1.2 and the ratio of the drag force and
the gravity on the ball when kicked softly is 0.0.
"""





