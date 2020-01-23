# 4.4

infile = open('Fdeg.dat', 'r')

# Skip the first three lines
infile.readline() # read line, move "file pointer" one line dowwnard
infile.readline() # read line, move "file pointer" one line dowwnard
infile.readline() # read line, move "file pointer" one line dowwnard

# Alternative: pro version 1:
#for i in range(3):
#    infile.readline()

# Alternative: pro version 2:
#lines = infile.readlines()
#for line in lines[3:]:

F = []
# Read one line at a time, starting where the "file pointer" is
for line in infile:
    words = line.split()
    F.append(float(words[-1]))  # (words[2])
infile.close()

# Newbie solution: build C list from empty list and foor loop
#C = []
#for F_ in F:
#    C.append((F_-32)*5.0/9)
# Pro solution: use list comprehensions
C = [(F_-32)*5.0/9 for F_ in F]  # (note F_ w/underscore, different from F)

# Write out the table, first on the screen for fine tuning

# Amateur solution:
#for i in range(len(F)):
    # C[i], F[i]

# Pro solution:
print '   F       C'
for C_, F_ in zip(C, F):
    print '%6.2f  %6.2f' % (F_, C_)

# Write table to file
outfile = open('FCdeg.dat', 'w')
outfile.write('   F       C\n')
for C_, F_ in zip(C, F):
    outfile.write('%6.2f  %6.2f\n' % (F_, C_))
outfile.close()



"""

[emilyd@vor chap_4]$ python f2c_file_read_write.py
   F       C
 67.20   19.56
 66.00   18.89
 78.90   26.06
102.10   38.94
 32.00    0.00
 87.80   31.00
 
"""