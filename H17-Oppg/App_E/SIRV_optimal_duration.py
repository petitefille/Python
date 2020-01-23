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

class ProblemSIR:
    def __init__(self, p, nu, beta, S0, I0, R0, V0, T):
        self.T = T
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.V0 = V0

        if isinstance(nu, (float, int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p

    def __call__(self, u, t):
        S, I, R, V = u
        return [
                -self.beta(t)*S*I - self.p(t)*S,
                self.beta(t)*S*I-self.nu(t)*I,
                self.nu(t)*I,
                self.p(t)*S]

    def term(self, u, t, i):
        S, I, R, V = u[i]
        eps = 1e-7
        return S + I + R + V - (self.S0 + self.I0 + self.R0 + self.V0) > eps

class SolverSIR:
    def __init__(self, problem, dt):
        self.problem = problem
        self.dt = dt

    def solve(self, method=ODESolver.RungeKutta4):
        'entry point'
        problem = self.problem
        solver = method(problem)
        solver.set_initial_condition([problem.S0, problem.I0, problem.R0, problem.V0])
        n = int(round(self.problem.T/float(self.dt)))
        tp = numpy.linspace(0, self.problem.T, n)
        u, t = solver.solve(tp, lambda u, t, i: problem.term(u, t, i))
        print 'Max infected', max(u[:,1]), 'for VT', problem.VT
        return tp, u

def doPlot(tp, u):
    plot(tp, u[:,0], 'r-')
    plot(tp, u[:,1], 'g-')
    plot(tp, u[:,2], 'b-')
    plot(tp, u[:,3], 'y-')

def main():
    beta = lambda t: 0.0005
    for VT in range(32):
        p = lambda t: 0.1 if 6 <= t <= 6 + VT else 0
        problem = ProblemSIR(T=60, p=p, nu=0.1, beta=beta, S0=1500, I0=1.0, R0=0.0, V0=0.0)
        problem.VT = VT
        solver = SolverSIR(problem, 0.5)
        tp, u = solver.solve()
        doPlot(tp, u)
    show()


if __name__ == '__main__':
    main()

'''
With beta = 0.0005 the optimal is reached after 9 days of vaccination.
'''


"""
[emilyd@sudur App_E]$ python SIRV_optimal_duration.py
Max infected 897.177648467 for VT 0
Max infected 780.87576441 for VT 1
Max infected 682.187946886 for VT 2
Max infected 602.886162641 for VT 3
Max infected 541.318556558 for VT 4
Max infected 497.260735423 for VT 5
Max infected 468.329612964 for VT 6
Max infected 452.297859475 for VT 7
Max infected 446.20897698 for VT 8
Max infected 445.580371321 for VT 9
Max infected 445.580371321 for VT 10
Max infected 445.580371321 for VT 11
Max infected 445.580371321 for VT 12
Max infected 445.580371321 for VT 13
Max infected 445.580371321 for VT 14
Max infected 445.580371321 for VT 15
Max infected 445.580371321 for VT 16
Max infected 445.580371321 for VT 17
Max infected 445.580371321 for VT 18
Max infected 445.580371321 for VT 19
Max infected 445.580371321 for VT 20
Max infected 445.580371321 for VT 21
Max infected 445.580371321 for VT 22
Max infected 445.580371321 for VT 23
Max infected 445.580371321 for VT 24
Max infected 445.580371321 for VT 25
Max infected 445.580371321 for VT 26
Max infected 445.580371321 for VT 27
Max infected 445.580371321 for VT 28
Max infected 445.580371321 for VT 29
Max infected 445.580371321 for VT 30
Max infected 445.580371321 for VT 31


"""