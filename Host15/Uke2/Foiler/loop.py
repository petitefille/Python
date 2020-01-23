degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print 'Celsius degrees:', C
    F = 9/5.*C + 32
    print 'Fahrenheit:', F
print 'The degrees list has', len(degrees), 'elements'

"""
Terminal> python loop.py
Celsius degrees: 0
Fahrenheit: 32.0
Celsius degrees: 10
Fahrenheit: 50.0
Celsius degrees: 20
Fahrenheit: 68.0
Celsius degrees: 40
Fahrenheit: 104.0
Celsius degrees: 100
Fahrenheit: 212.0
The degrees list has 5 elements
"""
