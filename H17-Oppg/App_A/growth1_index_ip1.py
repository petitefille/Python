from scitools.std import *
x0 = 100 	# initial amount
p = 5 		# interest rate
N = 4		# number of years
index_set = range(N+1)
x = zeros(len(index_set))

# Compute Solution
x[0] = x0
for i in index_set[0:-1]:
	x[i+1] = x[i] + (p/100.0)*x[i]
print x
plot(index_set, x, 'ro', xlabel='years', ylabel='amount')
raw_input('Press Enter to quit: ')

"""
[emilyd@sudur App_A]$ python growth1_index_ip1.py
[ 100.        105.        110.25      115.7625    121.550625]
Press Enter to quit:
"""