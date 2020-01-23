import sys 

try: 
   r1 = float(sys.argv[1])
   print r1 
   r2 = float(sys.argv[2])
   print r2 
   r3 = float(sys.argv[3])
   print r3 
except IndexError:
   print 'Not enough command-line arguments!', sys.argv[1:]
except ValueError:
   print 'Illegal conversion to float!'
   
"""
 
[emilyd@vetur 2013]$ python prog.py
Not enough command-line arguments! []
[emilyd@vetur 2013]$ python prog.py 3 6 hello world
3.0
6.0
Illegal conversion to float!

[emilyd@vetur 2013]$ python prog.py 3 6
3.0
6.0
Not enough command-line arguments! ['3', '6']

------------------------------------

>>> x = range(10)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[1:]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
   