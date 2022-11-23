from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_anti_clockwise():
    tim.setheading(tim.heading() + 10)


def move_clockwise():
    tim.setheading(tim.heading() - 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.setposition(0, 0)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_anti_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
