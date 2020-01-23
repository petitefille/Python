class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)

    def __sub__(self, other):
        """Return self - other as Polynomial object."""
        # Two cases:
        #
        # self:   X X X X X
        # other:  X X X X X X X X
        #
        # or:
        #
        # self:   X X X X X X X
        # other:  X X X

        # treat the common powers first, then the rest

        # start with the longest list and subtract the other,
        # place result in result_coeff list
        if len(self.coeff) > len(other.coeff):
            # self:   X X X X X X X
            # other:  X X X
            result_coeff = self.coeff[:]  # copy
            for i in range(len(other.coeff)):
                result_coeff[i] -= other.coeff[i]
            # the rest of result_coeff is just self.coeff and ok
        else:
            # self:   X X X X X
            # other:  X X X X X X X X
            result_coeff = [0]*len(other.coeff)
            # treat common powers first:
            for i in range(len(self.coeff)):
                result_coeff[i] = self.coeff[i] - other.coeff[i]
            # need to take 0 - other for the rest of the powers in other:
            for i in range(len(self.coeff), len(other.coeff)):
                result_coeff[i] = 0 - other.coeff[i]

            # alternative: pad self.coeff with zeros, then subtract
            # result_coeff = self.coeff[:] +
            #         [0]*(len(self.other)-len(self.coeff)
            # result_coeff[i] -= other.coeff[i]

        # Alternative: reuse __add__!
        #coeff = [-coeff for coeff in other.coeff]
        #return self + Polynomial(coeff)
        return Polynomial(result_coeff)

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        #s = s.replace('x^1', 'x') # will replace x^100 by x^00
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

def test_Polynomial():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])

    # Test the two cases in __sub__
    p3 = p1 - p2
    p3_exact = Polynomial([1, -2, 0, 0, 6, 1])
    msg = 'p1 = %s, p2 = %s\np3=p1-p2 = %s\nbut wrong p3 = %s'%\
          (p1, p2, p3_exact, p3)
    assert p3.coeff == p3_exact.coeff, msg
    # Note __add__ applies lists only, here with integers, so
    # == for comparing lists is not subject to round-off errors

    p4 = p2 - p1
    p4_exact = Polynomial([-1, 2, 0, 0, -6, -1])
    msg = 'p1 = %s, p2 = %s\np3=p2-p1 = %s\nbut wrong p4 = %s'%\
          (p1, p2, p3_exact, p3)
    assert p4.coeff == p4_exact.coeff, msg


if __name__ == '__main__':
    p = Polynomial([1, 2, 3])
    q = Polynomial([2, 3])
    r = p-q
    print r.coeff
    r = q-p
    print r.coeff
	
"""

[emilyd@sudur kap7]$ python Polynomial_sub.py
[-1, -1, 3]
[1, 1, -3]

"""