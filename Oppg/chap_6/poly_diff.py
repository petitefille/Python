def diff(p) :
    # p is assumed to be a dict
    res = {}
    for j in p :
        if j != 0 :
            res[j-1] = j*p[j]

    return res

# 4x**3 - x**2 + 5
p = {3 : 4, 2 : -1, 0 : 5 }
print p
print diff(p)

"""

[emilyd@vestur chap_6]$ python poly_diff.py
{0: 5, 2: -1, 3: 4}
{1: -2, 2: 12}

"""