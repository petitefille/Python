# Ex 1

C = 22
F = 9*C/5 + 32
print F

# Ex 3:

values = []
value = 0.5
end_value = 1 
while value <= end_value:
    values.append(value)
    value += 0.1

print [0.1*i for i in range(10)]
# range(0.5, 1.05, 0.1)
print [0.5+i for i in range(10)]
print [(i+1)*0.1 for i in range(10)]
print [0.5+ i*0.1 for i in range(6)]


[0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9]
[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
[0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9, 1.0]
[0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	


# Ex 4:

def f(x):
    return Q*x**p
Q = 4; p = 2; x = -1; z = 1
print '%g' % f(2*x - z)

# Exercise 5:

n = 5
C = []
for i in range(n):
    x = i**2
    C.append(i+x)
print C

# Ex. 7: 

def sumk2(M, N):
    sum = 0
    j = M
    while j <= N:
        sum += j**-4
        j += 1
    return sum
	
result = sumk2(2, 10)



# Ex. 8

def area(vertices):
    x1 = vertices[0][0]; y1 = vertices[0][1]
    x2 = vertices[1][0]; y2 = vertices[1][1]
    x3 = vertices[2][0]; y3 = vertices[2][1]
    A = 0.5*(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)
    return A


# Ex. 9 

from scitools.std import *
try:
    k = eval(sys.argv[1])
    omega = eval(sys.argv[2])
    t = eval(sys.argv[3])
    x_min = eval(sys.argv[4])
    x_max = eval(sys.argv[5])
    n = eval(sys.argv[6])
except:
    print 'Usage: %s k omega t x_min x_max n' %sys.argv[0]
    sys.exit(1)
	
x = linspace(x_min, x_max, n)
f = exp((-k*x - omega*t)**2)*sin(k*x - omega*t)
plot(x, f)


# Ex. 10:

from math import pi

def S(x, N):
    sj_prev = 0
    aj_prev = x
    for j in range(1, N+1):
        sj = sj_prev + aj_prev
        aj = x**2/((2*j+1)*(2*j))*aj_prev
        sj_prev = sj
        aj_prev = aj
    return sj, aj
	
	
print S(pi, 20)
