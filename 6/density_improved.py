def read_densities1(filename):
    infile = open(filename, 'r')
    densities1 = {}
    for line in infile:
        words = line.split()
        density1 = float(words[-1])
        substance1 = ' '.join(words[:-1])
        densities1[substance1] = float(density1)
    infile.close()
    return densities1


def read_densities2(filename):
    infile = open(filename, 'r')
    densities2 = {}
    for line in infile:
        line = line.strip()
        
        substance_start = 0
        density_start = 12
        substance2 = line[substance_start:density_start]
        substance2 = substance2.rstrip()
        density2 = (line[density_start:])
        densities2[substance2] = float(density2)
    infile.close()
    return densities2

densities1 = read_densities1('densities.dat')
densities2 = read_densities2('densities.dat')

for substance1 in densities1:
   print substance1, densities1[substance1]

print '----------------------------------'

for substance2 in densities2:
   print substance2, densities2[substance2]





def test_densities():
    densities1 = read_densities1('densities.dat')
    densities2 = read_densities2('densities.dat')
    for i in range(0, len(densities1)):
        assert densities1.keys()[i] == densities2.keys()[i], 'The substance: %s produced by read_densities1 is not the same as the substance: %s produced by read_densities2. ' % (densities1.keys()[i], densities2.keys()[i])
    tol = 1E-14
    for i in range(0, len(densities1)): 
        assert abs(densities1.values()[i] - densities2.values()[i]) < tol, 'The value for the density %.3f, of the substance: %s and produced by read_densities1 is not the same as the value for the density: %.3f of the substance: %s and produced by read_densities2.' % (densities1.value()[i], densities1.keys()[i], densities2.values()[i], densities2.keys()[i])

"""
Terminal> $ nosetests density_improved.py
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
[emilyd@exxilon mytest]$ 

"""

    


