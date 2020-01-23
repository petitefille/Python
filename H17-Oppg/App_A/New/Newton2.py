# Import from Newton.py which is located in src/diffeq in the
# file tree with all example codes from the book.
# Copy Newton.py to the present folder.
import sys, os
from Newton import Newton
from scitools.std import *

def Newton_plot(f, x, dfdx, epsilon=1E-7):
    x, info = Newton(f, x, dfdx, epsilon, store=True)
    iterations = range(len(info))
    roots  = [info[i][0] for i in iterations]
    plot(iterations, roots, 'r-', savefig='tmp_roots.pdf',
         title='Convergence of x toward a root %g' % x,
         xlabel='iterations', ylabel='root')
    figure()
    values = [abs(info[i][1]) for i in iterations]  # |f(x_n)|
    plot(iterations, values, 'r-', savefig='tmp_values.pdf',
         title='Convergence of f(x) toward zero',
         xlabel='iterations', ylabel='abs(f(x))', log='y')
    return x, info

def demo():
    try:
        x = float(sys.argv[1])
    except IndexError:
        print 'You must give initial x as command-line argument!'
        sys.exit(1)

    def g(x):
        return x**6*sin(pi*x)

    def dg(x):
        return 6*x**5*sin(pi*x) + x**6*pi*cos(pi*x)

    x, info = Newton_plot(g, x, dg, epsilon=1E-13)
    import pprint; pprint.pprint(info)

if __name__ == '__main__':
    demo()
	
"""
[emilyd@sudur New]$ python Newton2.py 0.3
[(0.3, 0.0005897733888993366),
 (0.25512173364753593, 0.00019808266338659032),
 (0.21747151495192485, 6.6778805321235292e-05),
 (0.18567437485440666, 2.2568344898722942e-05),
 (0.15870219937866722, 7.6398741992719903e-06),
 (0.13575420741996411, 2.5892658499117298e-06),
 (0.11618919813944417, 8.7825938164833231e-07),
 (0.099483796706838212, 2.9807316085624199e-07),
 (0.085204972433605169, 1.0120585786638405e-07),
 (0.072990958735342906, 3.437325322247692e-08),
 (0.062537411966676809, 1.1677011006370418e-08),
 (0.053587002068770408, 3.967461784111064e-09),
 (0.045921351032295665, 1.3481708973839067e-09),
 (0.039354640828672155, 4.5815723430137596e-10),
 (0.033728449791792958, 1.5570822107411088e-10),
 (0.028907520358615393, 5.292107005811992e-11),
 (0.024776251196868167, 1.7987069717254993e-11),
 (0.021235764883368119, 6.1136845320214593e-12),
 (0.018201440895275971, 2.0780383804199658e-12),
 (0.015600830046543172, 7.0633370001246395e-13),
 (0.013371885037196336, 2.4008806248114643e-13),
 (0.011461455182265511, 8.1608302998073174e-14)]

"""