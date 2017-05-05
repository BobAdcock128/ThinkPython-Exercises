import turtle

t = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, radius):
    pi = 3.14159
    circumference = 2*pi*radius
    n = radius*10
    length = circumference/n
    polygon(t, length, n)

def arc(t, radius, angle):
    pi = 3.14159
    n = radius*10
    length = 2*pi*10*angle/360
    polygon(t, length, n)

arc (t, 10, 90)
