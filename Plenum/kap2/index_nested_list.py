q = [['a','b','c'],['d','e','f'],['g','h']]


print "a)"
print q[0][0]
print q[1]
print q[-1][-1], q[2][1]
print q[1][0]

print """
q[-1][-2] has value 'g' because index q[-1] is the last element of q,
i.e. ['g','h'], and q[-1][-2] then becomes the second to last element
of this list.
"""

print "b)"
for i in q:
    for j in range(len(i)):
        print i[j]
        #print type(i), type(j), type(i[j])

print """
The i's are lists, j's are integers, while i[j] are of type str.
"""

""" Terminal > python index_nested_list.py 
a)
a
['d', 'e', 'f']
h h
d

q[-1][-2] has value 'g' because index q[-1] is the last element of q,
i.e. ['g','h'], and q[-1][-2] then becomes the second to last element
of this list.

b)
a
b
c
d
e
f
g
h

The i's are lists, j's are integers, while i[j] are of type str.
"""
