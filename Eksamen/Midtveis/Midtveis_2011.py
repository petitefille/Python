# Ex. 1:

# (a)

q = -0.17 
print '%.1f' % q 

# (b)

for i in range(-2, 6, 3):
    print i-1

# (c)

a = 11
b = 10/a + 1 
print b 

# (d)
A = [-1, 1, 5] + ['plot1.eps', "plot1.png"]
del A[1]
print A

# (e)

A = [-1, 9, 2, 5, 19, 21, 33]
print A[3:-2]

# (f)

integers = []
value = 0 
stop = 1
increment = 1
while value <= stop: 
    integers.append(value)
	value += increment 
for v in integers: 
    print v

# (g)

print [0.2*(i+1) for i in range(2)]

# (h)

from math import sqrt 

def f(x):
    return a*sqrt(x)

x = 6; a = -2
print '%g' % f(x + a)
	



# (i)

for i in range(2, 4):
    for j in range(i-1, i+2):
	    if i != j:
		    print i, j+1

# (j)

def func1(x, y):
    if x > 0:
	    print 'quadrant I or IV'
	if y > 0:
	    print 'quadrant I or II'

def func2(x, y):
    if x > 0:
	    print 'quadrant I or II' 
	elif y > 0: 
	    print 'quadrant II' 

		for x, y in (-1, 1), (1, 1):
		    func1(x, y)
			func2(x, y)
			
# Ex 2

from math import pi, log as ln

def egg(M, To=20, Ty=70):
    """
    Return the cooking time of an egg with mass
    M at temperature To. The target yolk temperature
    is Ty.
    """
    c = 3.7 # specific heat capacity
    rho = 1.038 # density
    K = 5.4E-03 # thermal conductivity
    Tw = 100 # boiling water temperature
    t = (M**(2.0/3)*c*rho**(1./3))/\
        (K*pi**2*(4*pi/3)**(2./3))*ln(0.76*\
        (To - Tw)/(Ty - Tw))
    return t
	
# Ex. 3
	
for M in [47, 57, 67]:
    for To in [4, 12, 20, 30]:
        for Ty in [63, 70]:
            if not (Ty == 63 and (To == 25 or To == 30)):
                t = egg(M, To, Ty)

# Ex. 4: 

from math import factorial

def S(x, n):
    s = 0
    for j in range(n+1):
        s = s + (-1)**j*x**(2*j+1)/factorial(2*j+1)
    return s
		
def verify():
    x = 1.2 # some arbitrary test value
    S0 = x
    S1 = x - x**3/6.0
    tol = 1E-14
    correct = True
    # Never test S(x,0) == S0, always use
    # abs of difference and a tolerance
    if abs(S(x, 0) - S0) > tol:
        correct = False
    if abs(S(x, 1) - S1) > tol:
        correct = False
    return correct

print 'The program is correct:', verify()
				
				

# Ex. 5:

from scitools.std import *
x_min = 0
x_max = 4*pi
x = linspace(x_min, x_max, 100)

plot(x, sin(x), 'k-',
     x, S(x, 1), 'r-',
     x, S(x, 2), 'b-',
     x, S(x, 3), 'y-',
     x, S(x, 6), 'g-',
     x, S(x, 12), 'c-',
     axis=[x_min, x_max, -2, 2],
     title='Taylor series approximation to the sine function',
     legend=('sin(x)', 'n=1', 'n=2', 'n=3', 'n=6', 'n=12'))
				

# Ex. 6:

def diffeq(x, n):
    pj_prev = 0
    qj_prev = x
    index = range(N+1)
    for j in index[1:]:
        pj = pj_prev + qj_prev
        qj = -x**2/float((2*j+1)*(2*j))*qj_prev
        pj_prev = pj
        qj_prev = qj

n = 20
from math import pi
x = pi
s_n, a_n = diffeq(x, n)
print s_n
				
			
			
	

