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
    if words[0] == "#":
        break
    temp.append(float(words[0]))
    density.append(float(words[1]))

    # alternative:
    #t, d = [float(word) for words in line.split()]
    #temp.append(t);  density.append(d)

infile.close()
from scitools.std import *
plot(temp, density, 'ro2')  # not strictly necessary to convert to arrays
legend('data')

raw_input('Press <CR>')