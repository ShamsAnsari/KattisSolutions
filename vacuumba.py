from math import *


def add(u, v):
    return u[0] + v[0], u[1] + v[1]


def getAngle(x, y):
    if x == 0:
        return 0
    else:
        return degrees(atan(y / x))


def vector(angle, distance):
    angle += 90
    angle = radians(angle)
    x = round(distance * cos(angle), 9)
    y = round(distance * sin(angle), 9)
    return x, y


n = int(input())

while n > 0:
    m = int(input())
    x, y = 0, 0
    prevAngle = 0
    while m > 0:
        angle, distance = [float(data) for data in input().split(" ")]
        x, y = add((x, y), vector(angle + prevAngle, distance))
        prevAngle += angle
        m -= 1
    print("{x:.8f} {y:.8f}".format(x=x, y=y))
    n -= 1
