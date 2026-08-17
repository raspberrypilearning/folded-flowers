# Folded flowers
# One fold, three shapes to cut out.

import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


def box(left, bottom, width, height):
    pen.penup()
    pen.goto(left, bottom)
    pen.setheading(0)
    pen.pendown()
    for side in [width, height, width, height]:
        pen.forward(side)
        pen.left(90)
    pen.penup()


def fold_line(x, bottom, top):
    pen.penup()
    pen.goto(x, bottom)
    pen.setheading(90)
    while pen.ycor() < top:
        pen.pendown()
        pen.forward(10)
        pen.penup()
        pen.forward(10)


def cut_out(corners):
    pen.penup()
    pen.goto(corners[0])
    pen.pendown()
    pen.begin_fill()
    for corner in corners:
        pen.goto(corner)
    pen.end_fill()
    pen.penup()


# 1. the paper, with a fold down the middle
box(-100, 40, 200, 200)
fold_line(0, 40, 240)

# 2. the folded paper, with shapes to cut out
box(-100, -210, 100, 200)

square = [(-100, -90), (-60, -90), (-60, -50), (-100, -50)]
triangle = [(0, -140), (0, -180), (-40, -160)]
rectangle = [(-90, -210), (-30, -210), (-30, -185), (-90, -185)]

cut_out(square)
cut_out(triangle)
cut_out(rectangle)

turtle.done()
