# t i I=[0, 2*v0/g]
v0 = 9.5
g = 9.81
n = 10  # no of subintervals in I
dt = (2*v0/g)/n  # subinterval size
#print '[%g, %g]' % (0, 2*v0/g)
print '  t     y'
for i in range(n+1):
    t = i*dt
    # t = t + dt  # alternative
    y = v0*t - 0.5*g*t**2
    print '%.3f %.3f' % (t, y)

# While loop
print '---------------------'
t = 0
# Avoid effect of round-off errors: + dt/2
while t <= 2*v0/g + dt/2:
    y = v0*t - 0.5*g*t**2
    print '%.3f %.3f' % (t, y)
    t = t + dt
#print 2*v0/g
"""
Terminal> python ball_table1.py
  t     y
0.000 0.000
0.194 1.656
0.387 2.944
0.581 3.864
0.775 4.416
0.968 4.600
1.162 4.416
1.356 3.864
1.549 2.944
1.743 1.656
1.937 0.000
---------------------
0.000 0.000
0.194 1.656
0.387 2.944
0.581 3.864
0.775 4.416
0.968 4.600
1.162 4.416
1.356 3.864
1.549 2.944
1.743 1.656
1.937 0.000
"""
