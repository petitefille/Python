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