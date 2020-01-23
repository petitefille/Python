import numpy
import sys
N = int(sys.argv[1])

r = numpy.random.random(N)
num_tails = numpy.sum(numpy.where(r <= 0.5, 0, 1))
print num_tails

"""

[emilyd@vestur kap8]$ python flip_coin_vec.py 1000
496

"""