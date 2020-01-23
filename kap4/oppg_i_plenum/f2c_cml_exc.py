import sys
try:
    F = float(sys.argv[1])
except IndexError:
    print '%s: missing command-line arg.'   % (sys.argv[0])
    sys.exit(1)  # Failure
C = (F-32)*5./9
print 'C=%5.1f' % C

"""
Terminal > python f2c_cml_exc.py
f2c_cml_exc.py: missing command-line arg.
Terminal > python f2c_cml_exc.py 3C=-16.1

"""