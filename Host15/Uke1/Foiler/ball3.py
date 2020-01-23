initial_velocity = 5
accel_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME -\
                         0.5*accel_of_gravity*TIME**2
print VerticalPositionOfBall

"""
Terminal> python ball1.py
1.2342

"""
