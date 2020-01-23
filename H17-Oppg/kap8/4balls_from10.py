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
    colors = 'red', 'blue', 'yellow', 'purple' # (tuple of strings)
    hat = []
    for color in colors:
        for i in range(10):
            hat.append(color)
    return hat

n = 10
N = int(raw_input('How many experiments? '))

# Run experiments
M = 0  # no of successes
for e in range(N):
    hat = new_hat()
    balls = []           # the n balls we draw
    for i in range(n):
        color, hat = draw_ball(hat)
        balls.append(color)
    if balls.count('blue') == 2 and balls.count('purple') == 2:
        M += 1
print 'Probability:', float(M)/N

"""

[emilyd@vestur kap8]$ python 4balls_from10.py
How many experiments? 10
Probability: 0.2
[emilyd@vestur kap8]$ python 4balls_from10.py
How many experiments? 1000
Probability: 0.084

"""