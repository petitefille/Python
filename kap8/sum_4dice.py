import sys
N = int(sys.argv[1])
r = float(sys.argv[2])

import random
start_capital = 1
money = start_capital
for i in range(N):
   money -= 1
   dice_1 = random.randint(1,6)
   dice_2 = random.randint(1,6)
   dice_3 = random.randint(1,6)
   dice_4 = random.randint(1,6)
   y = dice_1 + dice_2 + dice_3 + dice_4
   if y < 9:
      money += r
    
      
net_profit_total = money - start_capital
net_profit_per_game = net_profit_total/float(N)
print 'Net profit per game in the long run:', net_profit_per_game

"""
Terminal> python sum_4dice.py 100 10
Net profit per game in the long run: -0.3
Terminal> python sum_4dice.py 1000 10
Net profit per game in the long run: -0.41
Terminal> python sum_4dice.py 10000 10
Net profit per game in the long run: -0.489
Terminal> python sum_4dice.py 100000 10
Net profit per game in the long run: -0.4588
Terminal> python sum_4dice.py 1000000 10
Net profit per game in the long run: -0.46101
"""


