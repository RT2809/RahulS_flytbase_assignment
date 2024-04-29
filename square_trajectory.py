#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation class

time.sleep(3)

print 'taking off 5m hight'
drone.take_off(5.0)

print ' move in a square trajectory'

drone.position_set(6.5, 0, 5, relative=True)

drone.position_set(0, 6.5, 5, relative=True)

drone.position_set(-6.5, 0, 5, relative=True)

drone.position_set(0, -6.5, 5, relative=True)

print 'Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
