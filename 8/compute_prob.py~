import random

def compute_prob(N):
   M = 0
   for i in xrange(N):
      outcome = random.random()
      if 0.5 < outcome < 0.6:
         M += 1
   return float(M)/N

i_1 = compute_prob(10**1)
print 'The probability of getting a number between\n \
0.5 and 0.6 when N = 10*1 is %.4f.' % (i_1)

i_2 = compute_prob(10**2)
print 'The probability of getting a number between\n \
0.5 and 0.6 when N = 10**2 is %.4f.' % (i_2)

i_3 = compute_prob(10**3)
print 'The probability of getting a number between\n \
0.5 and 0.6 when N = 10**3 is %.4f.' % (i_3)

i_6 = compute_prob(10**6)
print 'The probability of getting a number between\n \
0.5 and 0.6 when N = 10**6 is %.4f.' % (i_6)

"""
Terminal> python compute_prob.py
The probability of getting a number between
0.5 and 0.6 when N = 10*1 is 0.2000.
The probability of getting a number between
0.5 and 0.6 when N = 10**2 is 0.0500.
The probability of getting a number between
0.5 and 0.6 when N = 10**3 is 0.1070.
The probability of getting a number between
0.5 and 0.6 when N = 10**6 is 0.1001.
"""
