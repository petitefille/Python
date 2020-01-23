import random
import sys
N = int(sys.argv[1])

HEAD = 1
TAIL = 2

num_heads = 0

for i in range(N):
    r = random.randint(HEAD, TAIL)
    if r == HEAD:
        print 'head'
        num_heads += 1
    else:
        print 'tail'
    """
    # Alternative:
    r = random.random()  # [0,1)
    if r <= 0.5:
        print 'head'
        num_heads += 1
    else:
        print 'tail'
    # Alternative:
    r = random.choice(['head', 'tail'])
    if r == 'head':
        print 'head'
        num_heads += 1
    else:
        print 'tail'
    """

print 'no of heads:', num_heads

"""

[emilyd@vestur kap8]$ python flip_coin.py 3
tail
head
tail
no of heads: 1
[emilyd@vestur kap8]$ python flip_coin.py 7
head
tail
head
tail
head
head
tail
no of heads: 4

"""
