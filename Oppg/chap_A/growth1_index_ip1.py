from scitools.std import *
x0 = 100                 # initial amount
p = 5                    # interest rate
N = 10                   # number of years
index_set = range(N+1)
x = zeros(len(index_set), float)
# solution:
x[0] = x0
for i in index_set[:-1]:
    x[i+1] = x[i] + (p/100.0)*x[i]
print x
plot(index_set, x, 'ro', xlabel='years', ylabel='amount')

raw_input('Press <CR>')
savefig('plot.png')

"""

 python growth1_index_ip1.py
[ 100.          105.          110.25        115.7625      121.550625
  127.62815625  134.00956406  140.71004227  147.74554438  155.1328216
  162.88946268]
Press <CR>

gnuplot> set terminal png fontscale 1.0
                          ^
         line 0: unrecognized terminal option

         line 0: warning: Too many axis ticks requested (>7)
         line 0: warning: Too many axis ticks requested (>7)
         line 0: warning: Too many axis ticks requested (>5)

"""

"""
python
Python 2.7.10+ (default, Nov  3 2015, 17:32:48) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> x0 = 100
>>> p = 5
>>> N = 10
>>> from scitools.std import #
  File "<stdin>", line 1
    from scitools.std import #
                             ^
SyntaxError: invalid syntax
>>> from scitools.std import *
>>> index_set = range(N+1)
>>> index_set 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = zeros(len(index_set), float)
>>> x
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
>>> index_set[:-1] 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
>>> x[0] = 100
>>> x
array([ 100.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
          0.,    0.])
>>> for in index_set[:-1]:
  File "<stdin>", line 1
    for in index_set[:-1]:
         ^
SyntaxError: invalid syntax
>>> for i in index_set[:-1]:
...     x[i+1] = x[i] + (p/100.0)*x[i]
... 
>>> print x
[ 100.          105.          110.25        115.7625      121.550625
  127.62815625  134.00956406  140.71004227  147.74554438  155.1328216
  162.88946268]
>>> 

"""
