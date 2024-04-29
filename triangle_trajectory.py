#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation cla$

time.sleep(3)

print 'taking off till 10m'
drone.take_off(10.0)

print ' move in a triangular trajectory of side length 10m at a height of 10m'

print ' A to B of triangle ABC'
# gives us the desired side length of 10m.
drone.position_set(8.66, 5, 0, relative=True)

print ' B to C of triangle ABC'
drone.position_set(-8.66, 5, 0, relative=True)

print '  C to A of triangle ABC'
drone.position_set(0, -10, 10, relative=True)


print ' Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
