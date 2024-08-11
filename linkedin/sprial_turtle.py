# https://www.linkedin.com/learning/python-recursion/recursion-in-action?autoSkip=true&resume=false&u=0
from turtle import Turtle

MAX_LENGTH = 250
INCREMENT = 10

def draw_spiral(turtle: Turtle, line_length: int):
    # base case
    if line_length > MAX_LENGTH:
        return

    # take action
    turtle.forward(line_length)
    turtle.right(90)    

    # movement towards base case
    line_length += INCREMENT

    # recursive call
    draw_spiral(turtle, line_length)

# initial conditions
charlie = Turtle(shape="turtle")
line_length = INCREMENT
charlie.pensize(5)
charlie.color("red")

# intial call
draw_spiral(charlie, line_length)

# finish up
