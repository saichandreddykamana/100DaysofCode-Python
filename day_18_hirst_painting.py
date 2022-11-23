import colorgram
from turtle import Turtle, Screen
import random

t = Turtle()
t.pensize(20)
t.speed('fastest')
t.colormode(255)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


def draw_dot(color):
    t.pencolor(int(color.r), int(color.g), int(color.b))
    t.dot(10)


def turtle_reset(i):
    t.penup()
    t.left(90)
    t.forward(20)
    t.setposition(0, i * 20)
    t.right(90)


def draw_line(size):
    for _ in range(size):
        color = random.choice(rgb_colors)
        draw_dot(color)
        t.penup()
        t.forward(20)


def draw_hirst_painting(size=5):
    for i in range(size):
        draw_line(size)
        turtle_reset(i + 1)
    t.hideturtle()


draw_hirst_painting(10)
s = Screen()
s.exitonclick()
