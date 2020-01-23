a = 2; b = 1; c = 2
from cmath import sqrt
q = b*b - 4 *a*c
q_sr = sqrt(q)
x1 = (-b + q_sr)/(2.0*a)
x2 = (-b - q_sr)/(2.0*a)
print x1, x2

"""
Terminal> python find_errors_roots.py
(-0.25+0.968245836552j) (-0.25-0.968245836552j)
"""
