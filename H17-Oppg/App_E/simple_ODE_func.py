# Given u - 10*u' = 0
# Generic form u' = f(u, t)
# Solve wrt u':
# u' = (1/10)*u
# f(u, t) = u/10.0

def f(u, t):
    return u/10.0

from ForwardEuler_func import ForwardEuler
U0 = 0.2
T = 20
dt = 5
n = int(round(T/float(dt)))
u,t = ForwardEuler(f, U0, T, n)

# Write solution to file
outfile = open('result.dat', 'w')
for t_, u_ in zip(t, u):
    outfile.write('%7.3f  %7.3f\n' % (t_, u_))
outfile.close()

# Compare exact and numerical solution for different
# time step lengths

from numpy import exp

def exact(t):
    return 0.2*exp(0.1*t)

for dt in [5, 2.5, 1, 0.5, 0.01]:
  n = int(round(T/float(dt)))
  u,t = ForwardEuler(f, U0, T, n)

  from scitools.std import plot, figure
  figure()
  plot(t, u, 'r-o', t, exact(t), 'b-',
       legend=['numerical', 'exact'],
       title='dt=%g' % dt)


raw_input()


"""
[emilyd@sudur App_E]$ python simple_ODE_func.py
Can't find PostScript prologue file /ifi/asgard/k00/inf1100/software/install/el7/share/gnuplot/4.4/PostScript/prologue.ps
        loadpath is empty
        no XAPPLRESDIR found in the environment,
            falling back to "/etc/X11/app-defaults/"
Please copy prologue.ps to one of the above directories
or set the loadpath appropriately
or set the environmental variable GNUPLOT_PS_DIR
        line 0: Plot failed!

Can't find PostScript prologue file /ifi/asgard/k00/inf1100/software/install/el7/share/gnuplot/4.4/PostScript/prologue.ps
        loadpath is empty
        no XAPPLRESDIR found in the environment,
            falling back to "/etc/X11/app-defaults/"
Please copy prologue.ps to one of the above directories
or set the loadpath appropriately
or set the environmental variable GNUPLOT_PS_DIR
         line 0: Plot failed!

Can't find PostScript prologue file /ifi/asgard/k00/inf1100/software/install/el7/share/gnuplot/4.4/PostScript/prologue.ps
        loadpath is empty
        no XAPPLRESDIR found in the environment,
            falling back to "/etc/X11/app-defaults/"
Please copy prologue.ps to one of the above directories
or set the loadpath appropriately
or set the environmental variable GNUPLOT_PS_DIR
         line 0: Plot failed!
"""
