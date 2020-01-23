def egg(M, To=20, Ty=70):
    Tw = 100    # water temperature
    rho = 1.038 # density
    K = 5.4E-3  # thermal conductivity
    c = 3.7     # specific heat

    from math import log as ln, pi

    t = M**(2./3)*c*rho**(1./3)/(K*pi**2*(4*pi/3)**(2./3))*\
    ln(0.76*(To - Tw)/(Ty - Tw))
    return t

for Ty in [63, 70]:
   for M in [47, 67]:
       for To in [4, 25]:
           time = egg(M, To, Ty)
           print 'Ty=%2d, M=%2d To=%2d time=%.2f' % (Ty, M, To, time/60.)
		   
"""

Terminal> python egg_func.py
Ty=63, M=47 To= 4 time=3.99
Ty=63, M=47 To=25 time=2.54
Ty=63, M=67 To= 4 time=5.05
Ty=63, M=67 To=25 time=3.21
Ty=70, M=47 To= 4 time=5.22
Ty=70, M=47 To=25 time=3.77
Ty=70, M=67 To= 4 time=6.61
Ty=70, M=67 To=25 time=4.77

	"""