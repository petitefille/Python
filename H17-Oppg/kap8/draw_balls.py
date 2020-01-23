import random

def draw_ball(hat):
    """Draw a ball using list index."""
    index = random.randint(0, len(hat)-1)
    color = hat.pop(index)
    return color, hat

def draw_ball(hat):
    """Draw a ball using list index."""
    index = random.randint(0, len(hat)-1)
    color = hat[index]
    del hat[index]
    return color, hat

def draw_ball(hat):
    """Draw a ball using list element."""
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

def new_hat():
    colors = 'red', 'yellow', 'green', 'brown'
    copies = [5, 5, 3, 7]
    hat = []
    for i, color in enumerate(colors):
        for j in range(copies[i]):
            hat.append(color)
    return hat

import sys
#n = int(sys.argv[1])
N = int(sys.argv[1])
from math import sqrt

def experiments(n, game_no, N):
    M = 0  # no of successes
    money = 0
    for e in range(N):
        hat = new_hat()
        balls = []           # the n balls we draw
        money -= 2*n
        for i in range(n):
            color, hat = draw_ball(hat)
            balls.append(color)
        if game_no == 1:
            if balls.count('red') == 3:
                M += 1
                money += 60
        elif game_no == 2:
            if balls.count('brown') >= 3:
                M += 1
                money += 7 + 5*sqrt(n)
        elif game_no == 3:
            if balls.count('yellow') == 1 and balls.count('brown') == 1:
                M += 1
                money += n**3 - 26
        elif game_no == 4:
            if balls.count('red') >= 1 and \
               balls.count('yellow') >= 1 and \
               balls.count('green') >= 1 and \
               balls.count('brown') >= 1:
                M += 1
                money += 23
    return float(money)/N, float(M)/N

# Go through all 4*7=28 possibilities of game type (1-4)
# and n (4,5,6,7,8,9,10), compute net income and list results

for n in range(4, 11):
    for game_no in range(1, 5):
        net_income_per_game, probability = experiments(n, game_no, N)
        if net_income_per_game > 0:
            print '>>>>>> ',  # prefix on the line
        print 'n=%d, game no=%d, net income=%g' % (n, game_no, net_income_per_game)
		
		
"""

[emilyd@vestur kap8]$ python draw_balls.py 1000
n=4, game no=1, net income=-6.2
n=4, game no=2, net income=-6.215
n=4, game no=3, net income=-0.02
n=4, game no=4, net income=-5.516
n=5, game no=1, net income=-6.46
n=5, game no=2, net income=-6.20031
>>>>>>  n=5, game no=3, net income=3.266
n=5, game no=4, net income=-3.675
n=6, game no=1, net income=-3.54
n=6, game no=2, net income=-5.80232
n=6, game no=3, net income=-1.17
n=6, game no=4, net income=-2.018
n=7, game no=1, net income=-4.28
n=7, game no=2, net income=-4.37111
n=7, game no=3, net income=-7.026
n=7, game no=4, net income=-1.028
n=8, game no=1, net income=-2.14
n=8, game no=2, net income=-3.42043
n=8, game no=3, net income=-13.084
n=8, game no=4, net income=-0.084
n=9, game no=1, net income=-0.96
n=9, game no=2, net income=-1.764
n=9, game no=3, net income=-18
n=9, game no=4, net income=-0.083
>>>>>>  n=10, game no=1, net income=0.28
n=10, game no=2, net income=-1.13498
n=10, game no=3, net income=-20
n=10, game no=4, net income=-0.519
[emilyd@vestur kap8]$ python draw_balls.py 1000
n=4, game no=1, net income=-6.02
n=4, game no=2, net income=-6.062
>>>>>>  n=4, game no=3, net income=0.208
n=4, game no=4, net income=-5.746
n=5, game no=1, net income=-4.78
n=5, game no=2, net income=-6.38211
>>>>>>  n=5, game no=3, net income=3.86
n=5, game no=4, net income=-3.767
n=6, game no=1, net income=-5.28
n=6, game no=2, net income=-5.28264
n=6, game no=3, net income=-0.03
n=6, game no=4, net income=-1.834
n=7, game no=1, net income=-3.74
n=7, game no=2, net income=-4.39134
n=7, game no=3, net income=-5.758
n=7, game no=4, net income=-0.085
n=8, game no=1, net income=-1.78
n=8, game no=2, net income=-3.52614
n=8, game no=3, net income=-11.14
>>>>>>  n=8, game no=4, net income=0.514
n=9, game no=1, net income=-1.86
n=9, game no=2, net income=-2.27
n=9, game no=3, net income=-15.891
>>>>>>  n=9, game no=4, net income=0.216
>>>>>>  n=10, game no=1, net income=1.96
n=10, game no=2, net income=-1.40872
n=10, game no=3, net income=-20
n=10, game no=4, net income=-0.381

"""
