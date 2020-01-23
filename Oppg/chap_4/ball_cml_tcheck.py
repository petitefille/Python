# 4.12

"""

ball_cml_tcheck.py
Her har du gjort det litt vanskeligere enn nødvendig. 
Testfunksjoner er vanligvis for å sjekke at programmet 
gjør det det skal. Det vi skulle her var å sjekke om brukeren av 
programmet gjør det den skal. Det hadde altså holdt med

import sys

t, v0 = map(float, sys.argv[1:])

if not 0 < t < 2*v0/9.81:
    sys.exit('Invalid t value.')

print v0*t - 4.905*t**2

"""

import sys

def y(t, v0):
    y =v0*t-0.5*g*t**2 
    return y   
 
t_str = sys.argv[1]
t_float = float(t_str)
v0_str = sys.argv[2]
v0_float = float(v0_str)

g = 9.81
b = (2*(v0_float))/g

def test_y():
    t_float = float(t_str)
    v0_float = float(v0_str)
    g = 9.81
    b = (2*(v0_float))/g 
    a = 0
    success = a < t_float < b 
    msg_if_failure = 'the value of t needs to be an element of the interval (0,(2*v0)/g)) = (0, %.2f)' % (b)
    assert success, msg_if_failure 

test_y()

print "When t = %.2f and t lies in the open interval (0,(2*v0)/g)) = (0, %.2f), while v0 = %.2f, y = %.4f." % (t_float, v0_float, b, y(t_float, v0_float))

"""
Terminal> python ball_cml_tcheck.py 3 0.60
Traceback (most recent call last):
  File "ball_cml_tcheck.py", line 26, in <module>
    test_y()
  File "ball_cml_tcheck.py", line 24, in test_y
    assert success, msg_if_failure 
AssertionError: the value of t needs to be an element of the interval (0,(2*v0)/g)) = (0, 0.12)
Terminal> python ball_tcml_check.py 0.60 3
When t = 0.60 and t lies in the open interval (0,(2*v0)/g)) = (0, 3.00), while v0 = 0.61, y = 0.0342.
"""
