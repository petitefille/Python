from scitools.std import *
v0 = 10
g = 9.81
n = 30 # no of intervals
t = linspace(0, 2*v0/g, n+1)
y = v0*t - 0.5*g*t**2
plot(t, y)
xlabel('time (s)')
ylabel('height (m)')
savefig('tmp1.png')
show()
raw_input('Return to quit: ')
"""
Terminal>
"""