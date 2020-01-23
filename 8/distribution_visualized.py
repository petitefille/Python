import random
N = 500 # no. of samples
x = range(N)
y = [random.uniform(-1,1) for i in x]
from scitools.std import plot, show,savefig
plot(x, y, 't', axis = [0, N-1, -1.2, 1.2])
savefig('distribution_visualized.png')
show()

