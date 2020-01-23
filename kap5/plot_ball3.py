from scitools.std import *

def yfunc(t, v0):
    return v0*t - 0.5*g*t**2

g = 9.81

if len(sys.argv) == 1:
    print 'Give v0 values on the command line!'
    sys.exit(1)

# need max v0 for computing the curve of largest extent
# in x and y extension
v0_max = 0
for v0_str in sys.argv[1:]:
    v0 = float(v0_str)
    if v0 > v0_max:
        v0_max = v0
    t = linspace(0, 2*v0/g, 101)
    y = yfunc(t, v0)
    plot(t, y)
    hold('on')
    legend('v0=%g' % v0)  # mark this curve with this text

tmax = 2*v0_max/g
xmin = 0
xmax = yfunc(tmax, v0_max)
ymax = yfunc(tmax/2, v0_max)
axis([xmin, xmax, ymin, 1.2*ymax])  # 20% space above highest curve
xlabel('time')
ylabel('height')
savefig('tmp.png')
show()

"""
"""