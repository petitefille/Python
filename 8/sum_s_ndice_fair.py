import sys
n = int(sys.argv[1]) # number of dice
N = int(sys.argv[2]) # number of experiments

import numpy as np

M = 0
v = np.zeros(n)

for i in xrange(N):
   for j in xrange(n):
      v[j] = np.random.randint(1, 7)
   y = np.sum(v)
   if y < 9:
      M += 1

p = float(M)/N
print 'probability:', p

"""
Terminal>  python sum_s_ndice_fair.py 4 100000
probability: 0.05375
(Note: r = q/p = 1./0.05375)
Terminal> python sum_4dice.py 10000 18.60465116
Net profit per game in the long run: 0.002790697524
Terminal> python sum_4dice.py 1000000 18.60465116
Net profit per game in the long run: 0.000204651012757
"""
