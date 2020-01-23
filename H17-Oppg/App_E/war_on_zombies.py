#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re

import numpy
import ODESolver
from matplotlib.pylab import *
from math import exp

def transformToFunction(valueOrFunction):
    if isinstance(valueOrFunction, (float, int)):
        return lambda t: valueOrFunction
    else:
        return valueOrFunction

class ProblemSIR:
    def __init__(self, sigma, beta, deltaS, rho, deltaI, alpha, S0, I0, Z0, R0, T):
        self.T = T
        self.S0 = S0
        self.I0 = I0
        self.Z0 = Z0
        self.R0 = R0

        for var in 'sigma', 'beta', 'deltaS', 'rho', 'deltaI', 'alpha':
            setattr(self, var, transformToFunction(vars()[var]))

    def __call__(self, u, t):
        S, I, Z, R = u
        return [
                self.sigma(t) - self.beta(t)*S*Z - self.deltaS(t)*S,
                self.beta(t)*S*Z - self.rho(t)*I - self.deltaI(t)*I,
                self.rho(t)*I - self.alpha(t)*S*Z,
                self.deltaS(t)*S + self.deltaI(t)*I + self.alpha(t)*S*Z]

    def term(self, u, t, i):
        S, I, Z, R = u[i]
        eps = 1e-7
        return S + I + Z + R - (self.S0 + self.I0 + self.Z0 + self.R0) > eps

class SolverSIR:
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=ODESolver.RungeKutta4):
        'entry point'
        problem = self.problem
        solver = method(problem)
        solver.set_initial_condition([problem.S0, problem.I0, problem.Z0, problem.R0])
        n = int(round(self.problem.T/float(self.dt)))
        tp = numpy.linspace(0, self.problem.T, n)
        u, t = solver.solve(tp) # set sigma = 0 to test with lambda u, t, i: problem.term(u, t, i))
        print 'Max infected', max(u[:,1])
        return tp, u

def doPlot(tp, u):
    plot(tp, u[:,0], 'r-')
    plot(tp, u[:,1], 'g-')
    plot(tp, u[:,2], 'b-')
    plot(tp, u[:,3], 'y-')

def main():
    beta = 0.03
    def alpha(t):
        w0 = 0.2*beta
        a = 50*w0
        small_sigma = 0.5
        w = 0.0
        T = [5.0, 10.0, 18.0]
        for i in range(len(T)):
            w += exp(-0.5*((t-T[i])/small_sigma)**2)
        w = a * w + w0
        return w

    problem = ProblemSIR(sigma=0.0, beta=beta, deltaS=0.0, deltaI=0.0, rho=1.0, alpha=alpha, S0=50.0, I0=0.0, Z0=3.0, R0=0.0, T=20)
    solver = SolverSIR(problem, 0.5)
    tp, u = solver.solve()
    doPlot(tp, u)
    show()


if __name__ == '__main__':
    main()

'''
Yes! Humans win!
A handful of survivors boast a painful but glorious victory.
'''

"""

[emilyd@sudur App_E]$ python war_on_zombies.py
Max infected 9.17922521856

"""