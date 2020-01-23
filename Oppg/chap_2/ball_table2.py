# 2.8
list_t = []
list_y = []
v0 = 5
g = 9.81
n = 10
dt = (2*v0/g)/n
for i in range(n + 1):
    t = i*dt
    y = v0*t - 0.5*g*t**2
    list_t.append(t)
    list_y.append(y)
print '  t     y'
for t, y in zip(list_t, list_y):
    print '%.3f %.3f' % (t, y)
"""
Terminal> python ball_table2.py
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
"""

  

