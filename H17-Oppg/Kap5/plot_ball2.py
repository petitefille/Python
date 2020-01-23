from scitools.std import *
import sys
v0_values = [float(v0) for v0 in sys.argv[1:]]
g = 9.81
n = 30 # no of intervals

legends = []  # text associated with each curve
for v0 in v0_values:
    t = linspace(0, 2*v0/g, n+1)
    y = v0*t - 0.5*g*t**2
    plot(t, y)
    hold('on')
    legends.append('v0=%g' % v0)
    
xlabel('time (s)')
ylabel('height (m)')
legend(legends)
show()
raw_input('Return to quit: ')
