# 4.14

"""

ball_file_read_write.py
Bra! Men det skulle helst vært i én fil. 
Samtidig er det fint å se at du mestrer importering fra egne 
moduler! Det blir nyttig senere. Og kjempefint at du bruker tempfile!

"""

import sys

def extract_data(filename):
    infile = open(filename, 'r')
    first_line = infile.readline().split()
    v0 = float(first_line[-1])
    infile.readline()
    T = []
    for line in infile:
        for value in line.split():
            T.append(float(value))
    infile.close()
    return v0, T

def write_data(outfile, v0, T):
    outfile = open(outfile, 'w')
    outfile.write('   t values        y values\n')
    for t in sorted(T):
        g = 9.81
        outfile.write('%2.11f %15.11f\n' % (float(t), float(t*v0 - 0.5*g*t**2)))

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    v0, T = extract_data(infile)
    write_data(outfile, v0, T)
    
"""
Terminal> python ball_file_read_write.py values.dat out.dat
Terminal> cat out.dat 
   t values        y values
0.04200000000   0.11734758000
0.05190850000   0.14250901491
0.10262264000   0.25621137239
0.11170000000   0.27390085455
0.15592000000   0.34851431741
0.17383923000   0.37328820796
0.20942940000   0.41315159607
0.21342619000   0.41685219728
0.21385894000   0.41724347530
0.27000000000   0.45242550000
0.28075000000   0.45563514094
0.29584013000   0.45822800875
0.34648150000   0.45060204662
0.35000000000   0.44913750000
0.36807889000   0.43969712026
0.37298500000   0.43658214085
0.39325246000   0.42121140576
0.50620017000   0.26175011761
0.52800000000   0.21656448000
0.53012000000   0.21192151337
0.57681501876   0.09847520570
0.57982969000   0.09041595757
"""
