# A.14 (sin_Taylor_series_diffeq.py, side 633)
"""
a[j] = - x**2 / ((2*j+1)*2*j) * a[j-1]
s[j] = s[j-1] + a[j-1]
"""

import numpy as np

def sin_Taylor(x, n):
    a = np.zeros(n+2)
    s = np.zeros(n+2)

    a[0] = x

    for j in range(1, n+2):
        a[j] = - x**2 / ((2*j+1)*2*j) * a[j-1]
        s[j] = s[j-1] + a[j-1]

    return s[-1], abs(a[-1])

def test_sin():
    
    x = 3*np.pi/2
    by_hand = x - x**3 / 6 + x**5 / 120
    computed = sin_Taylor(x, 2)
    difference = abs(by_hand - computed[0])
    assert difference < 1E-15

x_values = [np.pi, 25*np.pi/6, 10*np.pi]
n_values = [1, 3, 6, 10, 100]

for x in x_values:
    for n in n_values:
        print '%10f %10d %20f %20f' % (x, n, sin_Taylor(x, n)[0], np.sin(x))
		
"""

[emilyd@vestur App_A]$ python sin_Taylor_series_diffeq.py
  3.141593          1            -2.026120             0.000000
  3.141593          3            -0.075221             0.000000
  3.141593          6             0.000021             0.000000
  3.141593         10             0.000000             0.000000
  3.141593        100             0.000000             0.000000
 13.089969          1          -360.731846             0.500000
 13.089969          3        -10223.980492             0.500000
 13.089969          6         25635.745903             0.500000
 13.089969         10          1461.220764             0.500000
 13.089969        100             0.500000             0.500000
 31.415927          1         -5136.296854            -0.000000
 31.415927          3      -5742765.186074            -0.000000
 31.415927          6    4002388084.529744            -0.000000
 31.415927         10  371389750939.568665            -0.000000
 31.415927        100            -0.000305            -0.000000

"""