print '-----------------'   # table heading
C = -20                     # start value for C
dC = 5                      # increment of C in loop
while C <= 40:              # loop heading with condition
   F = (9.0/5)*C + 32       # 1st statement inside loop
   print C, F               # 2nd statement inside loop
   C = C + dC               # last statement inside loop
print '-----------------'   # end of table line


"""
Terminal> python while.py
-----------------
-20 -4.0
-15 5.0
-10 14.0
-5 23.0
0 32.0
5 41.0
10 50.0
15 59.0
20 68.0
25 77.0
30 86.0
35 95.0
40 104.0
-----------------
"""

