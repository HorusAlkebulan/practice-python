import turtle

if __name__ == "__main__":

    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.title("Colorful Sprial")
    screen.bgcolor("black")

    sally = turtle.Turtle()
    sally.speed(10)
    sally.width(3)

    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    for x in range(100):
        sally.pencolor(colors[x % 6])
        sally.forward(x * 2)
        sally.left(59)

    sally.hideturtle()
    turtle.done()
