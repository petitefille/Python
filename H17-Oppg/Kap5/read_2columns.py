infile = open('xy.dat', 'r')
x = [];  y = []
for line in infile:
    words = line.split()
    x.append(float(words[0]))
    y.append(float(words[1]))
infile.close()
from scitools.std import *
x = array(x)
y = array(y)
plot(x, y)
print 'y min: %g, ymax: %g' % (y.min(), y.max())

raw_input('Press <CR>')