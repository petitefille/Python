# Exercise 3.23
# Author: Noah Waterfield Price

def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

print heaviside(-0.5)
print heaviside(0)
print heaviside(10)

"""
Sample run:
python Heaviside.py
0
1
1
"""

def H(x):
    if x < 0:
        value = 0
    elif x >= 0:
        value = 1
    return value


def test_H():
    x = -10
    exact_result = 0
    computed_result = H(-10)
    success = computed_result == exact_result
    msg_if_failure = 'got %s, should have %s' % (computed_result, exact_result)
    assert success, msg_if_failure
    x = -10**-15
    exact_result = 0
    computed_result = H(-10**-15)
    success = computed_result == exact_result
    msg_if_failure = 'got %s, should have %s' % (computed_result, exact_result)
    assert success, msg_if_failure
    x = 0
    exact_result = 1
    computed_result = H(0)
    success = computed_result == exact_result
    msg_if_failure = 'got %s, should have %s' % (computed_result, exact_result)
    assert success, msg_if_failure
    x = 10**-15
    exact_result = 1
    computed_result = H(10**-15)
    success = computed_result == exact_result
    msg_if_failure = 'got %s, should have %s' % (computed_result, exact_result)
    assert success, msg_if_failure
    x = 10
    exact_result = 1
    computed_result = H(10)
    success = computed_result == exact_result
    msg_if_failure = 'got %s, should have %s' % (computed_result, exact_result)
    assert success, msg_if_failure

test_H()

"""
Terminal> python Heaviside.py
"""
