import scitools.std as plt
# (Animations are easier with scitools.std
# than with matplotlib, see the book for how
# to do it with matplotlib)

import numpy as np
# (not strictly necessary - numpy functions can be
# reached through plt. prefix as well)

import time  # for pause between frames in animations

def animate_series(fk, M, N, xmin, xmax, ymin, ymax,
                   n, exact):
    x = np.linspace(xmin, xmax, n)
    S = 0  # summation variable
    for k in range(M, N+1):
        S += fk(k, x)
        plt.plot(x, S, 'b-',
                 x, exact(x), 'r-',
                 axis=[xmin, xmax, ymin, ymax],
                 legend=['k=%d' % k, 'exact'])
        # filenames: tmp_0000.png tmp_0001.png, tmp_0002.png
        plt.savefig('tmp_%04d.png' % k)
        time.sleep(1)  # pause: 1 sec

# Remove all existing plot files tmp_*.png
import glob, os
for filename in glob.glob('tmp_*.png'):
    os.remove(filename)


# exp(-x):
from math import factorial

def fk_exp_mx(k, x):
    # x^k/k!
    return (-x)**k/float(factorial(k))

def exp_mx_exact(x):
    return np.exp(-x)

# sin(x):
def fk_sin(k, x):
    return (-1)**k*x**(2*k+1)/float(factorial(2*k+1))

def sin_exact(x):
    return np.sin(x)

animate_series(fk=fk_sin, M=0, N=20, xmin=0,
               xmax=20, ymin=-1, ymax=2, n=10001,
               exact=sin_exact)

# Command for making video:
cmd = 'avconv -r 1 -i tmp_%04d.png -vcodec libtheora movie.ogg'
os.system(cmd)  # run command cmd in the operating system