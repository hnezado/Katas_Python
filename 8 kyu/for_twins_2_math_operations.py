import math


def ice_brick_volume(radius, bottle_length, rim_length):
    return math.sqrt(((2*radius)**2)/2)**3


print(ice_brick_volume(1, 10, 2))
