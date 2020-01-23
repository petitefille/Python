import sys
try:
    filename = sys.argv[1]
except IndexError:
    print 'Usage: %s filename' % sys.argv[0]
    sys.exit(1)

infile = open(filename, 'r')
# Read the first four (useless) lines
for i in range(4):
    infile.readline()

temp = []; density = []  # to be filled with file data
for line in infile:
    words = line.split()
    temp.append(float(words[0]))
    density.append(float(words[1]))

    # alternative:
    #t, d = [float(word) for words in line.split()]
    #temp.append(t);  density.append(d)

infile.close()
from scitools.std import *
plot(temp, density, 'ro2')  # not strictly necessary to convert to arrays
legend('data')

# fit a 1st degree polynomial to the data:
degree = 1
coeff = polyfit(temp, density, degree)
density_poly_1st = poly1d(coeff)  # also from numpy
print density_poly_1st
hold('on')
density_fit1 = density_poly_1st(temp)
plot(temp, density_fit1)
legend('%d degree polynomial fit' % degree)

# fit a 2nd degree polynomial to the data:
degree = 2
coeff = polyfit(temp, density, degree)
density_poly_2nd = poly1d(coeff)  # also from numpy
print density_poly_1st
hold('on')
density_fit2 = density_poly_2nd(temp)
plot(temp, density_fit2)
legend('%d degree polynomial fit' % degree)
