from numpy import exp  # need vectorized exp now

def g(t):
    return exp(-a*t)
	
a = 2
import numpy as np
t = np.linspace(0, 5/float(a), 101)
g_curve, dg_curve = g(t)

# Plotting with matplotlib 

import matplotlib.pyplot as plt 
plt.plot(t, g_curve, t, dg_curve)
plt.xlabel('t')
plt.legend(['g', "g'"])
plt.savefig('plot.png')
plt.show()

# Alternative plotting with scitools
"""
from scitools.std import *
plot(t, g_curve, t_dg_curve,
	 xlabel='t', savefig='plot.png')
     legend=['g', "g'"],
"""