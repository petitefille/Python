from scitools.StringFunction import StringFunction
import sys
from numpy import *

formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
n = int(sys.argv[4])
filename = str(sys.argv[5])


x = linspace(a, b, n)
f = StringFunction(formula)
f.vectorize(globals())
y = f(x)

outfile = open(filename, 'w')
outfile.write('  x      f(x)  \n')
for xvalue, yvalue in zip(x, y):
    outfile.write('%5.3f %7.3f\n' % (xvalue, yvalue))
outfile.close()

"""
Terminal > python write_cml_function.py 'sin(x)' 0 2*pi 10 patience.dat
"""
