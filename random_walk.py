import turtle
from turtle import Turtle, Screen
import random

dd = Turtle()
dd.shape("turtle")
dd.width(10)
dd.speed("fastest")
turtle.colormode(255)

def colo():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    dd.color(r,g,b)



def direct():
    direction = [0, 90, 180, 360]
    turn = random.choice(direction)
    return turn


def right_back():
    dd.right(direct())
    dd.back(25)


def right_front():
    dd.right(direct())
    dd.forward(25)


def left_front():
    dd.left(direct())
    dd.forward(25)


def left_back():
    dd.left(direct())
    dd.back(25)


choic = [1, 2, 3, 4]
for i in range(200):
    a = random.choice(choic)
    if a == 1:
        right_back()
        colo()
    elif a == 2:
        right_front()
        colo()
    elif a == 3:
        left_back()
        colo()
    else:
        left_front()
        colo()

screen = Screen()
screen.exitonclick()

