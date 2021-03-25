"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""
import math


def litres(time):
    return math.floor(0.5 * time)


def litres_sol_2(time):
    """
    A little bit cleaner version
    """
    return time // 2


print(litres(2), 1, "should return 1 litre")
print(litres(1.4), 0, "should return 0 litres")
print(litres(12.3), 6, "should return 6 litres")
print(litres(0.82), 0, "should return 0 litres")
print(litres(11.8), 5, "should return 5 litres")
print(litres(1787), 893, "should return 893 litres")
print(litres(0), 0, "should return 0 litres")
