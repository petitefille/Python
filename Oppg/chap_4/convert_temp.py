# 4.19

"""
>>> from convert_temp import *
>>> F2C(80)
26.666666666666668
>>> c = 37
>>> C2K(c)
310.15
>>> f = 78
>>> F2K(f)
298.7055555555555
>>>
"""

def C2F(c):
    return c*9./5 +32

def F2C(f):
    return (f-32)*5./9

def C2K(c):
    return c+ 273.15

def K2C(k):
    return k-273.15

def F2K(f):
    return C2K(F2C(f))

def K2F(k):
    return C2F(K2C(k))

def conversion_cml():
    import sys
    try:
        value = float(sys.argv[1])
        scale = sys.argv[2]
    except ValueError:
        print "First command line argument must be a number."
        sys.exit(1)

    if scale == 'C' or scale == 'c':
        F = C2F(value)
        K = C2K(value)
        print "%g degrees Celsius is %g Fahrenheit and %g Kelvin" %(value, F,K)
    elif scale.lower() == 'k': #simpler than checking for k and K
        F = K2F(value)
        C = K2C(value)
        print "%g degrees Kelvin is %g Fahrenheit and %g Celsius" %(value, F,C)
    elif scale.lower() == 'f':
        C = F2C(value)
        K = F2K(value)
        print "%g degrees Fahrenheit is %g Celsius and %g Kelvin" %(value, C, K)
    else:
        print "Unknown temperature scale, should be C, K, or F."
        sys.exit(1)


def test_conversion():
    f = 100.0
    c = 20.0
    tol = 1e-13

    success0 = abs(f - C2F(F2C(f))) < tol
    success1 = abs(c - K2C(C2K(c))) < tol
    success2 = abs(f - K2F(F2K(f))) < tol
    success = success0 and success1 and success2   
    assert success


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'verify':
        test_conversion()
    elif len(sys.argv) > 2:
       conversion_cml()
    else:
        print "Command line arguments should be either 'verify'\nor a number followed by a temperature scale."

"""
Terminal> python convert_temp.py
Command line arguments should be either 'verify'
or a number followed by a temperature scale.
Terminal> python convert_temp.py verify
Terminal> python convert_temp.py 21 C
21 degrees Celsius is 69.8 Fahrenheit and 294.15 Kelvin
"""


       
            
        