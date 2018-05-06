from turtle import *

def Hello_world():
    for i in range(3):
        print ("Hello world!!")

def epsilon(x,y):
    print (sum(x,y))

def draw_square(x, y):
    color(y)
    for i in range(4):
        forward(x)
        left(90)

def draw_star(x,y, length):
    left(26)
    forward(length)
    left(144)
    forward(length)
    left(144)
    forward(length)
    left(144)
    forward(length)
    left(144)
    forward(length)
