# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 04/17/2024
# Description: Program that returns the distance in meters that the object has fallen in that time.

def fall_distance(time):
    '''Returns distance in meters than an object has fallen'''
    g = 9.8
    t = time
    meters = (1/2) * g * t ** 2
    return meters
