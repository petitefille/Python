
def sum_1k(M):
    s = 0
    for k in range(1,M+1):
        s = s + 1.0/k
    return s


def test_sum_1k():
    #During development, add a print statement
    #to know the test has been called:
    print "Test function called"
    expected = 1.0+1.0/2+1.0/3
    computed = sum_1k(3)
    tol = 1e-10
    success = abs(expected-computed) < tol
    msg = "Expected %g, got %g" %(expected, computed)
    assert success, msg

#compute sum for two values of M:
M = [3,10]
for m in M:
    print "For M = %d, the sum is %g" %(m,sum_1k(m))

#Remember to call the test function:                                
test_sum_1k()

"""
Terminal> python sum_func.py 
For M = 3, the sum is 1.83333
For M = 10, the sum is 2.92897
Test function called
"""

