# Function roots(a, b, c) that returns the roots of the equation
def roots(a, b, c): 
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2

# Testing the type and value of the returned objects with real roots

def test_roots_float():
    root1, root2 = roots(3, 7, 2)
    print 'Real roots:'
    print 'Root 1: %.4f and root 2:%.4f' % (root1, root2)
    if isinstance(root1, float):
       print "The first root is an element of real numbers."
    elif isinstance(root1, complex):
        print "The first root is an element of complex numbers."
    if isinstance(root2, float):
        print "The second root is an element of real numbers."
    elif isinstance(root2, complex):
        print "the second root is an element of complex number."
    exact_result1, exact_result2 = -2.0/6, -2
    computed_result1, computed_result2 = roots(3, 7, 2)
    tol = 1E-14    
    success = abs(exact_result1 - computed_result1) < tol
    msg_if_failure = 'computed_result = %d != % d' % (computed_result1, exact_result1)
    success = abs(exact_result2 - computed_result2) < tol
    msg_if_failure = 'computed_result = %d != % d' % (computed_result2, exact_result2)
    assert success, msg_if_failure

from math import sqrt    
test_roots_float()

# Testing the type of the returned objects with complex roots
    
def test_roots_complex():
    root3, root4 = roots(3, 2, 6)
    print """Complex roots
Root 1: {c.real:.4f} + {c.imag:.4f}j and root 2: {a.real:.4f} {a.imag:.4f}j""".format(c=root3, a=root4)
    if isinstance(root3, float):
        print "The first root is an element of real numbers."
    elif isinstance(root3, complex):
        print "The first root is an element of complex numbers."
    if isinstance(root4, float):
        print "The second root is an element of real numbers."
    elif isinstance(root4, complex):
        print "The second root is an element of complex numbers."
    exact_result1, exact_result2 = -0.33333333333333331+1.3743685418725535j, -0.33333333333333331-1.3743685418725535j 
    computed_result1, computed_result2 = roots(3, 2, 6)
    tol = 1E-14
    success = abs(exact_result1 - computed_result1) < tol 
    msg_if_failure = 'computed_result = ({c.real:.4f} + {c.imag:.4f}j) != ({a.real:.4f} {a.imag:.4f}j'.format(c=computed_result1, a=exact_result1)  
    success = abs(exact_result2 - computed_result2) < tol
    msg_if_failure = 'computed_result = ({c.real:.4f} + {c.imag:.4f}j) != ({a.real:.4f} {a.imag:.4f}j'.format(c=computed_result2, a=exact_result2)
    assert success, msg_if_failure

from cmath import sqrt as sqrt   
test_roots_complex()

"""
Terminal> python roots_quadratic.py
Real roots:
Root 1: -0.3333 and root 2:-2.0000
The first root is an element of real numbers.
The second root is an element of real numbers.
Complex roots
Root 1: -0.3333 + 1.3744j and root 2: -0.3333 -1.3744j
The first root is an element of complex numbers.
The second root is an element of complex numbers.
"""



