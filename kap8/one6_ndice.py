import sys 
n = int(sys.argv[1]) # number of dice 
N = int(sys.argv[2]) # number of experiments


import numpy as np
M = 0
r = np.random.randint(1, 7)


for i in xrange(N):
   for j in xrange(n):
      r= np.random.randint(1, 7)
      if r >= 6:
         M += 1
   
      
       
p = float(M)/N  

print 'probability:', p

"""
Terminal> python one6_ndice.py 2 10
probability: 0.3
Terminal> python one6_ndice.py 2 100
probability: 0.44
Terminal> python one6_ndice.py 2 1000
probability: 0.34
Terminal> python one6_ndice.py 2 10000
probability: 0.3311
Terminal> python one6_ndice.py 2 100000
probability: 0.33393
Terminal> python one6_ndice.py 2 1000000
probability: 0.333677
"""




