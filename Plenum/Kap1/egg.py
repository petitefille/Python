from math import pi, log
#in the math module, the natural logarithm is named
#log, while 10-logarithm is named log10

#properties of the egg
M = 67       #mass (g)
c = 3.7      #specific heat capacity (J*g**(-1)*K**(-1))
K = 5.4e-3   #thermal conductivity (W*cm**(-1)*K**(-1)
rho = 1.038  #density (g*cm**(-3))

Tw = 100.0   #Water temperature (C)
To = 20.0    #Initial egg temperature (C)
Ty = 70.0    #Target center temperature (C)

time = ((M**(2.0/3.0)*c*rho**(1.0/3.0))/(K*pi**2*(4*pi/3)**(2.0/3.0))) \
    *log(0.76*(To-Tw)/(Ty-Tw)) 

print "Boil time = %g minutes and %g seconds" %(int(time/60), int(time%60))

"""
Terminal> python egg.py
Boil time = 5 minutes and 15 seconds
"""
