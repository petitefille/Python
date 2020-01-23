from math import exp 
import sys 

def g(t):
    return exp(-a*t), -a*exp(-a*t)


try: 
    t = float(sys.argv[1])
    a = float(sys.argv[2])
except IndexError:
    print 'Not enough command-line arguments (two are needed)', sys.argv[1:]
    sys.exit(1)
except ValueError:
    print 'Cannot convert command-line arguments to floats', sys.argv[1:]
    sys.exit(1)
    

g_value, dg_value = g(t)
print dg_value

"""

[emilyd@vetur 2013]$ python Ex_three.py
Not enough command-line arguments (two are needed) []
[emilyd@vetur 2013]$ python Ex_three.py 0.1
Not enough command-line arguments (two are needed) ['0.1']
[emilyd@vetur 2013]$ python Ex_three.py 0.1 2
-1.63746150616
[emilyd@vetur 2013]$ python Ex_three.py 0.1 A
Cannot convert command-line arguments to floats ['0.1', 'A']


"""