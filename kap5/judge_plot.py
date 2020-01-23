import numpy as np
x = np.linspace(0, 2, 100000)
#y = x*(2 - x)
y = np.cos(18*np.pi*x)
#from scitools.std import *
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.savefig('tmp3.png')
plt.show()

