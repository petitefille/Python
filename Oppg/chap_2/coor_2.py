
a = 1.0
b = 2.0
n = 10
# 2.6
h = (b-a)/n

# a)
coor = []

for i in range(n+1) :
    x_i = a + i*h
    coor.append(x_i)

print coor

# b)
# Generate equally spaced points
coor = [a+i*h for i in range(n+1)]

print coor
