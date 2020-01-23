# Oppg. 2.16 a):
print '---------------------'
foo = [[], []]
v0 = 5
g = 9.81
n = 10
dt = (2*v0/g)/n
for i in range(n + 1):
    t = i*dt
    y = v0*t - 0.5*g*t**2
    foo[0].append(t)
    foo[1].append(y)
print '  t     y'
for t, y in zip(foo[0], foo[1]):
    print '%.2f %.2f' % (t, y)
    foo.append([t, y])
print '------------------'

# Oppg. 2.16 b):
v0 = 5
g = 9.81
n = 10
dt = (2*v0/g)/n
list_t = [i*dt for i in range(n + 1)]
list_y = [v0*t - 0.5*g*t**2 for t in list_t]
ty2 = [[t, y] for t, y in zip(list_t, list_y)]
print '   t     y'
for t, y in ty2:
    print '%.3f %.3f' % (t, y)
print '------------------'

"""
Terminal>python ball_table3.py
---------------------
  t     y
0.00 0.00
0.10 0.46
0.20 0.82
0.31 1.07
0.41 1.22
0.51 1.27
0.61 1.22
0.71 1.07
0.82 0.82
0.92 0.46
1.02 0.00
------------------
   t     y
0.000 0.000
0.102 0.459
0.204 0.815
0.306 1.070
0.408 1.223
0.510 1.274
0.612 1.223
0.714 1.070
0.815 0.815
0.917 0.459
1.019 0.000
------------------
"""
