"""
Algorithm:

length = ... # m
unit = 1000   # 1 km
lenth_in_km = length/unit
"""
length = 640 # m

inch = 2.54/100  # m
foot = 12*inch   # m
yard = 3*foot    # m
mile = 1760*yard # m

length_in_inches = length/inch
length_in_feet = length/foot
length_in_yards = length/yard
length_in_miles = length/mile

# printf syntax:
print """
Original length: %.1f m
corresponds to
%.2f inches
%.2f feet
%.2f yards
%.4f miles
""" % (length, 
       length_in_inches,
       length_in_feet,
       length_in_yards,
       length_in_miles)
"""
Terminal> python length_conversion.py 

Original length: 640.0 m
corresponds to
25196.85 inches
2099.74 feet
699.91 yards
0.3977 miles

"""
