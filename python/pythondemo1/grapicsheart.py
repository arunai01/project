"""import math
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(1500)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()"""



#graphics 2
"""

from turtle import *
import colorsys
bgcolor('black')
tracer(500)
def draw():
    h=0
    for i in range (100):
        c=colorsys.hcv_to_rgb(h,1,1)
        h +=0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt(98)
        circle(i,15)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j,299,step=2)
        end_fill()
    draw|()
done()"""

#graphics 3
import turtle
import colorsys
t = turtle.Turtle()
s= turtle.Screen().bgcolor('white')
t.speed(100)
n = 70
h = 0
for i in range(6000):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h+= 1/n
    t.color(c)
    t.right(1)
    t.fd(1)
    for j in range(3):
        t.right(3)
        t.circle(200)
