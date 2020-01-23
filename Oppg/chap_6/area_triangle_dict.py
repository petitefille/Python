# 6.9 

# .5 * |x2 y3 - x3 y2 - x1 y3 + x3 y1 + x1 y2 - x2 y1 |

#vertices stored as dict: {1:(x1,y1), 2:(x2,y2),3:(x3,y3)}

def area(t):
    return 0.5*abs(t[2][0]*t[3][1]-t[3][0]*t[2][1] - \
                   t[1][0]*t[3][1]+t[3][0]*t[1][1]+t[1][0]*t[2][1] -t[2][0]*t[1][1])

def dump(tri):
    print "Area of triangle %s is %s " %(tri, area(tri)) 

"""
When testing this function it is a good idea to use a simple triangle shape, but
avoid zero coordinates. If x or y is zero, terms in the formula will cancel
and errors are easily hidden.
"""

tri1 = {1: (1,1), 2: (2,1), 3: (1,3)} #area = 1.0
tri2 = {1:(1,1),2:(3,1),3:(1,3)} #area = 2.0

dump(tri1)
dump(tri2)

"""
python area_triangle_dict.py
Area of triangle {1: (1, 1), 2: (2, 1), 3: (1, 3)} is 1.0
Area of triangle {1: (1, 1), 2: (3, 1), 3: (1, 3)} is 2.0


"""