import math
from turtle import *

#############################################
# Program by Lindsey Weiskopf               #
# Draws fractals based on degree input      #
#############################################

setup(1000,1000)
sc = Screen()
sc.title("Fractals")

t = Turtle()
t.speed("fastest")
t.hideturtle()


def koch(degree, unit):
    if degree == 0:
        t.fd(unit)

    else:
        koch(degree-1, unit/3)
        t.left(60)
        koch(degree-1, unit/3)
        t.right(120)
        koch(degree-1, unit/3)
        t.left(60)
        koch(degree-1, unit/3)

def kochSnowflake(degree, unit):
    for i in range(0,3):
        koch(degree, unit)
        t.right(120)


def sierpinski(degree, unit):
    if degree == 0:
        for i in range(0,3):
            t.fd(unit)
            t.left(120)
    else:
        sierpinski(degree-1, unit/2)
        t.right(60)
        sierpinski(degree-1, unit/2)
        t.bk(unit/2)
        sierpinski(degree-1, unit/2)
#base case works

#mandelbrot
#sierpinski carpet
#figure out how to do it without turtle

def main():
    degree = int(input("degree? "))
    unit = float(input("length of unit? "))*3

    sc = Screen()

    sc.title("Fractals")

    #for i in range(0,4):
    t.penup()
    t.setx(-440)
    t.pendown()
    koch(degree, unit)
    
    sc.exitonclick()
main()



