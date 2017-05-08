import turtle
import math

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def square(t, length):
    polygon(t, length, 4)

def arc(t, radius, angle):
    circumference = 2 * math.pi * radius
    maxSides = radius * 10
    fractionalSides = (angle/360) * maxSides
    numSides = math.floor(fractionalSides)
    length = circumference/maxSides
    for i in range(numSides):
        t.fd(length)
        t.lt(360/maxSides)

def circle(t, radius):
    arc(t, radius, 360)

