from math import pi, log
#in the math module, the natural logarithm is named
#log, while 10-logarithm is named log10


def egg(M,To=20,Ty=70):
    c = 3.7      #specific heat capacity (J*g**(-1)*K**(-1))
    K = 5.4e-3   #thermal conductivity (W*cm**(-1)*K**(-1)
    rho = 1.038  #density (g*cm**(-3))
    Tw = 100.0   #Water temperature (C)

    time = ((M**(2.0/3.0)*c*rho**(1.0/3.0))/(K*pi**2*(4*pi/3)**(2.0/3.0))) \
        *log(0.76*(To-Tw)/(Ty-Tw))

    return time



#use lists to hold the different values
M = [47,67]
T0 = [4,25]
TT = [63,70]

#for loop over all possible combinations
for m in M:
    for ty in TT:
        for to in T0:
            time = egg(m,To=to,Ty=ty)
            print "An egg with mass %g and initial temperature %g, has core temperature %g degrees after %d minutes and %d seconds" %(m,to,ty,int(time/60),time%60)

"""        
Terminal> python egg_func.py 
An egg with mass 47 and initial temperature 4, has core temperature 63 degrees after 3 minutes and 59 seconds
An egg with mass 47 and initial temperature 25, has core temperature 63 degrees after 2 minutes and 32 seconds
An egg with mass 47 and initial temperature 4, has core temperature 70 degrees after 5 minutes and 13 seconds
An egg with mass 47 and initial temperature 25, has core temperature 70 degrees after 3 minutes and 46 seconds
An egg with mass 67 and initial temperature 4, has core temperature 63 degrees after 5 minutes and 2 seconds
An egg with mass 67 and initial temperature 25, has core temperature 63 degrees after 3 minutes and 12 seconds
An egg with mass 67 and initial temperature 4, has core temperature 70 degrees after 6 minutes and 36 seconds
An egg with mass 67 and initial temperature 25, has core temperature 70 degrees after 4 minutes and 46 seconds
"""
