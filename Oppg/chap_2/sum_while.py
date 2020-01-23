# 2.10
"""
The wrong program:

s = 0; k = 1; M = 100
while k < M:
    s += 1/k
print s

The correct program:
"""

s = 0; k = 1; M = 100
while k <= 100:
   s += 1.0/k
   k += 1 
print s 
 
""" 
Terminal> sum_while.py
5.18737751764 
"""
"""
The three errors are: 

_ k < M vs. k <= M:
If k = 1 is less than M = 100 and does not include M = 100, the sum of 1/k that will be calculated will only involve the upper limit of M = 99, and not M = 100. 

_ It is important to write 1.0/k, implying a float object and therefore float division. 

_Third, the program needs to specify k = k + 1. This is because if not, k will not change and will remain equal to one. This is not the goal of this task, which is to calculate the sum of 1/k from the lower limit of k = 1 to the upper limit of M = 100.
"""





