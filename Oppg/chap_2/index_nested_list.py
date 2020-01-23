# 2.14
# Short version:
q = [['a','b','c'], ['d','e','f'], ['g','h']]

print q[0][0], q[1][:], q[-1][-1], q[1][0], q[-1][-2]

# ----------- More comprehensive version ----------------

q = [['a', 'b', 'c'], [42, 'e', 'f'], ['g', 'h']]

# Retrieve a

print q[0][0]
print   #blank line

# Retrieve the list ['d', 'e', 'f']

print q[1]
print

# The last element h

print q[2][-1]
print q[-1][1]
print

# Get d

print q[1][0]
print

# Print all the letters
for e in q:
    print e
    for b in e:
        print b

print
print q[len(q)-1]
print len(q)
print range(len(q))

# Print all the letters using indices
print

for i in range(len(q)):
    print q[i]
    for j in range(len(q[i])):
        print q[i][j]
		
"""
python index_nested_list.py
a ['d', 'e', 'f'] h d g
a

[42, 'e', 'f']

h
h

42

['a', 'b', 'c']
a
b
c
[42, 'e', 'f']
42
e
f
['g', 'h']
g
h

['g', 'h']
3
[0, 1, 2]

['a', 'b', 'c']
a
b
c
[42, 'e', 'f']
42
e
f
['g', 'h']
g
h


"""