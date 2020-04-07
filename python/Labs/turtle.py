# Turtle

from turtle import *


def draw_square():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)


    done()
draw_square()

def fill_square():
    fillcolor('red')
    begin_fill()

    
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)

    end_fill()

    done()
# fill_square()

def draw_star():
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)
    right(144)
    forward(100)

    done()
# draw_star()

def square_loop():
    i = 0 
    while i < 4:
        forward(100)
        left(90)
        i += 1
    done()
# square_loop()

def draw_stair():
    i = 0
    while i < 4:
        forward(100)
        left(90)
        forward(100)
        right(90)
        i += 1

    done()
# draw_stair()


def n_side():
    edge_length = 100
    n_sides = 5

    i = 0
    while i < n_sides:
        forward(edge_length/n_sides)
        right(360/n_sides)
        i += 1

    done()

# n_side()

def eight_sided():
    fillcolor('blue')

    n_sides = 8
    edge_length = 0

    i = 0
    begin_fill()
    while i < 150:
        forward(edge_length)
        right(360/n_sides)
        i = i + 1
        
        edge_length = edge_length + 1 # this makes forward longer thus big spiral
    end_fill()

    done()
# eight_sided()

def expand_star():
    edge_length = 0
    i = 0
    while i < 100:
        forward(edge_length)
        right(144)

        edge_length += 4

    done()    

# expand_star()


