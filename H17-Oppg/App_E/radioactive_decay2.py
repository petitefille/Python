"""
def f(u, t):
    u_A, u_B = u
    return [u_B/tau_B - u_A/tau_A,
            u_A/tau_A - u_B/tau_B]

tau_A = 8
tau_B = 40
"""

class Problem:
    def __init__(self, tau_A, tau_B):
        self.tau_A, self.tau_B = tau_A, tau_B

    def __call__(self, u, t):
        u_A, u_B = u
        tau_A, tau_B = self.tau_A, self.tau_B
        return [u_B/tau_B - u_A/tau_A,
                u_A/tau_A - u_B/tau_B]

    def test_asymptotic_limit(self, u_A, u_B, tol=0.01):
        # u_A, u_B: arrays
        limit = self.tau_A/float(self.tau_B)
        u_A_div_u_B = u_A[-1]/u_B[-1]
        diff = abs(u_A_div_u_B - limit)
        print 'diff limit:', diff
        success = diff < tol
        return success

def test_asymptotic_limit():
    U0 = [1, 1]

    f = Problem(tau_A=8, tau_B=40)
    from ODESolver import RungeKutta4
    solver = RungeKutta4(f)
    solver.set_initial_condition(U0)
    dt = 10/60.0  # minutes
    T = 50  # 50 min
    n = int(round(T/float(dt)))
    import numpy as np
    time_points = np.linspace(0, T, n+1)
    u, t = solver.solve(time_points)

    # Plot
    u_A = u[:,0]
    u_B = u[:,1]
    assert f.test_asymptotic_limit(u_A, u_B, tol=0.001)

    from matplotlib.pyplot import plot, show, legend
    plot(t, u_A, t, u_B)
    legend(['u_A', 'u_B'], loc='lower left')
    show()

test_asymptotic_limit()

"""

[emilyd@sudur App_E]$ python radioactive_decay2.py
diff limit: 0.000265539250534

"""