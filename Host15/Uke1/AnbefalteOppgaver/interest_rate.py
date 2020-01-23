p = 5.0/100 # a bank's interest rate in percent per year
A = 1000 # an inial amount in euros
n = 3 # years
G = A*((1 + p/100)**n) # the growth of money in bank
print 'An initial amount of 1000 euros has grown to %.2f after three years with 5 percent interest rate.' % (G)

"""
Terminal> python interest_rate.py
An initial amount of 1000 euros has grown to 1001.50 after three years with 5 percent interest rate.
"""
